import cv2
import numpy as np

image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev3\\para3.jpg")
image = cv2.resize(image, (640, 480))
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(gray_img,(5,5),0)

binary_image = cv2.adaptiveThreshold(
    gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3
)

contours,hierarchy = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

i = 0

for cnt in contours:
    if cv2.contourArea(cnt)>350:
        (x,y),r = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y)) 
        r =  int(r)
        i+=1
        cv2.drawContours(image,[cnt],-1,(0,255,0),2)

cv2.putText(image, f"para sayisi: {i}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 2)

    
    

cv2.imshow("binary",binary_image)  
cv2.imshow("orig",image)
cv2.waitKey(0)
cv2.destroyAllWindows()