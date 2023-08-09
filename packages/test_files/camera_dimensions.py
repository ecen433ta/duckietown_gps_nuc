import cv2 as cv

cap = cv.VideoCapture('/dev/video6')
print(cap.get(cv.CAP_PROP_EXPOSURE))

camera_width = 1440
camera_height = 720

cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)
cap.set(cv.CAP_PROP_EXPOSURE, 10)

ret, frame = cap.read()

cv.imwrite('after.jpg', frame)

cap.release()