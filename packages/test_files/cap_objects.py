import cv2 as cv
import numpy as np
from dt_apriltags import Detector

blue_matrix = [2012.2586482532602,2032.1612183033274,959.556055442904,539.4482475170423]
yellow_matrix = [1004.1853533373741,1003.1103206081148,969.3279317187869,487.2596891135381]
green_matrix = [952.93349542,950.89084502,955.39429755,526.05641969]
red_matrix = [1257.0849187162933,1264.2959825648034,891.4609476376864,519.1376957263653]

homo_matrix_blue = np.matrix([[0.003593820427807904, 0.0009335293647671857, 0.8838635335942813], 
                         [0.0001481422640947083, -0.0029053307712818503, 2.136444514595243], 
                         [0.0001643286416833784, 0.0004714120412393716, 1.0]])

homo_matrix_red = np.matrix([[0.0005515797858128073, 0.0033584795861948797, 2.680176319096309], 
                             [0.003398362660694037, 0.0002671371165452805, 1.145174501183925], 
                             [0.0001332704072440824, 0.00010056738010977809, 1.0]])

homo_matrix_yellow = np.matrix([[-0.0044496217906466766, 0.002372276794620305, 5.398570164595315], 
                                [0.002813927028515018, 0.010888234953657172, 2.566912128621428], 
                                [0.000918715545524084, 0.0016612648139417094, 1.0]])

homo_matrix_green = np.matrix([[-5.4122782681711266e-05, -0.002636313037765463, 1.826839694324287], 
                               [-0.0027056071183383344, 0.000151538499647164, 3.3784706699688587], 
                               [-8.847034336522136e-06, 5.199010485918986e-05, 1.0]])

class Caps:
    def __init__(self):
        self.blue_cap = cv.VideoCapture('/dev/video0')
        camera_width = 1200
        camera_height = 1000
        self.blue_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.blue_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.blue_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.blue_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64

        ret,frame = self.blue_cap.read()
        ret,frame = self.blue_cap.read()

        self.red_cap = cv.VideoCapture('/dev/video2')
        camera_width = 1200
        camera_height = 1000
        self.red_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.red_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.red_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.red_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64
        ret,frame = self.red_cap.read()
        ret,frame = self.red_cap.read()

        self.yellow_cap = cv.VideoCapture('/dev/video4')
        camera_width = 1200
        camera_height = 1000
        self.yellow_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.yellow_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.yellow_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.yellow_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64
        ret,frame = self.yellow_cap.read()
        ret,frame = self.yellow_cap.read()

        self.green_cap = cv.VideoCapture('/dev/video6')
        camera_width = 1200
        camera_height = 1000
        self.green_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.green_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.green_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.green_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64
        ret,frame = self.green_cap.read()
        ret,frame = self.green_cap.read()



caps_object = Caps()

detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,refine_edges=1,decode_sharpening=0.25, searchpath=['apriltags'],debug=0)

for i in range(1):
    ret,frame = caps_object.green_cap.read()

if ret == False:
    print("Picture not acquired")

gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
tags = detector.detect(gray,estimate_tag_pose=False,camera_params=blue_matrix,tag_size=0.047)

# Use this section of code to simply print the centers of each apriltag in the u,v plane for the homography calibration ---------------------------------------

# for tag in tags:
#     print(tag.tag_id)
#     print(tag.center)
#     x=tag.center[0]
#     y=tag.center[1]
#     cv.circle(frame,[int(x),int(y)],5,(0,0,255),3)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# This section of code will use a generated homography matrix and do the necessary calculations to find correct x,y coordinates. Use it for testing homography results
for tag in tags:
    tag_matrix = [[tag.center[0]],[tag.center[1]],[1]]
    distance_matrix = np.matmul(homo_matrix_green ,tag_matrix)
    print(f"{tag.tag_id}:\n {distance_matrix[0,0]},{distance_matrix[1,0]},{distance_matrix[2,0]}")
    print(f"Normalized:\n{distance_matrix[0,0]/distance_matrix[2,0]},{distance_matrix[1,0]/distance_matrix[2,0]},{distance_matrix[2,0]/distance_matrix[2,0]}\n\n")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
cv.imwrite('capture.jpg',frame)

