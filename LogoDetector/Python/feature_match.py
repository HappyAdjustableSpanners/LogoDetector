import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# used to remove false positive noise in the brute force match.
matchesThreshold = 0.6

lastFrameMatch = 0

def detect(img1, img2, frameNum, showPlot):
    global lastFrameMatch
    # Initiate SIFT detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    try: 
        matches = bf.match(des1,des2)
    except cv2.Exception:
        print("Oops!  That was no valid number.  Try again...")
        return

    # Sort them in the order of their distance.
    #matches = sorted(matches, key = lambda x:x.distance)

     # Filter the matches
    dist = [m.distance for m in matches]
    thres_dist = (sum(dist) / len(dist)) * matchesThreshold
    matches = [m for m in matches if m.distance < thres_dist]

    numMatches = len(matches)

    if numMatches > 8 and abs(lastFrameMatch - frameNum) > 50:
        print ('lots of matches at frame %d', frameNum)
        fileName = os.getcwd() + '/matches/' + `frameNum` + '.jpg'
        print (fileName)
        cv2.imwrite(fileName, img2)
        lastFrameMatch = frameNum


    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:100], None, flags=2)
	
    if showPlot: 
		cv2.imshow('img', img3)
    #plt.show()
    

