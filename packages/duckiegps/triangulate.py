from dt_apriltags import Detector
import cv2 as cv
import numpy as np
from params_matrices import homo_matrix_blue,homo_matrix_green,homo_matrix_red,homo_matrix_yellow
import time
from threading import Thread
from results import Results
from cap_objects import Caps

TAG_SIZE = 0.047 # Current size in meters of the Apriltags used by the duckiebots. Not used with the homographies, but relevent if you want to get tag poses.

def scanner_thread(cap:cv.VideoCapture, matrix, results: Results):
    ret, frame = cap.read()
    detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,
                        refine_edges=1, decode_sharpening=0.25,searchpath=['apriltags'],debug=0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    car_tags = detector.detect(gray, estimate_tag_pose=False, camera_params=None, tag_size=None)
    if len(car_tags) < 1: # set flags for if any cameras don't have a car in their range 
        return
    elif len(car_tags) >= 1:
        results.has_car = True
        distances_matrices = []
        for tag in car_tags: # Homography calculations are done here
            tag_matrix = [[tag.center[0]],[tag.center[1]],[1]]
            distance_matrix = np.matmul(matrix,tag_matrix)
            normalized_matrix = [tag.tag_id, distance_matrix[0,0]/distance_matrix[2,0],distance_matrix[1,0]/distance_matrix[2,0]]
            distances_matrices.append(normalized_matrix)
            results.set_data(float(tag.tag_id),float((distance_matrix[0,0]/distance_matrix[2,0])),float((distance_matrix[1,0]/distance_matrix[2,0])))



def triangulate(caps: Caps):
    BLUE = '/dev/video2'
    GREEN = '/dev/video4'
    YELLOW = '/dev/video0'
    RED = '/dev/video6'

    #Block of code for the threading of the 4 cameras
    threads = [None] * 4
    red_results = Results()
    blue_results = Results()
    green_results = Results()
    yellow_results = Results()

    red_thread = Thread(target=scanner_thread,args=(caps.get_cap(RED),homo_matrix_red,red_results))
    blue_thread = Thread(target=scanner_thread,args=(caps.get_cap(BLUE),homo_matrix_blue,blue_results))
    green_thread = Thread(target=scanner_thread,args=(caps.get_cap(GREEN),homo_matrix_green,green_results))
    yellow_thread = Thread(target=scanner_thread,args=(caps.get_cap(YELLOW),homo_matrix_yellow,yellow_results))
    threads[0] = red_thread
    threads[1] = blue_thread
    threads[2] = green_thread
    threads[3] = yellow_thread

    for t in range(len(threads)):
        threads[t].start()
    for t in range(len(threads)):
        threads[t].join()

    #flatten the results and append them to a master array
    results_objects = [red_results,blue_results,green_results,yellow_results]
    results = []
    for r in results_objects:
        if r.has_car:
            flat_array = [item for sublist in r.location_array for item in sublist]
            results.append(flat_array)
    results_flat = [item for sublist in results for item in sublist] # there may be repeating values/locations if the car was detected by two cameras at once

    return results_flat
           