import cv2
import numpy as np

image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev3\\para.jpg")
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(gray_img,(5,5),0)

_,binary_image=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

#canny_edge = cv2.Canny(binary_image,30,150)
#hem canny hem thresh aynı anda sıkıntı bi tık sanki.

#dilate = cv2.dilate(binary_image,(1,1),iterations=2)

#dilate ile bu threshte beyazlar geldi ya mesela paralar, küçük boşlukları kaoadik
#aslinda cok da lazim değil,diğer eğitim videolarınd akullandik diye bir yazdiydim.
contours,hierarchy = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

i = 0

for cnt in contours:
    if cv2.contourArea(cnt)>77:
        (x,y),r = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y)) #float olarak dondukleri icin.
        r =  int(r)
    
        #area = cv2.contourArea(cnt)
        #print(area)
        i+=1
        cv2.drawContours(image,cnt,-1,(0,255,0),2)
        #cv2.circle(gray_img, center, r, (0, 255, 0), 2)
        #circle neden yanlis ciziliyor bir bak,sor umuda felan.

cv2.putText(image, f"para sayisi: {i}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 2)

    
    

cv2.imshow("binary",binary_image)  
#cv2.imshow("gray",gray_img)  
cv2.imshow("orig",image)
cv2.waitKey(0)
cv2.destroyAllWindows()