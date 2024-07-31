import cv2

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        # Store the point coordinates
        points.append((x, y))
        print(f"Point selected: {(x, y)}")
#get the file and from it is extension and from it detect if video or image
def select_rois(file_path):
    global points
    points = []
    rois = []

    # Open video capture or load image
    cap = None
    image = None
    if file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            return []
    else:
        image = cv2.imread(file_path)
        if image is None:
            print("Error: Could not open image.")
            return []

    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', mouse_callback)

    while True:
        if cap:
            ret, frame = cap.read()
            if not ret:
                break
        else:
            frame = image.copy()

        # Draw points and lines if points are selected
        for point in points:
            cv2.circle(frame, point, 5, (0, 255, 0), -1)
        if len(points) >= 2:
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
        if len(points) >= 3:
            cv2.line(frame, points[1], points[2], (0, 255, 0), 2)
        if len(points) == 4:
            cv2.line(frame, points[2], points[3], (0, 255, 0), 2)
            cv2.line(frame, points[3], points[0], (0, 255, 0), 2)
            print(f"Rectangle coordinates: {points}")

        cv2.imshow('Frame', frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            points = []  # Reset points
            print("Points reset.")
        elif key == ord('s'):
            if len(points) == 4:
                roi_id = input("Enter ID for the selected ROI: ")
                x_min = min(points[0][0], points[1][0], points[2][0], points[3][0])
                x_max = max(points[0][0], points[1][0], points[2][0], points[3][0])
                y_min = min(points[0][1], points[1][1], points[2][1], points[3][1])
                y_max = max(points[0][1], points[1][1], points[2][1], points[3][1])
                cropped_image = frame[y_min:y_max, x_min:x_max]
                rois.append({"id": roi_id, "coordinates": points.copy(), "cropped_image": cropped_image})
                points = []  # Reset points after storing ROI
                print("ROI stored.")
            else:
                print("Rectangle was not fully defined. Select 4 points.")

    if cap:
        cap.release()
    cv2.destroyAllWindows()

    return rois

