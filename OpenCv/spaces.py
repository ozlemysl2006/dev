import cv2 as cv
import matplotlib.pyplot as plt 
#opencv displays images in BGR format but matplotlib displays images in RGB format so we need to convert the image to RGB format before displaying it using matplotlib

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()
cv.waitKey(0)