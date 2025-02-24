import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3],np.int32) #ilk parametre dizimiz,ikinci parametemiz ise türü.
print(x)

"""
np.array fonksiyonu, bir ndarray nesnesi oluşturur. 
Yani, np.array ile bir dizi oluşturduğunuzda, aslında numpy kütüphanesinin ndarray sınıfından bir nesne (object) oluşturmuş olursunuz.


    NumPy'nın kendisi Python'da bir kütüphane, ancak bu kütüphane altında tanımlanmış
    ndarray sınıfı, NumPy dizilerinin temelini oluşturur.   
    #KONU İLE ALAKALI CHAT SOHBET LİNKİM https://chatgpt.com/share/678f67eb-7bc4-800f-830f-89c2044b243b
"""
print(type(x)) # <class 'numpy.ndarray'> ndarray sınıfından bir nesne oluşturulduğunu gösterir.
print(x[0]);print(x[1]);print(x[2]) # 1 2 3
print(x[-1]) #sondan başlayıp  yazdirma işte.
print(x[-2])
