import cv2 as cv

#Resizing and Rescaling for image

img = cv.imread('photos/ITU.jpg')
cv.imshow('ITU', img)

def rescaleFrame(frame, scale=0.75): # function to rescale images,videos and live videos
   width = int(frame.shape[1] *scale)
   height = int(frame.shape[0] *scale)
   dimensions = (width, height)

   return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # resizes the frame to particiular dimemsions

resized_image = rescaleFrame(img) # resizes the image to 20% of its original size
cv.imshow('Image', resized_image) # displays the resized image as a new window

def changeRes(width, height): # function to change the resolution of the image it works for live videos and this is not going to work for standalone video files which are already exist on the files
     
    capture.set(3,width)
    capture.set(4,height)

#Resizing and Rescaling for video
capture = cv.VideoCapture('videos/ITU.mp4')
while True:
    isTrue, frame = capture.read() 

    frame_resized = rescaleFrame(frame, scale=0.5) # resizes the frame to 50% of its original size
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized) # displays the resized video as a new window

    if cv.waitKey(20) & 0xFF == ord('d'): 
        break
capture.release()
cv.destroyAllWindows() 