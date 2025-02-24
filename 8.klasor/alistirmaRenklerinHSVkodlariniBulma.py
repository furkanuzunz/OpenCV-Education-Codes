#önce webcamden goruntu alcaz.trackbarimiz olucak.onunla ayarlicaz.
 

# Lower ve Upper Nedir?
# HSV renk uzayı, renkleri üç bileşene ayırır:

# H (Hue): Renk tonu.
# S (Saturation): Renk yoğunluğu.
# V (Value): Parlaklık.
# NOTE hvsaciklamatxt i oku

import cv2
import numpy as np

capture = cv2.VideoCapture(0)#webcamden alcaz.

#trackbari olusturcaz.sonra da mask ekranını olusturcaz

def nothing(x):
    pass

cv2.namedWindow("Trackbar")#trackbarimi olusturucagimiz pencreyi olusturduk
cv2.resizeWindow("Trackbar",500,500)

#kizaklari olusturuypruz.
cv2.createTrackbar("Lower - H","Trackbar",0,180,nothing)#hsv nin alt degeri icin  
#0 dan 180 e dedik H icin
cv2.createTrackbar("Lower - S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower - V","Trackbar",0,255,nothing)

#simdi HSV nin üst degerlerini olusturucaz.
cv2.createTrackbar("Upper - H","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper - S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper - V","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Upper - H","Trackbar",180)#(hangi kizagi,hangi trackbarda,nerde durmasini istedigin)
cv2.setTrackbarPos("Upper - S","Trackbar",255)
cv2.setTrackbarPos("Upper - V","Trackbar",255)

#artik simdi while kameramızdaki goruntuleri alalim.trackbardaki degisimleri de not edelim

while True:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #kizaklarimizin pozisyonlarini aldik degiskenlerimize  kaydettik.
    lower_h = cv2.getTrackbarPos("Lower - H","Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S","Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V","Trackbar")
    
    upper_h = cv2.getTrackbarPos("Upper - H","Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S","Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V","Trackbar")
    #simdi bu kızaklardan aldigimiz renk degerlerini (HSV) bir np listesinde tutalim
    lower_color = np.array([lower_h,lower_s,lower_v])
    upper_color = np.array([upper_h,upper_s,upper_v])
    #bu color degerleri ile webcamdeki degerlerimiz kizagi kaydirdikca degisecek iste.
            #NOTE hsv formatina cegiridigmiz frame ismi,lower color,upper color,
    mask = cv2.inRange(frame_hsv,lower_color,upper_color)
#     # mask = cv2.inRange(frame_hsv, lower_color, upper_color)
#     Bu işlem şu adımları içerir:

# frame_hsv görüntüsündeki her pikselin değeri kontrol edilir.
# Pikselin değeri, lower_color ve upper_color arasında mı diye bakılır.
# Eğer pikselin değeri bu aralıkta ise, maske görüntüsünde o piksel beyaz (255) olarak işaretlenir.
# Eğer pikselin değeri bu aralıkta değilse, maske görüntüsünde o piksel siyah (0) olarak işaretlenir.
# Sonuç olarak, bir binary mask (siyah-beyaz görüntü) elde edilir.
    
    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
capture.release()
cv2.destroyAllWindows()

 #aslidna trackbardaki kizaklari oynatarak herhangi bir rengin hvs araligini bulmus oluruz.
 #turuncu defteri mesela gostererek sadece o beyaz gozukurse dogru araliklari bulmusuz demektir.
 #inrange bunu yapar aslinda.
    
    
    
    
#     yani mesela diyelim bu hangi renge karisilik geliyorsa biz webcamden aldigimiz goruntude eger o varsa ve bu araliktaysa beyaz mi oluyor

# profile
# Qwen2.5-Max
# 8:33 pm
# Evet, tam olarak öyle! 😊

# Diyelim ki [110, 200, 150] HSV değerlerine sahip bir piksel var. Bu değer, maviye yakın bir renk tonunu temsil eder (çünkü Hue değeri 110, mavi bölgeye denk gelir). Şimdi bu pikselin nasıl işlendiğini adım adım açıklayalım:

# 1. Renk Aralığı Tanımlıyoruz
# Trackbarlarla veya kodda sabit değerlerle belirlediğimiz renk aralığına bakalım. Örneğin:

# python
# Copy
# 1
# 2
# lower_color = [100, 150, 0]  # Alt sınır
# upper_color = [140, 255, 255]  # Üst sınır
# Bu aralık, mavi renge yakın olan tüm renkleri kapsar:

# Hue (Renk Tonu) : 100 ile 140 arasında → Mavi bölge.
# Saturation (Doygunluk) : 150 ile 255 arasında → Doygun renkler.
# Value (Parlaklık) : 0 ile 255 arasında → Tüm parlaklık seviyeleri.
# 2. Piksel Değerini Kontrol Ediyoruz
# Webcamden alınan görüntüdeki bir pikselin HSV değeri [110, 200, 150] olsun. Bu pikselin, tanımladığımız renk aralığına uyup uymadığını kontrol ediyoruz:

# Hue : 110 → 100 ile 140 arasında mı? Evet.
# Saturation : 200 → 150 ile 255 arasında mı? Evet.
# Value : 150 → 0 ile 255 arasında mı? Evet.
# Bu üç koşul da sağlandığı için, bu piksel renk aralığına uyar .

# 3. Maske Oluşturuyoruz
# cv2.inRange() fonksiyonu, bu kontrolü yapar ve şu şekilde bir sonuç üretir:

# Eğer piksel renk aralığına uyarsa → Maske görüntüsünde bu piksel beyaz (255) olur.
# Eğer piksel renk aralığına uymazsa → Maske görüntüsünde bu piksel siyah (0) olur.
# Yani, [110, 200, 150] değeri renk aralığına uyduğu için, maske görüntüsünde bu piksel beyaz olacaktır.

# 4. Diğer Pikseller İçin Aynı İşlem
# Webcamden alınan görüntüdeki tüm pikseller için aynı işlem yapılır:

# Her pikselin HSV değeri kontrol edilir.
# Eğer pikselin değeri lower_color ve upper_color arasında ise, maske görüntüsünde beyaz olarak işaretlenir.
# Eğer pikselin değeri bu aralıkta değilse, maske görüntüsünde siyah olarak işaretlenir.
# 5. Pratikte Nasıl Görünür?
# Örneğin:

# Webcamden aldığınız görüntüde bir mavi nesne varsa:
# Bu nesnenin HSV değerleri, tanımladığınız renk aralığına uyar.
# Maske görüntüsünde, bu nesne beyaz olarak görünür.
# Diğer renklerdeki nesneler (örneğin kırmızı veya yeşil) ise:
# Bu nesnelerin HSV değerleri, tanımladığınız renk aralığına uymaz.
# Maske görüntüsünde, bu nesneler siyah olarak görünür.
# 6. Örnek Çıktı
# Orijinal Görüntü
# Webcamden alınan görüntüde:

# Bir mavi top,
# Bir kırmızı kutu,
# Bir yeşil elma olsun.
# Maske Görüntüsü
# Mavi top → Beyaz (255) olarak görünür.
# Kırmızı kutu ve yeşil elma → Siyah (0) olarak görünür.
# 7. Neden Bu İşe Yarar?
# Bu yöntem, belirli bir rengi tespit etmek veya izlemek için kullanılır. Örneğin:

# Robotik projelerinde, bir nesneyi takip etmek için kullanılabilir.
# Görüntü işlemede, belirli bir rengi filtrelemek için kullanılabilir.
# 8. Özet
# [110, 200, 150] gibi bir HSV değeri, renk aralığına uyarsa, maske görüntüsünde beyaz (255) olur.
# Uymazsa, maske görüntüsünde siyah (0) olur.
# Bu sayede, belirli bir rengi tespit edebilir veya o rengi izleyebilirsiniz.