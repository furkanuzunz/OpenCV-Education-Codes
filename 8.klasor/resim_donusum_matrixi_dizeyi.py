#bazı geometrik donusumleri yapicaz

import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"

img = cv2.imread(path,0)

# row satir
# #col sütun
# row: Resmin yüksekliği (satır sayısı veya piksel sayısı).
# col: Resmin genişliği (sütun sayısı veya piksel sayısı).
row,col = img.shape#bize bu satır ve sütunu aslında piksel sayilairni veriyordu.

#burada biraz kesim vs yapicaz. buna transformasyon matrisi (dönüşüm) dizeyi kullanicaz.




# cv2.warpAffine() fonksiyonu, dönüşüm matrisinin float32 tipinde olmasını gerektirir.
Matris = np.float32([[1,0,10],
                     [0,1,70]]) #bu dönüşüm matrisini resim üzerine uygulicaz şimdi
# Bu matris, afin dönüşüm (affine transformation) için kullanılır.
# Afin dönüşüm, bir resmi kaydırma (translation), döndürme (rotation), ölçeklendirme (scaling) veya eğme (shearing) gibi işlemlerle değiştirmek için kullanılır.
# Matrisin yapısı şu şekildedir:
            # [[1, 0, tx],
            #     [0, 1, ty]]
# tx: Resmin yatayda (x ekseni) ne kadar kaydırılacağını belirtir.
# ty: Resmin dikeyde (y ekseni) ne kadar kaydırılacağını belirtir.
# 1 ve 0 değerleri, dönüşümün sadece kaydırma işlemi olduğunu gösterir. Eğer bu değerler değiştirilirse, ölçeklendirme veya döndürme gibi farklı dönüşümler de yapılabilir.
# Örneğin:
# tx = 10: Resim x ekseninde 10 piksel sağa kaydırılır.
# ty = 70: Resim y ekseninde 70 piksel aşağı kaydırılır.


dst = cv2.warpAffine(img,Matris,(row,col))
# cv2.warpAffine() fonksiyonu, belirtilen dönüşüm matrisini (Matris) resme uygular.
# Parametreler:
# img: Kaynak resim.
# Matris: Dönüşüm matrisi.
# (row, col): Çıktı resminin boyutları. Burada orijinal resimle aynı boyutta bir çıktı elde etmek için (row, col) kullanılıyor.
# Bu işlem sonucunda, resim belirtilen miktar kadar kaydırılır ve yeni bir resim (dst) oluşturulur







cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# print(row)
# print(col)