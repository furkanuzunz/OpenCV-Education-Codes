import cv2
import numpy as np

path  = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev2\\WhatsApp Video 2025-03-02 saat 21.17.25_afaa2583.mp4"

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    #frame = cv2.resize(frame,(640,480))
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #MASKELEYELİM
    sensitive = 15
    lower_white = np.array([0,0,255-sensitive])
    upper_white = np.array([255,sensitive,255])
    
    mask_frame = cv2.inRange(hsv_frame,lower_white,upper_white)
    bitwise_frame = cv2.bitwise_and(frame,frame,mask=mask_frame)
    
    cv2.imshow("bitwise",bitwise_frame)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


capture.release()
cv2.destroyAllWindows()