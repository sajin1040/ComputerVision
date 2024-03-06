import cv2
image = cv2.imread("C:/Users/SAJIN/Pictures/Screenshots/Screenshot (5).png")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Kernel for dilation
dilated_image = cv2.dilate(grayscale_image, kernel, iterations=1)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
