import cv2
image = cv2.imread("C:/Users/SAJIN/Pictures/Screenshots/Screenshot (5).png")
cv2.imshow('Original Image', image)
cv2.waitKey(0)
blur_image = cv2.GaussianBlur(image, (15,15), 0)
cv2.imshow('Blurred Image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
