
import cv2
from pathlib import Path

# Find the image relative to this Python file
project_folder = Path(__file__).parent
image_path = project_folder / "images" / "leaf_sample.jpg"

# Load the image
image = cv2.imread(str(image_path))

# Check whether OpenCV loaded it
if image is None:
    print("Image could not be loaded.")
    print(f"Check that this file exists: {image_path}")
else:
    # Display the image dimensions
    height, width, channels = image.shape

    print("Image loaded successfully!")
    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")
    print(f"Colour channels: {channels}")

    # Display the crop image
    cv2.imshow("VisionDrone - Crop Image", image)

    print("Press Q to close the image window.")

    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
