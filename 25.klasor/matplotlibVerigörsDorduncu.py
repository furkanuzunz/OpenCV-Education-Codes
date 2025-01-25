import numpy as np
import matplotlib.pyplot as plt

# cv2 kütüphaneis ile resmi okurken cv2.imread ve cv2.imshow dermişiz.

#simdi ise pyplot modülünden okicaz
# plt.imread ve plt.imshow

path = "C:\\Users\\Furkan\\Downloads\\10.1 coins.jpg.jpg"
img = plt.imread(path)
#print(img) #sayisal bir şeyler çıktı olursa okuma başarilidr. #bu yazili biz görsel istiyoruz tabi

# plt.imshow(img)
# plt.show() # 2 adimda gösterebiliyo bize.

print("dizeyini yani liste şeyini verdi\n",img);print("type:",type(img));print(" shape :",img.shape);print("ndim:",img.ndim);print("size",img.size);print("dtype",img.dtype)

#resmin channel değerlerine erişçez kırmızı yeşil ve maci channela.

print("red channel",img[50,50,0]) #rgb ise red = 0.indekste green 1 , blue ise 2 dedir.
#bunun anlami 50 ye 50 pikseldeki red degerini ver.
print("green channel",img[50,50,1])
print("blue channel",img[50,50,2])

#hepsine birden ulasmak istersek
print("rgb channel value :",img[50,50,:])

print(img[:,:,0])