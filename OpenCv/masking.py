import cv2 as cv
import numpy as np

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # creates a black image of the same size as the original image
cv.imshow('Blank', blank) # displays the black image as a new window

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # creates a circular mask
cv.imshow('Mask', mask) # displays the mask as a new window

masked = cv.bitwise_and(img, img, mask=mask) # applies the mask to the original image
cv.imshow('Masked', masked) # displays the masked image as a new window

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
weird_shape = cv.bitwise_and(mask, rectangle) # creates a weird shape by combining the mask and rectangle
cv.imshow('Weird Shape', weird_shape) # displays the weird shape as a new window

cv.waitKey(0)