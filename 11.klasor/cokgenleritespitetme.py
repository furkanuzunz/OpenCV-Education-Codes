#kacgen olacagını bulucaz.önce konturları bulucaz sonra buradan
#kac koseli olduklarını bulucaz.
#3 nokta yani 3 köşesi varsa 3 noktası yani üçgen olcak

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\11.klasor\\polygons.png"

#bir font belirleyelim önce
font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#simdi contourslara bi tık daha yaklascaz.
#bir fonksiyon ile ve dongu ile hatırla
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour,True)
    approx_yani_yaklasma = cv2.approxPolyDP(contour,epsilon,True)
    
    cv2.drawContours(img,[approx_yani_yaklasma],0,(0),5)
    
    #simdiki fonksiyon dik sütunları satıra döker.
    #iste bunu approxa uygulicaz. sıfırnıc indeks x i , 1inci indeks y yi temsil edecek.
    
    x = approx_yani_yaklasma.ravel()[0] #şöyle düşün altta reshape ile dizinin her satrını sadece [10,20] oclak yani x,y koordinatları 
    #olacak sekilde ayarladık ya.iste ravelde aynısını yaptı aslında ve biz 0 ıncı indeklse x i aldık.
    y = approx_yani_yaklasma.ravel()[1]
    
    #approx_yani_yaklasma yi aslinda sadec satirlardan oluscak sekilde yaptık ki kaç nokta var görebilelim.
    #x, y ile ise sadece yazi icin
    
    if len(approx_yani_yaklasma) == 3:
    #print(approx_yani_yaklasma)  
    #print(len(approx_yani_yaklasma)) 
        cv2.putText(img,"Triangle",(x,y),font,1,0)
    elif len(approx_yani_yaklasma) == 4:
        cv2.putText(img,"Rectangle",(x,y),font,1,0)
    elif len(approx_yani_yaklasma) == 5:
        cv2.putText(img,"pentagon",(x,y),font,1,0)
    elif len(approx_yani_yaklasma) == 6:
        cv2.putText(img,"hexagon",(x,y),font,1,0)
    elif len(approx_yani_yaklasma) > 6:
        cv2.putText(img,"elipse",(x,y),font,1,0)

cv2.imshow("IMG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(contours)

#reshape ile ? ve ravel ile acıklama altta.ravel, reshapeden sonra.
# nasıl dik den satıra gecmi soluyor mantıgı nasıl ?
# ü
# ChatGPT:
# Mantığını şöyle anlatayım:

# 1. OpenCV’nin approxPolyDP Çıktısı
# OpenCV cv2.approxPolyDP() fonksiyonunu çalıştırınca 3 boyutlu bir dizi döndürür. Örneğin:


# approx = np.array([
#     [[10, 20]],
#     [[30, 40]],
#     [[50, 60]],
#     [[70, 80]]
# ], dtype=np.int32)
# Bu dizinin şekli (4,1,2) olur.
# Anlamı:

# 4 → 4 tane nokta var.
# 1 → Her nokta içinde ekstra bir iç içe liste var. (OpenCV’nin formatı böyle)
# 2 → (x, y) koordinatlarını tutuyor.
# 2. Dik Formatın Yapısı
# Şu an approx dizisi şöyle duruyor:

# lua
# Kopyala
# Düzenle
# [
#     [[10, 20]],
#     [[30, 40]],
#     [[50, 60]],
#     [[70, 80]]
# ]
# Burada her nokta [x, y] değerini içeren bir 1 elemanlı liste içinde duruyor.
# Yani gereksiz bir ekstra boyut var ((N,1,2)).

# 3. reshape(-1, 2) Ne Yapıyor?
# Şimdi bunu approx.reshape(-1, 2) ile (N,2) haline getirelim:

# python
# Kopyala
# Düzenle
# approx = approx.reshape(-1, 2)
# Bu işlem şu şekilde çalışır:

# -1 → NumPy otomatik olarak satır sayısını belirler. Yani N değerini korur.
# 2 → Artık her satır (x, y) içerecek.
# Sonuç olarak dizi şöyle olur:

# csharp
# Kopyala
# Düzenle
# [
#     [10, 20],
#     [30, 40],
#     [50, 60],
#     [70, 80]
# ]
# Böylece gereksiz iç içe liste kaybolmuş olur.

# 4. Mantık Açıklaması
# Önce (Dikey Format - (N,1,2))
# Şöyle düşünebiliriz:
# Dizi aslında şunun gibi iç içe bir yapıydı:

# lua
# Kopyala
# Düzenle
# Her nokta: [[X, Y]]
# Bu yüzden approx[0] dediğimizde bile [[10,20]] dönerdi, çünkü hala ekstra bir liste var.

# Sonra (Satır Formatı - (N,2))
# reshape(-1, 2) yaptığımızda o ekstra liste kaybolur ve her satır sadece (x, y) değerlerini içerir:

# less
# Kopyala
# Düzenle
# Her nokta: [X, Y]
# Böylece artık doğrudan approx[0][0] dediğimizde X değerine, approx[0][1] dediğimizde Y değerine ulaşabiliriz.

# 5. Sonuç
# Önce: (N,1,2) formatında dikey gibi duran iç içe listeler var.
# Sonra: (N,2) formatına çevirerek her satır bir nokta olacak şekilde düzenliyoruz.

#--------------------------------------------------------------------

# Senin attığın kodda, özellikle approxPolyDP fonksiyonunu kullanarak konturları bir poligona (yaklaşık bir şekle) dönüştürüyorsun. Bu işlemin sonunda, her bir kontur yaklaşıklaştırılmış poligonlara dönüşür. Bu poligonlar genellikle düzgün şekiller (örneğin, üçgen, dörtgen, vb.) oluştururlar.

# Bu kodda ravel()[0] ve ravel()[1] şeklinde iki indeksin alınmasının nedeni şu:

# 1. approxPolyDP Fonksiyonu
# approxPolyDP fonksiyonu, verilen konturu daha düzgün bir şekle (yaklaşık bir poligon) dönüştürür. Bu, özellikle keskin köşelerle tanımlanmış, düzgün olmayan şekilleri daha düzgün ve anlaşılabilir bir hale getirmeye yarar.
# Bu fonksiyon, her poligonun köşelerinin koordinatlarını döndürür.
# 2. Düzleştirme (ravel())
# ravel() fonksiyonu, numpy dizisini tek bir düz diziye dönüştürür. Bu, çok boyutlu bir diziyi 1D diziye çevirmek için kullanılır.

# approxPolyDP fonksiyonu ile elde edilen kontur koordinatları, çoğunlukla bir çok boyutlu dizi olarak gelir. Örneğin, bir üçgenin koordinatları şu şekilde olabilir:

# python
# Kopyala
# Düzenle
# approx = [[[10, 20]], [[30, 40]], [[50, 60]]]
# Eğer ravel() kullanırsak, bu dizi şu şekilde düzleşir:

# python
# Kopyala
# Düzenle
# flattened = [10, 20, 30, 40, 50, 60]
# Bu düzleştirilmiş diziyi kullanarak, her bir köşe koordinatına erişebiliriz.

# 3. İlk ve İkinci İndeksin Kullanılması
# Kodu şu şekilde açıklayalım:

# python
# Kopyala
# Düzenle
# x = approx_yani_yaklasma.ravel()[0]  # ilk köşe (x) koordinatını alıyoruz
# y = approx_yani_yaklasma.ravel()[1]  # ilk köşe (y) koordinatını alıyoruz
# ravel() ile diziyi düzleştirdik ve 0. ve 1. indeksler üzerinden ilk köşenin x ve y koordinatlarını aldık.

# Neden Bu İndeksler Kullanıldı?
# Buradaki mantık, şu şekilde işler:

# approx_yani_yaklasma.ravel()[0]: Bu, düzleştirilmiş dizinin ilk elemanıdır ve ilk köşenin x koordinatıdır.
# approx_yani_yaklasma.ravel()[1]: Bu, düzleştirilmiş dizinin ikinci elemanıdır ve ilk köşenin y koordinatıdır.
# Eğer bir şekil (örneğin, üçgen) varsa, ravel() işlemi sonrası her köşe sırasıyla x, y koordinatlarını düz bir dizi içinde yerleştirir. Bu yüzden ilk iki eleman ilk köşe'yi (x1, y1), sonraki iki eleman ikinci köşe'yi (x2, y2) ve üçüncü iki eleman da üçüncü köşe'yi (x3, y3) temsil eder.

# Neden Sadece ravel()[0]** ve **ravel()[1]` Kullanılıyor?
# Bu kodda sadece ilk köşe'yi işliyoruz. Çünkü drawContours veya diğer işlemler, genellikle sadece ilk köşe (ya da ilk iki koordinat) üzerinden işlem yapar. Bu işlem, sadece gösterim ya da sınıflandırma gibi bir işlemse, ilk köşeye bakmak yeterli olabilir.
# Eğer diğer köşelere erişmek isteseydik, ravel()[2] ve ravel()[3] (ikinci köşe), ravel()[4] ve ravel()[5] (üçüncü köşe) gibi indeksler kullanılırdı.
# Örnek:
# Bir üçgenin köşelerinin koordinatları şöyle:

# python
# Kopyala
# Düzenle
# approx = [[[10, 20]], [[30, 40]], [[50, 60]]]
# ravel() ile düzleştirildiğinde şu hale gelir:

# python
# Kopyala
# Düzenle
# flattened = [10, 20, 30, 40, 50, 60]
# flattened[0] = x1 = 10
# flattened[1] = y1 = 20
# flattened[2] = x2 = 30
# flattened[3] = y2 = 40
# flattened[4] = x3 = 50
# flattened[5] = y3 = 60
# Bu durumda, ravel()[0] ile ilk köşenin x koordinatına, ravel()[1] ile ilk köşenin y koordinatına ulaşmış olduk.

# Sonuç:
# Kodundaki ravel()[0] ve ravel()[1] kullanımı, sadece ilk köşe'yi almak için yapılmıştır. Eğer poligonun tüm köşelerine ihtiyacınız varsa, diğer köşelere erişmek için dizinin diğer indekslerine de bakabilirsiniz (örneğin, ravel()[2], ravel()[3]).