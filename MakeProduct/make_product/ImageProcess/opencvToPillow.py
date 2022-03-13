import cv2
import numpy as np
from PIL import Image

img = cv2.imread("path/to/img.png")

# You may need to convert the color.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_pil = Image.fromarray(img)

# For reversing the operation:
im_np = np.asarray(im_pil)