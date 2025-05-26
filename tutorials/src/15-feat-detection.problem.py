# Exercise #15
# ------------
#
# Compute the features of an image with the Harris corner detection. Adjust the parameters using sliders.

import numpy as np
import cv2

def generate_unique_colors(n):
    # Generate evenly spaced hues in HSV color space
    value_range = (0, 256)         # range for each channel [inclusive, exclusive)

    # Generate random array: shape (num_colors, 3)
    return np.random.randint(low=value_range[0], high=value_range[1], size=(n, 3), dtype=np.uint8)


def show_images_side_by_side(img_A, img_B):
    """Helper function to draw two images side by side"""
    total_image = np.concatenate((img_A, img_B), axis=1)
    cv2.imshow(window_name, total_image)
    return


# TODO: Define callback function
"""callback function for the sliders"""
def slider_change(x):
    global window_name
    global img_grey
    global img
    
    # Read slider positions
    number = cv2.getTrackbarPos("Max_Number", window_name)
    quality = cv2.getTrackbarPos("Quality", window_name) / 255
    distance = cv2.getTrackbarPos("Euclidian_Distance", window_name)
    
    #get the features
    features =cv2.goodFeaturesToTrack(img_grey, number, quality, distance, useHarrisDetector=True)

    colors = generate_unique_colors(len(features))
    
    result_image = img.copy()
    #draw circles 
    for i in range(len(features)):
        feature = features[i]
        position = feature[0]
        print(position)    
        
        selection_BGR = (int(colors[i][0]), int(colors[i][1]), int(colors[i][2]))

        # Draw selection color circle
        result_image = cv2.circle(img=result_image, center=(int(position[0]),int(position[1])), radius=5, color=selection_BGR, thickness=2)

        
        
# Show the resulting images in one window using the show_images_side_by_side function
    show_images_side_by_side(img,result_image)
    

# TODO Load example image as color image
img = cv2.imread("./tutorials/data/images/window01.jpg")
img = cv2.resize(img, (512, 512))
# TODO Create a greyscale image for the corner detection
img_grey = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)


# TODO Create window with sliders
# Define a window name
window_name = "Feature Detection"

# TODO Show the resulting images in one window
show_images_side_by_side(img, cv2.cvtColor(img_grey, cv2.COLOR_GRAY2BGR))


# TODO Create sliders for all parameters and one callback function
cv2.createTrackbar("Max_Number", window_name, 1, 1000, slider_change)
cv2.createTrackbar("Quality", window_name, 1, 255, slider_change)
cv2.createTrackbar("Euclidian_Distance", window_name, 1, 255, slider_change)


# Call the function from above to draw the corners into the image
slider_change(0)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
