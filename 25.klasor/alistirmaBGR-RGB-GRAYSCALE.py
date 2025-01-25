import numpy as np
import matplotlib.pyplot as plt
import cv2

# path = "C:\\Users\\Furkan\\Downloads\\11.2 smile.jpg.jpg"
# img = cv2.imread(path,1)  #0 yazdigimizda boz tonlarda yani gri tonlarda okurdu.1 de ise bgr formatinda okur #cv2 imread bunu BGR formatta okuyor.
# #bgr da mavi,yeşil , kirmizi şeklinde siralanir. rgb de ise kirmizi yeşil mavi şekilde

# plt.imshow(img)
# plt.show() #resimin biraz degisik cikmasinin sebebi ben resmimi cv2 imread ile okudum ama plt.imshow ile gösterdim.bundna dolayı plt de rgb formatinda gözükür.
# #bu yüzden resim bi tık degisik cikar.

# #bu karmasikligi düzeltecez.bunu da ilk başta bgr formatinda okudum resmi cv2 kütüphanesi kullanarak rgb formatina cevirecez.

# #---------------------------------------------------# 
 
# path = "C:\\Users\\Furkan\\Downloads\\11.2 smile.jpg.jpg"
# img = cv2.imread(path,1)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# plt.imshow(img) #rgb gelcek
# plt.show() #orijinal halindeki gibi cikicak.


#------------------------------
#peki resmi gri formatta göstermek istersek ??? 

# path = "C:\\Users\\Furkan\\Downloads\\11.2 smile.jpg.jpg"
# img = cv2.imread(path,1)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# plt.imshow(img,cmap = "gray",interpolation= "BICUBIC") #cmap demek color map aslinda.
# #GRİ YAPARKEN CMAP VE İNTERPOLATİON KEYWORDLERİNİ KULLANMAMİZ GEREKİYOR.
# plt.show()

#--------------------
# bunu daha kisa şekilde yapabiliriz.
path = "C:\\Users\\Furkan\\Downloads\\11.2 smile.jpg.jpg"
img = cv2.imread(path,0) #2.parametreyi sifir yapariz otomatikmen gri olur.
plt.imshow(img,cmap = "gray",interpolation= "BICUBIC")
plt.show()