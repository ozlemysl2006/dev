import cv2 as cv
import numpy as np

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # creates a black image of the same size as the original image

b,g,r= cv.split(img) #splits the image into its blue, green and red channels
blue = cv.merge([b,blank,blank]) #merges the blue channel with two black channels to create a blue image
green = cv.merge([blank,g,blank]) #merges the green channel with two black channels to create a green image
red = cv.merge([blank,blank,r]) #merges the red channel with two black channels to create a red image

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape) #prints the shape of the image
print(b.shape) #prints the shape of the blue channel
print(g.shape) #prints the shape of the green channel
print(r.shape) #prints the shape of the red channel

merged = cv.merge([b,g,r]) #merges the blue, green and red channels back into a single image
cv.imshow('Merged', merged) #displays the merged image as a new window

cv.waitKey(0)