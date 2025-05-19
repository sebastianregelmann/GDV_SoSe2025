# Tutorial #9
# -----------
#
# Demonstrating Gaussian blur filter with OpenCV.

import cv2
import numpy as np
import time


# TODO Implement the convolution with opencv
def convolution_with_opencv(image, kernel):
    # Flip the kernel as opencv filter2D function is a
    # Correlation not a convolution
    kernel = cv2.flip(kernel, -1)
    
    # When ddepth=-1, the output image will have the same depth as the source.
    # Run filtering
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


def show_kernel(kernel):
    # Show the kernel as image
    # Note that window parameters have no effect on MacOS
    title_kernel = "Kernel"
    cv2.namedWindow(title_kernel, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_kernel, 300, 300)

    # Scale kernel to make it visually more appealing
    kernel_img = cv2.normalize(kernel, kernel, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    kernel_img = cv2.resize(kernel_img, (300,300), interpolation=cv2.INTER_NEAREST)
    cv2.imshow(title_kernel, kernel_img)
    cv2.waitKey(0)

# Load the image.
image_name = "./tutorials/data/images/smarties01.jpg"
image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)



# TODO Define kernel size
kernel_size = 3

# TODO Define Gaussian standard deviation (sigma). If it is non-positive,
sigma = -1

# TODO Create the kernel with OpenCV
#kernel = cv2.getGaussianKernel(ksize=kernel_size, sigma=sigma, ktype=cv2.CV_32F)
#kernel = kernel * np.transpose(kernel)
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], np.float32)

kernel2 = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]], np.float32)

kernel3 = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]], np.float32)
kernel4 = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]], np.float32)
#kernel = kernel/kernel.sum()

# Visualize the kernel
#show_kernel(kernel)


# Run the convolution and write the resulting image into the result variable
result_1 = convolution_with_opencv(image, kernel)
result_2 = convolution_with_opencv(image, kernel2)
result_3 = convolution_with_opencv(image, kernel3)
result_4 = convolution_with_opencv(image, kernel4)
result = np.add(np.add(np.add(result_1, result_2),result_3), result_4)


# Note that window parameters have no effect on MacOS
title_original = "Original image"
cv2.namedWindow(title_original, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title_original, image)

title_result = "Resulting image"
cv2.namedWindow(title_result, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title_result, result)

cv2.waitKey()