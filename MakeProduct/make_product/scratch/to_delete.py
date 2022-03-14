import cv2
import imutils

# img = cv2.imread("Media/img_download.jpg")
# print(img.shape)
image = cv2.imread("Media/img_contour.png")
img_resized = imutils.resize(image, width=640)

cv2.imwrite("Media/img_resized.png", img_resized)
