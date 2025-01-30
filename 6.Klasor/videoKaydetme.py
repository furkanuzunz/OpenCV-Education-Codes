#webcamden aldıgımız goruntuleri bir dosya olarak kaydetmeyi öğrenicez.
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#her framelerimi bu outputa atıcam.sonra bu frmaleri dosya şeklinde kaydetmem gerekiyor. Bunun icin videoWriter fonksiyonunu kullanicaz.
fileName = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\6.Klasor\\webcam.avi"
#video ses ve görüntülerden olusur.biz bunları birleştirmek icin cesitli algoritmalar kullaniriz.codec dedigimiz bu kod çözucu de bu algoritmalardan biridir.
codec = cv2.VideoWriter_fourcc("W","M","V","2")
frameRate = 30 #frame odagımız
resolution = (640,480) #çözünürlük

videoFileOutput = cv2.VideoWriter(fileName,codec,frameRate,resolution)



while True:
    ret,frame = cap.read()
    if ret == 0:
        print("kamera acilamadi")
        break
    
    
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)
    cv2.imshow("webcam live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()