import cv2

# A transparent image has four channels —— 3 for color, and one
# for transparency. These images can be read in OpenCV using
# the IMREAD_UNCHANGED flag
img = cv2.imread('Media/afterRmBg2.png', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(
    img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(img, (x, y), (x+w, y+h), (200, 0, 0), 2)

# Convert img color to BGRA

# Convert img color to BGRA

cv2.imwrite("img_contour.png", img)
