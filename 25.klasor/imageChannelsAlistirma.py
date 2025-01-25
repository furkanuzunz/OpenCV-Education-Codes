
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Users\\Furkan\\Downloads\\13.2 map.jpeg.jpeg"
#resmin icindeki rgb piksellerinin bulundugu yerleri cekicez ve bunlari degisken üzerinde tutup onlara bir bakicaz.

#resimlerin channels leri ile ilgilencez rgb kanallari ile yani

img = plt.imread(path) #rgb formatinda okur. red green blue

# [r,g,b] şeklinde her pikselde bir yogunluklari vardir bu kanallarin.
# yani ben herhangi bir pikselin sıfırıncı indeksindeki channel değerine ulaşırsam neye ulaşmış olurum ;;;
# ; o pikseldeki red degerine ulasmis oluyorum.



#yani diyelimki 50 ye 50 pikseldekim red degerini [50,50,0] seklinde aliriz.
# tüm piksellerdeki mavi rengi cekmek istersem [:,:,2] seklinddir
# r -> 0 255 degerleri arasinda degisir.
# g -> 0 255
# b -> 0 255

#buradaki kafa karisikligi 
# C:\Users\Furkan\Desktop\OpenCVegitim\kaydedilenlerveaciklamalar\kanalRenkDizi_mevzusu.txt burada var

red_channel = img[:,:,0] #buradaki anlam aslinda tüm satir ve sütunları tarayip red degerini alicagimizdi.
#hani image statistics dosyasinda print(img) dedik ya orada noldu bize işte
# # [148 214 238]
#   [148 214 238]
#   [148 214 238]
# şu şekilde bi çikti verdi demi.yani aslinda görüntünün numpy dizisi olarak temsil edilmiş halidir.
# bu dizideki her bir eleman , bir pikselin RGB degerlerini icerir.
# her bir satir , görüntünün bir satirini temsil eder, ve her bir eleman bir pikselin rgb değerlerini içerir.
# örneğin 148,214,238 var ya red 148 green 214 blue 238 dir.
# aslinda dizi şu şekilde temsil ediliyor ve şekli [yükseklik,genişlik,3] şeklinde
# yani satir sütun ve 0:red, 1:green,2:blue 3 tane yani.
# red kanalini almak icin [:,:,0] kullanilir. tüm satir ve tüm sütunları tara redi al.

# bu üstte 12.satirda şey demişiz ya [r,g,b] işte o bu üstte cikan 148 214 238 degerleri aslinda.
# [148 214 238]
#   [148 214 238]
#   [148 214 238] Bu yapı, bir görüntünün bir bölgesindeki piksellerin RGB değerlerini gösterir. Her bir satır, bir pikselin RGB (Red, Green, Blue) değerlerini içerir. Örneğin:
#bu yapi 3 satır işte.

# DORDUNCU matplotlibVerigörs dosyasinda var bir şeyler oraya da bak.

# [148, 214, 238]: Bir pikselin RGB değerleri.

# Red (Kırmızı): 148

# Green (Yeşil): 214

# Blue (Mavi): 238

# -----------
# Evet, her bir satır farklı bir pikseli gösterir. Örneğin:

# İlk satır [148, 214, 238]: Birinci pikselin RGB değerleri.

# İkinci satır [148, 214, 238]: İkinci pikselin RGB değerleri.

# Üçüncü satır [148, 214, 238]: Üçüncü pikselin RGB değerleri.


# #Verilen çıktıda, örneğin ilk piksel [148, 214, 238] şeklindedir:

# Red (Kırmızı): 148

# Green (Yeşil): 214

# Blue (Mavi): 238

# Eğer bu pikselin Red (Kırmızı) değerini almak isterseniz:

# code:
# pixel = [148, 214, 238]
# red_value = pixel[0]  # Red (Kırmızı) değeri
# print(red_value)  # Çıktı: 148
# Aynı şekilde, tüm görüntünün Red (Kırmızı) kanalını almak için:



# Verilen çıktıda:

# [[[148 214 238] ...:

# Bu, görüntünün ilk satırındaki piksellerin RGB değerlerini gösterir.

# Örneğin, [148, 214, 238] pikselinin Red değeri 148'dir.

# ... [162 219 239] ...:

# Bu, görüntünün başka bir bölgesindeki piksellerin RGB değerlerini gösterir.

# Örneğin, [162, 219, 239] pikselinin Red değeri 162'dir.

# [[241 237 234] ...:

# Bu, görüntünün başka bir satırındaki piksellerin RGB değerlerini gösterir.

# Örneğin, [241, 237, 234] pikselinin Red değeri 241'dir.





red_channel = img[:, :, 0]
green_channel = img[:,:,1]
blue_channel = img[:,:,2]

output = [img,red_channel,green_channel,blue_channel]
titles = ["image","red","green","blue"]
for i in range(4): #4kez dönecek sıfırdan baslayip
    plt.subplot(2,2, i + 1) #bu fonksiyon alt çizgiler alt grafikler olsuturucak
    # 2 satir ve 2 sütundan oluscak diyoruz.
    # i + 1 diyoruz cunku 1.grafik diye baslicak.
    #bu sublot aslinda bir alani 2 satir ve 2 sütun olcak sekilde 4 parcaya ayirir.i+1 ise grafiklerin sağ üstte cart curtunu belirler.
    plt.axis("off") #eksenleri kapadik
    plt.title(titles[i]) #grafiklerin isimlerini cekcek
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap = "gray") # rgblerin bölgelerni daha net görmek icin griye cevirebiliriz
        #aydinlik kisimlarda mesela red daha fazladir 2.grafikte gibi vs vs
    plt.show()
    
#numpy da bir fonksiyon var ve bu fonksiyonla daha önce elde ettigim renk degerlerini karistiriarak mix ederek
#orijinal resmi elde edebiliriz.
output = np.dstack((red_channel, green_channel, blue_channel))
plt.imshow(output)
plt.show()