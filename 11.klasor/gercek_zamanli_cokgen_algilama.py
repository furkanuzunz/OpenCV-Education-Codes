import  cv2
import numpy as np

def nothing(x):
    pass

capture = cv2.VideoCapture(0)
cv2.namedWindow("settings")


font = cv2.FONT_HERSHEY_SIMPLEX

#hue = renk tonu
#saturation = doygunluk

cv2.createTrackbar("lower-hue","settings",0,180,nothing)
cv2.createTrackbar("lower-saturation","settings",0,255,nothing)
cv2.createTrackbar("lower-value","settings",0,255,nothing)
cv2.createTrackbar("upper-hue","settings",0,180,nothing)
cv2.createTrackbar("upper-saturation","settings",0,180,nothing)
cv2.createTrackbar("upper-value","settings",0,255,nothing)

while(1):
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    lh = cv2.getTrackbarPos("lower-hue","settings")
    ls = cv2.getTrackbarPos("lower-saturation","settings")
    lv = cv2.getTrackbarPos("lower-value","settings")
    uh = cv2.getTrackbarPos("upper-hue","settings")
    us = cv2.getTrackbarPos("upper-saturation","settings")
    uv = cv2.getTrackbarPos("upper-value","settings")
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])
    #maskeleme icin değerleir halletitk
    mask = cv2.inRange(hsv,lower_color,upper_color)
    
    #erozyon için bir kernel olusturalım
    kernel = np.ones((5,5),np.uint8) #maskelemeden sonra beyaz noktalar üzrindeki siyah noktaları kaybetmek icin
    mask = cv2.erode(mask,kernel)
    
    #maskelemenin son haline ulaştıktan sonra contoruları aricaz.
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        
        epsilon = 0.02 * cv2.arcLength(contour,True)
        approx_yani_yaklasim = cv2.approxPolyDP(contour,epsilon,True)
        
        x = approx_yani_yaklasim.ravel()[0] #konturların basladıkları noktlara atadim
        y = approx_yani_yaklasim.ravel()[1]
        
        
        area = cv2.contourArea(contour)
    
        if area > 400:
            cv2.drawContours(frame,[approx_yani_yaklasim],0,(0,0,0),5)#birden fazla kontur olsaydı -1 yazardik.
        
            if len(approx_yani_yaklasim)==3:
                cv2.putText(frame,"Triangle",(x,y),font,1,(0,0,0))
            elif len(approx_yani_yaklasim) == 4:
                cv2.putText(frame,"rectangle",(x,y),font,1,(0,0,0))
            elif len(approx_yani_yaklasim) >6 :
                cv2.putText(frame,"circle",(x,y),font,1,(0,0,0))
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
