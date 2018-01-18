
import os
import cv2
import numpy as np
import sys

import feature_match
import img_helper_library

# ---Constants, Tunable params---
# subsample ratio is used to downsize the camera image.]
subsamplingRatio = 0.5

# read 1 frame every x frames (speed vs number of matches)  
frameDelay = 10

# min required feature matches ( how many feature matches means its a good enough match?)
# 8 seems good, but can inc/dec for different results. 
# Lower means less fussy, but more possibly innacurate matches
# Higher means more fussy, so more accurate matches but less of them
minRequiredMatches = 8

# if we find a match, how many frames forward until we allow a match again?
matchFrameDistanceLimit = 50

# template files
fileList = []

# get passed args
print(sys.argv)
vidName = sys.argv[1]
folder = sys.argv[2]
for file in os.listdir(folder):
    print file
    filepath = os.path.join(folder, file)
    fileList.append(filepath)

# read in folder of images 
#cwd = os.getcwd()
#folder = os.getcwd() + '/files'
#for file in os.listdir(folder):
#    print file
#    filepath = os.path.join(folder, file)
#    fileList.append(filepath)

# init vidcap
vidcap = cv2.VideoCapture(vidName)
success,image = vidcap.read()
count = 0
success = True
while success:

  # 1ms delay
  cv2.waitKey(1)

  # read through x frames, but don't use them (effectively skipping ahead till after our frameDelay)
  for x in range(0, frameDelay):
    success,image = vidcap.read()
    count += 1
  
  if image is None:
	continue
	
  
  # resize vidcap img, apply greyscale
  vidFrame = cv2.resize(image, (0, 0), fx=subsamplingRatio, fy=subsamplingRatio)
  vidFrame = cv2.cvtColor(vidFrame, cv2.COLOR_RGB2GRAY)

  # read in each of our template files
  for x in range(0, len(fileList)):
	
	# read file
    template = cv2.imread(fileList[x],0)  

    #slightly blur template img (optional, don't tend ot see better results')
    #kernel = np.ones((5,5),np.float32)/25
    #template = cv2.filter2D(template,-1,kernel)

	#truncate template img size
    template = img_helper_library.shrinkImg(template, 250, 250 )

    # match
    feature_match.detect(template, vidFrame, count, minRequiredMatches, matchFrameDistanceLimit, True)
