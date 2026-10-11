import cv2 as cv
#Bluring methods

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

#1.averaging
average = cv.blur(img, (7,7)) #averaging the image with a kernel size of 3x3
cv.imshow('Average', average)

#2.Gaussian
gauss = cv.GaussianBlur(img, (7,7), 0) #Gaussian blurring the image with a kernel size of 3x3
cv.imshow('Gaussian', gauss)

#3.Median
median = cv.medianBlur(img, 7) #Median blurring the image with a kernel size of 3x3
cv.imshow('Median', median)

#4.Bilateral the most effective one
bilateral = cv.bilateralFilter(img, 10, 35, 25) #Bilateral blurring the image with a kernel size of 3x3
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)