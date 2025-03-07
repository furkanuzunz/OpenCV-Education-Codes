import cv2
import numpy as np
import math

vid = cv2.VideoCapture(0)

while 1:
    try:
        ret,frame = vid.read()
        frame = cv2.flip(frame,1)
        
        kernel = np.ones((3,3),np.uint8)
        
        roi = frame[100:300,100:300]
        
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),2)
        hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        
        lower_skin = np.array([0,20,70],dtype=np.uint8)
        upper_skin = np.array([20,255,255],dtype=np.uint8)
        
        mask = cv2.inRange(hsv,lower_skin,upper_skin)
        mask = cv2.dilate(mask,kernel,iterations=4)
        mask = cv2.GaussianBlur(mask,(5,5),100)
        
        contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        cnt = max(contours,key = lambda x: cv2.contourArea(x))
        
        
    except:
        pass
    
    
    if cv2.waitKey(40) & 0xFF==ord('q'):
            break