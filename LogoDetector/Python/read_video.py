
import os
import cv2
import feature_match
import numpy as np
# ---Constants, Tunable params---
# subsample ratio is used to downsize the camera image.
subsamplingRatio = 0.5

# read in folder of images 
fileList = []
  
 # read in folder of images 
cwd = os.getcwd()
folder = cwd + '/files'
for file in os.listdir(folder):
    print file
    filepath = os.path.join(folder, file)
    fileList.append(filepath)

# init vidcap
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:

  # read x frames
  for x in range(0, 10):
    success,image = vidcap.read()
    count += 1

  cv2.waitKey(1)
  

  # read frame
  success,image = vidcap.read()
  #print('Read a new frame %d: ', count, success)

  # resize vidcap img, apply greyscale
  vidFrame = cv2.resize(image, (0, 0), fx=subsamplingRatio, fy=subsamplingRatio)
  vidFrame = cv2.cvtColor(vidFrame, cv2.COLOR_RGB2GRAY)

  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  for x in range(0, len(fileList)):
    # read in template img (img to look for)
    template = cv2.imread(fileList[x],0)  

    #slightly blur template img
    #kernel = np.ones((5,5),np.float32)/25
    #template = cv2.filter2D(template,-1,kernel)

    # shrink img if needed
    height, width = template.shape[:2]
    max_height = 250
    max_width = 250

    # only shrink if img is bigger than required
    if max_height < height or max_width < width:
      # get scaling factor
      scaling_factor = max_height / float(height)
      if max_width/float(width) < scaling_factor:
          scaling_factor = max_width / float(width)
      # resize image
      template = cv2.resize(template, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # match
    feature_match.detect(template, vidFrame, count, False)
    
