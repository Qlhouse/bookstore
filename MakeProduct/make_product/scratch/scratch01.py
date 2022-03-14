import cv2
import imutils
height, width = 800, 900
size = "height" if height > width else "width"

img = cv2.imread("final_img.png", cv2.IMREAD_UNCHANGED)

print(img.shape[:2])
