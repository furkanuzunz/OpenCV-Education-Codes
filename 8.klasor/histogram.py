import numpy as np
import cv2
import matplotlib.pyplot as plt 

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"

img2 = cv2.imread(path)
cv2.imshow("img2",img2)


#histogramdan bgr degerlerine ulasmasi zor olduug icin biz ulasalim
#cv2.split() resmin bgr degerlerini ayirir.
b, g, r = cv2.split(img2) #img2 3 tane deger sakladiği icin 3 tane verir

#sirasiyla bu degerlerin histogramlarini cizelim.
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

#histogramı kullanarak bazı çözümlemeler yapabiliriz
#histogram nedir? 
 #histogrami bir grafik olarak düsünebiliriz aslinda.
 #bu grafik bize resmin deger yogunlukları ile ilgili bilgiler verir.
 #yani bir resmin histogrmaina bakina o resmin aydinlik noktalarina  karanlik noktalarina ve konstrat degerleri ile
 #alakalı cikarimlarda bulunabiliyoruz.
 
 #önce bir resim olusturucaz ve bu resmin histogramini incelicez.
 #matplotlibkütphanesi ile yapcaz
 
img = np.zeros((500,500),np.uint8) + 50 #bos bir tuval olsutrduk siyah

#resim üzerine bir şeyler çizelim ve bakalim histogramimiz nasil olacak
cv2.rectangle(img,(0,60),(200,250),(255,255,255),-1)
cv2.imshow("img",img)



#histogrami cizme
#ilk parametre: imgyi ravelliyoruz.histogram cizebilmemiz icin.500w 500 lük bir siyah ekran olustrudk ya az önce
#bu pikselleri tek bir satir haline getiriyor.histogrami cizebilmemiz icin onemli.
#print(img.ravel()) calistir ve anla

#plt.hist(img.ravel(),bins = 256,range = [0,256]) #buradaki 256 aslinda 0 dan 255e kadar renk degerlerimv ya toplam 256 tane iste.
#500*500 250000 eder.grafikte bu kadar piksel oldugu y ekseninde gozukur. hepsi sifirlardan olusur siyahtir cunku


#plt.hist(img2.ravel(),bins = 256,range = [0,255])




#histogrami gosterme
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()
    

 
 