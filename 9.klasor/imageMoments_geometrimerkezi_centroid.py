import numpy as np
import matplotlib.pyplot as plt 
import cv2

#cv2.moment fonksiyonu bazı degerler tutuypr resimle alakalı,bir sözlük içinde tutuyor bunları.
#şeklimiizn merkeizni verir bize

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\contour.png"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

moment = cv2.moments(thresh)
#print(moment) #ciktida goruyoruz ki bir key value olayı var.ve {}ler arasinda tutuluyor bu bir sözlüktü demi
#buradaki değerlerin bazılarını kulanarak şekillerin ağırlık merkezlerini kullanabilirim değil mi.

#merkez koordinatlar x,y olsun. yukarıdaki moment degelerinin ilk üc kısmı ile ulascaz noktalara.

X = int(moment["m10"]/moment["m00"]) #print ile momenti yazdir orda görürsün m00 ları vesaire.
Y = int(moment["m01"]/moment["m00"])

cv2.circle(img,(X,Y),5,(0,125,255),-1)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
