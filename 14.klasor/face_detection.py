import cv2

path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\face.png"

image = cv2.imread(path1)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")



gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#resimimiz,resmin ne kadar kucultulerek taranacagi parametresi,bir bölgenin yüz olarak kabul edilmesi için gerekken minimum komşu sayısını belirtir.
faces = face_cascade.detectMultiScale(gray_image,1.3,5)
#suan burada face degiskeninde koordinatları tutuyoruz aslında

for (x,y,w,h) in faces: #sol üst köşe (x,y) sağ alt köşe ise w ve h eklenmiş halleri
    cv2.rectangle(image,(x,y),(x + w , y + h),(0,0,255),2)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
etectMultiScale fonksiyonu, OpenCV’nin Haar Cascade sınıflandırıcısı ile yüz tespiti yaparken kullanılan bir fonksiyondur. Bu fonksiyon, belirli ölçeklerde ve farklı pencere boyutlarında nesneleri (örneğin yüzleri) algılamaya çalışır.

Fonksiyonun Kullanımı

faces = face_cascade.detectMultiScale(gray_image, scaleFactor, minNeighbors)
Parametreler ve Çalışma Mantığı
gray_image: Gri tonlamalı resim (Haar Cascade modeli gri görüntü ile çalışır).
scaleFactor (1.3 gibi): Resmin ne kadar küçültülerek taranacağını belirler.
1.1 gibi küçük bir değer yüz tespitini daha hassas yapar ama yavaş çalışır.
1.3 veya 1.5 gibi büyük bir değer daha hızlı çalışır ama yüz atlamalar olabilir.
minNeighbors (5 gibi): Bir bölgenin yüz olarak kabul edilmesi için gereken minimum komşu sayısını belirtir.
Düşük değer (örneğin 3): Daha fazla yüz algılanabilir ama yanlış pozitif ihtimali artar.
Yüksek değer (örneğin 6): Daha az yanlış pozitif olur ama bazen gerçek yüzleri atlayabilir.
Ekstra Parametreler (Opsiyonel):
minSize: Algılanacak en küçük nesne boyutu.
maxSize: Algılanacak en büyük nesne boyutu.
Çalışma Mantığı
Resim önce scaleFactor oranında küçültülerek farklı boyutlarda taranır.
Haar Cascade filtresi ile her ölçek için yüz olup olmadığı test edilir.
Komşu dikdörtgenler (bounding box) sayısına göre en olası yüzler belirlenir (minNeighbors).
Algılanan yüzlerin koordinatları döndürülür: (x, y, w, h).
Örnek Çıktı
Eğer yüz algılanırsa faces değişkeninde şu şekilde değerler olur:


array([[34, 65, 100, 100], [200, 150, 90, 90]], dtype=int32)
Burada:

İlk yüzün sol üst köşesi (34, 65) ve genişliği 100 piksel, yüksekliği 100 piksel.
İkinci yüz (200,150) koordinatında ve 90x90 piksel boyutlarında.
Bu bilgiyi kullanarak cv2.rectangle() ile yüzlerin etrafına dikdörtgen çiziyoruz.
'''