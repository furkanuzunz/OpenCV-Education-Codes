#webcamden aldıgımız goruntuleri bir dosya olarak kaydetmeyi öğrenicez.
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#her framelerimi bu outputa atıcam.sonra bu frmaleri dosya şeklinde kaydetmem gerekiyor. Bunun icin videoWriter fonksiyonunu kullanicaz.
fileName = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\6.Klasor\\webcam.avi"
#video ses ve görüntülerden olusur.biz bunları birleştirmek icin cesitli algoritmalar kullaniriz.codec dedigimiz bu kod çözucu de bu algoritmalardan biridir.
# Video kaydı için codec belirleniyor. WMV2 codec'i seçildi.

codec = cv2.VideoWriter_fourcc("W","M","V","2")#codecimizi belirledik. 4 tane karakter alır. # 
frameRate = 30 #frame odagımız
resolution = (640,480) #çözünürlük

# VideoWriter nesnesi oluşturuluyor. Video kaydını dosyaya yazmak için kullanacağız.

videoFileOutput = cv2.VideoWriter(fileName,codec,frameRate,resolution)
# Video kaydetmek için VideoWriter nesnesi oluşturuluyor.
# VideoWriter, kareleri belirli bir formatta video dosyasına yazmak için kullanılır.


while True:
    ret,frame = cap.read()# Kameradan bir kare (frame) okuyoruz.
    if ret == 0:
        print("kamera acilamadi")
        break
    
    
    frame = cv2.flip(frame,1)# Yatay olarak çeviriyoruz (ayna efekti verir).
    videoFileOutput.write(frame)  # Kaydedilecek videoya bu kareyi ekliyoruz
    cv2.imshow("webcam live",frame)
    # Klavyeden 'q' tuşuna basıldığında döngüden çıkıyoruz.
    # waitKey(1) fonksiyonu, 1 milisaniye boyunca bir tuşa basılıp basılmadığını kontrol eder.
    # Eğer basılan tuş 'q' ise, döngüyü sonlandırırız.
    # & 0xFF işlemi, farklı işletim sistemlerinde tutarlı sonuç almak için kullanılır.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()


