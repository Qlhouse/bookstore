import cv2
import math
import numpy as np
from os.path import basename

# Install openCV
'''
pip install opencv-python
'''

# Refer to websites
# [learnopencv.com](https://learnopencv.com/edge-detection-using-opencv/)
# [quora.com](https://www.quora.com/How-can-I-detect-an-object-from-static-image-and-crop-it-from-the-image-using-openCV)

#############  Output image information  ##############
def showImageInformation():
    image = cv2.imread(r'C:\Users\xq127\Desktop\Screenshot.jpg')
    print(image.shape)

def detectAngleAndRotateImage():
    pass

#############  Resize image  ################
def resizeDownImage():
    image = cv2.imread(r'C:\Users\xq127\Desktop\bookContent.jpg')

    height, width, channels = image.shape

    # Scale down the image 0.6 times by specifying a single scale factor
    # scaleDown = 1000 / width
    scaleDown = 1000 / height
    resizeDown = cv2.resize(image, None, fx=scaleDown, fy=scaleDown, interpolation=cv2.INTER_AREA)

    '''
    cv2.namedWindow("Scale Down", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Scale Down", resizeDown)
    cv2.waitKey(0)
    '''

    return resizeDown

##### Crop Image #####
def cropImage():
    #  Crop images using OpenCV
    img = cv2.imread(r'C:\Users\xq127\Desktop\cropImage.png')

    # Print dimensions of the image
    print(img.shape)

    # Display the original image
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Slicing to crop the image
    # cropped = img[start_row:end_row, start_col:end_col]
    croppedImage = img[180:280, 25:330]

    # Display the cropped image
    cv2.imshow("cropped", croppedImage)
    cv2.waitKey()
    cv2.destroyAllWindows()

##############  Image Threshold  #################


##############  Edge Detection  ##################
def sobelEdgeDetection():
    img = cv2.imread(r'C:\Users\xq127\Desktop\input_image-1.jpg', flags=0)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)

    # Sobel edge detection
    # Sobel edge detection on the X axis
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                       dx=1, dy=0, ksize=5)

    # Sobel edge detection on the Y axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                       dx=0, dy=1, ksize=5)

    # Sobel edge detection conbined X and Y direction
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                        dx=1, dy=1, ksize=5)

    # Display Sobel edge detection images
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)

    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)

    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)

def cannyEdgeDetection():
    img = cv2.imread(r'C:\Users\xq127\Desktop\input_image-1.jpg', flags=0)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)

    edges = cv2.Canny(image=img_blur, threshold1=20, threshold2=100)

    # Display Canny edge detection image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)


#############  Crop image after edge detected  ##############
def cropImageWithEdgeDetection():
    # Read the image
    # image = cv2.imread(r'C:\Users\xq127\Desktop\bookCrop.jpg')
    image = resizeDownImage()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edged = cv2.Canny(gray, 50, 250)
    # cv2.namedWindow("Edged Image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Egded Image", edged)
    cv2.waitKey(0)

    # Find contours
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)

    # Crop image
    idx = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w > 300 and h > 200:
            idx += 1
            newImage = image[y:y+h, x:x+w]
            cv2.imwrite(str(idx) + '.png', newImage)

###########  Using rectangular crop image  ################
def cropRectangularImage():
    '''
    1. Get contours
    2. Remove contours that are too small or too large in area
    3. Find the min/max x/y over all remaining contours
    4. Use those values to create a rectangle to crop in
    '''

def getContours(img):
    # First make the image 1-bit and get contours
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray, 30, 255, cv2.THRESH_BINARY)

    cv2.imwrite('thresh.jpg', thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    # Filter contours that are too large or small
    size = get_size(img)
    contours = [cc for cc in contours if contourOK(cc, size)]
    return contours

def get_size(img):
    height, width = img.shape[:2]
    return width * height

def contourOK(cc, size=1000000):
    x, y, w, h = cv2.boundingRect(cc)
    if w < 50 or h > 50: return False # Too narrow or wide is bad
    area = cv2.contourArea(cc)
    return area > 200
        
def findBoundaries(img, contours):
    # Margin is the minimum distance from the edges of the image, 
    # as a fraction
    imgHeight, imgWidth = img.shape[:2]
    minx = imgWidth
    miny = imgHeight
    maxx = 0
    maxy = 0

    for cc in contours:
        x, y, w, h = cv2.boundingRect(cc)
        if x < minx: minx = x
        if y < miny: miny = y
        if x + w > maxx: maxx = x + w
        if y + h > maxy: maxy = y + h

    return (minx, miny, maxx, maxy)

def crop(img, boundaries):
    minx, miny, maxx, maxy = boundaries
    return img[miny:maxy, minx:maxx]

def processImage(fname):
    img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
    contours = getContours(img)
    cv2.drawContours(img, contours, -1, (0, 255, 0))
    cv2.imshow("CountourImg", img)
    cv2.waitKey(0)

    bounds = findBoundaries(img, contours)
    cropped = crop(img, bounds)
    if get_size(cropped) < 400: return # Too small
    cv2.imwrite('cropped_' + basename(fname), cropped)

# processImage(r'C:\Users\xq127\Desktop\bookContent2.jpg')

# sobelEdgeDetection()
# cannyEdgeDetection()
# cropImageWithEdgeDetection()
# showImageInformation()
# resizeDownImage()

def contourDetech(image):
    img = cv2.pyrDown(cv2.imread(image, cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

    contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # Find bounding box coordiantes
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (120, 255, 0), 2)

        # Find minimum area
        rect = cv2.minAreaRect(c)
    
        # Calculate coordinates of the minimum area rectangle
        box = cv2.boxPoints(rect)

        # Normalize coordiantes to integers
        box = np.int0(box)

        # draw contours
        cv2.drawContours(img, [box], 0, (255, 0, 0), 3)
        cv2.imshow("contours", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



'''
        cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
        cv2.imshow("contours", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
'''
# contourDetech(r'C:\Users\xq127\Desktop\bookContent2.jpg')

# cropBooks
'''
1. edge images
2. Recognize lines
3. Rotate image by changing lines vertically or horizonly
4. Edge image again
5. Recognize line
6. Crop image by rectangle shaped by lines
'''

def lineDetect():
    # Load image
    filePath = r'C:\Users\xq127\Desktop\bookContent1.jpg'
    src = cv2.imread(cv2.samples.findFile(filePath), cv2.IMREAD_GRAYSCALE)

    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        return -1

    dst = cv2.Canny(src, 20, 200, None, 3)

    # Copy edges to the images that will display the results in BGR
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    cdtsP = np.copy(cdst)

    # Standard Hough Line Transform
    lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))

            cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdtsP, (l[0], l[1]), (l[2], l[3]), 3, cv2.LINE_AA)

    cv2.imshow("Source", src)
    cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv2.imshow("Detected Lines (in red) - Probablilistic Hough Line Transform", cdtsP)

    cv2.waitKey()
    return 0

# lineDetect()

