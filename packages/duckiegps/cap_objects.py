import cv2 as cv
from dt_apriltags import Detector


class Caps:
    def __init__(self):
        self.blue_cap = cv.VideoCapture('/dev/video2')
        camera_width = 1200
        camera_height = 1000
        self.blue_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.blue_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.blue_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.blue_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64

        ret,frame = self.blue_cap.read()
        ret,frame = self.blue_cap.read()

        self.red_cap = cv.VideoCapture('/dev/video4')
        camera_width = 1200
        camera_height = 1000
        self.red_cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
        self.red_cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
        self.red_cap.set(cv.CAP_PROP_BRIGHTNESS, -50)  # Set brightness to default (0) -64 to 64
        self.red_cap.set(cv.CAP_PROP_CONTRAST, 60)    # Set contrast to default (1) - 64 to 64
        ret,frame = self.red_cap.read()
        ret,frame = self.red_cap.read()

        self.yellow_cap = cv.VideoCapture('/dev/video0')
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



    def get_cap(self, port):
        if port == '/dev/video2':
            return self.blue_cap
        elif port == '/dev/video0':
            return self.yellow_cap
        elif port == '/dev/video4':
            return self.green_cap
        elif port == '/dev/video6':
            return self.red_cap