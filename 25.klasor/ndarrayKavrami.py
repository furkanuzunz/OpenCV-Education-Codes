#ndarray    n dimensional array demektir.
#ndarray cok boyutlu diziler için kullanılan bir kavramdır.

import numpy as np

# np.array bir fonksiyondur: np.array kütüphanedeki bir fonksiyon olup, çağrıldığında bir NumPy dizisi (numpy.ndarray nesnesi) döndürür.
# Python'da modüller, içlerinde fonksiyonlar, sınıflar ve diğer öğeler barındıran yapılardır. 
# Bir modülün içindeki bir öğeye erişmek için "nokta" (.) operatörü kullanılır.


#np ile numpy kütüpüne erişip .array ile array fonksiyonuna ulaşıyoruz.
#NP.ARRAY CAGİRİLDİĞİNDA NUMPY.NDARRAY sınıfından bir nesne oluşturur ve geri döndürür.
#NDARRAY NUMPY KÜTÜPHANESİNDE BİR SINIF ZATEN. NP.ARRAY İLE DE BU SINIFTAN BİR NESNE OLUŞTURUYRUZ.

x = np.array([[-2,-1,0,5],[9,4,5,-7]],np.int32)
print(x)

#ndarray aslında numpy kütüphanesinin bir sınıfıdr.np.array diye cagirdigimizda aslında ndarray sınıfının 
#bir nesnesini , örneğini oluştumuş oluyoruz.

print(x.shape) # x in boyutunu verir. 2 satır 4 sütun
print(x.ndim) # x in kaç boyutlu olduğunu verir. 2 boyutlu
print(x.dtype) # x in veri tipini verir. int32
print("\n",x.T,"\n") #bu x dizisinin transpozunu alır. 2x4 lük matrisi 4x2 lik matrise çevirir.
#yani satırları sütunları , sütunları satirlara cevirir.


print("******")
y = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],np.int32)
print(y.ndim) # y nin kaç boyutlu olduğunu verir. 3 boyutlu.
print(y.size) # y nin içinde kaç eleman olduğunu verir. 12 eleman var.