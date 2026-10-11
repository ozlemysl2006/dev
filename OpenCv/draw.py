import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # creates a black image of 500x500 pixels
cv.imshow('Blank', blank) # displays the black image as a new window

#paint the image a certain color
blank[200:300, 300:400] = 0,255,0 # paints the image green
cv.imshow('Green', blank) # displays the green image as a new window

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1) # draws a green rectangle on the image
cv.imshow('Rectangle', blank) # displays the image with the rectangle as a new window

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) # draws a red circle on the image
cv.imshow('Circle', blank) # displays the image with the circle as a new window

#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3) # draws a white line on the image
cv.imshow('Line', blank) # displays the image with the line as a new window

#write text on an image
cv.putText(blank, 'Hello World', (180,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2) # writes text on the image
cv.imshow('Text', blank) # displays the image with the text as a new window

cv.waitKey(0) 
