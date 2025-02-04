#istedigimiz herhangi bir rengi pencereye atamayı ogrenicez.
#bir kızak sistemi olusturucaz
#opencvde buna track bar denir.
#track bardaki kizaklari kaydirarak,pencerenin rengini degistiricez.
#herhangi bir görüntünün,pikseli üç adet rengin belirli yogunluklardaki karısımıyla ifade edilir.
#trackabardaki bu kızakları kaydırırız ve yogunlukları degistmirs olurz.

#webcamden aldıgımız goruntuleri gene trackbar ile değiştirebiliriz.

import numpy as np
import cv2

def nothing(x):
    pass

#bir ekranın resmini degisebilmek icin elimizde bir pencere olması gerekir

img = np.zeros((512,512,3),np.uint8)
#olusturdgumuz pencereye bir ad vermemiz gerekiyor.bunun nedeni
# trackbar ile burada olusturdgumuz pencerenin aynı yerde bulunmasini sağlamak.
cv2.namedWindow("image")#içerik eklenince imshow gibi aclir gösterilir pencere.
#kisacasi : trackbar ara yüzünü,bu rengini değişeceğimiz pencereye yerleştireceğimiz belirtmektir.

#rgb denilen 3 tane kanal olusturuacağız. bir tane anahta switch olacak. bu anahtarlar acık oldugunda bu renkler degisebiliyo olucak.
#bu anahtar kapalı oldugunda se renkler değiştiremiyor olucak.

#ilk parametre : kizagin adi,kizagın yerleseceği pencerenin adi,kizağin başlangiç ve bitiş değerleri, nothing fonkisyonu
cv2.createTrackbar("R","image",0,255,nothing) # bu ilk kizağimizdi ve kirmizi icindi
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
#simdi de anahtari olusturalim
switch = "0: OFF, 1:ON"
cv2.createTrackbar(switch,"image",0,1,nothing)



#renkleri de alabilmemiz görebilmemiz icin,cv2gettrackbarposition gibi bir sey.
#track abrların pozisoynlarını alıcam ve aldıgım değerleri , renk degerlerini pencereye yansıtıcam.
#ama ben bu pzisyonları sürekli değişiyorum , bir while dongusu kurmam gerekiyor ki , pencere sürekli yenilensin.
while True:
     cv2.imshow("image",img)
     if cv2.waitKey(1) & 0xFF == ord("q"):
         break #burada yaptigimiz pencereyi görmek ve q ya bastigimda pencerenein kapanmasi.1 girmemizin sebebi de
                #1mlsaniyede pencerenin kapanıp tekrar acılması aslinda.
     r = cv2.getTrackbarPos("R","image")
     g = cv2.getTrackbarPos("G","image")
     b = cv2.getTrackbarPos("B","image")
     sw = cv2.getTrackbarPos(switch,"image")
     #pozisyon degerlerimizi aldik, degiskenlere atadik.
     if sw == 0: #anahatar durumu icin kosullar.""
        img[:,:,:] = [0,0,0] #anahtar kapalıyken tum degerler sıfır olsun pencere siyah gözüksün
     #simdi degiskenleri , penceremize göndericez.ki renk değişebilsin.
     if sw == 1 :
         img[:,:,:] = [b,g,r] #imgnin bütün renk kanallarina eriştim ve bunlara atadim bu pozisyonları.
     #img de bizim penceremiz by the way
     # tusu cektigimde mesela red kızağını o değer gidiyor img penceresinin r kanalina ataniyor. böylelikle pencere kirmizi oluyor.
    

cv2.destroyAllWindows()
     
cv2.waitKey(0)

