import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
import pyttsx3

def detect_color():
    # Capture an image of a face
    image_path = face_capture_image()
    
    # Check if the image capture was successful
    if image_path is None:
        print("Error: Could not capture face image")
        return
    
    # Load the captured image
    frame = cv2.imread(image_path)
    
    # Define common colors and their ranges
    common_colors = {
        # Define your common colors and their ranges here...
    }
    
    # Convert the image to HSV format
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Initialize an empty mask
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)

    # Initialize a dictionary to store the frequency of each detected color
    color_frequency = {}

    # Iterate through each common color
    for color, (lower, upper) in common_colors.items():
        lower_color = np.array(lower)
        upper_color = np.array(upper)

        # Create a mask for the current color range
        color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Combine the current mask with the overall mask
        mask = cv2.bitwise_or(mask, color_mask)

        # Check if any pixels of the current color are present in the frame
        if cv2.countNonZero(color_mask) > 0:
            if color in color_frequency:
                color_frequency[color] += 1
            else:
                color_frequency[color] = 1

    # Print the most prominent color in the terminal
    if color_frequency:
        most_prominent_color = max(color_frequency, key=color_frequency.get)
        return most_prominent_color
    


def text_capture_image():
    cap = cv2.VideoCapture(0)

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



def face_capture_image():
    cap = cv2.VideoCapture(0)

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
    image_path = 'img_temp.png'
    cv2.imwrite(image_path, frame)

    return image_path

def play_sound(sound):
    filename = f'sounds/{sound}.wav'  
    data, samplerate = sf.read(filename)
    # Play the Apple sound
    sd.play(data, samplerate, blocking=True)
    
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.5)  

    engine.say(text)
    engine.runAndWait()