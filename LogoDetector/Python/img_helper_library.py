import cv2

def shrinkImg(img, max_h, max_w):
	height, width = img.shape[:2]
	# only shrink if img is bigger than required
	if max_h < height or max_w < width:
		# get scaling factor
		scaling_factor = max_h / float(height)
		if max_w/float(width) < scaling_factor:
		    scaling_factor = max_w / float(width)
		# resize image
		img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        return img