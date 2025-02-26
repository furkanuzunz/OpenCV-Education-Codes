import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\11.klasor\\hsv.mp4"
capture = cv2.VideoCapture(path)

circles = []
#tıklanan noktaların saklandıgı bir listedir. elemanları (x,y) koordinatları olacak


def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

cv2.namedWindow("frame")       
cv2.setMouseCallback("frame",mouse)
#frame penceresinde bir fare olayı gerceklestiğinde mouse fonksiyonunu cagirmasini söylüyoruz.
#OpenCV, bu pencereyi sürekli dinlemeye başlıyor.
# # OpenCV otomatik olarak mouse fonksiyonunu çağırıyor.
#  İşte burada devreye OpenCV'nin içsel C++ altyapısı giriyor.

# Kullanıcı pencereye tıkladığında, OpenCV bu olayı tespit eder.
# Tıklanan noktanın (x, y) koordinatlarını hesaplar.
# # Bu değerleri, cv2.setMouseCallback tarafından bağlanan mouse fonksiyonuna parametre olarak gönderir.
# Fonksiyon şu şekilde çağrılır:
# # mouse(cv2.EVENT_LBUTTONDOWN, x_koordinatı, y_koordinatı, flags, params)
# cv2.setMouseCallback("Frame", mouse)
# #"Frame" penceresinde fare olayı olursa mouse fonksiyonunu çağır ve koordinatları gönder.
# cv2.setMouseCallback: Zili kapıya takar ve çalınca sana haber verir.
# Kullanıcı tıklayınca (zil çalınca): OpenCV (x, y) bilgisini alır.
# mouse fonksiyonu: Zil çaldığında seni arayan kişi gibi, koordinatlarla birlikte çağrılır.


while True:
    ret,frame = capture.read()
    frame = cv2.resize(frame,(640,480))
    
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)
        #CİRCLES, aslinda (x,y) lerden olusur.centerda onlara tek tek ulasir
#         #her framede center koordinatlarına 20 yarıçapında mavi daire çizilir.
#         İlk tıklama: (100, 150)  O noktada bir daire oluşur.
# İkinci tıklama: (200, 250)  Başka bir daire oluşur. 
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("h"):
        circles = []
    
    
capture.release()
cv2.destroyAllWindows()  
    