import cv2 as cv
webcam = cv.VideoCapture(0) #0 laptop camera, 1 external camera

while True:
    ret, frame = webcam.read() # ret(return)
    if not ret:
        print("Görüntü Alınamadı")
        break

    cv.imshow('Webcam', frame)
          
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

webcam.release()
cv.destroyAllWindows()
