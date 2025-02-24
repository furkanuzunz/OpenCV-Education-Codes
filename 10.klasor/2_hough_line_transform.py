import cv2
import numpy as np

path = path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\10.klasor\\line.mp4"

capture = cv2.VideoCapture(path)

while(1):
    ret,frame = capture.read()
    frame = cv2.resize(frame,(640,480)) #boyutu kuculttuk  
    #biizm şeritlerimiz sari oldugu icin,renkleri hsvye cevirip ,sari çizglierimiiz çekmeye çalişçaz
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hsv range for yellow
    #burada hsv formatina cevirip hsv degisenine atadik iste
    lower_yellow = np.array([18,94,140],np.uint8) #sari değerleri icin hani google a basvurabilirdik.
    upper_yellow = np.array([48,255,255],np.uint8)
    
    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    #cv2.imshow("mask",mask)
    #simdi mask ugyuladıktan sonra köşeleri bulcaz.köşelerini cıkartıcaz.hani böyle bos olcak iste içi
    edges = cv2.Canny(mask,75,250)
    #cv2.imshow("edges",edges)
    
    #simdi bu köşelerini buldugumuz çizgiler üzerinde bir tespit uyapcaz.
    #cunku python idesi suand omalrin bir cizgi oldugnu bilmiyor.
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
        
    cv2.imshow("son",frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()





