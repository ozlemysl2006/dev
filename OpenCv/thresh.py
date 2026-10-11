import cv2 as cv

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh_inv) #inverse beyaz yerine siyah ve siyah yerine beyaz yapar

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) #11 ve 3 sayıları arttıkça daha fazla detay görünür
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)