import cv2


def version_1():
    # load image with alpha channel.  use IMREAD_UNCHANGED to ensure loading of alpha channel
    image = cv2.imread('scratch.png', cv2.IMREAD_UNCHANGED)

    # make mask of where the transparent bits are
    trans_mask = image[:, :, 3] == 0

    # replace areas of transparency with white and not transparent
    image[trans_mask] = [255, 255, 255, 255]

    # new image without alpha channel...
    # new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    cv2.imwrite("replace_transparency.png", image)


def version_2():
    import cv2
    import numpy as np

    src = cv2.imread('scratch.png', cv2.IMREAD_UNCHANGED)

    bgr = src[:, :, :3]  # Channels 0..2
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    # Some sort of processing...

    bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    alpha = src[:, :, 3]  # Channel 3
    result = np.dstack([bgr, alpha])  # Add the alpha channel

    cv2.imwrite('51IgH_result.png', result)


version_2()
