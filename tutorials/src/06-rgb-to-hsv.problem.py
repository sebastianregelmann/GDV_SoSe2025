# Tutorial #6
# -----------
#
# Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask
# them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does not work
# in RGB color space.

import numpy as np
import cv2
import math

# Print keyboard usage
print("This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.")
print("The masked image shows only the pixels with the given HSV color within \
a given range.")
print("Use h/H to de-/increase the hue.")
print("Use s/S to de-/increase the saturation.")
print("Use v/V to de-/increase the (brightness) value.\n")
print("Double-click an image pixel to select its color for masking.")

# Capture webcam image
cap = cv2.VideoCapture(0)

# Get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))

print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# Drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = 0.6
font = cv2.FONT_HERSHEY_SIMPLEX

# TODO Define  RGB colors as variables
bgrColor = np.array([255, 0, 0], dtype=np.uint8)

# Exemplary color conversion (only for the class), tests usage of cv2.cvtColor
#hsvColor = cv2.cvtColor(bgrColor, cv2.COLOR_BGR2HSV)
# TODO Enter some default values and uncomment
hue = 90
hue_range = 10
saturation = 128
saturation_range = 100
value = 128
value_range = 100


# Callback to pick the color on double click
def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print("New color selected:", (hue, saturation, value))


#create images
cv2.namedWindow("original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("mask", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("masked", cv2.WINDOW_AUTOSIZE)

cv2.setMouseCallback("original", color_picker)
while True:

    # Get video frame (always BGR format!)
    ret, frame = cap.read()
    if ret:
        # Copy image to draw on
        original =  cv2.flip(frame.copy(), 1)
        original_text = original.copy()
        mask = original.copy()
        masked = original.copy()


        # TODO Compute color ranges for display
        min_hsv = (hue - hue_range, saturation - saturation_range, value - value_range)
        max_hsv = (hue + hue_range, saturation + saturation_range, value + value_range)

        selection_hsv_image = np.full((1,1,3), [hue, saturation, value], dtype=np.uint8)
        selection_bgr = cv2.cvtColor(selection_hsv_image, cv2.COLOR_HSV2BGR)[0][0]
        
        # TODO Draw selection color circle and text for HSV values
        original_text = cv2.circle(original_text, (width - 50, height - 50), 30, (int(selection_bgr[0]), int(selection_bgr[1]), int(selection_bgr[2])), -1)
        original_text = cv2.putText(original_text, "H = " + str(hue), (width - 200, height - 75), font, font_size_smaller, [255,0,0], thinner)
        original_text = cv2.putText(original_text, "S = " + str(saturation), (width - 200, height - 50), font, font_size_smaller, [255,0,0],
                          thinner)
        original_text = cv2.putText(original_text, "V = " + str(value), (width - 200, height - 25), font, font_size_smaller, [255,0,0], thinner)

        # TODO Convert to HSV
        hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

        # TODO Create a bitwise mask
        mask = cv2.inRange(hsv,min_hsv, max_hsv)

        # TODO Apply mask
        masked = cv2.bitwise_and(original,original, mask=mask)

        # TODO Show the original image with drawings in one window
        cv2.imshow("original", original_text)

        # TODO Show the masked image in another window
        cv2.imshow("mask",mask)

        # TODO Show the mask image in another window
        cv2.imshow("masked",masked)

        # TODO Deal with keyboard input
        if cv2.waitKey(10) == ord("q"):
            break
    
    else:
        print("Could not start video camera")
        break

cap.release()
cv2.destroyAllWindows()
