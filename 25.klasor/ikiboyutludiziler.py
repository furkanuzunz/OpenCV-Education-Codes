import numpy as np
import matplotlib.pyplot as plt #Bu ifade, matplotlib kütüphanesinin pyplot modülünü içe aktarır ve plt takma adıyla kullanılabilir hale getirir

x = np.array([[1,2,3],[4,5,6]],np.int32) #iki boyutlu dizi oluşturduk.matris gibi
print(x)
print("----")
y = np.array([[1,2,3],[3,4,6],[3,4,5]],np.int32) 
print(y)
#cok boyutlu dizilerin elemanlarına erişim
print("-----")
print(x[0]) # [1 2 3]  ilk satiri yazdirir.
print(x[0][0]) # 1 cıktısını verecek 0ıncının 0ıncı elemanı
print("-----")
print(y[1][2])

#diyelim ki ben x dizisinde 1 e ve 4e erişmek sitiyorum aynı satırda.farklı farklı cagırarak deği.
print("*****")
# : her şeyi tara anlamına gelir.  :, ise bu x de her şeyi tara.
print(x[:,0]) # taradıklarından 0ıncı elemanları al.yani iki sütuna da gidip bakcak sıfırıncı indekslerini alacak. ##Bu ifade, x dizisinin tüm satırlarını tarar ve her satırın 0. indeksindeki elemanları alır. Yani, ilk sütunu alır.
print(x[:,1]) #  Bu ifade, x dizisinin tüm satırlarını tarar ve her satırın 1. indeksindeki elemanları alır. Yani, ikinci sütunu alır. Çıktı [2 5] olacaktır.
print(x[:,2]) # Bu ifade, x dizisinin tüm satırlarını tarar ve her satırın 2. indeksindeki elemanları alır. Yani, üçüncü sütunu alır. Çıktı [3 6] olacaktır.


#bu yukarıda yaptıgımız aslında satırları tarayarak süutunları almak anlamına gelir.
#peki sütunları tarayarak satırları almak istersek;
print("*****")
print(x[0,:]) # Bu ifade, x dizisinin 0. satırını tarar ve tüm sütunlarını alır. Yani, ilk satırı alır. Çıktı [1 2 3] olacaktır.
print(x[1,:]) # Bu ifade, x dizisinin 1. satırını tarar ve tüm sütunlarını alır. Yani, ikinci satırı alır. Çıktı [4 5 6] olacaktır.

## yani ;     x[:, n] ifadesi tüm satirlari tarar ve n'inci sütundakileri alır. böylelikle sütunları çekmiş oluruz.
##            x[m ,:] ifadesi ise m'inci satiri tarar ve tüm sütunları alır. böylelikle satırları çekmiş oluruz.

