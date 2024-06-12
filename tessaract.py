import cv2
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

def text_capture_image():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_EXPOSURE, 0.5)  # Example: set exposure to 50%
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)  # Example: set brightness to 50%
    cap.set(cv2.CAP_PROP_CONTRAST, 1)  # Example: increase contrast by 20%

    if not cap.isOpened():
        print("Error: Could not open video device")
        return None

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        return None

    # Release the webcam
    cap.release()

    # Save the captured frame to an image file
    image_path = 'text_temp.png'
    cv2.imwrite(image_path, frame)

    return image_path

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    return text


# print(extract_text_from_image(text_capture_image()))