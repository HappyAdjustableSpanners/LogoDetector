import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# used to remove false positive noise in the brute force match.
matchesThreshold = 0.6

# used to ensure we don't read in frame matches right next to each other
lastFrameMatch = 0

def detect(template, vidFrame, frameNum, minRequiredFeatureMatches, matchFrameDistanceLimit, showPlot):
    
	# make sure its global (weird python rule..)
	global lastFrameMatch

    # Initiate ORB detector ( optional params to play with )
	orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
	kp1, des1 = orb.detectAndCompute(template,None)
	kp2, des2 = orb.detectAndCompute(vidFrame,None)

    # create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
	print("template is ")
	print(template)
	print("vidFrame is ")
	print(vidFrame)
	print("des1 is ")
	print(des1)

	print("des2 is ")
	print(des2)

	if(des1 is None or des2 is None):
		return 
	matches = bf.match(des1,des2)
	#except Exception:
	#	print("Oops!  That was no valid number.  Try again...")
	#	return

    # Sort them in the order of their distance.
    #matches = sorted(matches, key = lambda x:x.distance)

     # Get top matches below threshold distance
	dist = [m.distance for m in matches]
	thres_dist = (sum(dist) / len(dist)) * matchesThreshold
	matches = [m for m in matches if m.distance < thres_dist]
	numMatches = len(matches)

	# if we get more than the minimum required feature matches, save the frame
	if numMatches > minRequiredFeatureMatches and abs(lastFrameMatch - frameNum) > matchFrameDistanceLimit:
		print ('lots of matches at frame %d', frameNum)
		fileName = os.getcwd() + '/matches/' + `frameNum` + '.jpg'
		print (fileName)
		cv2.imwrite(fileName, vidFrame)
		lastFrameMatch = frameNum

    # Draw first 10 matches.
	img3 = cv2.drawMatches(template,kp1, vidFrame,kp2,matches[:100], None, flags=2)
	
	if showPlot: 
		cv2.imshow('img', img3)
    #plt.show()
    

