import cv2

path = "C:\\Users\\Furkan\\Desktop\\Yeniklasör\\calisma.mp4"
#bu videoyu kaydedelim.

capture = cv2.VideoCapture(path)
#sey gibi aslinda iste Book sınıfı var ya , Book nesne gibi burda da nesne = VideoCapture() gibi. pythonda nesne tanimlama sytnaxi farkli biraz.
#cv2.VideoCapture OpenCV kütüphanesinin bir parçasıdır ve video dosyalarını veya 
 #kamera akışlarını okumak için kullanılan bir sınıftır.
# capture = cv2.VideoCapture(path) satırında, VideoCapture sınıfından bir nesne oluşturuyorsunuz.
# Bu nesne (capture), belirtilen video dosyasını (path) açar ve bu videoyla ilgili tüm işlemler için kullanılır.
# Yani, capture nesnesi, VideoCapture sınıfının bir örneği (instance) olarak düşünülebilir.
#Bir sınıfın metodlarına (fonksiyonlarına) erişmek için nesne adını ve nokta (.) operatörünü kullanırsınız.
#18.satirda bunun örneği var.

kaydedilecekYer = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\6.Klasor\\istenilenAndakiFrame.jpg"

while True:
    ret,frame = capture.read() # VideoCapture sınıfının capture nesnesi yolu ile read() metodu çağrılıyor.
    if(ret == 0):
        print("video bitti")
        break
    cv2.imshow("dersVideosu",frame)
    if (cv2.waitKey(1) & 0xFF == ord("s")):
        cv2.imwrite(kaydedilecekYer,frame)
        print("frame kaydedildi",{kaydedilecekYer}) #s ye basarsam o anki frameyi kaydeder.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
capture.release()
cv2.destroyAllWindows()#tüm pencereleri kapatır.




    