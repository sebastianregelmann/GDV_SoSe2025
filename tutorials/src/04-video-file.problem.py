# Exercise #4
# -----------
#
# Loading a video file and mirror it.

import numpy as np
import cv2

# TODO Open a video file
video = cv2.VideoCapture(r"tutorials\data\videos\objects_UH.MOV")

# TODO Get camera image parameters from get()
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(video.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))
print("Frame Count =  " + str(frameCount))

# TODO Start a loop
for frameIndex in range(frameCount):
    
# TODO (In loop) read one video frame
    frameAvailable, frame = video.read(frameIndex)

# TODO (In loop) create four tiles of the image
    newWidth = int(width/2)
    newHeight = int(height/2)
    
    topLeft = cv2.resize(frame, (newWidth,newHeight ))
    topRight = cv2.resize(frame, (newWidth, newHeight))
    bottomLeft = cv2.resize(frame, (newWidth, newHeight))
    bottomRight = cv2.resize(frame, (newWidth, newHeight))

# TODO (In loop) show the image
    #combine images back to one frame
    top_half = np.hstack((topLeft, topRight))
    bottom_half = np.hstack((bottomLeft, bottomRight))
    frame = np.vstack((top_half, bottom_half))
    cv2.imshow("Video Playback", frame)
    print("Frame Shape = " + str(frame.shape))
# TODO (In loop) close the window and stop the loop if 'q' is pressed
    if cv2.waitKey(10) == ord("q"):
        cv2.destroyAllWindows()
        break
# TODO Release the video and close all windows
video.release()
cv2.destroyAllWindows()