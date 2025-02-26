import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\11.klasor\\eye_motion.mp4"

video = cv2.VideoCapture(path)

while 1:
    ret,frame = video.read()
    if ret is False:
        break

    roi = frame[80:210,230:450]
    rows,cols,_ = roi.shape
    #(height, width, channels) döndürür.

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    
    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)
    
    
    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    contours = sorted(contours,key=lambda x : cv2.contourArea(x), reverse=True)
    #contourlarımı sıralıcam
    #2. parametre ise neye göre sıralicamiz,lambda fonksiyonu tanımlıyprum , x degskeni kullanilacak bu fonksiyonda
    #contour degerlerim lambda fonksiyonuna göre sıralancak.yani areaların büyüklüğüne göre
    #x ler de contourstan geliyor.
    #reverse ise tersten sırala demek.büyükten kucuge yani
    #mantık su göz bebeğimin bulundgu o konturlarda en buyuk kontur alanıma odaklanicam
    
    
    
    #simdi o en büyük kontur alanıma odaklanip oraya dikdörtgen cizicez.
    #altta da aslinda ilk conoturuma çizip break diyip cıkıyorum..en büyüğü zaten az önce
    # sıralayıp en basa aldik ya.
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        #x = dikdörtgenin sol üst köşesinin x koordinatı
        #y = dikdörtgenin sol üst köşesinin y koordinatı
        #w = dikdörtgenin genişliği
        #h = diködrtgenin yüksekliği
        
        #(x,y) dikdörtgenin sol köşesi 
        #(x + w, y + h) ise diködrtgenin sağ alt köşesi.şöyle düşün y artınca aşağı iniyosun.ters düşün
        cv2.rectangle(roi,(x,y),(x + w, y + h),(255,0,0),2)
        cv2.line(roi,(x + int(w/2) , 0),(x + int (w / 2),rows),(0,255,0),2)
        cv2.line(roi,(0, y + int(h / 2)),(cols,y + int(h/2)),(0,255,0),2)
        
        break
    
    frame[80:210,230:450] = roi
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(80) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    