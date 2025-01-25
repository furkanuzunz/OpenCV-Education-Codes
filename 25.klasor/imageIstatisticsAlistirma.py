#aslinda resim dedigimiz sey her bir pikseldeki renklerin belli bir oranda bir araya gelmesinden oluşur.
#biz bu piksellerin ve renklerin birleşmesine resim diyoruz.
# biz bu pikselllerdei renk degerlerini kullanarak bazi istatistiksel hesaplamalar yapabiliriz.
#bu sekilde hangi rengin nerede daha yogun oldugunu bulabiliriz.

import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Furkan\\Downloads\\11.2 smile.jpg.jpg"
img = plt.imread(path)

#önce resmin sahip olduğu piksellerdeki en kucuk degeri bulcaz
print(img)
print("min value",img.min()) #cikti sifir geldi yani bir yerlerde sifir da varmiş.
#Görüntüdeki en küçük piksel değerini bulur.
#Eğer görüntü renkli (RGB) ise, tüm kanallardaki (Red, Green, Blue) en küçük değer bulunur.

print("max value",img.max())
#rgb, red green blue zaten 
#yani mesela red 255 tir green 255tir blue da 255tir orası beyazdır
#hepsinin sifir oldugu yerler siyahtir.
"""
rgb de bu şekilde 
Bir pikselin değeri [255, 0, 0] ise, bu tam red rengi temsil eder.
[0, 255, 0] tam green, [0, 0, 255] tam blue rengini temsil eder.
"""
print("mean : (ortalam)",img.mean())

print("medyan : ",np.median(img)),
print("average:",np.average(img))
print("mean2 : ortalamanin bir diğer hesaplama şekli",np.mean(img))
#aklimiza gelecek her türlü hesaplamayi numpy kütüpü ile yapariz.
