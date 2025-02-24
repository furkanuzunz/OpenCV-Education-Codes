import numpy as np

x = np.array( [[1,2,3],[4,5,6]],np.int32)
#print(x)
#tek boyut tek bir yönde ilerleyen diziler demektir.
#ama hem doğu batı hem kuzey güneyde ilerlerlse iki boyutlu demektir.
#üçüncü boyutu nasıl yapacağız.

#üç boyutlu dizi oluşturmak için:
#hem aşağı yukarı hem sağa sola hem de bir derinlik olur hani z kooridnatı gibi düşün.

y = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]],np.int32) #2 katmanı var bunun.her katmanda 2 satır ve 3 sütun var.
print(y)
#aslında her bir köşeli parantez boyut belirtiyor.
print(y.shape) # (2, 2, 3) 2 katman var her bir katmanda 2 satır ve 3 sütun var.
#yani aslında ilk iki dizimde benim 2 boyutlu bir düzlemim vardı.o parantezden cıkıp
#yeni bir 2 boyutlu düzlem oluşturunca derinliği arttırmış oluyorum.en sonunda da tümünü tek paranteze alıp 3.boyutu oluşturuyorum.

#elemanlara ulaşma
print(y[0,0,0]) #1e ulasirirz. olusturdugmuz bu 3 boyutlu diziyi koordinat sistemi olarak düşünücez.
 # ilk "0" bize katmanı verir. ikinci "0" bize satır. üçüncü "0" bize sütun verir.
 #yani ilk sıfır bize ilk iki boyutlu düzleme giriş yapmamızı sağlar. 

print(y[0,1,0]) #4 ü verir. 0 ıncı katmanın 1.satirinin 0 inci sütunu.
print(y[1,1,1]) #11 i verir. 1. katmanın 1. satırının 1. sütunu.
print("*****")
 #dizinin tamamını print(y[:,:,:]) yazarak da yazdırabiliriz.
print(y[0,:,:]) # 0. katmanın tüm satırlarını ve sütunlarını yazdırır.
print("*****")
print(y[0,1,:]) # 0. katmanın 1. satırını ve tüm sütunlarını yazdırır.
print("*****")
print(y[0,:,0]) # 0. katmanın tüm satırlarını ve 0. sütununu yazdırır. yani 1 ve 4 ü.