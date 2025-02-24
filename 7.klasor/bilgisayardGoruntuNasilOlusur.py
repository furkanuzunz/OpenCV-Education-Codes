import cv2
import numpy as np

img = np.zeros((10,10,3),np.uint8)
#bilgisayarlarin bir pikseli gorunutye nasi isledigini anlamak icin  biz de tek tek pikselleri boayaylım
img[0,0] = (255,255,255) # sifira sifir koordinatidaki PİKSELE eristik resmin.
#her piksel uc kanala sahiptir.[R, G, B]. Bu nedenle, img[0, 0] aslında (0, 0) koordinatındaki pikselin [R, G, B] değerlerini temsil eder.
# img[0, 0] ile [:, :, 0] Arasındaki Fark
# img[0, 0]: Tek bir pikselin RGB değerlerine erişir veya değiştirir.
# Örneğin: img[0, 0] = (255, 255, 255) → (0, 0) pikselini beyaz yapar.
# img[:, :, 0]: Tüm piksellerin Red (Kırmızı) kanalına erişir veya değiştirir.
# Örneğin: img[:, :, 0] = 255 → Tüm piksellerin Kırmızı kanalını maksimum (255) yapar.
img[0,1] = (255,255,200) 
img[0,2] = (255,255,150) 
img[0,3] = (255,255,15) #beyazdan mavinin tonlarina göre yönelim yaptım.
#bilgisayar işte , aldıgı veriye göre boyuyor aldıgı değerleri.

# #siyah beyaz görüntüde üç kanal verisi yoktur.o renkli resimler icin geceerldiri.
# img = np.zeros((10,10),np.uint8)
# img[0,0] = 255
# img[0,1] = 200
# img[0,2] = 150
# img[0,3] = 20



img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)

cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
