import cv2
import numpy as np

img = cv2.imread("c:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/klon1.jpg")

#iki tane ayni boyut lazim.bunlar kendimiz opencv ile olsuturucaz.

#neden ayni boyutlarda olmalari lazim? aslidna resimler birer dizelerdir.
#matrislerdir. ve matrislerde toplama islemi yaparken matrislerin boyutları aynı olmasi gerekir.

tuvalForcircle = np.zeros((512,512,3),np.uint8) + 255 #bu bize beyaz bir bos tuval verir.
cv2.circle(tuvalForcircle,(256,256),60,(255,0,0),-1)
#cemberin cizileceği tuval,konumu,radiusu,rengi,iiçi dolu mu degil mi

tuvalForRectangle = np.zeros((512,512,3),np.uint8) + 255 #gene bos bir tuval olsutrdul.
cv2.rectangle(tuvalForRectangle,(150,150),(350,350),(0,0,255),-1)
#sol köşesinin nerden balsyıp sağ alt köşesinin nerden bitecegini sectik.

#resimleri toplamak icin add fonksiyonunu kullanicaz
add = cv2.add(tuvalForcircle,tuvalForRectangle)
print(add[256,256]) #iki tuvalin birlesiminin(ust uste eklenme) 256ya 256 pikselindeki renk degerini verir.
#[255   0 255] BGR, blue ve red varmis mesela ;). 
#hadi imshow ile add i görelim.
cv2.imshow("add",add) ## mor bir sey geldi.ve de daire seklinde ama neden daire?

cv2.imshow("rectangle",tuvalForRectangle)
cv2.imshow("tuvalForcircle",tuvalForcircle)
cv2.waitKey(0)
cv2.destroyAllWindows()


hello = np.zeros()
    

