#her br kare(frame)ler birer resimdr.bunlar videoları olusturur.
#kare : videonun herhangi bir anındaki resimdir
#video bir çok karenin bir araya gelmesidir.

import cv2

#webcam ile video okuma --  capture(video yakalama) 
capture = cv2.VideoCapture(0) #sıfır dersen webcamden okuamdir.adres girersen bir dosyavideosundan okumadir.

while(True): #videoların karelerini tek tek okuyarak o şekilde videoları gösterecez.videonun süresini bilmedigimiz icin ben durduruna dek devam etsin döngü
    ret, frame = capture.read() #videonun karelerini okuyoruz. iki deger dondurur.videoları dogru okuduysa true/false.ikincisi ise kareler,framelerdir.
    frame = cv2.flip(frame,1) #webcamdeki görüntüyü ters çeviriyoruz.1 ise yatayda ters çevirir.y eksenine göre yani simetri alır.
    cv2.imshow("webcam",frame) #bi üstteki satirla frameleri okicaz,sonra bu frameleri göstercez.
    cv2.waitKey(1) #girilen  milisaniye kadar beklicek frameler.
    #sıfır yazarsan ilk framei alir.1 dersen 1ms bekler her frame arasinda
    if cv2.waitKey(1) & 0xFF == ord("q"): #qya basarsam videomu yani kamerami kapat.
        break #donguyu kiriyoruz.
    #0xFF in karsiliği klavyede q harfidir.ord fonksiyonu ise karakterin ascii degerini dondurur.

capture.release() #kamerayı serbest bırakıyoruz.eğer kapamazsak buununla bir islem yapamayiz.
#wordu kapatmazsan silemezsin mesela.
cv2.destroyAllWindows()#pencereyi kapatıyoruz.
    
#cekilen videoyu okuma gosterme
path = "C:\\Users\\Furkan\\Desktop\\video_okuma_izleme\\antalya.mp4"


capture2 = cv2.VideoCapture(path) #videonun adını yazıyoruz.
while(True):
    ret,frame = capture2.read()
    if ret == 0:
        print("video bitti")
        break
    cv2.imshow("antalya",frame)
    cv2.waitKey(1)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
    
capture2.release()
cv2.destroyAllWindows()