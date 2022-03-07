from superResolutionImg import SR
import cv2

image = cv2.imread("Media/teenager.jpg")
model = 'Model/super_resolution.onnx'

img_super_resolution = SR(image, model).super_resolution()
cv2.imwrite("Media/teenager_SR.jpg", img_super_resolution)
