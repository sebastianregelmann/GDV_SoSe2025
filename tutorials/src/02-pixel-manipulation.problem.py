# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
colorImage = cv2.imread(r"tutorials\data\images\chewing_gum_balls01.jpg")
colorImageOriginal = colorImage.copy()
greyImage = cv2.imread(r"tutorials\data\images\chewing_gum_balls01.jpg",cv2.IMREAD_GRAYSCALE)

# TODO Do some print out about the loaded data using type, dtype and shape
print("Color Image:(" + "type" + str(type(colorImage)) + " dtype: " + str(colorImage.dtype) + " shape: " + str(colorImage.shape) +")")
print("Grey Image:(" + "type" + str(type(greyImage)) + " dtype: " + str(greyImage.dtype) + " shape: " + str(greyImage.shape) +")")

# TODO Continue with the grayscale image
# TODO Extract the size or resolution of the image
width = greyImage.shape[0]
height = greyImage.shape[1]
print("Width: " + str(width) + " Height: " + str(height))

# TODO Resize image
newWidth = int(width / 2)
newHeight = int(height /2)
greyImage = cv2.resize(greyImage, (newWidth, newHeight))

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
print("Row: ")
print(greyImage[0])

# TODO Print first column
print("Column: ")
print(greyImage[:,0])

# TODO Continue with the color image
# TODO Set an area of the image to black
rectangleStart = [50, 80]
rectangleEnd = [250, 180]
for x in range(rectangleEnd[0] - rectangleStart[0]):
    xPos = rectangleStart[0] + x
    for y in range(rectangleEnd[1] - rectangleStart[1]):
        yPos = rectangleStart[1] + y
        colorImage[yPos][xPos] = [0, 0, 0]

# TODO Show the image and wait until key pressed
cv2.imshow("ColorImage", colorImage)
cv2.waitKey(0)

# TODO Find all used colors in the image
all_rgb_codes = colorImage.reshape(-1, colorImage.shape[-1])
colors = np.unique(all_rgb_codes, axis=0, return_counts=False)
print("Colors: " + str(colors))

# TODO Copy one part of an image into another one
copySize = [90, 120]
copyFromPosition = [100,120]
copyToPosition = [400, 400]
copyData = colorImage[copyFromPosition[1]:copyFromPosition[1] + copySize[1], copyFromPosition[0]: copyFromPosition[0]+ copySize[0]]
colorImage[copyToPosition[1]:copyToPosition[1] + copySize[1], copyToPosition[0]: copyToPosition[0]+ copySize[0]] = copyData

# TODO Save image to a file
#cv2.imwrite(filename=r"C:\Users\sebas\Desktop\GDV\GDV_SoSe2025\Test\test.jpg", img=image)

# TODO Show the image again
cv2.imshow("ColorImage", colorImage)

# TODO Show the original image (copy demo)
cv2.imshow("Original Color Image", colorImageOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows()