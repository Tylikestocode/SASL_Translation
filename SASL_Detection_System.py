import cv2
import tensorflow as tf
import mediapipe as mp 
import numpy as np
from scipy import stats


#Creating function to capture keypoints
mp_holistic = mp.solutions.holistic
mp_draw = mp.solutions.drawing_utils

#Load in model
model = tf.keras.models.load_model('C:\\Users\\Tyron\\Sign_Language_Detection\\SASL_Sign_Language_Detection\\LSTM_Model_Final_2.h5')
print('Model Loaded Successfully')

def Media_Pipe_Detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    image.flags.writeable = False
    result = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, result

#Function to draw keypoints
def draw_keypoints(result, image):

    mp_draw.draw_landmarks(image, result.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1))
    
    mp_draw.draw_landmarks(image, result.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4))

    mp_draw.draw_landmarks(image, result.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4))

    mp_draw.draw_landmarks(image, result.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),
                           mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1))

def collect_keypoints(result):
    face = np.array([[res.x, res.y, res.z] for res in result.face_landmarks.landmark]).flatten() if result.face_landmarks else np.zeros(1404)
    right_hand = np.array([[res.x, res.y, res.z] for res in  result.right_hand_landmarks.landmark]).flatten() if result.right_hand_landmarks else np.zeros(63)
    left_hand = np.array([[res.x, res.y, res.z] for res in result.left_hand_landmarks.landmark]).flatten() if result.left_hand_landmarks else np.zeros(63)
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in result.pose_landmarks.landmark]).flatten() if result.pose_landmarks else np.zeros(132)
    return np.concatenate([face, right_hand, left_hand, pose])

#Real Time Detection
sequence = []
sentence = []
word = []
predictions = []
threshold = 0.5
classes = ['Hello', 'How are you', 'Thanks', 'Braai', 'Pap']

capture = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while capture.isOpened():

        ret, frame = capture.read()
        image, results = Media_Pipe_Detection(frame, holistic)
        draw_keypoints(results, image)

        keypoints = collect_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]
        
        #Prediction Logic 
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(classes[np.argmax(res)])
            predictions.append(np.argmax(res))
            
            
        #3. Viz logic
            if np.unique(predictions[-10:])[0]==np.argmax(res): 
                if res[np.argmax(res)] > threshold: 
                    
                    if len(sentence) > 0: 
                        if classes[np.argmax(res)] != sentence[-1]:
                            sentence.append(classes[np.argmax(res)])
                    else:
                        sentence.append(classes[np.argmax(res)])

            if len(sentence) > -1: 
                sentence = sentence[-1:]

        cv2.rectangle(image, (0,0), (220, 40), (0, 52, 255), -1)
        cv2.putText(image, ' '.join(sentence), (3,30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Cam Feed', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
