from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import cv2
import time

input_path = 'removeBackground.jpg'
output_path = 'afterRmBg2.png'
padding = 80

# Remove background
# Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
# ImageFile.LOAD_TRUNCATED_IMAGES = True

f = np.fromfile(input_path)
result = remove(f)
img = Image.open(io.BytesIO(result)).convert("RGBA")
# img.save(output_path)

# Convert PIL image to OpenCV image，想先存储再用opencv打开，但试了没影响
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGRA)
cv2.imwrite('img_pil_opencv.png', img)

# Resize image to specific width or height
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def getContours(img, img_contour):
    """
    img: the input image
    img_contour: draw contour on the image
    """
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    object_contour, contour_size = None, 0
    # padding = 50

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > contour_size:
            object_contour = cnt

    peri = cv2.arcLength(object_contour, True)
    approx = cv2.approxPolyDP(object_contour, 0.02 * peri, True)
    print(len(approx))
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 5)
    return x, y, w, h

    # cv2.drawContours(img_contour, object_contour, -1, (255, 0, 255), 7)

# Create trackbar
def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 30, 400, empty)
cv2.createTrackbar("Threshold2", "Parameters", 30, 400, empty)

# DO NOT scale down image, 降低了图片分辨率
# img = ResizeWithAspectRatio(img, height = 1200)
# cv2.imwrite("img_resized.png", img)
# cv2.waitKey(0)
img_blur = cv2.GaussianBlur(img, (5, 5), 1)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGRA2GRAY)

while True:
    # Edge detect, remove noise, find contours
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    img_canny = cv2.Canny(img_gray, threshold1, threshold2)
    
    # Dilation function
    kernel = np.ones((10, 10))
    img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
    
    x, y, w, h = getContours(img_dilation, img_blur)

    cv2.imshow('img', img_blur)
    
    # Mark corners
    # for i in corners:
        # x, y = i.ravel()
        # cv2.circle(img, (x, y), 3, 255, -1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Cut image
        img_cropped = img[y-padding:y+h+padding+1, x-padding:x+w+padding+1]
        # img_cropped = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2BGRA)
        cv2.imwrite("img_contour.png", img_cropped)
        # Resize the cutted image
        # 存储的图片总是黑底的。目前解决办法：存储后，再调用rembg，去除黑底背景，后面有其它方法再改
        # f = np.fromfile("img_contour.jpg")
        # result = remove(img_cropped)
        # img = Image.open(io.BytesIO(result)).convert("RGBA")
        # img.save("img_contour.jpg")
        # Remove background, then save
        break




