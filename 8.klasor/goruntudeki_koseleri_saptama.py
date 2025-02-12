import numpy as np
import cv2

path2 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\contour.png"
path1 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\text.png"
img2 = cv2.imread(path2)
img1 = cv2.imread(path1)

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#Bu fonksiyonun doğru çalışması için, giriş görüntüsünün float32 türünde olması gereklidir. 
gray = np.float32(gray)
# img1,en fazla kac kose,kalite degeri,köşeler arasi min mesafe
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)


#bu köseleri cizebilmek icin
corners = np.int64(corners) #tekrardan inte cevirmemizin sebebi,çemberler cizerken float sayilar kullanamiyoruz.
#köşeleri çemberlerle belirlicez ondan

for corner in corners:
    x,y = corner.ravel() #çemberin merkez koordinatlari aldik.önce cornersi tek bir satir haline getirdik.
    cv2.circle(img1,(x,y),3,(0,0,255),-1) # img1 in üstüne çizicez
    #buradaki mevzuyu köşebulma.txt dosyasında acıklamayı oku
cv2.imshow("corners",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()