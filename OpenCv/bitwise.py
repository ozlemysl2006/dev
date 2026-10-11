import cv2 as cv
import numpy as np

#bitwise operations 

blank = np.zeros((400,400), dtype='uint8') # creates a black image of 400x400 pixels

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # draws a white rectangle on the image
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) # draws a white circle on the image

cv.imshow('Rectangle', rectangle) # displays the image with the rectangle as a new window
cv.imshow('Circle', circle) # displays the image with the circle as a new window

#1.AND resimleri kesiştirir, sadece kesişim alanını gösterir, intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle) # performs a bitwise AND operation on the rectangle and circle images
cv.imshow('Bitwise AND', bitwise_and) # displays the result of the bitwise

#2.OR resimleri bireştirir, non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle) # performs a bitwise OR operation on the rectangle and circle images
cv.imshow('Bitwise OR', bitwise_or) # displays the result of the bitwise

#3.XOR non-intersectiong regions
bitwise_xor = cv.bitwise_xor(rectangle, circle) # performs a bitwise XOR operation on the rectangle and circle images
cv.imshow('Bitwise XOR', bitwise_xor) # displays the result of the bitwise

#4.NOT converts white to black and black to white 
bitwise_not = cv.bitwise_not(rectangle) # performs a bitwise NOT operation on the rectangle image
cv.imshow('Bitwise NOT', bitwise_not) # displays the result of the bitwise

cv.waitKey(0)