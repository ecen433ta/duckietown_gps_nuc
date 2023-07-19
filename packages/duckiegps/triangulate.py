from dt_apriltags import Detector
import cv2 as cv
import numpy as np
from params_matrices import red_matrix, blue_matrix, green_matrix, yellow_matrix
import time
from threading import Thread
from tag_locations import return_fixed_loc
from results import Results, Final_List

def scanner_loop(cam_num,tag_num):
    cap = cv.VideoCapture(cam_num)
    ret, frame = cap.read()
    fixed_tags = []
    detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,
                        refine_edges=1, decode_sharpening=0.25,searchpath=['apriltags'],debug=0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    tags = detector.detect(gray, estimate_tag_pose=True, camera_params=None, tag_size=0.066)


    for t in tags:
        if int(tag_num) == int(t.tag_id):
            present = True
            x,y = t.center
            pose = t.pose_t
        elif t.tag_id > 100:
            fixed_tags.append(t.tag_id)

    return present, pose, fixed_tags
           

def scanner_thread(cam_num, matrix, results: Results):
    # cap = cv.VideoCapture(cam_num)
    # ret, frame = cap.read()
    frame = cv.imread('images/pic.jpg')
    fixed_tags = []
    detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,
                        refine_edges=1, decode_sharpening=0.25,searchpath=['apriltags'],debug=0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    tags = detector.detect(gray, estimate_tag_pose=True, camera_params=matrix, tag_size=0.035)

    car_tags = []
    fixed_tags = []

    for t in tags:
        if t.tag_id < 100:
            car_tags.append(t)
        else:
            fixed_tags.append(t)

    results.set_data(car_tags=car_tags, fixed_tags=fixed_tags)


def final_locator(pose,tags):
    car_x = pose[0]
    car_y = pose[1]
    tag1_pose = tags[0].pose_t
    tag1_x = tag1_pose[0]
    tag1_y = tag1_pose[1]

    tag2_pose = tags[1].pose_t
    tag2_x = tag2_pose[0]
    tag2_y = tag2_pose[1]

    delta1_x = car_x - tag1_x
    delta1_y = car_y - tag1_y
    delta2_x = car_x - tag2_x
    delta2_y = car_y - tag2_y

    local_tag1_x, local_tag1_y = return_fixed_loc(tags[0].tag_id)
    local_tag2_x, local_tag2_y = return_fixed_loc(tags[1].tag_id)

    middle1_x = local_tag1_x + delta1_x
    middle1_y = local_tag1_y + delta1_y
    middle2_x = local_tag2_x + delta2_x
    middle2_y = local_tag2_y + delta2_y

    final_x = (middle1_x + middle2_x)/2
    final_y = (middle1_y + middle2_y)/2
    return final_x, final_y


def triangulate():
    RED,BLUE,GREEN,YELLOW = range(4)    

    #Block of code for the threading of the 4 cameras
    threads = [None] * 4
    red_results = Results()
    blue_results = Results()
    green_results = Results()
    yellow_results = Results()

    red_thread = Thread(target=scanner_thread,args=(RED,red_matrix,red_results))
    blue_thread = Thread(target=scanner_thread,args=(BLUE,blue_matrix,blue_results))
    green_thread = Thread(target=scanner_thread,args=(GREEN,green_matrix,green_results))
    yellow_thread = Thread(target=scanner_thread,args=(YELLOW,yellow_matrix,yellow_results))
    threads[0] = red_thread
    threads[1] = blue_thread
    threads[2] = green_thread
    threads[3] = yellow_thread

    for t in range(len(threads)):
        threads[t].start()
    for t in range(len(threads)):
        threads[t].join()

    results_list = [red_results,blue_results,green_results,yellow_results]
    
    # Here will be a function that will take the car pose, and the april tag id numbers to return the x and y locations of the bot relative to the location 
    final_list = Final_List()

    for results in results_list:
        for car in results.car_tags:
            x,y = final_locator(car.pose_t,results.fixed_tags)
            car_list = [car.tag_id,x,y]
            final_list.add_car(car_data=car_list)

    return final_list.get_cars()
           