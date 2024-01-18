from deepface import DeepFace
import cv2 as cv

cap = cv.VideoCapture(1)
counter =100

while counter >=1:
    ret, frame =  cap.read()
    counter -=1
    


cv.imwrite("temp1.jpg",frame)

analysis = DeepFace.analyze(img_path = "temp.jpg", actions = ["age", "gender", "emotion", "race"]) 
print(analysis)
