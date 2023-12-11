# Duckietown GPS

This is the code to create the container for the GPS system to be used by the duckiebots. This container is specifically made to be used on the NUC that connects to all the cameras. The program uses homographies to transform coordinates from the camera's view plane to the real-world plane. A list of all detected Apriltags is published in a sequence that follows: id number - x position - y position. This list is sent to the Duckiebots over LCM using the dt-communications-utils library. The list is parsed by the code in the duckiebots.

This repo was based on the duckietown repo found [here](https://github.com/duckietown/template-ros).

**WARNING**
If any of the cameras are moved at all, the homography for the camera will need to be recalibrated.

## How to use it

### 1. Clone Repository

Clone this repository onto the NUC, which can be accessed via ssh.

### 2. Build the image

Build the gps image by running ```dts devel build -f``` from the top directory of the repository if the container needs to be updated or has not yet been built.

### 3. Run the image

To start the container, run the command:
```docker run -it --network host --device /dev/video0 --device /dev/video2 --device /dev/video4 --device /dev/video6 [CONTAINER ID] bash```
where CONTAINER_ID is the ID number displayed by the container when you run the command ```docker image ls```.

### 4. Run the GPS program

Running the 'docker run' command in step 3 will start the image and put you into the terminal. To start the program, use:
```python3 packages/duckiegps/publisher.py```

The program will start to run and print out all the detected Apriltags with their x,y coordinates to the console. If the progam ends abruptly with a
'segmentation fault' error, then simple end and restart the program. It should work just fine after the first restart if the problem arises. If there is a segmentaton fault, it will be within the first 10-15 seconds of program start.


## Test files

The folder 'test_files' that is located right next to the 'duckiegps' directory contains a few files that are used for testing the cameras and data, as well as making the homography matrices. Short descriptions of the files and their functions are in the heading of each file.

## Camera info

All 4 of the webcams are to be set using udev rules for the device that they are on. If the rules are changed for one reason or another, and the cameras are no longer /dev/video0, /dev/video2, /dev/video4, and /dev/video6, then the input will have to be changed for the capture method in the cap_object.py file.

Many variables and matrices in the code are labelled by color, which distinguishes what camera the information is relevent to. Cameras in the duckietown room are distinguished by color with a piece of tape of the respective color on the ceiling right above them.
