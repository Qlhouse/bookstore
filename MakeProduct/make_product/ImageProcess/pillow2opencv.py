from PIL import Image
import cv2
import numpy as np

image = Image.open("scratch.png")


def pillow2cv(image):
    """Input pillow mode image, return opencv mode image"""
    # img = cv2.imread("scratch.png", cv2.IMREAD_UNCHANGED)

    img_opencv = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

    # return img_opencv
    cv2.imwrite("img_opencv.png", img_opencv)
    # img_pil.save("openct2PIL.png")


pillow2cv(image)
