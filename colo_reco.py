import cv2
import random

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 500)

while True:

    _, frame = cap.read()
    hsv_color = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    height , width,_ = frame.shape
    cx=int(width/2)
    cy=int(height/2)
    pixel_center=hsv_color[cy , cx]
    hue_value = pixel_center[0]
    
    color = "undefined"
    if  hue_value < 5:
        color = "RED"
    elif hue_value < 10:
        color = "orange"    
    elif hue_value < 15:
        color = "ORANGE"
    elif hue_value < 20:
        color ="dark yellow"
    elif hue_value < 25:
        color =  "mustard"
    elif hue_value < 30:
        color ="pale yellow"
    elif hue_value < 35:
        color ="yellowish green"
    elif hue_value < 40:
        color ="light green"
    elif hue_value < 45:
        color ="green"
    elif hue_value < 50:
        color = "dark green"
    elif hue_value < 55:
        color ="dark green"
    elif hue_value < 60:
        color = "dark green"
    elif hue_value < 65:
        color = "leafy green"   
    
    elif hue_value < 85:
        color ="sky blue"
    elif hue_value < 90:
        color = "light blue"
    elif hue_value < 95:
        color = "blue"
    elif hue_value < 100:
        color = "blue"
   
    elif hue_value < 120:
        color ="dark blue"
    elif hue_value < 130:
        color = "purple"
    elif hue_value < 140:
        color = "lavender"
    elif hue_value < 150:
        color = "dark pink"
    elif hue_value < 160:
        color = "light pink"
    elif hue_value < 170:
        color = "VIOLET"

    else:
       color="red"

    pixel_center_bgr=frame[cx,cy]
   
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (255,255,255), 2)
    cv2.circle(frame, (cx, cy), 5, (0, 0, 500), -1)

    cv2.imshow('frame' , frame)
    key=cv2.waitKey(1)
    if key==27:
      break

cap.release()
cv2.destroyAllWindows