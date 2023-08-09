import cv2 as cv
import time

cap = cv.VideoCapture('/dev/video2')
camera_width = 2560 #1000
camera_height = 1440 #600

cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)

# print(cap.get(cv.CAP_PROP_BRIGHTNESS))
# print(cap.get(cv.CAP_PROP_CONTRAST))
# print(cap.get(cv.CAP_PROP_SATURATION))
# print(cap.get(cv.CAP_PROP_WHITE_BALANCE_BLUE_U))

# Try to set manual exposure (if supported)
# if cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0):  # 0 means manual exposure
#     # Set the exposure time (in seconds)
#     exposure_time = 0.05  # Example: 50 milliseconds
#     cap.set(cv.CAP_PROP_EXPOSURE, exposure_time)

#     # Verify if the exposure setting was successful
#     if cap.get(cv.CAP_PROP_EXPOSURE) == exposure_time:
#         print(f"Exposure time set to {exposure_time} seconds.")
#     else:
#         print("Exposure time setting failed.")
# else:
#     print("Camera does not support manual exposure control.")
#     print(cap.get(cv.CAP_PROP_EXPOSURE))

# cap.set(cv.CAP_PROP_BRIGHTNESS, 0)  # Set brightness to default (0) -64 to 64
# cap.set(cv.CAP_PROP_CONTRAST, 32)    # Set contrast to default (1) - 64 to 64
# cap.set(cv.CAP_PROP_SATURATION, 64)  # Set saturation to default (1) 1 to 128
# cap.set(cv.CAP_PROP_WHITE_BALANCE_BLUE_U, 0)  # Set white balance to default (0) Doesn't seem to affect anything
# cap.set(cv.CAP_PROP_GAMMA, 0)  # Doesn't appear to do anything

# cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)  # Enable auto-exposure
cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv.CAP_PROP_EXPOSURE, 5000)
#cap.set(cv.CAP_PROP_EXPOSURE, 62)
# cap.set(cv.CAP_PROP_AUTO_WB, 1)        # Enable auto-white balance appears to be 0 or 1 value only
# time.sleep(1)

# print("Brightness:", cap.get(cv.CAP_PROP_BRIGHTNESS))
# print("Contrast:", cap.get(cv.CAP_PROP_CONTRAST))
# print("Saturation:", cap.get(cv.CAP_PROP_SATURATION))
# print("White Balance Blue U:", cap.get(cv.CAP_PROP_WHITE_BALANCE_BLUE_U))
#print("Exposure:", cap.get(cv.CAP_PROP_EXPOSURE))
# cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)
# cap.set(cv.CAP_PROP_EXPOSURE, 50)
1
# print("Exposure:", cap.get(cv.CAP_PROP_AUTO_EXPOSURE))
# print("Gama:", cap.get(cv.CAP_PROP_GAMMA))
# print("Auto White Balance:", cap.get(cv.CAP_PROP_AUTO_WB))

# cap.set(cv.CAP_PROP_BRIGHTNESS, 0)  # Set brightness to default (0)
# cap.set(cv.CAP_PROP_CONTRAST, 32)    # Set contrast to default (1)
# cap.set(cv.CAP_PROP_SATURATION, 64)  # Set saturation to default (1)
# cap.set(cv.CAP_PROP_WHITE_BALANCE_BLUE_U, -1)  # Set white balance to default (0)

ret,frame = cap.read()

if ret:
    cv.imwrite('blue.jpg',frame)
else:
    print('failed to write frame')

cap.release