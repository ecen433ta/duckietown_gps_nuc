import cv2

# Open the webcam
cap = cv2.VideoCapture(0)  # 0 indicates the default webcam

# Capture a frame from the webcam
ret, frame = cap.read()

if not ret:
    print("Error capturing the frame")
else:
    # Save the captured frame as "test_image1.jpg"
    cv2.imwrite("test_image1.jpg", frame)
    print("Image saved as test_image1.jpg")

# Release the webcam
cap.release()
cv2.destroyAllWindows()