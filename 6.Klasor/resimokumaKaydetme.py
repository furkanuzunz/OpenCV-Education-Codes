import cv2
import numpy as np
import matplotlib.pyplot as plt

#resimleri okuma- ekranda görebilmemiz icin
#resim okumak demeki matematiksel arka planını anlamasıdır.piksellerini ve renk degerlerini hafızasına kaydetmesidir
#sonrasında onu bize verebilir.

path = "C:\\Users\\Furkan\\Desktop\\resim_okuma_gosterme_kaydetme\\klon.jpg"
img = cv2.imread(path)
# print(img)#resimler matrislerden oluşan , renk yogunluklarından oluşan matrislerdir aslinda.

cv2.namedWindow("image",cv2.WINDOW_NORMAL)#resmi yeniden boyutlandıralabilir hale getirmek.

#resmi ekranda gösterme
cv2.imshow("image",img)

#resmi kaydetme
cv2.imwrite("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\6.Klasor\\klon1.jpg",img)
#hangi isimle kaydedeceğimiz ilk parametre

cv2.waitKey(0) #ben herhangi bir tuşa basana kadar ekranda durur.
cv2.destroyAllWindows()#tüm pencereleri kapatır.tuşu biz belirleriz.

#bu haldyken resmi büyültüp küçültemiyoruz bunun icin fonksiyon eklicez.
