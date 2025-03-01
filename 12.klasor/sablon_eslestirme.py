import cv2
import numpy as np

'''
template.shape
Bu ifade, NumPy dizisinin boyutlarını (shape) döndürür.

Eğer template bir 2D görüntü ise (cv2.IMREAD_GRAYSCALE ile yüklendiğinde), template.shape şu şekilde bir tuple döndürür: (yükseklik, genişlik) (satır sayısı ve sütun sayısı).
Eğer template bir renkli görüntü ise (cv2.IMREAD_COLOR ile yüklendiğinde), template.shape şu şekilde bir tuple döndürür: (yükseklik, genişlik, kanal_sayısı).
2. [::-1]
Bu Python'da dilimleme (slicing) işlemi ile bir diziyi ters çevirir.

template.shape[::-1] ifadesi, shape tuple'ını ters çevirir.
Örneğin: (yükseklik, genişlik) -> (genişlik, yükseklik).
3. w, h
Bu kısımda, ters çevrilmiş tuple, iki değişkene atanır:

w (width): Şablonun genişliği.
h (height): Şablonun yüksekliği.
Neden Kullanılır?
OpenCV'de birçok işlem, görüntünün genişlik (x ekseni) ve yükseklik (y ekseni) değerlerine göre yapılır.
Ancak, NumPy'nın shape özelliği bu değerleri (yükseklik, genişlik) olarak döndürür. [::-1] ile bu sıralama (genişlik, yükseklik) olarak değiştirilir ve kodun daha okunabilir olması sağlanır.

'''
image_path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\starwars.jpg"
template_path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\starwars2.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template = cv2.imread(template_path,cv2.IMREAD_GRAYSCALE)#yukseklik ve genislik donderdi.
w,h = template.shape[::-1] #biz bunu genislik ve yukseklik olarak kullanacagiz.

#[::-1] işlemleri pythonda bir dizi veya stringin elemanlarını ters çevirmek için kullanılır.

result = cv2.matchTemplate(gray_image,template,cv2.TM_CCOEFF_NORMED)
#result matrisinde her piksel, şablonun o noktada ne kadar iyi eşleştiğini belirtir. Bu matrisin değerleri 0 ile 1 arasında değişir.
location = np.where(result >= 0.95)#resultumdan gelen degerler ne kadar 1 e yakinsa şablonumun bulunacagi yerde o kadar yakindir.
#np.where(result >= 0.95) ifadesi, 0.95 veya daha yüksek değerlerin bulunduğu yerleri (yani yüksek eşleşme değerlerini) döndüren bir indeksler listesi verir.







#bir tuple veya listenin ögelerini ayrı ayrı elemanlar olarak kullanılabilir hale getirmek istersek
# başına * koyabiliriz.


#zip fonnksiyonu birden fazla iteratif yapısını örneğin liste, tuple, string vb.
#birleştirip, her biri bir eleman içeren bir tuple yapısına dönüştürür.
#zip fonksiyonu ile birleştirilen yapılardan en kısa olanı baz alınır.
for point in zip(*location[::-1]):
    cv2.rectangle(image,point,(point[0] + w , point[1] + h),(0,255,0),3)
    '''
    Hayır, point ile point[0] aynı şey değiller. Aralarındaki farkı açıklayayım:

point:
point, *zip(location[::-1]) ile elde edilen her bir eşleşme koordinatıdır ve bu bir tuple (iki elemanlı bir liste) olarak gelir. Bu tuple'da:
point[0]: x koordinatını (sütun koordinatı) temsil eder.
point[1]: y koordinatını (satır koordinatı) temsil eder.
Örneğin, point = (50, 30) olduğunda:
point[0] = 50 (x koordinatı, yani sol üst köşedeki yatay pozisyon).
point[1] = 30 (y koordinatı, yani sol üst köşedeki dikey pozisyon).
point[0]:
point[0], point tuple'ının ilk elemanıdır. Bu genellikle x koordinatını ifade eder (yani, sol üst köşe koordinatındaki yatay pozisyon).
Örneğin:

point = (50, 30) olduğunda:
point[0] = 50, x koordinatıdır.
point[1] = 30, y koordinatıdır.
Kodda Kullanım
Kodda şu kısımla karşılaşıyoruz:

python
Kopyala
Düzenle
cv2.rectangle(image, point, (point[0] + w, point[1] + h), (0, 255, 0), 3)
point: Bu, şablonun eşleştiği sol üst köşe koordinatlarını (x, y) içerir.
point[0] + w: Bu, dikdörtgenin sağ alt köşesinin x koordinatını hesaplar. point[0] başlangıçtaki x koordinatıdır, w ise şablonun genişliğidir, yani sağa doğru olan mesafedir.
point[1] + h: Bu, dikdörtgenin sağ alt köşesinin y koordinatını hesaplar. point[1] başlangıçtaki y koordinatıdır, h ise şablonun yüksekliğidir, yani aşağıya doğru olan mesafedir.
Özet
point: Tuple (x, y) koordinatlarıdır.
point[0]: point tuple'ının ilk elemanı olan x koordinatıdır.
    '''

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
location = np.where(result >= 0.95)
np.where, result matrisindeki değerleri kontrol eder.
result matrisinde, eşleşme oranı 0.95 veya daha yüksek olan elemanların indekslerini döndürür.
Sonuç: location bir tuple’dır ve her boyut için eşleşme indekslerini içerir:
location[0]: Y eksenindeki eşleşme indeksleri (satırlar).
location[1]: X eksenindeki eşleşme indeksleri (sütunlar).
2. location[::-1]
location[::-1] ifadesi, location tuple'ını tersine çevirir:
İlk eleman X ekseni (sütunlar), ikinci eleman Y ekseni (satırlar) olur.
Bu, OpenCV’nin dikdörtgen çizerken x, y sıralaması beklemesi nedeniyle yapılır.
3. *location[::-1]
* operatörü, ters çevrilmiş location tuple’ını açar (unpack eder).
Sonuç:
zip(*location[::-1]) ifadesi, X ve Y eksenindeki eşleşme indekslerini birleştirerek birer birer tuple haline getirir.
4. zip(*location[::-1])
zip, X ve Y eksenindeki koordinatları eşleştirir:
Örneğin:
python
Kopyala
Düzenle
location = (array([50, 100]), array([30, 70]))
zip(*location[::-1])  # [(30, 50), (70, 100)]
Bu çıktı, eşleşen bölgelerin koordinatlarını sağlar: (x, y) formatında.
5. for point in zip(*location[::-1])
Döngü, her eşleşen bölge için bir point değeri alır.
point, bir tuple’dır ve şablonun bulunduğu sol üst köşe koordinatlarını içerir: (x, y).
6. cv2.rectangle
Her döngü adımında:

point: Eşleşen bölgenin sol üst köşesinin koordinatlarıdır.
(point[0] + w, point[1] + h): Eşleşen bölgenin sağ alt köşesinin koordinatlarını hesaplar.
w: Şablonun genişliği.
h: Şablonun yüksekliği.
cv2.rectangle: Görüntü üzerinde dikdörtgen çizer.
image: Üzerinde işlem yapılan ana görüntü.
point: Dikdörtgenin sol üst köşesi.
(point[0] + w, point[1] + h): Dikdörtgenin sağ alt köşesi.
(0, 255, 0): Dikdörtgenin rengi (yeşil).
3: Dikdörtgenin kalınlığı.
Özet
Amaç: Şablonun eşleştiği bölgeleri ana görüntüde işaretlemek.
Döngünün Çalışma Mantığı:
zip(*location[::-1]) ile eşleşen bölgelerin (x, y) koordinatlarını birer birer alır.
Bu koordinatlara göre bir dikdörtgen çizer.
Tüm eşleşen bölgeler üzerinde işlem yapar.
Görsel Çıktı: Ana görüntüde, şablonun bulunduğu yerler yeşil dikdörtgenlerle işaretlenmiş olur.







Şunu dedin:
location = (array(\[50, 100\]), array(\[30, 70\])) zip(\*location\[::-1\]) \# \[(30, 50), (70, 100)\]

burada nasil 30,50 oldu
ChatGPT:
Bu örnekte, location şu şekilde tanımlanmış:

python
Kopyala
Düzenle
location = (array([50, 100]), array([30, 70]))
Burada location bir tuple'dır ve bu tuple'ın iki elemanı vardır:

array([50, 100]): Bu, şablon eşleşmesinin X eksenindeki (sütunlar) koordinatlarını temsil eder. Yani, şablonun eşleştiği X koordinatları: 50 ve 100.
array([30, 70]): Bu da şablon eşleşmesinin Y eksenindeki (satırlar) koordinatlarını temsil eder. Yani, şablonun eşleştiği Y koordinatları: 30 ve 70.
location[::-1] Açıklaması:
[::-1] ile location tuple'ı tersine çevriliyor, yani X ve Y koordinatları yer değiştiriyor. Bu durumda:

python
Kopyala
Düzenle
location[::-1]  # [(30, 50), (70, 100)]
Orijinal: ([50, 100], [30, 70])
Ters çevrilmiş: ([30, 70], [50, 100])
Yani, Y koordinatları (satırları) ve X koordinatları (sütunları) tersine çevrilmiş oldu.

zip(*location[::-1]) Açıklaması:
Burada * operatörü location[::-1] tuple'ını açarak Y ve X koordinatlarını birbirine eşleştirir. Yani:

İlk eleman (30, 50)
İkinci eleman (70, 100)
Bu durumda zip fonksiyonu şu şekilde çalışır:

python
Kopyala
Düzenle
zip([30, 70], [50, 100])  # [(30, 50), (70, 100)]
Sonuçta:

(30, 50): Y eksenindeki 30, X eksenindeki 50 ile eşleşir.
(70, 100): Y eksenindeki 70, X eksenindeki 100 ile eşleşir.
Bu şekilde her bir (y, x) koordinat çifti elde edilir.

Özet:
location[::-1] ifadesi, Y ve X koordinatlarını yer değiştirir.
zip(*location[::-1]) ile bu yeni koordinatlar (y, x) formatında birleştirilir.
'''

