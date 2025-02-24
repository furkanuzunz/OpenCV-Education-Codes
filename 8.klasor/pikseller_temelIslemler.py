import cv2
import numpy as np

img = cv2.imread("c:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/klon1.jpg")

#belirledigimiz bir koordinattaki BGR degerlerini bulduk.
# color = img[205,250]
# #color dgiskenim,150 ye 200 koordinatındaki pikselin renk degerini tutsun
# print(color) #bakalım hangi renk degerlerine sahip
# #[159 154 145] BGR degerleri.

#olcuyu bulduk
# dimension = img.shape
# print(dimension)
# #(426, 640, 3) cikti.426 ya 640 lıkmıs ve de 3 kanala sahipmis.BGR kanallari
 
 #herhangi bir koordinattaki mesela sadece mavi renk degerine nasıl erişirim.
blue = img[150,200,0]#420 ye 500 pikselindeki mavi deger(sıfırncı indeksi)
#biz mesela yukarda bgr degerleri icin ciktimiz [150,154,145] cikti.sifirnci indeks bize mavi degerini verir.
print(blue) 
#peki bu piksellerdeki mavi degeri nasil degisiriz.
img[150,200,0] = 250
print("new blue:",img[150,200,0])


#bunlar yerine itemset fonksiyonlarını kullanabiliriz.
blue1 = img.item(150,200,0) #150ye 200deki mavi degerini blue1 degiskenine atadim.
#yukarida blue = img[150,200,0] bir lsite kullanmistik.img[] yapısı, Python listelerine benzer şekilde çalışır, ancak arka planda bir NumPy dizisidir.
#OpenCV'de bir görüntü (img), aslında bir NumPy dizisi olarak temsil edilir.
# import numpy as np
# dizi = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(dizi[1, 2])  # Çıktı: 6
# Görüntü işlemede, img[] yapısı da bu şekilde çalışır. Ancak burada, img bir NumPy dizisi olduğundan, doğrudan piksellerin renk değerlerine erişebiliriz.
#itemle aslinda sadece degere ulasiriz. 
#itemset ile ise o renk degerini degisebiliriz.

# img.itemset((150,200,0),255)#ilk parametre hangi pikselin hang rengini degismek istedigimiz.ikicni parametre ise neyle degismek istedigimz.
# print("item set ile degistikten sonraki:",img[150,200,0]) #cikti 255 olmalidir.
# #vee hata aldik.cunku numpy 2.o ın ustunde itemset kaldirilmis.

#item() fonksiyonu, bir NumPy dizisindeki tek bir elemanın değerini almak için kullanılır









#cv2.imshow("klon askeri",img)

cv2.waitKey(0)
cv2.destroyAllWindows()