import cv2 as cv

cap = cv.VideoCapture('/dev/video4')
ret,frame = cap.read()

if ret:
    cv.imwrite('yellow.jpg',frame)
else:
    print('failed to write frame')
