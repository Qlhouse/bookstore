# [Install OpenCV 4.3.0 from source](https://bleedai.com/installation-of-opencv-4-3-0-in-windows-10-from-source-with-nvidia-gpu-support-non-free-flags-enabled/)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from cv2 import dnn_superres

# [TODO] Refactor classes for each model
# Create an SR object, create the dnn_superres constructor
sr = dnn_superres.DnnSuperResImpl_create()

# Read the image
image = cv2.imread("Media/afterRmBg2.png")

# Define model path, if you want to use a different model
# then just change the path.
model_path = "Model/EDSR_x4.pb"

# Extract model name, get the text between '/' and '_'
model_name = model_path.split('/')[1].split('_')[0].lower()

# Extract model scale
model_scale = int(model_path.split('/')[1].split('_')[1].split('.')[0][1])

# Display the name and scale
print("Model name: " + model_name)
print("Model scale: " + str(model_scale))

# Read the desired model
sr.readModel(model_path)

# Set the desired model and scale to get correct
# pre-processing and post-processing
sr.setModel(model_name, model_scale)

start_time = time.time()
# Upscale the image
final_img = sr.upsample(image)

elapsed = time.time() - start_time
print(elapsed)

cv2.imwrite("Media/book_EDSR.png", final_img)
cv2.imwrite("Media/book_EDSR.jpg", final_img)
