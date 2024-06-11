import os
import cv2
from deepface import DeepFace

def load_known_faces(folder):
    known_faces = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                name = os.path.splitext(filename)[0]
                known_faces.append((name, img))
            else:
                print(f"Error loading image {img_path}")
    return known_faces

def recognize_faces(unknown_img, known_faces):
    recognized_names = []
    for name, known_img in known_faces:
        try:
            result = DeepFace.verify(unknown_img, known_img, model_name='VGG-Face', enforce_detection=False)
            if result["verified"]:
                recognized_names.append(name)
        except Exception as e:
            print(f"Error verifying with {name}: {str(e)}")
    return recognized_names

def recognize_face_from_image(image_path, known_faces_folder="people/"):
    known_faces = load_known_faces(known_faces_folder)
    if not known_faces:
        print("No known faces found.")
        return []

    unknown_img = cv2.imread(image_path)
    if unknown_img is None:
        print(f"Error loading image {image_path}")
        return []

    return recognize_faces(unknown_img, known_faces)
