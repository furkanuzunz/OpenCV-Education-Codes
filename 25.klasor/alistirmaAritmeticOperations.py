import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Furkan\\Downloads\\13.2 map.jpeg (1).jpeg"
img = plt.imread(path)

plt.subplot(4,2,1)
#ilk 2 argümanı kaça kaçlık (2 satir ve 2 sütun) bir graifk olustruacagımız yaziyoruz.üçüncü parametre ise
# ilk grafiği nereye hangi positiona koyacagımızı söylüyor.

plt.title("original image")
plt.imshow(img)
#iste resmin x ve y eksenlerine göre yansiamalrina bakcaz. bunu da subplot ile tek bir pencere üstünde görebilecez.z

#simdi resmi birbiri üzerine eklicez img+img . gibi. aslinda iki resmi toplamak
# iki resmin renk degerlerini toplamak demek.

plt.subplot(4,2,2)
plt.title("img + img")
#topladiginiz resimlerin boyutlarının aynı olmasına dikkat edin shape ile bakin iste ona da.
plt.imshow(img + img)

plt.subplot(4,2,3)
plt.title("img - img")
plt.imshow(img - img) #bütün renk degerlerini cikinca 0 olur siyah bir sey elde ederiz.

plt.subplot(4,2,4)
plt.title("np.flip 0 argümanli hali")
plt.imshow(np.flip(img,0)) # ikinci argüman 0,1,2 olabilir.
#0 x eksenine göre
#1 y eksenine göre
#2 renk degerleri degisiyo. yansima yok.

plt.subplot(4,2,5)
plt.title("np.flip 1 argümanli hali")
plt.imshow(np.flip(img,1))

plt.subplot(4,2,6)
plt.title("np.flip 2 argümanli hali")
plt.imshow(np.flip(img,2))

plt.subplot(4,2,7)
plt.title("np.fliplr(img)") #lr mean's left to right solu sağa koyuyo birnevi y eksenine göre simetri aliyo.
plt.imshow(np.fliplr(img))




plt.subplot(4,2,8)
plt.title("np.flipud(img)") # updownd resmi baş aşaği et demek.
plt.imshow(np.flipud(img))




plt.show()



