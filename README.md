# ROI Coordinates Extraction
This project contains a function that extracts Region of Interest (ROI) coordinates from images or videos. It is designed to help in various computer vision tasks by providing accurate ROI extraction.

## Features
- Extracts ROI coordinates from images
- Extracts ROI coordinates from videos
- Supports multiple input formats
- Easy integration with other computer vision tasks

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/karimelatbanyHV/cams.git
    cd roi-coordinates-extraction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Usage
To use the ROI extraction function, follow these steps:

1. Import the function in your Python script:
    ```python
    from roi_extraction import get_roi_coordinates
    ```

2. Use the function to get ROI coordinates from an image:
    ```python
    image_path = 'path/to/your/image.jpg'
    roi_coordinates = get_roi_coordinates(image_path)
    print(roi_coordinates)
    ```

3. Use the function to get ROI coordinates from a video:
    ```python
    video_path = 'path/to/your/video.mp4'
    roi_coordinates = get_roi_coordinates(video_path, is_video=True)
    print(roi_coordinates)
    ```

## Example
Provide a detailed example of how to use your function.

Example:
```markdown
## Example
Here's a complete example of how to use the ROI extraction function:

```python
# Import the necessary modules
import cv2
from roi_extraction import get_roi_coordinates

# Define the path to the input image
image_path = 'sample_image.jpg'

# Get the ROI coordinates from the image
roi_coordinates = get_roi_coordinates(image_path)

# Display the ROI on the image
image = cv2.imread(image_path)
x, y, w, h = roi_coordinates
cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
## and for video you can use this 
# Define the path to the input video
video_path = 'sample_video.mp4'

# Get the ROI coordinates from the video
roi_coordinates = get_roi_coordinates(video_path, is_video=True)

# Print the coordinates
print(roi_coordinates)


