import cv2

path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\face.png"

image = cv2.imread(path1)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\eye.xml")
#cascade dosyalarını dahil et.

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x + w, y + h),(0,255,0),2)

#bu buldugumuz yuz koordinatlarında gozleri arayacagız.

#görseller satır,sütun formatında tutulur.yani (heigh,width) formatında.
#şöyle düşün satır sayısı aşağı doğru gidiyor bundan dolayı yukseklik yani y koordinatıdır.
#sütun sayısı ise sağa veya sola gidiyor genişlik yani x koordinatıdır.
gray_frame2 = gray_image[y:y+h,x:x+w] #tespit edilen koordinatlarla framei aslinda 
#satır bakımından y den baslayıp o yüüzn yüksekliği kadar aldık
#sütun bakıından ise x den baslayıp o yüzün genisliği kadar alıp sınırlamıs olduk yüzümüzü
 #şimdi bununla işlem yapcz. 
 
 #ve de gozlerimize dikdörtgen cizeceğimiz renkli resmin roisini alalım yuz icin
roi_image = image[y:y+h,x:x+w]

#simdi az önce gray_frame2 yi almıştık onunla eye detection yapalım

eyes = eye_cascade.detectMultiScale(gray_frame2)

for (eye_x,eye_y,eye_w,_eye_h) in eyes:
    cv2.rectangle(roi_image,(eye_x,eye_y),(eye_x + eye_w,eye_y + _eye_h),(0,0,255),2)
    
cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Kodda, gözleri tespit ettiğinizde roi_image üzerine dikdörtgenleri çiziyorsunuz. Ancak roi_image, image dizisinin bir alt kümesi (slice) olduğu için yapılan değişiklikler image üzerinde de etkili oluyor.

Python'da NumPy dizileriyle çalışırken, roi_image = image[y:y+h, x:x+w] dediğinizde, roi_image bağımsız bir kopya değil, image dizisinin belirli bir bölgesine referans verir. Yani roi_image üzerinde yaptığınız değişiklikler doğrudan image üzerinde de değişiklik yapar.

Bu yüzden, gözlere dikdörtgen çizdiğinizde aslında image dizisi değişiyor ve cv2.imshow("image", image) ile gösterdiğinizde, hem yüz hem de gözler üzerinde dikdörtgenler eklenmiş olarak görüntüleniyor.

Eğer gerçekten roi_image üzerinde değişiklik yapmak istiyorsanız ve bu değişikliğin image'i etkilemesini istemiyorsanız, şu şekilde bir kopya almanız gerekir:


roi_image = image[y:y+h, x:x+w].copy()
Bu şekilde, roi_image bağımsız bir kopya olur ve image'i etkilemez. Ancak şu anki kodda bu gerekmez çünkü zaten değişiklikleri image üzerinde görmek istiyorsunuz.

"""


