import cv2
import numpy as np

path  = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev2\\red.MOV"

capture = cv2.VideoCapture(path)

while True:
    ret,frame = capture.read()
    
    frame = cv2.resize(frame,(640,480))
    q
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #MASKELEYELİM
    sensitive = 10
    lower_red = np.array([90 - sensitive,70,50])
    upper_red = np.array([90 + sensitive,255,255])
    
    mask_frame = cv2.inRange(hsv_frame,lower_red,upper_red)
    bitwise_frame = cv2.bitwise_and(frame,frame,mask=mask_frame)
    
    cv2.imshow("bitwise",bitwise_frame)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


capture.release()
cv2.destroyAllWindows()