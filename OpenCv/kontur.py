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

    contours, hierarchies = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cv.contourArea(cnt) > 500:
            x, y, w, h = cv.boundingRect(cnt) #konturu kare sarıcak, x sol üst y sol alt
            # Karenin merkezini bulma
            cX = x + (w // 2)
            cY = y + (h // 2)

            #karenin merkezinin koordinatları
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Yeşil kutu
            cv.circle(frame, (cX, cY), 5, (0, 0, 255), -1) # Kırmızı merkez noktası oluşturur, -1 dairenin içini doldurur

            #satır sutün tespiti ve yazdırması
            yukseklık, genıslık = frame.shape[:2]
            huce_yukseklık = yukseklık //3
            hucre_genıslık = genıslık //3
            if cX < hucre_genıslık:
                    sutun = 1 
            elif cX <hucre_genıslık * 2:
                    sutun = 2
            else:
                    sutun = 3
            
            if cY < huce_yukseklık:
                     satır = 1
            elif cY < huce_yukseklık * 2:
                    satır = 2
            else:
                     satır = 3
            cv.putText(frame, f"Merkez: ({cX},{cY})- Satir: {satır}, Sutun: {sutun}", (int(x), int(y - 10)), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) #f" anlık değer

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
