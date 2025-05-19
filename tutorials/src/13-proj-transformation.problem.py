# Tutorial #12
# ------------
#
# Click three points in two images and compute the appropriate affine transformation. Inspired by
# https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

import numpy as np
import cv2

# Define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []

circle_colors = [(0,255,0), (255,0,0), (0,0,255), (255,255,0)]


# TODO Define one callback functions for each image window
def click_src(event, x, y, flags, param):
    # Grab references to the global variables
    global ref_pt_src
    global img
    global circle_colors
    # If the left mouse button was clicked, add the point to the source array
    if  event== cv2.EVENT_LBUTTONDBLCLK:
        
    # in if block: Draw a circle around the clicked point
        img = cv2.circle(img, (x, y), 8, circle_colors[len(ref_pt_src)], 2)        
        ref_pt_src.append((x,y))

    # in if block: Redraw the image
        cv2.imshow("Original", img)


def click_dst(event, x, y, flags, param):
    # Grab references to the global variables
    global ref_pt_dst
    global dst_img
    # If the left mouse button was clicked, add the point to the source array
    if  event== cv2.EVENT_LBUTTONDBLCLK:
        
    # in if block: Draw a circle around the clicked point
        dst_img = cv2.circle(dst_img, (x, y), 8, circle_colors[len(ref_pt_dst)], 2)        
        ref_pt_dst.append((x,y))

    # in if block: Redraw the image
        cv2.imshow("Transformed", dst_img)

# Load image and resize for better display
img = cv2.imread("./tutorials/data/images/test.jpg", cv2.IMREAD_COLOR)
#img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

# Helper variables and image clone for reset
rows, cols, dim = img.shape
clone = img.copy()
dst_img = np.zeros(img.shape, np.uint8)
# TODO Initialize windows including mouse callbacks
cv2.imshow("Original", img)
cv2.imshow("Transformed", dst_img)
cv2.setMouseCallback("Original", click_src)

# Keep looping until the 'q' key is pressed
computationDone = False
src_points_selected = False
dst_points_selected = False


def emptyMethod(event, x, y, flags, param):#
    pass

while True:
    #check if all src points are selected
    if len(ref_pt_src) == 4 and src_points_selected == False:
        src_points_selected = True
        cv2.setMouseCallback("Transformed", click_dst)
        cv2.setMouseCallback("Original", emptyMethod)


    if len(ref_pt_dst) == 4 and dst_points_selected == False:
        dst_points_selected = True
        cv2.setMouseCallback("Transformed", emptyMethod)

        
    # TODO Change the condition to check if there are three reference points clicked
    if src_points_selected and dst_points_selected and computationDone == False:
        # TODO Compute the transformation matrix (using cv2.getAffineTransform)
        src_pts = np.array(ref_pt_src, dtype=np.float32)
        dst_pts = np.array(ref_pt_dst, dtype=np.float32)
        matrix = cv2.getPerspectiveTransform(src_pts,dst_pts, solveMethod=cv2.DECOMP_SVD)
        
        # TODO print its values
        print(matrix)
        
        # TODO and apply it with cv2.warpAffine
        dst_img = cv2.warpPerspective(img, matrix, (cols, rows))

        # TODO Display the image and wait for a keypress
        cv2.imshow("Transformed", dst_img)

        computationDone = True
        
        # TODO If the 'r' key is pressed, reset the transformation
        key = cv2.waitKey()
        if key == ord("r"):
            computationDone = False
            src_points_selected = False
            dst_points_selected = False
            ref_pt_dst.clear()
            ref_pt_src.clear()
            img = clone.copy()
            dst_img = np.zeros(img.shape, np.uint8)
            cv2.imshow("Original", img)
            cv2.imshow("Transformed", dst_img)
            cv2.setMouseCallback("Original", click_src)
            cv2.setMouseCallback("Transformed", emptyMethod)
        # TODO If the 'q' key is pressed, break from the loop
        if key == ord("q"):
            break
    cv2.waitKey(1)

cv2.destroyAllWindows()
