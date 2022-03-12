import cv2

img = cv2.imread('Media/afterRmBg2.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)

# Convert img color to BGRA

# Convert img color to BGRA

cv2.imwrite("img_contour.png", img)
