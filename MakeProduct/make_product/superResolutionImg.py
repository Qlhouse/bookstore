import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Initialize DNN Module
model = 'Model/super_resolution.onnx'
net = cv2.dnn.readNetFromONNX(model)

# Read image
image = cv2.imread("Media/teenager.jpg")
# print(image.shape)

# Display image
# plt.figure(figsize= &  # 91;10, 10])
#            plt.imshow(image&  # 91;:,:,::-1]);plt.axis("off");

# Process the image
# Create a copy of Image for preprocessing
img_copy = image.copy()

# Resize the image into Required Size
img_copy = cv2.resize(img_copy, (224, 224), cv2.INTER_CUBIC)

# Convert image into YCbCr
image_YCbCr = cv2.cvtColor(img_copy, cv2.COLOR_BGR2YCrCb)

# Split Y, Cb and Cr channel
image_Y, image_Cb, image_Cr = cv2.split(image_YCbCr)

# Convert Y channel into a numpy arrary
img_ndarray = np.asarray(image_Y)

# Reshape the image to (1,1,224,224)
reshaped_image = img_ndarray.reshape(1, 1, 224, 224)

# Convert to float32 and as a normalization step divide the image by 255.0
blob = reshaped_image.astype(np.float32) / 255.0

# Set the processed blob as input to the neural network
net.setInput(blob)

# Perform a forward pass of the image
output = net.forward()

# Post-processing
# Reshape the output and get rid of those extra dimensions
reshaped_output = output.reshape(672, 672)

# Get the image back to the range 0-255 from 0-1
reshaped_output = reshaped_output * 255

# Clip the values so the output is it between 0-255
final_output = np.clip(reshaped_output, 0, 255)

# Resize the Cb and Cr channel according to the output dimension
resized_Cb = cv2.resize(image_Cb, (672, 672), cv2.INTER_CUBIC)
resized_Cr = cv2.resize(image_Cr, (672, 672), cv2.INTER_CUBIC)

# Merge all 3 channels together
final_img = cv2.merge((final_output.astype('uint8'), resized_Cb, resized_Cr))

# Covert back to BGR channel
final_img = cv2.cvtColor(final_img, cv2.COLOR_YCR_CB2BGR)

cv2.imwrite("Media/teenager_SR.jpg", final_img)
