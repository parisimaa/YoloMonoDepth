'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images.
'''
import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('camera.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame and saving images with 5 intervals
    ret, frame = cap.read()
    # With 'if' statement you can choose the frames you want to save
    if currentFrame % 5 ==0:
        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1
    else: 
        currentFrame += 1
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()