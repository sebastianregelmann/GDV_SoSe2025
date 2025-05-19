# Tutorial #11
# ------------
#
# Geometric transformations a.k.a. image warping.

import numpy as np
import cv2

# Load image and resize for better display
img = cv2.imread("./tutorials/data/images/nl_clown.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)
rows, cols, dims = img.shape

# TODO Define translation matrix for translation about 100 pixels to the right and 50 up
translation_x = 100
translation_y = 50
T_translation = np.float32([[1, 0, translation_x], [0, 1, translation_y]])

# A pretty print for the matrix:
print("\nTranslation\n", "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_translation]))

# TODO Apply translation matrix on image using cv2.warpAffine
dst_translation = cv2.warpAffine(img, T_translation,(int(cols + translation_x), int(rows + translation_y)))

# TODO Define anisotropic scaling matrix that stretches to double length horizontally
# and squeezes vertically to the half height
scale_x = 2
scale_y = 0.5
T_anisotropic_scaling = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])


print(
    "\nAnisotropic scaling\n",
    "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_anisotropic_scaling]),
)

# TODO Apply anisotropic scaling matrix on image using cv2.warpAffine
dst_anisotropic_scaling = cv2.warpAffine(img, T_anisotropic_scaling, (int(cols * scale_x), int(rows * scale_y)))
# TODO Define rotation matrix for 45° clockwise rotation
rotation_angle = -45
rotation_angle = np.deg2rad(rotation_angle)
T_rotation = np.float32([[np.cos(rotation_angle), np.sin(rotation_angle),0], 
                         [-np.sin(rotation_angle), np.cos(rotation_angle),0]])

print("\nRotation\n", "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_rotation]))

# TODO Apply rotatio matrix on image using cv2.warpAffine

dst_rotation = cv2.warpAffine(img, T_rotation, (int(cols), int(rows)))

# TODO Rotate around image center for 45° counterclockwise using cv2.getRotationMatrix2D
rotation_angle = 45
T_rotation_around_center = cv2.getRotationMatrix2D((int(cols/2), int(rows/2)),rotation_angle, 1)
dst_rotation_around_center = cv2.warpAffine(img, T_rotation_around_center, (int(cols), int(rows)))

print(
    "\nRotation around center\n",
    "\n".join(["\t".join(["%03.3f" % cell for cell in row]) for row in T_rotation_around_center]),
)

# TODO Apply rotatio matrix on image using cv2.warpAffine
rotation_angle = 30
rotation_angle = np.deg2rad(rotation_angle)

#define all matricies
T_translate_to_center = np.float32([[1, 0,-cols/2], [0,1,-rows/2], [0,0,1]])
T_rotation = np.float32([[np.cos(rotation_angle), np.sin(rotation_angle),0], 
                         [-np.sin(rotation_angle), np.cos(rotation_angle),0],[0,0,1]])
T_translate_back = np.float32([[1, 0,cols/2], [0,1,rows/2],[0,0,1]])
#combine matrizen
T_whole_transformation = np.matmul(np.matmul(T_translate_back, T_rotation), T_translate_to_center)
#convert 3x3 matrix to 3x2 matrix
T_whole_transformation = T_whole_transformation[:2, :]
#transform image
dst_rotation_around_center_custom = cv2.warpAffine(img, T_whole_transformation, (int(cols), int(rows)))

# Show the original and resulting images
cv2.imshow("Original", img)
cv2.imshow("Translation", dst_translation)
cv2.imshow("Anisotropic scaling", dst_anisotropic_scaling)
cv2.imshow("Rotation", dst_rotation)
cv2.imshow("Rotation around center", dst_rotation_around_center)
cv2.imshow("Rotation around center Custom", dst_rotation_around_center_custom)


# Keep images open until key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
