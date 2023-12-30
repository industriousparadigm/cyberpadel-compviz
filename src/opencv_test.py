import cv2
import numpy as np

# Create a black image using NumPy
# Image dimensions: 500x500 pixels, 3 color channels (RGB)
image = np.zeros((500, 500, 3), dtype="uint8")

# Draw a red rectangle
# Top-left corner (50, 50), bottom-right corner (450, 450)
cv2.rectangle(image, (50, 50), (450, 450), (0, 0, 255), 2)

# Draw a green circle
# Center (250, 250), radius 100
cv2.circle(image, (250, 250), 100, (0, 255, 0), 3)

# Draw a blue line
# Starting point (100, 100), ending point (400, 400)
cv2.line(image, (100, 100), (400, 400), (255, 0, 0), 3)

# Display the image
cv2.imshow("Test Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
