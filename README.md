# South African Sign Language Translation
## Project Overview
South African Sign Language is the 12th official language of South Africa. The University of Free State estimates that around 600 000 thousand people in South Africa actually use sign language as a means of communication. This means that the SASL is a minority language in South Africa. I have attempted to bridge the gap between the people who understand sign language and those who do not in South Africa. This project is specifically targeted to translate the recognized South African Sign Language dictionary the SASL. 
## Data Collection Process
The Data Collection Process involved me my webcam and a designated spot to capture data. I stood infront of my webcam and recorded myself doing 400 instances of 5 different SASL phrases resulting in a dataset of 2000 instances across the board. I used the python library CV2 to access my webcam and collect the keypoints of my hands, face and posture which where detected by Google's mediapipe library. Each instance of a phrase consisted of 30 frames that were collected. Here is a visual representation of how my data collection process looked like. Note the keypoints that the python library mediapipe picked up on my body. 


![Untitled video - Made with Clipchamp](https://github.com/Tylikestocode/SASL_Translation/assets/107248071/1ddb2c64-0bce-4494-89d2-8269e6230acf)
## Model Creation and Evaluation 
## Model in Action
## Conclusion
