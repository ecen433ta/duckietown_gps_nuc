from dt_apriltags import Detector
import cv2 as cv
import numpy as np
from params_matrices import red_matrix, blue_matrix, green_matrix, yellow_matrix, origin_matrix
import time
from threading import Thread
from tag_locations import return_fixed_loc
from results import Results, Final_List, Num_Matrix
from cap_objects import Caps

TAG_SIZE = 0.047

def scanner_thread(cap:cv.VideoCapture, matrix, results: Results):
    ret, frame = cap.read()
    detector = Detector(families="tagStandard41h12",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,
                        refine_edges=1, decode_sharpening=0.25,searchpath=['apriltags'],debug=0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    tags = detector.detect(gray, estimate_tag_pose=True, camera_params=matrix, tag_size=TAG_SIZE)
    car_tags = []
    fixed_tags = []
    car_matrices = []
    for t in tags:
        if t.tag_id < 100:
            car_tags.append(t)
        else:
            fixed_tags.append(t)
    fixed_tag = fixed_tags[0] # we only need one. This is just so it doesnt break if there are two
    r = fixed_tag.pose_R
    t = fixed_tag.pose_t
    cam_tag_matrix = np.matrix([[r[0,0],r[0,1],r[0,2],t[0,0]],
                            [r[0,0],r[1,1],r[1,2],t[1,0]],
                            [r[2,0],r[2,1],r[2,2],t[2,0]],
                            [0,0,0,1]])
    

    

    tag_cam_matrix = np.linalg.inv(cam_tag_matrix)

    
    
    if len(car_tags) < 1: # set flags for if any cameras don't have a car in their range 
        return
    elif len(car_tags) >= 1:
        results.has_car = True

        for tag in car_tags:
            r = tag.pose_R
            t = tag.pose_t
            matrix = np.matrix([[r[0,0],r[0,1],r[0,2],t[0,0]],
                                [r[0,0],r[1,1],r[1,2],t[1,0]],
                                [r[2,0],r[2,1],r[2,2],t[2,0]],
                                [0,0,0,1]])
            car_matrices.append(Num_Matrix(tag.tag_id,matrix))
        
        print("Cam to Car Matrix:\n\n\n")
        print(matrix)
        print("\n\n\n")

        for i in car_matrices:
            tag_car_matrix = np.matmul(tag_cam_matrix,i.cam_car_matrix) # multiply the inverse of the cam-to-tag matrix by the cam-to-car matrix to get the tag-to-car matrix
            

            i.set_tag_car_matrix(tag_car_matrix) # 
            origin_car_matrix = np.matmul(return_fixed_loc(fixed_tag.tag_id),i.tag_car_matrix)

            print("Cam to Tag Matrix:\n\n\n")
            print(cam_tag_matrix)
            print("\n\n\n")

            print("Tag to Cam Matrix:\n\n\n")
            print(tag_cam_matrix)
            print("\n\n\n")

            print("Tag to Car Matrix:\n\n\n")
            print(tag_car_matrix)
            print("\n\n\n")

            print("Origin to Car Matrix:\n\n\n")
            print(origin_car_matrix)
            # print(origin_car_matrix.shape)
            # print(type(origin_car_matrix))
            print("\n\n\n")

            results.set_data(i.id,origin_car_matrix[0,3],origin_car_matrix[1,3])



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


    red_thread = Thread(target=scanner_thread,args=(caps.get_cap(RED),red_matrix,red_results))
    blue_thread = Thread(target=scanner_thread,args=(caps.get_cap(BLUE),blue_matrix,blue_results))
    green_thread = Thread(target=scanner_thread,args=(caps.get_cap(GREEN),green_matrix,green_results))
    yellow_thread = Thread(target=scanner_thread,args=(caps.get_cap(YELLOW),yellow_matrix,yellow_results))
    threads[0] = red_thread
    threads[1] = blue_thread
    threads[2] = green_thread
    threads[3] = yellow_thread

    for t in range(len(threads)):
        threads[t].start()
    for t in range(len(threads)):
        threads[t].join()

    # print('red results')
    # print(red_results.location_array)
    # print('blue results')
    # print(blue_results.location_array)
    # print('green results')
    # print(green_results.location_array)
    # print('yellow results')
    # print(yellow_results.location_array)

    #flatten the results and append them to a master array
    results_objects = [red_results,blue_results,green_results,yellow_results]
    results = []
    for r in results_objects:
        if r.has_car:
            flat_array = [item for sublist in r.location_array for item in sublist]
            results.append(flat_array)
    results_flat = [item for sublist in results for item in sublist] # there may be repeating values/locations if the car was detected by two cameras at once
    



    #convert to numpy arrays
    # np_red = np.array(red_array)
    # np_blue = np.array(blue_array)
    # np_green = np.array(green_array)
    # np_yellow = np.array(yellow_array)

    # results_list = np.concatenate(np_red,np_blue,np_green,np_yellow)
    
    # Here will be a function that will take the car pose, and the april tag id numbers to return the x and y locations of the bot relative to the location 
    # final_list = Final_List()

    # for results in results_list:
    #     for car in results.car_tags:
    #         x,y = final_locator(car.pose_t,results.fixed_tags)
    #         car_list = [car.tag_id,x,y]
    #         final_list.add_car(car_data=car_list)

    return results_flat
           