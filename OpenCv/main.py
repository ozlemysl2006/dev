import cv2 as cv
import numpy as np
webcam = cv.VideoCapture(0) #0 laptop camera, 1 external camera

while True:
    ret, frame = webcam.read() # ret(return)
    if not ret:
        print("Görüntü Alınamadı")
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #BGR to HSV
    lower_mavi = np.array([100,150,50]) #sayılar HSV(hue, saturation, value)'nin değerleri mavinin alt ve üst sınırlarını veriyor.
    upper_mavi = np.array([130,255,255])
    mask_mavi = cv.inRange(hsv, lower_mavi, upper_mavi)
    lower_red = np.array([0,150,50])
    upper_red = np.array([10,255,255])
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask = cv.bitwise_or(mask_mavi, mask_red)
    cv.imshow('Mask', mask)

    h, w = frame.shape[:2] #height, weight ve renk kanalı sayısına bağlı. Sadece h w için [:2]
    # 3x3 grid çizgileri için
    cv.line(frame, (w//3, 0), (w//3, h), (255, 255, 255), 2) 
    cv.line(frame, (2*w//3, 0), (2*w//3, h), (255, 255, 255), 2)
    cv.line(frame, (0, h//3), (w, h//3), (255, 255, 255), 2)
    cv.line(frame, (0, 2*h//3), (w, 2*h//3), (255, 255, 255), 2)
    cv.imshow('Webcam', frame)

    contours, hierarchies = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    kare = 0 #başta kare yok 
    for cnt in contours:
        if cv.contourArea(cnt) > 500:
            kare = 1
            x, y, w, h = cv.boundingRect(cnt) #konturu kare sarıcak, x sol üst y sol alt
            # Karenin merkezini bulma
            cX = x + (w // 2)
            cY = y + (h // 2)

            #karenin merkezinin koordinatları
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Yeşil kutu
            cv.circle(frame, (cX, cY), 5, (0, 0, 255), -1) # Kırmızı merkez noktası oluşturur, -1 dairenin içini doldurur

            #satır sutün tespiti ve yazdırması
            h, w = frame.shape[:2]
            hucre_yukseklık = h //3
            hucre_genıslık = w//3
            if cX < hucre_genıslık:
                    sutun = 1 
            elif cX <hucre_genıslık * 2:
                    sutun = 2
            else:
                    sutun = 3
            
            if cY < hucre_yukseklık:
                     satır = 1
            elif cY < hucre_yukseklık * 2:
                    satır = 2
            else:
                     satır = 3
            #hücre hesaplama
            x1 = (sutun-1) * hucre_genıslık
            y1 = (satır-1) * hucre_yukseklık
            x2 = sutun * hucre_genıslık
            y2 = satır * hucre_yukseklık
            #hücreye saydam dolgu ekleme
            overlay = frame.copy()
            cv.rectangle(overlay, (x1, y1), (x2, y2), (100, 255, 100), -1)   
            cv.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)       
            cv.putText(frame, f"Merkez: ({cX},{cY})- Satir: {satır}, Sutun: {sutun}", (int(x), int(y - 10)), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) #f" anlık değer
    if  kare == 0: 
        cv.putText(frame, "Kare Aranıyor",(50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    h, w = frame.shape[:2] #height, weight ve renk kanalı sayısına bağlı. Sadece h w için [:2]
    # 3x3 grid çizgileri için
    cv.line(frame, (w//3, 0), (w//3, h), (255, 255, 255), 2) 
    cv.line(frame, (2*w//3, 0), (2*w//3, h), (255, 255, 255), 2)
    cv.line(frame, (0, h//3), (w, h//3), (255, 255, 255), 2)
    cv.line(frame, (0, 2*h//3), (w, 2*h//3), (255, 255, 255), 2)
    cv.imshow('Webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    cv.imshow('Webcam', frame)

webcam.release()
cv.destroyAllWindows()