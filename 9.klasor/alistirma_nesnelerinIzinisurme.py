import numpy as np
import matplotlib.pyplot as plt 
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\dog.mp4"

capture = cv2.VideoCapture(path)

while(1):
    ret,frame = capture.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #rgb sesklinde iz süremeyeiz ondan framelerimizi hsvye ceviriyoruz.
    #beyaz nesnenin tespiti icin en uygun aralıgı bulmaliyiz.google dan bulabiliriz
    sensitivity = 15
    lower_white = np.array([0,0,255 - sensitivity]) #hsv code for red
    upper_white = np.array([255,sensitivity,255])
    
    #hsvye cevirdigimiz frameleri cagırıyoruz.
    mask = cv2.inRange(hsv,lower_white,upper_white) #maske uyguladık aslında
    #cv2.inRange(hsv, lower_white, upper_white) fonksiyonu, her bir pikselin HSV değerini kontrol eder ve şu işlemi uygular:
    result_frame = cv2.bitwise_and(frame,frame,mask = mask)
     #result = cv2.bitwise_and(frame, frame, mask = mask)
        #  Bu satırda:
        # 1. İlk `frame` kaynak görüntüyü temsil eder
        # 2. İkinci `frame` hedef görüntüyü temsil eder
        # 3. `mask` parametresi ise hangi piksellerin işleme alınacağını belirler

        # `cv2.bitwise_and()` fonksiyonu iki görüntü arasında "VE" (AND) mantıksal operasyonu gerçekleştirir. Burada aynı görüntüyü (frame) iki kere kullanarak, maskenin belirlediği bölgelerde orijinal görüntüyü korumak, diğer bölgeleri ise karartmak istiyoruz.

        # Eğer farklı iki görüntü kullansaydık:
        # ```python
        # result = cv2.bitwise_and(image1, image2, mask = mask)
        # ```
        # Bu durumda `image1` ve `image2`'nin kesişim bölgelerini görürdük. Ancak amacımız sadece maskenin belirlediği bölgeleri göstermek olduğu için, aynı görüntüyü iki kere kullanıyoruz.

        # Bu işlem sonucunda:
        # - Maskenin beyaz (1) olduğu bölgelerde orijinal görüntü korunur
        # - Maskenin siyah (0) olduğu bölgeler karartılır
    
    cv2.imshow("frame",frame)
    cv2.imshow("maske",mask)
    cv2.imshow("result",result_frame)    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:#(yani escye bastigimizda)
         break
    
cv2.destroyAllWindows()