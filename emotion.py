import os
import cv2
import numpy as np
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from keras.preprocessing.image import load_img, img_to_array 
from keras.models import  load_model
# import matplotlib.pyplot as plt
import numpy as np
from deepface import DeepFace

# load model
model = DeepFace.build_model("Emotion")

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
        roi_gray = cv2.resize(roi_gray, (224, 224))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion analysis ', resized_img)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows

# import cv2 
# from deepface import DeepFace


# # Load the pre-trained emotion detection model
# model = DeepFace.build_model("Emotion")

# # Define emotion labels
# emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# # Load face cascade classifier
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Start capturing video
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if not ret:
#       break
#     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
#     # Convert frame to grayscale

#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         # Extract the face ROI (Region of Interest)
#         face_roi = gray_frame[y:y + h, x:x + w]

#         # Resize the face ROI to match the input shape of the model
#         resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)

#         # Normalize the resized face image
#         normalized_face = resized_face / 255.0

#         # Reshape the image to match the input shape of the model
#         reshaped_face = normalized_face.reshape(1, 48, 48, 1)

#         # Predict emotions using the pre-trained model
#         preds = model.predict(reshaped_face)[0]
#         emotion_idx = preds.argmax()
#         emotion = emotion_labels[emotion_idx]

#         # Draw rectangle around face and label with predicted emotion
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
#         cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

#     # Display the resulting frame
#     cv2.imshow('Real-time Emotion Detection', frame)

#     # Press 'q' to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture and close all windows
# cap.release()
# cv2.destroyAllWindows()