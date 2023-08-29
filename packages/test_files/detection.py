# this is a simple file to detect april tags in images

from dt_apriltags import Detector
import cv2 as cv
import argparse

detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,refine_edges=1,decode_sharpening=0.25, searchpath=['apriltags'],debug=0)

yellow_matrix = [1004.1853533373741,1003.1103206081148,969.3279317187869,487.2596891135381]

frame = cv.imread('derek_capture.jpg')

gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
tags = detector.detect(gray,estimate_tag_pose=True,camera_params=yellow_matrix,tag_size=0.035)
for t in tags:
    print(t.tag_id)
    x=t.center[0]
    y=t.center[1]
    cv.circle(frame,[int(x),int(y)],5,(0,0,255),3)

cv.imwrite('detected.jpg',frame)
