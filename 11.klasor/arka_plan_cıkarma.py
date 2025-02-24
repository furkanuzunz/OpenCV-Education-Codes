import cv2
import numpy as np

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\11.klasor\\car.mp4"
capture = cv2.VideoCapture(path)

#otomatiklesen yöntem

# bg_substractor = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold=120,detectShadows= True)


# while 1:
#     ret,frame = capture.read()
#     frame = cv2.resize(frame,(640,480))
#     fg_mask = bg_substractor.apply(frame) #foreground maske hali, önün yani
    
#     cv2.imshow("frame",frame)
#     cv2.imshow("fg_mask",fg_mask)
    
#     if cv2.waitKey(20) & 0xFF == ord("q"):
#         break

# capture.release()
# cv2.destroyAllWindows()


######bu otomatik olan yöntemdi şimdi ise manueli yapalim
#bunu da şöyle yapicaz. 
#ilk frame ile diğer framee farklı olan yerleri beyaza aynı olan yerleri siyaha boyicaz.

#---ŞUNU HER ARKA PLAN CIKARMA İSLEMİNDE YAPARİZ, RESMİ GRİ TONA ÇEVİRMEK VE BİRAZCIK DA YUMUŞATMAK
#CUNKU GRİ TONA CEVİRİNCE BAZI RENK DEGERLERİNDEN KURTULUYORUZ İŞLEMLERİMİZ KOLAYLAŞIYOR.
# yumuşatmak = blurlamak

_,first_frame = capture.read() #tüm döngüleir çekmek istesek while ile yapariz işte
first_frame = cv2.resize(first_frame,(640,480))
first_f_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_f_gray = cv2.GaussianBlur(first_f_gray,(5,5),0)

while 1:
    _,frame = capture.read()
    frame = cv2.resize(frame,(640,480))
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray,(5,5),0)
    
    #grimsi şeyler görmek istemiyoruz o yüzden threshold uygulicaz.
    #difference_Frameye uygulicaz
    
    difference_frame  = cv2.absdiff(first_f_gray,frame_gray)
    # cv2.absdiff() fonksiyonu, iki görüntü arasındaki mutlak farkı hesaplamak için kullanılır. 
    # Bu yöntem, her piksel için iki görüntü arasındaki farkın mutlak değerini alır ve sonuç olarak bir fark görüntüsü oluşturur. 
    # Eğer iki çerçeve arasında değişiklik yoksa, sonuç görüntüsü tamamen siyah olacaktır. 
    _,difference_frame = cv2.threshold(difference_frame,25,255,cv2.THRESH_BINARY)
    #yani şuan sadece 1 ve sıfırlardan olustu
    cv2.imshow("frame",frame)
    cv2.imshow("first_frame",first_frame)
    cv2.imshow("diff",difference_frame)
    
    
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


 
 
capture.release()
cv2.destroyAllWindows()


# #difference frame e uyguladıgımız thresh islemi
# Kodunuzda uyguladığınız cv2.threshold() fonksiyonu, iki görüntü arasındaki mutlak farkı hesapladıktan sonra elde edilen difference_frame üzerinde bir eşikleme (thresholding) işlemi gerçekleştirir. Eşikleme, görüntü işleme alanında yaygın olarak kullanılan bir tekniktir ve temel olarak görüntüyü ikili (binary) hale getirir. Bu işlem, belirli bir eşik değerine göre piksellerin değerlerini sınıflandırır.

# Eşikleme İşlemi
# Kod Parçası
# python
# _, difference_frame = cv2.threshold(difference_frame, 25, 255, cv2.THRESH_BINARY)
# Parametreler
# difference_frame: cv2.absdiff() ile hesaplanan ve gri tonlamalı fark görüntüsünü temsil eden giriş görüntüsü.

# 25: Eşik değeri. Bu değer, piksellerin hangi koşulda beyaz (255) veya siyah (0) olacağını belirler.

# 255: Eşik değerinin üstündeki piksellere atanacak yeni değer. Yani, eğer bir pikselin değeri 25'ten büyükse, bu piksel 255 (beyaz) olarak ayarlanır.

# cv2.THRESH_BINARY: Uygulanan eşikleme türü. Bu türde, piksel değeri eşik değerinin altında ise 0 (siyah), üstünde ise 255 (beyaz) olarak ayarlanır.

# Nasıl Çalışır?
# Giriş Görüntüsü: difference_frame, iki çerçeve arasındaki mutlak farkı gösteren gri tonlamalı bir görüntüdür. Bu görüntüdeki piksellerin değeri genellikle 0 ile 255 arasında değişir.

# Eşik Değerinin Uygulanması:

# Eğer bir pikselin değeri 25'ten büyükse, bu pikselin değeri 255 (beyaz) olarak ayarlanır.

# Eğer bir pikselin değeri 25 veya daha az ise, bu pikselin değeri 0 (siyah) olarak ayarlanır.

# Sonuç: Elde edilen difference_frame, sadece iki renk içerir: beyaz ve siyah. Beyaz pikseller, iki çerçeve arasında önemli bir fark olduğunu gösterirken; siyah pikseller, değişiklik olmayan alanları temsil eder.

# Sonuç
# Eşikleme işlemi sayesinde, hareketli nesnelerin veya değişikliklerin daha belirgin hale gelmesini sağlarsınız. Bu tür bir ikili maske, daha sonra hareket tespiti veya nesne izleme gibi uygulamalarda kullanılabilir. Örneğin, beyaz pikseller hareketli nesneleri temsil ederken, siyah pikseller arka planı temsil eder. Bu işlem, görüntüdeki gürültüyü azaltmak ve yalnızca önemli değişiklikleri vurgulamak için oldukça etkilidir.