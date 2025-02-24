import numpy as np
import matplotlib.pyplot as plt 
import cv2
#konturlar şekilimizin sınır çizgilerdir.ve sınır çizgileri art arda gelmiş noktalardan oluşur.

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\contour2.png"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # griye çevirdik resmi
#grayi aslinda kontur koordinatlarını bulmak icin kullandik.sonra ise o koordinatlarla normal img üstüne resimlerimizi cizdik.

#threshold iki değişken döndürür.

# _ bize dönen eşik değeirni verir
# thresh ise binary goruntu matrisni dondurur.
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#simdi kontur koordinatlarını bulcaz

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #bu binaryli matriste çeşitli işlemlere tabii tutacak
#ve koordinatları elde edecek

#print(contours)

cv2.drawContours(img,contours,-1,(0,0,255),3)
#ilk degisken cizim yapmak istedigimz resim
#ikincisi koordinatlarımız 
#uc -1
#4 renk degerleri
#5 ise kalınlık

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()