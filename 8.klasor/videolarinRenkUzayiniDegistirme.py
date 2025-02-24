#toplu olarak videonun renk uzayını degistriemeyiz
#tek tek frameleri cekip o sekilde yapcaz.
#tek tek frameleri okicaz.

import cv2
import numpy as np
path = "C:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/antalya.mp4"
capture = cv2.VideoCapture(path)


while True:
    ret,frame = capture.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret == False:
        break    
    
    cv2.imshow("video",frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    

capture.release()
cv2.destroyAllWindows()