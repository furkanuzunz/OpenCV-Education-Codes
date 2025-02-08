#renk uzayi basitce belirli renk organizasyonlarina verilen isimdir
#reismler belirli renklerin bir araya gelmesiyle oluşutlrar.
#bu bir araya gelmesi aslinda bir renk organizasyonudur.
# renklerin cok fazla olmasi onlari siniflandirma ihtiyacı duymustur bu sekildede renk uzayi kavrami cikmistir.

#BGR renk uzayi, temel islemleri bgr formatinda yapariz.
#NOTE her bir goruntu belirli bir renk organizasyonuna , renk uzayına sahiptir.BGR,RGB modda olabilir.
#bir modlari birbirine donsutruebiliriz
#cv2.color fonksiyonunu kullanabiliriz

import cv2
path = "c:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/klon1.jpg"
img = cv2.imread(path)

#normalde BGR formatinda.bunu ben degisebilirim.
#rgbye cevirelim
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#rgbye donderdigimizde renk yogunuklari bi tık degisti mesela.

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("klon BGR",img)
cv2.imshow("klon RGB",img_rgb)
cv2.imshow("klon HSV",img_hsv)
cv2.imshow("klon GRAY SCAEL",img_gray)

#INFO goruntu islemede resimleri gri skalaya getirmemizdeki amac aslinda, renkli gorsellerde uc kanal oldugu icin islemesi zor olmasidir.
#grileri ise islemesi kolaydir.




cv2.waitKey(0)
cv2.destroyAllWindows()