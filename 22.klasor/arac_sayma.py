import cv2
import numpy as np

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\22.klasor\\traffic.avi"
video = cv2.VideoCapture(path)

backsub = cv2.createBackgroundSubtractorMOG2()  #arka plan cıkarıcı nesnesi olustrudk
#ilk kareyi arka plan olarak alir,her yeni kare geldiğinde önceki arka planla karşılaştırarak değişen(haraketli)alanları
#belirler.değişen kısımları 255 , arka planı ise 0 olarak gösterir
#zamanla arka planı guncelleyerek ortam değişikliklerine uyum sağlar.

#cv2.createBackgroundSubstractorMOG2() nesne oluşturur, bu nesne kendi metodlarına sahiptir.
#backsub nesnesi mesela apply(frame) ederek , o framei işler ve arka planı cıkartır. 

c = 0# arac sayacimiz olsun

while True:
    ret,frame = video.read()
    if ret:
        foreground_mask = backsub.apply(frame)#arka planı cıkart,ön plan kalsın demek aslinda
        #framei alır,arka plan cıkarımı algoritmasi,bu yeni framede değişen pikselleritespiteder.ön planda olan bölgeler 255,arkadakiler 0 siyah olur yani.
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)
        
        contours,hierarchy = cv2.findContours(foreground_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try:hierarchy = hierarchy[0] ## buranin mantigini txt dosyasinda anlattim , bu mantıgı daha öncede kurmuştun.
        except:hierarchy=[]  ##hierarhy aslinda bi işimize yaramicak ama gene de hata ihtimaline karşin
        
        for contour,hierar in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)#bir konturu çevreleeyen dikdörtgenin koordinatlarını ve boyutlarını döndürür.
            if w > 40 and h > 40:
                cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
                if x > 50 and y < 70:
                    c+=1
        
        
        cv2.putText(frame,"car : "+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,cv2.LINE_AA)
        
        cv2.imshow("car counting",frame)
        cv2.imshow("fgmask",foreground_mask)
        
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break
video.release()
cv2.destroyAllWindows()