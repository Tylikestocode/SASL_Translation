# South African Sign Language Translation
## Project Overview
South African Sign Language is the 12th official language of South Africa. The University of Free State estimates that around 600 000 thousand people in South Africa actually use sign language as a means of communication. This means that the SASL is a minority language in South Africa. I have attempted to bridge the gap between the people who understand sign language and those who do not in South Africa. This project is specifically targeted to translate the recognized South African Sign Language dictionary the SASL. 
## Data Collection Process
The Data Collection Process involved me my webcam and a designated spot to capture data. I stood infront of my webcam and recorded myself doing 400 instances of 5 different SASL phrases resulting in a dataset of 2000 instances across the board. I used the python library CV2 to access my webcam and collect the keypoints of my hands, face and posture which where detected by Google's mediapipe library. Each instance of a phrase consisted of 30 frames that were collected. Here is a gif for a  visual representation of how my data collection process looked like. Note the keypoints that the python library mediapipe picked up on my body. 


![Untitled video - Made with Clipchamp](https://github.com/Tylikestocode/SASL_Translation/assets/107248071/1ddb2c64-0bce-4494-89d2-8269e6230acf)
## Model Creation and Evaluation 
For this project because I am working with sequential data in the form of frames and sign language often works in sequences I decided to Implement a Long-Short Term Memory Neural Network to handle this complex task. I created a Deep layered LSTM neural network consisting of 4 LSTM Layers with a total 2.6 million total trainable parameters as shown here below.

<img src="https://github.com/Tylikestocode/SASL_Translation/assets/107248071/fe508a35-89a4-4677-9bb6-3fde794b49b9" width="400">

The Model was trained over 1000 epochs using a custom TensorFlow callback to stop the training after a certain classification accuracy, loss, validation classification accuracy, and validation loss had been reached which I determined to be a classification accuracy of 0.95 and a loss of 0.1. The system only took 25 epochs to train and ended up with a validation classification accuracy of 0.9833 and a validation loss of 0.0583 as shown here below:

<img src="https://github.com/Tylikestocode/SASL_Translation/assets/107248071/21e43ed5-65a5-457a-b7c0-96dd2caed79d" width="400" height="15">


The model was evaluated using the following metrics:
1. Confusion Matrix
2. Accuracy Score

The results of the confusion matrix where graphed and showed the following results:

<img src="https://github.com/Tylikestocode/SASL_Translation/assets/107248071/e4336914-2cb0-4076-9d25-51d8ae2f2314" width="400">

The accuracy score of the model was as follows:

<img src="https://github.com/Tylikestocode/SASL_Translation/assets/107248071/c1a1d162-2cf3-4faa-9b4b-f657695e9373" width="400">

## Model in Action
Here is a video of the actual system in action translating the words Hello and then Braai. I have chosen to add braai to one of the phrases as it is a South African tradition that many of us South Africans enjoy and know it is something that is uniquely special to South Africa and a key indicator to indicate that this is indeed a specialized sign language detection system. 
{insert video}

## Conclusion
This project has taught me a lot about South African Sign Language and the pressing issues that are present within such a minority group, I have gained experience in deep learning and creating real time prediction systems whilst tackling this project. Overall this project was a massive success and also gained a lot of attention at our universities IT showcase. I believe we have the capabilities and technology to create systems to help bridge the gap of communication between the deaf community and the rest of South Africa.
