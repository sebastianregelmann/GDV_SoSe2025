# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

# TODO Capture webcam image
videCapture = cv2.VideoCapture(0)

# TODO Get camera image parameters from get()
width = int(videCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(videCapture.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# TODO Create a window for the video
windowName = "Video Feed"
window = cv2.namedWindow(windowName,cv2.WINDOW_FREERATIO)

# TODO Start a loop
while True:
# TODO (In loop) read a camera frame and check if that was successful
    frameAvailable,frame = videCapture.read()
    if frameAvailable:
        frame = np.flip(frame, axis=1)

# TODO (In loop) create four flipped tiles of the image
        quaterSize = [int(width/2 - 20), int(height/2)]

        topLeft = frame[0:quaterSize[1], 0:quaterSize[0]]
        topRight = frame[0:quaterSize[1], quaterSize[0]:width]
        bottomLeft = frame[quaterSize[1]: height, 0:quaterSize[0]]
        bottomRight = frame[quaterSize[1]: height, quaterSize[0]:width]

        #flip images
        topLeft = np.flip(topLeft, axis=1)
        topRight = np.flip(topRight, axis=1)
        bottomLeft = np.flip(bottomLeft, axis=1)
        bottomRight = np.flip(bottomRight, axis=1)
        bottomLeft = np.flip(bottomLeft, axis=0)
        bottomRight = np.flip(bottomRight, axis=0)

        #combine images back to one frame
        top_half = np.hstack((topLeft, topRight))
        bottom_half = np.hstack((bottomLeft, bottomRight))
        frame = np.vstack((top_half, bottom_half))

# TODO (In loop) display the image
        cv2.imshow(windowName, frame)
        
# TODO (In loop) press q to close the window and exit the loop
    if cv2.waitKey(10) == ord("q"):
            break
# TODO Release the video capture object and window
videCapture.release()
cv2.destroyAllWindows()