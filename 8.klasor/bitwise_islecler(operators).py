#bitwise islecler , b,tw,se fonksiyonlar kafa karistirici olabilir.
import cv2
import numpy as np
#qwene bitwise islecleri anlat dediginde mükemmel bir sekilde özet geciyor.

# Binary görüntüler, her pikselin sadece siyah (0) veya beyaz (1) olduğu görüntülerdir. Bu tür görüntüler genellikle 
# maskeleme veya şekil algılama gibi işlemlerde kullanılır.

# # Bitwise işlemler, bu siyah-beyaz pikseller üzerinde çalışır. İşte her bir işlemin nasıl yorumlandığı:

# a. AND (&)
# AND işlemi, iki görüntünün karşılık gelen piksellerini karşılaştırır:

# Eğer her iki piksel de 1 ise, sonuç 1 (beyaz) olur.
# Aksi halde, sonuç 0 (siyah) olur.

# OR (|)
# OR işlemi, iki görüntünün karşılık gelen piksellerini karşılaştırır:

# Eğer en az bir piksel 1 ise, sonuç 1 (beyaz) olur.
# Her iki piksel de 0 ise, sonuç 0 (siyah) olur.

# XOR işlemi, iki görüntünün karşılık gelen piksellerini karşılaştırır:

# Eğer pikseller farklıysa (0 ve 1 veya 1 ve 0), sonuç 1 (beyaz) olur.
# Pikseller aynıysa (0 ve 0 veya 1 ve 1), sonuç 0 (siyah) olur.

# . NOT (~)
# NOT işlemi, bir görüntünün piksellerini tersine çevirir:

# 0 → 1 (siyah → beyaz)
# 1 → 0 (beyaz → siyah)

# cv2.bitwise_and(): İki görüntüyü kesiştirir.
# cv2.bitwise_or(): İki görüntüyü birleştirir.
# cv2.bitwise_xor(): İki görüntünün farklı bölgelerini alır.
# cv2.bitwise_not(): Bir görüntünün tersini alır.


path1 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\bitwise_1.png"
path2 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\bitwise_2.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

cv2.imshow("original img1",img1)
cv2.imshow("original img 2",img2)


bit_and = cv2.bitwise_and(img2,img1) #bit düzeyinde ve islemlerini gerceklestiricek bu fonksiyon
#cv2.imshow("bit_and",bit_and)
#simdi mevzu su. siyahlar 0,beyazlar 1 dondurur. gibi dusun.
# 1 & 0 aslinda = 0 dir.yani siyah ekran olur
# 1 & 1 aslidna = 1 dir.yani beyaz olur.


bit_or = cv2.bitwise_or(img2,img1)
#cv2.imshow("bit_or",bit_or)
# 1 or anything = 1 beyaz
# 0 or 0 = 0  siyah

bit_xor = cv2.bitwise_xor(img2,img1)
#cv2.imshow("bit_xor",bit_xor)
# Eğer pikseller farklıysa (0 ve 1 veya 1 ve 0), sonuç 1 (beyaz) olur.
# Pikseller aynıysa (0 ve 0 veya 1 ve 1), sonuç 0 (siyah) olur.

bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)#tek bir goruntu üzerinde calisir
# cv2.imshow("bit_not",bit_not)
# cv2.imshow("bit_not2",bit_not2)
# NOT işlemi, bir görüntünün piksellerini tersine çevirir:




cv2.waitKey(0)
cv2.destroyAllWindows()

