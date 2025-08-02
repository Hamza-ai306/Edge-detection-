
import cv2

path = input("Enter image path: ")
color_img = cv2.imread(path)
if color_img is None:
    print("Could not open or find the image.")
    exit()
    
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Original')
cv2.namedWindow('Edge Detection')
cv2.namedWindow('Sobel Edges')

cv2.createTrackbar('Min Threshold', 'Edge Detection', 50, 500, lambda x: None)
cv2.createTrackbar('Max Threshold', 'Edge Detection', 150, 500, lambda x: None)

while True:
    min_val = cv2.getTrackbarPos('Min Threshold', 'Edge Detection')
    max_val = cv2.getTrackbarPos('Max Threshold', 'Edge Detection')
    canny_edges = cv2.Canny(gray_img, min_val, max_val)
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    sobel_result = cv2.convertScaleAbs(sobel_combined)
    
    cv2.imshow('Original', color_img)
    cv2.imshow('Edge Detection', canny_edges)
    cv2.imshow('Sobel Edges', sobel_result)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
