import cv2 as cv
import numpy as np

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converts the image to grayscale
cv.imshow('Gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F) # applies the Laplacian operator to the grayscale image
lap = np.uint8(np.absolute(lap)) # converts the result to an unsigned 8-bit integer
cv.imshow('Laplacian', lap) # displays the Laplacian image as a new window

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0) # applies the Sobel operator in the x direction
sobely = cv.Sobel(gray, cv.CV_64F, 0,1) # applies the Sobel operator in the y direction
combined_sobel = cv.bitwise_or(sobelx, sobely) # combines the Sobel x and y images using a bitwise OR operation

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175) # applies the Canny edge detection algorithm to the grayscale image
cv.imshow('Canny Edges', canny) # displays the Canny edges as a new window  

cv.waitKey(0)