# import opencv
import cv2

# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# startt  web cam
cap = cv2.VideoCapture('videos/school_girl.mp4')

while True:
    # read image from webcam
    respose, color_img = cap.read()



