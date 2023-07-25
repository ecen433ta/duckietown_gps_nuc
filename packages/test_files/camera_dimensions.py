import cv2 as cv

cap = cv.VideoCapture('/dev/video0')
print(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))

camera_width = 1440
camera_height = 720

cap.set(cv.CAP_PROP_FRAME_WIDTH, camera_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, camera_height)

ret, frame = cap.read()

cv.imwrite('./test.jpg', frame)