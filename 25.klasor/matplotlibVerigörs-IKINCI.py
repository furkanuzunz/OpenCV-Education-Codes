import numpy as np
import matplotlib.pyplot as plt

# N = 11
# x = np.linspace(0,10,N) #bu fonksiyon girdigim araliklarda bana veriler üretir.0 dan 10 a kadar toplamda N sayi yani 10 sayi versin.
# print(x) #birbirleriyle eşit aralıkta olacak şekilde üretir bu veriyi.

# y = x
# plt.plot(x,y,"o--") 
# #diyelimki çizdirdigimiz grafiğin eksenlerini görmek istemiyoruz.axis fonksiyonu kullaniriz.

# plt.axis("off") #eksenlerimiz kayboldu.
# plt.show()

print("*******")

z = [1,3,5,7,9]
plt.plot(z,[y**2 for y in z]) 
#bu üstteki y ekseni için yaptiğimiz ifade şunu diyor: y değerimiz z nin içinde dolaşsın sırayla
# ve her y degeri için de sirasiyla y**2 işlemi yapilarak listeye kaydedilsin.



plt.show()
