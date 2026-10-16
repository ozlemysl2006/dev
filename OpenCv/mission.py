import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

def find_square(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 40])
    mask_black = cv.inRange(hsv, lower_black, upper_black) 
    contour_black,_ = cv.findContours(mask_black, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    contour_green,_ = cv.findContours(mask_green, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    bulunan_sekıller = []
    for cnt in contour_black: 
        if cv.contourArea(cnt) > 500:
            bulunan_sekıller.append(cnt)
    for cnt in contour_green:
        if cv.contourArea(cnt) > 500:
            bulunan_sekıller.append(cnt)
    return bulunan_sekıller
def find_center(cnt):
    M = cv.moments(cnt)
    if M['m00'] == 0:
        return None
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return cx, cy
def find_cell(cx, cy, w, h):
    row = cy // (h // 3)
    col = cx // (w // 3)
    return row, col
def draw_grid(frame):
    h, w = frame.shape[:2]
    x1 = w // 3
    x2 = 2 * (w // 3)
    cv.line(frame, (x1, 0), (x1, h), (255, 255, 255), 2)
    cv.line(frame, (x2, 0), (x2, h), (255, 255, 255), 2)
    
    y1 = h // 3
    y2 = 2 * (h // 3)
    cv.line(frame, (0, y1), (w, y1), (255, 255, 255), 2)
    cv.line(frame, (0, y2), (w, y2), (255, 255, 255), 2)
    
    return frame

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    h, w = frame.shape[:2]
    contours = find_square(frame)    
    all_objects = False   
    if contours:
        for cnt in contours:
            all_objects = True
            x, y, bw, bh = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
            
            center = find_center(cnt)
            if center:
                cx, cy = center
                row, col = find_cell(cx, cy, w, h)
                cell_w = w // 3
                cell_h = h // 3
                x1 = int(col * cell_w)
                x2 = int((col + 1 ) * cell_w)
                y1 = int(row * cell_h)
                y2 = int((row + 1) * cell_h)

                renkli_cell = frame[y1:y2, x1:x2]
                dolgu = np.full(renkli_cell.shape, (50, 150, 50), dtype=np.uint8)
                frame[y1:y2, x1:x2] = cv.addWeighted(renkli_cell,0.7 ,dolgu ,0.3 ,0)
                cv.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                cv.putText(frame, f"satır{row+1}, sutun{col+1}", (cx - 40, cy - 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                cv.putText(frame, f"x={cx}, y={cy}", (cx - 40, cy + 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)                           
    else:
        cv.putText(frame, "Kare Aranıyor", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    frame = draw_grid(frame)
    cv.imshow("Webcam", frame)    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

webcam.release()
cv.destroyAllWindows()