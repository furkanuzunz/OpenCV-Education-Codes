import numpy as np

x = np.empty([4,3],np.uint32)
print(x); # aslinda boş diziden kasitta da rastgele sayilar atanıyor derleyici tarafindan.

print("*****")

y = np.full([3,3,3],dtype = np.int32,fill_value=5)
print(y) # bu yaptıgımız bizim belirlediğimiz sayiyla gene bizim belirlediğimiz boyutlardaki matrisi doldurmakti.

print("****")

z = np.ones([2,5,5],dtype=np.int32)
print(z) #birlerden olusan bir matris verdi.
#görüntü işlemede birlerden olusan bir dizi beyaz ekranı temsil ediyor.

print("****")

s = np.zeros([2,3,3],dtype=np.int32)
#görüntü işlemede sifirlardan olusan bir dizi   siyah ekranı temsil ediyor.
print(s)