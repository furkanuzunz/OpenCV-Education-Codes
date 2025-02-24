import cv2
import numpy as np

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\10.klasor\\coins.jpg"
path2 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\10.klasor\\balls.jpg" 
image1 = cv2.imread(path)
image2 = cv2.imread(path2)

gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

#MEDYAN BLUR İŞLEMİ UGYULCAİZ.KARINCALAMARI GİDERSİN DİYE

img1_blur = cv2.medianBlur(gray1,5)
img2_blur = cv2.medianBlur(gray2,5)  #blurlamak önerilir ama zorunlu degil

#ikinci parametre = algılama methodu,çözünürlük oranı,min mesafe tespit edilen çemberler arasında,metoda özel parametre 1(gradient degeri),metoda özel parametre 2(threshold degeridir),çemberlerde bulunacagını düşündüğümüz min radius,max radius
circles = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,image1.shape[0]/4,param1 = 200,param2 = 10,minRadius=25,maxRadius=80) #cemberlerimin 5 ile 30 arasında bir deger esahip olunacagını tahmi ettik
 #mesafe tespiti icin yüksekliği 64 e bolduk.
#Bu fonksiyon circles adında bir değişken döndürür. 
# Eğer daireler tespit edilirse, bu değişken bir (1, N, 3) boyutlu NumPy dizisi olur. 
# Buradaki N, tespit edilen çember sayısını gösterir.
# Her çember [x, y, radius] formatında tutulur.

 
if circles is not None:
    circles = np.uint16(np.around(circles)) #bu 8, 16 feln bunlar aslında intin tuttugu aralıgı arttırmaktır.baska bir sey değil.
    #                      bu around aslında circlesin tuttugu degerleri yuvarlıyor
    #circles dizisindeki tespit edilen çemberlerin merkez koordinatlarını ve yarıçaplarını yuvarlar.
# HoughCircles fonksiyonu bu değerleri float32 olarak döndürür, ancak pikseller tam sayı olmalıdır.
# Yuvarlama ile bu değerler float yerine tam sayıya yakınsar.
# Yuvarlandıktan sonra, np.uint16() ile 16 bitlik işaretsiz tamsayıya dönüştürülü.circles.
# Bu aşamada negatif değerler olsaydı bile (örneğin -5 gibi), uint16 yalnızca 0 ve pozitif değerleri desteklediğinden negatif değerler sıfıra dönüştürülürdü
    for i in circles[0,:]: #0 dan 50 ye dolasaagız circlein icinde.
        cv2.circle(image1,( i[0] , i[1] ), i[2] ,(0,255,0),2) #x,y ile merkezi,i[2] ile radiusu aldık.
      


cv2.imshow("image1",image1)  
cv2.waitKey(0)
cv2.destroyAllWindows()
        
        
