import cv2 as cv
import time
from dt_apriltags import Detector

cap = cv.VideoCapture('/dev/video6')
camera_width = 1200
camera_height = 1000

cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)

cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0)  # Enable auto-exposure
cap.set(cv.CAP_PROP_AUTO_WB, 1)        # Enable auto-white balance appears to be 0 or 1 value only

cap.set(cv.CAP_PROP_BRIGHTNESS, 0)  # Set brightness to default (0)
cap.set(cv.CAP_PROP_CONTRAST, 32)    # Set contrast to default (1)
cap.set(cv.CAP_PROP_SATURATION, 64)  # Set saturation to default (1)
cap.set(cv.CAP_PROP_WHITE_BALANCE_BLUE_U, -1)  # Set white balance to default (0)
detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,refine_edges=1,decode_sharpening=0.25, searchpath=['apriltags'],debug=0)

while(1):
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    tags = detector.detect(gray,estimate_tag_pose=False,camera_params=None,tag_size=None)
    tags_list = []
    for t in tags:
        tags_list.append(t.tag_id)
        # x=t.center[0]
        # y=t.center[1]
        # cv.circle(frame,[int(x),int(y)],5,(0,0,255),3)
    # cv.imshow('camera',frame)
    # if cv.waitKey(1):
    #     break
    print(tags_list)
# cv.destroyAllWindows()
cap.release