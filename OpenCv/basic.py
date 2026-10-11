import cv2 as cv

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

#converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #sayı arttıkça bulanıklık artıyor
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 175) #125 ve 175 arasındaki değerler arasındaki fark ne kadar büyükse kenarlar o kadar belirgin olur
cv.imshow('Canny Edges', canny)

#dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3) #kenarları kalınlaştırır
cv.imshow('Dilated', dilated)

#erode the image
eroded = cv.erode(dilated, (7,7), iterations=3) #kenarları inceltir
cv.imshow('Eroded', eroded)

#resize the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #resizes the image to 500x500 pixels  
cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400] #crops the image from 50 to 200 pixels in height and 200 to 400 pixels in width
cv.imshow('Cropped', cropped)

cv.waitKey(0)