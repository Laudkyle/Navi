from deepface import DeepFace
import cv2 as cv

cap = cv.VideoCapture(0)
counter =100

while counter >=1:
    ret, frame =  cap.read()
    counter -=1
    


cv.imwrite("people/temp.png",frame)

cap.release()

analysis = DeepFace.analyze(img_path = "people/temp.jpg", actions = ["gender", "emotion"]) 
print(analysis)

verification = DeepFace.verify(img1_path = "people/temp.jpg", img2_path = "people/temp1.jpg")
print(verification)

# def detect_person():
#     cap = cv.VideoCapture(0)
#     counter =100
#     while counter >= 1:
#         ret, frame =  cap.read()
#         counter -=1
#     cv.imwrite("temp.jpg",frame)
#     cap.release()
    