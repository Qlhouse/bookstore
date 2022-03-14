import cv2
import imutils
height, width = 800, 900
size = "height" if height > width else "width"

img = cv2.imread("final_img.png", cv2.IMREAD_UNCHANGED)

frame = imutils.resize(
    img, height=height) if height > width else imutils.resize(img, width=width)

# display the frame to our screen
cv2.imshow("Frame", frame)
cv2.waitKey(0)
