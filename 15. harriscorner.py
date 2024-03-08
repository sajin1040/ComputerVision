import cv2
import numpy as np
image = cv2.imread("C:/Users/SAJIN/Pictures/Screenshots/Screenshot (5).png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
threshold = 0.01 * dst.max()
corner_image = np.zeros_like(image)
corner_image[dst > threshold] = [0, 0, 255]
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Detected Corners', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
