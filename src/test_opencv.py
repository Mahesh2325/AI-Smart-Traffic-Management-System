import cv2
import numpy as np

# Create black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

print("Window should open now...")

cv2.imshow("OpenCV Test", img)

cv2.waitKey(0)

cv2.destroyAllWindows()