from ultralytics import YOLO
import cv2
import time

def detect_and_notify(video_path, event_file):
    model = YOLO('yolov8n.pt')
    last_detection_count = -1  # Initial state, no detection

    # Open video stream
    cap = cv2.VideoCapture(video_path)
    frame_skip = 12  # Number of frames to skip

    while cap.isOpened():
        for _ in range(frame_skip):
            ret = cap.grab()  # Grab the frame but do not decode it
            if not ret:
                break
        
        ret, frame = cap.read()  # Read the 13th frame
        if not ret:
            break
        
        results = model.predict(
            source=frame,
            device='cpu',
            conf=0.7,
            max_det=100,
            save=False,
            show=True,
            show_boxes=True,
            show_labels=True,
            save_crop=False,
            classes=0
        )

        detection_count = len(results[0].boxes)

        if detection_count != last_detection_count:
            last_detection_count = detection_count
            with open(event_file, 'w') as f:
                f.write(f"{detection_count} person detected.\n")
        
        time.sleep(0.5)  # Adjust the sleep time based on your requirements

    cap.release()
