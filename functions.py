import cv2
import numpy as np
import time


def detect_color():
    cap = cv2.imread('../Navi Env/pic3.jpg')
    common_colors = {
        # "Red": ([0, 0, 0], [0, 255, 255]),
        # "Reddish_Brown": ([0, 255, 125], [0, 255, 125]),
        "Dark_Red": ([0, 255, 60], [0, 255, 175]),
        "Light_Red": ([0, 255, 135], [0, 255, 255]),
        "Blue": ([120, 180, 175], [130, 255, 255]),
        "Sky_Blue": ([80, 90, 170], [130, 180, 255]),
        "Dark_Blue": ([100, 200, 50], [130, 255, 150]),
        "Light_Blue": ([80, 90, 170], [100, 180, 255]),
        "Green": ([50, 130, 0], [75, 255, 255]),
        "Yellow": ([25, 140, 75], [35, 255, 255]),
        "Orange": ([10, 180, 60], [20, 255, 255]),
        "Dark_Orange": ([10, 100, 50], [20, 255, 100]),
        "Light_Orange": ([10, 100, 150], [20, 255, 255]),
        "Purple": ([130, 100, 100], [160, 255, 255]),
        "Dark_Purple": ([130, 100, 50], [160, 255, 100]),
        "Light_Purple": ([130, 100, 150], [160, 255, 255]),
        "Pink": ([160, 80, 200], [170, 255, 255]),
        "Brown": ([0, 150, 50], [10, 255, 200]),
        "Gray": ([0, 0, 30], [180, 0, 160]),
        "Black": ([0, 0, 0], [180, 255, 30]),
        "White": ([0, 0, 200], [180, 30, 255]),
        "Light_White": ([0, 0, 200], [180, 30, 255]),
        "Very_Light_White": ([0, 0, 220], [180, 20, 255]),
        "Beige": ([20, 30, 150], [40, 100, 255]),
        "Dark_Beige": ([20, 30, 100], [40, 100, 200]),
        "Light_Beige": ([20, 30, 200], [40, 100, 255]),
        "Turquoise": ([80, 100, 100], [110, 255, 255]),
        "Dark_Turquoise": ([80, 100, 50], [110, 255, 100]),
        "Light_Turquoise": ([80, 100, 150], [110, 255, 255]),
        "Lavender": ([130, 30, 150], [160, 100, 255]),
        "Dark_Lavender": ([130, 30, 100], [160, 100, 200]),
        "Light_Lavender": ([130, 30, 200], [160, 100, 255]),
        "Cyan": ([80, 100, 100], [110, 255, 255]),
        "Dark_Cyan": ([80, 100, 50], [110, 255, 100]),
        "Light_Cyan": ([80, 100, 150], [110, 255, 255]),
        "Magenta": ([140, 100, 100], [170, 255, 255]),
        "Dark_Magenta": ([140, 100, 50], [170, 255, 100]),
        "Light_Magenta": ([140, 100, 150], [170, 255, 255]),
        "Indigo": ([100, 100, 100], [130, 255, 255]),
        "Dark_Indigo": ([100, 100, 50], [130, 255, 100]),
        "Light_Indigo": ([100, 100, 150], [130, 255, 255]),
        "Maroon": ([0, 100, 50], [10, 255, 100]),
        "Dark_Maroon": ([0, 100, 25], [10, 255, 75]),
        "Light_Maroon": ([0, 100, 75], [10, 255, 150]),
        "Teal": ([80, 100, 50], [110, 255, 100]),
        "Dark_Teal": ([80, 100, 25], [110, 255, 75]),
        "Light_Teal": ([80, 100, 75], [110, 255, 150]),
        "Olive": ([40, 100, 50], [80, 255, 100]),
        "Dark_Olive": ([40, 100, 25], [80, 255, 75]),
        "Light_Olive": ([40, 100, 75], [80, 255, 150]),
        "Coral": ([0, 100, 50], [10, 255, 100]),
        "Dark_Coral": ([0, 100, 25], [10, 255, 75]),
        "Light_Coral": ([0, 100, 75], [10, 255, 150]),
        "Gold": ([20, 100, 50], [40, 255, 100]),
        "Dark_Gold": ([20, 100, 25], [40, 255, 75]),
        "Light_Gold": ([20, 100, 75], [40, 255, 150]),
        "Silver": ([0, 0, 75], [180, 5, 200]),
        "Dark_Silver": ([0, 0, 50], [180, 5, 150]),
        "Light_Silver": ([0, 0, 100], [180, 10, 255]),
        "Bronze": ([20, 100, 30], [40, 255, 75]),
        "Dark_Bronze": ([20, 100, 20], [40, 255, 50]),
        "Light_Bronze": ([20, 100, 40], [40, 255, 100]),
        "Peach": ([0, 50, 150], [20, 100, 255]),
        "Dark_Peach": ([0, 50, 100], [20, 100, 200]),
        "Light_Peach": ([0, 50, 200], [20, 100, 255]),
        "Mint": ([80, 30, 150], [110, 100, 255]),
        "Dark_Mint": ([80, 30, 100], [110, 100, 200]),
        "Light_Mint": ([80, 30, 200], [110, 100, 255]),
        "Lime": ([40, 100, 50], [80, 255, 100]),
        "Dark_Lime": ([40, 100, 25], [80, 255, 75]),
        "Light_Lime": ([40, 100, 75], [80, 255, 150]),
        "Navy": ([100, 100, 50], [130, 255, 100]),
        "Dark_Navy": ([100, 100, 25], [130, 255, 75]),
        "Light_Navy": ([100, 100, 75], [130, 255, 150]),
        "Plum": ([130, 50, 50], [160, 255, 100]),
        "Dark_Plum": ([130, 50, 25], [160, 255, 75]),
        "Light_Plum": ([130, 50, 75], [160, 255, 150]),
        "Violet": ([140, 30, 150], [170, 100, 255]),
        "Dark_Violet": ([140, 30, 100], [170, 100, 200]),
        "Light_Violet": ([140, 30, 200], [170, 100, 255]),
        "Salmon": ([0, 50, 100], [20, 100, 200]),
        "Dark_Salmon": ([0, 50, 75], [20, 100, 150]),
        "Light_Salmon": ([0, 50, 125], [20, 100, 255]),
        "Khaki": ([30, 30, 150], [50, 100, 255]),
        "Dark_Khaki": ([30, 30, 100], [50, 100, 200]),
        "Light_Khaki": ([30, 30, 200], [50, 100, 255]),
        "Ruby": ([0, 100, 50], [10, 255, 100]),
        "Dark_Ruby": ([0, 100, 25], [10, 255, 75]),
        "Light_Ruby": ([0, 100, 75], [10, 255, 150]),
        "Sapphire": ([100, 100, 50], [130, 255, 100]),
        "Dark_Sapphire": ([100, 100, 25], [130, 255, 75]),
        "Light_Sapphire": ([100, 100, 75], [130, 255, 150]),
        "Emerald": ([80, 100, 50], [110, 255, 100]),
        "Dark_Emerald": ([80, 100, 25], [110, 255, 75]),
        "Light_Emerald": ([80, 100, 75], [110, 255, 150]),
        "Amber": ([20, 100, 50], [40, 255, 100]),
        "Dark_Amber": ([20, 100, 25], [40, 255, 75]),
        "Light_Amber": ([20, 100, 75], [40, 255, 150]),
        "Crimson": ([0, 100, 20], [10, 255, 75]),
        "Dark_Crimson": ([0, 100, 10], [10, 255, 50]),
        "Light_Crimson": ([0, 100, 30], [10, 255, 100]),
        "Ivory": ([0, 0, 200], [180, 30, 255]),
        "Dark_Ivory": ([0, 0, 180], [180, 20, 240]),
        "Light_Ivory": ([0, 0, 220], [180, 40, 255]),
        "Lilac": ([140, 30, 150], [170, 100, 255]),
        "Dark_Lilac": ([140, 30, 100], [170, 100, 200]),
        "Light_Lilac": ([140, 30, 200], [170, 100, 255]),
        "Mahogany": ([0, 100, 25], [10, 255, 75]),
        "Dark_Mahogany": ([0, 100, 15], [10, 255, 60]),
        "Light_Mahogany": ([0, 100, 35], [10, 255, 90]),
        "Pearl": ([0, 0, 175], [180, 20, 255]),
        "Dark_Pearl": ([0, 0, 150], [180, 15, 220]),
        "Light_Pearl": ([0, 0, 200], [180, 25, 255]),
        "Slate": ([210, 5, 75], [240, 30, 200]),
        "Dark_Slate": ([210, 5, 50], [240, 25, 175]),
        "Light_Slate": ([210, 5, 100], [240, 40, 255]),
        "Topaz": ([30, 100, 50], [50, 255, 100]),
        "Dark_Topaz": ([30, 100, 25], [50, 255, 75]),
        "Light_Topaz": ([30, 100, 75], [50, 255, 150]),
        "Brick": ([0, 100, 25], [10, 255, 75]),
        "Dark_Brick": ([0, 100, 15], [10, 255, 60]),
        "Light_Brick": ([0, 100, 35], [10, 255, 90]),
        "Rose": ([0, 100, 75], [10, 255, 150]),
        "Dark_Rose": ([0, 100, 60], [10, 255, 135]),
        "Light_Rose": ([0, 100, 90], [10, 255, 165]),
        "Tangerine": ([10, 100, 50], [20, 255, 100]),
        "Dark_Tangerine": ([10, 100, 25], [20, 255, 75]),
        "Light_Tangerine": ([10, 100, 75], [20, 255, 150]),
        "Aqua": ([80, 30, 150], [110, 100, 255]),
        "Dark_Aqua": ([80, 30, 100], [110, 100, 200]),
        "Light_Aqua": ([80, 30, 200], [110, 100, 255]),
        "Cerulean": ([100, 100, 50], [130, 255, 100]),
        "Dark_Cerulean": ([100, 100, 25], [130, 255, 75]),
        "Light_Cerulean": ([100, 100, 75], [130, 255, 150]),
        "Cocoa": ([0, 50, 25], [20, 100, 75]),
        "Dark_Cocoa": ([0, 50, 15], [20, 100, 60]),
        "Light_Cocoa": ([0, 50, 35], [20, 100, 90]),
    }

    while True:
        start_time = time.time()

        while time.time() - start_time < 3:
            frame = cap

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

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
        cv2.imshow("image",frame)
        if color_frequency:
            most_prominent_color = max(color_frequency, key=color_frequency.get)
            print(f"Most Prominent Color: {most_prominent_color}")

    cap.release()
    cv2.destroyAllWindows()


detect_color()
