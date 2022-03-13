import cv2


# A vast majority of images are 8-bits per channel images.
# They can be read using default flags
img = cv2.imread('Media/afterRmBg2.jpg')

# Read as 8-bit Grayscale image
img = cv2.imread('Media/afterRmBg2.jpg', cv2.IMREAD_GRAYSCALE)


# Most digital SLR cameras are capable of recording images at
# a higher bit depth than 8-bits / channel. The raw images
# from these cameras can be converted to 16-bit / channel PNG
# or TIFF images. These 16-bit / channel images can be read
# using IMREAD_ANYCOLOR or IMREAD_ANYDEPTH flag
img = cv2.imread('Media/afterRmBg2.png',
                 cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

# A transparent image has four channels —— 3 for color, and one
# for transparency. These images can be read in OpenCV using
# the IMREAD_UNCHANGED flag
img = cv2.imread('Media/afterRmBg2.png', cv2.IMREAD_UNCHANGED)
