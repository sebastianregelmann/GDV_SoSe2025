# Tutorial #14
# ------------
#
# Compute the edges of an image with the Canny edge detection. Adjust the parameters using sliders.

import numpy as np
import cv2


def show_images_side_by_side(img_A, img_B, img_C):
    """Helper function to draw two images side by side"""
    total_image = np.concatenate((img_A, img_B,img_C), axis=1)
    cv2.imshow(window_name, total_image)
    return


# TODO: Define callback function
"""callback function for the sliders"""
def slider_change(x):
    global window_name
    global img_grey
    global img
    
    # Read slider positions
    blur = cv2.getTrackbarPos("Blur: ", window_name)
    threshold_upper = cv2.getTrackbarPos("Threshold_upper: ", window_name)
    threshold_lower = cv2.getTrackbarPos("Threshold_lower: ", window_name)
    # Blur the image
    blured_image = cv2.GaussianBlur(img_grey,(int(blur), int(blur)), -1)

    # Run Canny edge detection with thresholds set by sliders
    edges = cv2.Canny(blured_image, float(threshold_upper), float(threshold_lower))
# Show the resulting images in one window using the show_images_side_by_side function
    show_images_side_by_side(img,cv2.cvtColor(blured_image, cv2.COLOR_GRAY2BGR) ,cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

    pass
    


# TODO Load example image as grayscale
img = cv2.imread("./tutorials/data/images/test.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# TODO Create window with sliders
# Define a window name
window_name = "Canny edge detection demo"

# TODO Show the resulting images in one window
show_images_side_by_side(img, cv2.cvtColor(img_grey, cv2.COLOR_GRAY2BGR),cv2.cvtColor(img_grey, cv2.COLOR_GRAY2BGR))


# TODO Create trackbars (sliders) for the window and define one callback function
# note that these calls lead to an assertion error as on_change is called once on creation
cv2.createTrackbar("Blur: ", window_name, 1, 150, slider_change)
cv2.createTrackbar("Threshold_lower: ", window_name, 30, 255, slider_change)
cv2.createTrackbar("Threshold_upper: ", window_name, 240, 255, slider_change)


# TODO Initial Canny edge detection result creation
slider_change(0)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
