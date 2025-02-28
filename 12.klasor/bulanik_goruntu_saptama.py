import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\starwars.jpg"
img = cv2.imread(path)

blurry_img = cv2.medianBlur(img,9)

laplacian = cv2.Laplacian(blurry_img,cv2.CV_64F)
laplacian_var = laplacian.var()
# Laplace Operatörü (Laplacian), matematikte ve görüntü işleme gibi alanlarda bir fonksiyonun ikinci türevini hesaplamak için kullanılan bir diferansiyel operatördür.
# Laplace operatörü genellikle kenar tespiti, görüntüdeki ani parlaklık değişikliklerini bulma ve görüntüyü keskinleştirme gibi işlemlerde kullanılır.

# Python'da var() metodu, varyans hesaplamak için kullanılır ve genellikle NumPy kütüphanesinde bulunur.
# # Bir veri kümesinin varyansı, verilerin ortalamadan ne kadar sapma gösterdiğini ölçer
# Düşük varyans: Veriler birbirine yakındır.
# Yüksek varyans: Veriler geniş bir aralığa dağılmıştır.

# #---------------------
# var(), görüntüdeki parlaklık değişimlerinin varyansını hesaplar.
# Laplacian sonucu genellikle kenarları ve yüksek frekanslı bileşenleri içerir. Varyans, bu bileşenlerin yoğunluğunu ölçmek için kullanılır.
# Daha keskin (az bulanık) görüntüler, daha yüksek varyansa sahip olur çünkü kenar detayları daha belirgindir.

print(laplacian)

if laplacian_var < 500:
    print("blurry image")
    
cv2.imshow("img",img)
cv2.imshow("blurry img",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Daha fazla kenar (keskin görüntüler) → Daha yüksek varyans.
# Daha az kenar (bulanık görüntüler) → Daha düşük varyans.

