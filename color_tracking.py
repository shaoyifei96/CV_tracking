import numpy as np
import cv2

cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_XI_FRAMERATE))
Lower = (0, 0, 0)
Upper = (359, 359, 50)
blueLower = (100, 68, 68)
blueUpper = (150, 255, 255)
# tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
# tracker_type = tracker_types[1]
# if tracker_type == 'BOOSTING':
#     tracker = cv2.TrackerBoosting_create()
# if tracker_type == 'MIL':
#     tracker = cv2.TrackerMIL_create()
# if tracker_type == 'KCF':
#     tracker = cv2.TrackerKCF_create()
# if tracker_type == 'TLD':
#     tracker = cv2.TrackerTLD_create()
# if tracker_type == 'MEDIANFLOW':
#     tracker = cv2.TrackerMedianFlow_create()
# if tracker_type == 'GOTURN':
#     tracker = cv2.TrackerGOTURN_create()
# ok, frame = cap.read()

# bbox = cv2.selectROI(frame, False)
# Initialize tracker with first frame and bounding box
# print (tracker.init(frame, bbox))

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(rgb, Lower, Upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	for c in cnts:
		((x, y), radius) = cv2.minEnclosingCircle(c)
		print(x,y,radius)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		print(radius)
		if radius > 20:
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
    # Our operations on the frame come here
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
    
	if cv2.waitKey(1) & 0xFF == 27:#press escape to quit
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
