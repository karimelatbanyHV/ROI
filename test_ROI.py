import ROI
import cv2


rois = ROI.select_rois('last.mp4')
print("Stored ROIs:")
for roi in rois:
    print(f"ID: {roi['id']}, Coordinates: {roi['coordinates']}")
    
    cv2.imwrite(f"cams/cropped/{roi['id']}.jpg", roi['cropped_image'])