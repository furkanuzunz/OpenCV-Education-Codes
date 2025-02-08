#ağirlikli toplama islemlerinde goruntuleri belirlikli yogunluklarda birbirine eklemeye verilen isimdir.

#f(x,y) = x*a + y*b + c    ----x i a yogunlugunda y yi b yogunlugunda birbirleri üzeirne eklersem yeni bir cikti alirim
#bir de sabit bir sayi ekledik.iste bu formülasyon üzerinden ilerleyen agirlikli toplama silemi,opencvde bize resimleri belirlikli yogunluklarda birbirleri üzerine eklemizi sağliyor.
import cv2
import numpy as np

img = cv2.imread("c:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/klon1.jpg")



tuvalForcircle = np.zeros((512,512,3),np.uint8) + 255
cv2.circle(tuvalForcircle,(256,256),60,(255,0,0),-1)

tuvalForRectangle = np.zeros((512,512,3),np.uint8) + 255 
cv2.rectangle(tuvalForRectangle,(150,150),(350,350),(0,0,255),-1)

new = cv2.addWeighted(tuvalForcircle,0.7,tuvalForRectangle,0.3,0)#renk olarak agirlikli olan circle olacak.
#yukaarıdaki formüle göre yazdik farkinda misin.
#mesela dikdörtgeni daha yogun yaparsan böyle dairede bi tık kırmızı gozukcek aslinda.o tarz bi yogunluktan bahsediyoruz.
cv2.imshow("new",new)










cv2.imshow("rectangle",tuvalForRectangle)
cv2.imshow("tuvalForcircle",tuvalForcircle)
cv2.waitKey(0)
cv2.destroyAllWindows()

