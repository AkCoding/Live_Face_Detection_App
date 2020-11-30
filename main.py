# import opencv
import cv2

# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# startt  web cam
cap = cv2.VideoCapture('Face.mp4')

while True:
    # read image from webcam
    respose, color_img = cap.read()

    # Convert to grayscale
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray_img, 1.4, 7)