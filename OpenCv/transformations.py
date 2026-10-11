import cv2 as cv
import numpy as np
img = cv .imread('photos/ITU.jpg')
cv.imshow('ITU', img)

#translation, shifting an image along x and y axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #transformation matrix
    dimensions = (img.shape[1], img.shape[0]) #dimensions of the image first width then height
    return cv.warpAffine(img, transMat, dimensions) #applies the transformation matrix to the image

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100) #translates the image 100 pixels to the right and 100 pixels down
cv.imshow('Translated', translated) #displays the translated image as a new window

#rotation, rotating an image around a point
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] #gets the height and width of the image
    if rotPoint is None: #if no rotation point is specified, rotate around the center of the image
        rotPoint = (width//2, height//2) #sets the rotation point to the center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #gets the rotation matrix
    dimensions = (width, height) #dimensions of the image first width then height

    return cv.warpAffine(img, rotMat, dimensions) #applies the rotation matrix to the image

rotated = rotate(img, 45) #rotates the image 45 degrees around the center of the image, - values rotate clockwise, + values rotate counter-clockwise
cv.imshow('Rotated', rotated) #displays the rotated image as a new window   

rotated_rotated = rotate(rotated,-45) #rotates the image -45 degrees around the center of the image, - values rotate clockwise, + values rotate counter-clockwise
cv.imshow('Rotated Rotated', rotated_rotated) #displays the rotated image as a new window

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #resizes the image to 500x500 pixels
cv.imshow('Resized', resized) #displays the resized image as a new window

#flipping
flip = cv.flip(img, 0) # 0 flips the image vertically, 1 flips the image horizontally, -1 flips the image both vertically and horizontally
cv.imshow('Flipped', flip) #displays the flipped image as a new window

#cropping
cropped = img[200:400, 300:400] #crops the image from 50 to 200 pixels in height and 200 to 400 pixels in width
cv.imshow('Cropped', cropped) #displays the cropped image as a new window

cv.waitKey(0)