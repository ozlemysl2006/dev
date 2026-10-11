import cv2 as cv
import numpy as np
img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # creates a black image of the same size as the original image
cv.imshow('Blank', blank) # displays the black image as a new window

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT) #sayı arttıkça bulanıklık artıyor
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #tresh looks an image and try tp find the edges of the image and returns a binary image

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1) # draws the contours on the black image
cv.imshow('Contours Drawn', blank) # displays the image with the contours as a new


cv.waitKey(0)