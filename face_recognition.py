from deepface import DeepFace
import cv2 as cv

cap = cv.VideoCapture(0)
counter =100

while counter >=1:
    ret, frame =  cap.read()
    counter -=1
    


cv.imwrite("people/temp.png",frame)

cap.release()

analysis = DeepFace.analyze(img_path = "people/temp.png", actions = ["age"," gender", "emotion"]) 
print(analysis)

verification = DeepFace.verify(img1_path = "people/temp.png", img2_path = "people/temp.png")
print(verification)

