import cv2

def list_cameras():
    num_cameras = 0
    while True:
        cap = cv2.VideoCapture(num_cameras)
        if not cap.isOpened():
            break
        print(f"Camera {num_cameras}:")
        print(f"  Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
        print(f"  Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
        cap.release()
        num_cameras += 1

list_cameras()

def set_camera_properties(camera_index, width, height, fps):
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.release()

# Replace the camera_index with the appropriate camera index from the list_cameras output.
camera_index = 0
width = 1920  # Set your desired width
height = 1080  # Set your desired height
fps = 30  # Set your desired frame rate

set_camera_properties(camera_index, width, height, fps)

