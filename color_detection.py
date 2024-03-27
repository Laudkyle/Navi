import numpy as np
import cv2 as cv

# Global variables to store HSV values
clicked_hsv = None

def callback(X):
    pass

def mouse_callback(event, x, y, flags, param):
    global clicked_hsv

    if event == cv.EVENT_LBUTTONDOWN:
        clicked_hsv = img[y, x]
        print("Clicked HSV:", clicked_hsv)

# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Creating the trackbar used for altering the mask
cv.namedWindow("Tracker")
cv.setMouseCallback("Tracker", mouse_callback)

cv.createTrackbar("lH", "Tracker", 0, 255, callback)
cv.createTrackbar("lS", "Tracker", 0, 255, callback)
cv.createTrackbar("lV", "Tracker", 0, 255, callback)
cv.createTrackbar("uH", "Tracker", 255, 255, callback)
cv.createTrackbar("uS", "Tracker", 255, 255, callback)
cv.createTrackbar("uV", "Tracker", 255, 255, callback)

while True:
    lH = cv.getTrackbarPos("lH", "Tracker")
    lS = cv.getTrackbarPos("lS", "Tracker")
    lV = cv.getTrackbarPos("lV", "Tracker")
    
    uH = cv.getTrackbarPos("uH", "Tracker")
    uS = cv.getTrackbarPos("uS", "Tracker")
    uV = cv.getTrackbarPos("uV", "Tracker")
    
    lb = np.array([lH, lS, lV])
    ub = np.array([uH, uS, uV])
    
    # Create a range of colors within the specified HSV range
    lower_bound = np.array([lH, lS, lV])
    upper_bound = np.array([uH, uS, uV])

    # Create a gradient of colors from lower_bound to upper_bound
    color_gradient = np.tile(np.linspace(lower_bound, upper_bound, 1000, endpoint=True), (500, 1, 1))

    # Fill the image with the color gradient
    img = cv.cvtColor(color_gradient.astype(np.uint8), cv.COLOR_HSV2BGR)

    cv.imshow("Color Tracker", img)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
