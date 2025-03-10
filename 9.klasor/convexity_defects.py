import numpy as np
import matplotlib.pyplot as plt
import cv2

#
#
#
#

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\star.png"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)

#simdi sirasyila convex hull fonksiyonunu ve convexity fonksiyonlarını uygulicam.

cntr = contours[0]
hull = cv2.convexHull(cntr,returnPoints= False) # FALSE OLDUGUNDA BU FONKSİYONDAN GELEND DEGERLERİN İNDEKSLERİ DÖNÜYOR.

defects = cv2.convexityDefects(cntr,hull) #bu fonksiyon aslidna 4 tane deger donderirdonderdigi degerleri asagida kullaniyoruz aslinda

#s = start point(uç noktaların baslangiclari)
#e = end point    ---------- s ve e ile çizgi çekeceğiz aslind auç noktalarla
#f = furthest point-------bu aslinda ice bükülmüş köşelerin oldugu yer
# d = distance-----------------
#defects boyutunun sifirinci elemanı kadar
for  i in range(defects.shape[0]): #bu dongu , iç bükey sayilari sayisi kadar döner.
    s,e,f,d = defects[i,0]
    start_point = tuple(cntr[s][0])
    end_po = tuple(cntr[e][0])
    farthest_point = tuple(cntr[f][0])
    cv2.line(img,start_point,end_po,[0,255,0],2)
    cv2.circle(img,farthest_point,5,[0,255,0],-1)

# https://chatgpt.com/share/67b8d4f8-e4a4-800b-8b3b-273747e5c6d5 bu mevzuyu anlatan

#guncel https://chatgpt.com/share/67cde47e-f910-800b-bfd2-1dc41349a7df



cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()