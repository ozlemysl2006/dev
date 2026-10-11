import cv2 as cv
#for reading images

img = cv.imread('photos/ITU.jpg') # image to matrix pixels

cv.imshow('ITU', img) # displays the image as a new window

cv.waitKey(0) # waits for a key event for 0 milliseconds

#for reading videos

capture = cv.VideoCapture('videos/ITU.mp4') # video to matrix pixels

while True:
    isTrue, frame = capture.read() # reads the video frame by frame
    cv.imshow('Video', frame) # displays the video as a new window

    if cv.waitKey(20) & 0xFF == ord('d'): # waits for a key event for 20 milliseconds
        break
capture.release() # releases the video capture object
cv.destroyAllWindows() # closes all the windows opened by OpenCV
