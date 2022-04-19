
# Python program to illustrate
# template matching
import cv2
import numpy as np
import time
from PIL import ImageGrab
import pyautogui


# # Read the main image
# img_rgb = cv2.imread('matchImage.jpg')

# # # Convert it to grayscale
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Read the template 
template = cv2.imread('matchImage.jpg', 0)
# Store width and height of template in w and h
w, h = template.shape[::-1]
while(True):
    screen = np.array(ImageGrab.grab())
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2GRAY)

    # Perform match operations.
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.8

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        print(pt)
        pyautogui.moveTo(pt[0], pt[1], duration=1)
        pyautogui.click(pt[0], pt[1])
        time.sleep(5)
        loc = []


    # cv2.imshow('my_screen', screen)
    # press escape to exit
    time.sleep(5)
    if (cv2.waitKey(30) == 27):
        break
cv2.destroyAllWindows()
# # Read the template
# template = cv2.imread('pix.jpg', 0)

# # Store width and height of template in w and h
# w, h = template.shape[::-1]

# # Perform match operations.
# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# # Specify a threshold
# threshold = 0.8

# # Store the coordinates of matched area in a numpy array
# loc = np.where(res >= threshold)

# # Draw a rectangle around the matched region.
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# # Show the final image with the matched area.
# cv2.imshow('Detected', img_rgb)
# print('test')
# cv2.imshow("Something", img_gray)
# cv2.waitKey(0)
