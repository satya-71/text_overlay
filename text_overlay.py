import numpy as np 
import cv2 
image = cv2.imread('simpsons_frame0 .png') 
#converting RGB image to Binary 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(gray_image,5,255,0) 
#calculate the contours from binary image
im,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
with_contours = cv2.drawContours(image,contours,-1,(0,255,255),3) 
cv2.imwrite("with_contours.jpg",with_contours)
originalImage = cv2.imread('with_contours.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 5, 255, cv2.THRESH_BINARY)
#converting RGB image to Black and white
cv2.imwrite('Black white image.jpg', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
#cv2.imwrite('Gray image.jpg', grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
