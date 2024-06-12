import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
import pyttsx3
from sklearn.cluster import KMeans



def detect_color_1():
    # Capture an image 
    image_path = text_capture_image()
    
    # Check if the image capture was successful
    if image_path is None:
        speak("Error: Could not capture the image")
        return
    
    # Load the captured image
    frame = cv2.imread(image_path)
    
    # Common colors and their ranges
    common_colors = {
        'Red': ([0, 100, 100], [10, 255, 255]),
        'Red': ([160, 100, 100], [179, 255, 255]), 
        'Orange': ([11, 100, 100], [25, 255, 255]),
        'Yellow': ([26, 100, 100], [35, 255, 255]),
        'Green': ([36, 100, 100], [85, 255, 255]),
        'Cyan': ([86, 100, 100], [95, 255, 255]),
        'Blue': ([96, 100, 100], [125, 255, 255]),
        'Purple': ([126, 100, 100], [145, 255, 255]),
        'Magenta': ([146, 100, 100], [159, 255, 255]),
        'White': ([0, 0, 200], [179, 30, 255]),
        'Gray': ([0, 0, 70], [179, 30, 200]),
        'Black': ([0, 0, 0], [179, 255, 69]),
        'Pink': ([145, 100, 100], [179, 255, 255])
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
    
def detect_color(num_clusters=3):
    # Capture an image 
    image_path = text_capture_image()
    
    # Check if the image capture was successful
    if image_path is None:
        speak("Error: Could not capture face image")
        return None
    
    # Load the captured image
    frame = cv2.imread(image_path)
    if frame is None:
        speak("Error loading image")
        return None
    
    # Convert the image to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Reshape the image to be a list of pixels
    pixels = frame_rgb.reshape((-1, 3))

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)

    # Get the cluster centers (the dominant colors)
    colors = kmeans.cluster_centers_
    counts = np.bincount(kmeans.labels_)

    # Find the most dominant colors
    sorted_indices = np.argsort(counts)[::-1][:num_clusters]
    dominant_colors = [colors[idx].astype(int) for idx in sorted_indices]

    # Define common colors and their RGB values
    common_colors = {
        'Red': [255, 0, 0],
        'Orange': [255, 165, 0],
        'Yellow': [255, 255, 0],
        'Green': [0, 255, 0],
        'Cyan': [0, 255, 255],
        'Blue': [0, 0, 255],
        'Purple': [128, 0, 128],
        'Magenta': [255, 0, 255],
        'White': [255, 255, 255],
        'Gray': [128, 128, 128],
        'Black': [0, 0, 0],
        'Pink': [255, 192, 203],
        'LightBlue': [173, 216, 230],
        'LightGreen': [144, 238, 144],
        'DarkRed': [139, 0, 0],
        'DarkBlue': [0, 0, 139],
        'DarkGreen': [0, 100, 0],
        'Brown': [165, 42, 42],
        'DarkOrange': [255, 140, 0],
        'Gold': [255, 215, 0],
        'DarkMagenta': [139, 0, 139],
        'Indigo': [75, 0, 130],
        'Lime': [0, 255, 0],
        'Olive': [128, 128, 0],
        'Teal': [0, 128, 128],
        'Navy': [0, 0, 128],
        'Silver': [192, 192, 192],
        'Maroon': [128, 0, 0],
        'Violet': [238, 130, 238],
        'SkyBlue': [135, 206, 235],
        'Turquoise': [64, 224, 208],
        'Salmon': [250, 128, 114],
        'Khaki': [240, 230, 140],
        'Lavender': [230, 230, 250],
        'Beige': [245, 245, 220],
        'Coral': [255, 127, 80],
        'HotPink': [255, 105, 180],
        'Crimson': [220, 20, 60],
        'DarkCyan': [0, 139, 139],
        'Aquamarine': [127, 255, 212],
        'Orchid': [218, 112, 214],
        'Thistle': [216, 191, 216],
        'MintCream': [245, 255, 250],
        'Seashell': [255, 245, 238],
        'Peru': [205, 133, 63],
        'Sienna': [160, 82, 45],
        'Moccasin': [255, 228, 181],
        'PapayaWhip': [255, 239, 213],
        'OldLace': [253, 245, 230],
        'Linen': [250, 240, 230],
        'PeachPuff': [255, 218, 185],
        'MistyRose': [255, 228, 225],
        'LightSalmon': [255, 160, 122],
        'AntiqueWhite': [250, 235, 215],
        'BurlyWood': [222, 184, 135],
        'DarkSlateGray': [47, 79, 79],
        'DarkOliveGreen': [85, 107, 47],
        'ForestGreen': [34, 139, 34],
        'LimeGreen': [50, 205, 50],
        'MediumSeaGreen': [60, 179, 113],
        'SpringGreen': [0, 255, 127],
        'MediumTurquoise': [72, 209, 204],
        'RoyalBlue': [65, 105, 225],
        'MediumPurple': [147, 112, 219],
        'Chocolate': [210, 105, 30],
        'RosyBrown': [188, 143, 143],
        'PaleVioletRed': [219, 112, 147],
        'SlateBlue': [106, 90, 205]
    }

    # Function to calculate the Euclidean distance between two colors
    def color_distance(color1, color2):
        return np.linalg.norm(np.array(color1) - np.array(color2))

    closest_color_names = []
    for dominant_color in dominant_colors:
        closest_color_name = min(common_colors, key=lambda name: color_distance(common_colors[name], dominant_color))
        closest_color_names.append(closest_color_name)

    return closest_color_names





def face_capture_image():

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_EXPOSURE, 0.5)  # Example: set exposure to 50%
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)  # Example: set brightness to 50%
    cap.set(cv2.CAP_PROP_CONTRAST, 1)  # Example: increase contrast by 20%
    # cap.set(cv2.CAP_PROP_SATURATION, 1.5)  
    # cap.set(cv2.CAP_PROP_WHITE_BALANCE_RED_V, 1)
    # cap.set(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, 1)

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
    
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.5)  

    engine.say(text)
    engine.runAndWait()