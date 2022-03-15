import cv2
import numpy as np
from PIL import Image

img = cv2.imread("scratch.png", cv2.IMREAD_UNCHANGED)

# You may need to convert the color.
img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
img_rgba[:, :, 3] = img[:, :, 3]
im_pil = Image.fromarray(img_rgba)

im_pil.save("openct2PIL.png")
