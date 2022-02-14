# [Refer](https://zhuanlan.zhihu.com/p/146706558)

import numpy as np

def conv(image, kernel, mode='same'):
    if mode == 'fill':
        h = kernel.shape[0] // 2
        w = kernel.shape[1] // 2
        image = np.pad(image, ((h, h), (w, w), (0, 0)), 'constant')

    conv_b = _convolve(image[:, :, 0], kernel)

def _convolve(image, kernel):
    h_kernel, w_kernel = kernel.shape
    h_image, w_image = image.shape
    res_h = h_image - h_kernel + 1
    res_w = w_image - w_kernel + 1
    res = np.zeros((res_h, res_w), np.uint8)