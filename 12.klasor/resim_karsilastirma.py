import cv2
import numpy as np


path1 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\aircraft.jpg"
path2 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\aircraft1.jpg"


img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

img3 = cv2.medianBlur(img1,7)


# if img1.shape == img2.shape:
#     print("same size")
# else:
#     print("not same")

#diff = difference
diff = cv2.subtract(img1,img3) #piksel bazlı farkları aldik.bu farklar her pikselin r,g,b degerleri üzerinden hesaplanir.
b,g,r = cv2.split(diff)#burada split ile bir görüntüyü b,g,r renk kanallarina bolup deegiskenlerimize atadik.

#subtract fonksiyonu iki resmi karşilaştirir farkli olan yerlerin regnini değiştirir
#aynı olan yerler ise siyaha boyanır,farklilari ise işte beyaza boyar.

if cv2.countNonZero(b) == 0 & cv2.countNonZero(g) == 0 & cv2.countNonZero(r) == 0:
    print("completely equal")
else:
    print("not completely equal") 
# Eğer tüm kanallarda sıfır olmayan piksel bulunmuyorsa (cv2.countNonZero() sıfır dönerse), iki görüntü arasındaki fark tamamen siyah bir görüntü oluşturmuştur. 
# # Bu, img1 ve img3'ün tamamen aynı olduğu anlamına gelir.
# Mantık
# cv2.subtract(img1, img3) fonksiyonu, img1 ile img3 arasındaki farkı piksel piksel hesaplar. Sonuç, bir fark matrisi (diff) olur.
# Eğer iki görüntü tamamen aynıysa, fark matrisi tüm pikselleri sıfır olan siyah bir görüntü olur.
# cv2.countNonZero(b) kontrolü, diff görüntüsünün mavi kanalında sıfır olmayan herhangi bir piksel olup olmadığını kontrol eder.
# Aynı işlem yeşil (g) ve kırmızı (r) kanallarında da yapılır.

cv2.imshow("difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()