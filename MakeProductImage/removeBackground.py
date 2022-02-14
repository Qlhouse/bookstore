CVZONE = False

if CVZONE:
    import cv2
    import cvzone
    from cvzone.SelfiSegmentationModule import SelfiSegmentation
    import os
    
    source = r'C:\Users\xq127\Desktop\Woman-Running-Sample-Image.jpg'
    img = cv2.imread(source)
    segmentor = SelfiSegmentation()
    
    # while True:
    imgOut = segmentor.removeBG(img, (255, 255, 255), threshold=0.05)
    
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    
    cv2.imshow('Image', imgStacked)
    # cv2.imwrite(r'C:\Users\xq127\Desktop\output.jpg', imgOut)
    cv2.waitKey()

# Step 1
# Gaussian Blur
import numpy as np
import cv2

image_vec = cv2.imread('image', 1)
g_blurred = cv2.GaussianBlur(image_vec, (5, 5), 0)