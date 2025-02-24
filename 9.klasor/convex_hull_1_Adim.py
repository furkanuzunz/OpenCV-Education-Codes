import numpy as np
import matplotlib.pyplot as plt
import cv2

#biz bazı şekillere çizdiğimiz konturların tamamen sınır çizgileri üzerinden geçmesini 
# gecmesini istemiyoruz. bazen onun üzerinde adeta örtü gibi durmasını istiyoruz.
#bu gibi durumlarda convex hull u kullanacaz.

#ya mesela bir kısmı iç bükey olan şekilde iç bükey kısmına değil de dış bükeyden örtsün anladın mı .dk 1.55 te analtıyor.
#yıldızın köşelerinden düz çizgiler çekip birleştirdigini düşün

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\map.jpg"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))
ret,thresh = cv2.threshold(blur,50,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

 #CONTOURS HULL NOKTALARINI , CONVEX HULL NOKTALARINI TUTABŞLMEMİZ İÇİN BOŞ BİR ARRAY OLSUTURACAZ.
 
hull = []
 
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))#false  değeri değil , indeksin dönmesini sağlar.
    #appendde bos diziye atcak surekli
    #buldugum konturları siyah ekranlara çizelim

backGround = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contours)):
    cv2.drawContours(backGround,contours,i,(0,0,255),3,8,hierarchy)
    cv2.drawContours(backGround,hull,i,(0,255,0),1,8)

#https://chatgpt.com/share/67b8db73-6124-800b-95ab-8ca0e041d285
#buradan oku

cv2.imshow("son",backGround)



# cv2.imshow("img",img)
# cv2.imshow("gray",gray)
# cv2.imshow("blur",blur)
# cv2.imshow("thresh",thresh)




cv2.waitKey(0)
cv2.destroyAllWindows()

