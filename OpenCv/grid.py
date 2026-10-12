import cv2 as cv
import numpy as np 

webcam = cv.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        print("Görüntü Alınamadı")
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #BGR to HSV
    lower = np.array([100,150,50]) #sayılar HSV(hue, saturation, value)'nin değerleri mavinin alt ve üst sınırlarını veriyor.
    upper = np.array([130,255,255])
    mask = cv.inRange(hsv, lower, upper)
    cv.imshow('Mask', mask)


    h, w = frame.shape[:2] #height, weight ve renk kanalı sayısına bağlı. Sadece h w için [:2]
    # 3x3 grid çizgileri için
    cv.line(frame, (w//3, 0), (w//3, h), (255, 255, 255), 2) 
    cv.line(frame, (2*w//3, 0), (2*w//3, h), (255, 255, 255), 2)
    cv.line(frame, (0, h//3), (w, h//3), (255, 255, 255), 2)
    cv.line(frame, (0, 2*h//3), (w, 2*h//3), (255, 255, 255), 2)
    cv.imshow('Webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

webcam.release()
cv.destroyAllWindows()