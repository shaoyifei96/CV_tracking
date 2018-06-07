import numpy as np
import cv2

cap = cv2.VideoCapture(0)
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
tracker_type = tracker_types[1]
if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
ok, frame = cap.read()

bbox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
print (tracker.init(frame, bbox))

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	ok,bbox = tracker.update(frame)
	print(ok,'   ', bbox)
	if ok:
		p1 = (int(bbox[0]), int(bbox[1]))
		p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
		cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
	else:
		print('no obj')
    # Our operations on the frame come here
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
	cv2.imshow('frame',frame)
    
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
