 #matplotlib bir veri görselleştirme kütühanesidir.
 #elimzideki verileri dataları daha anlamlı hale getiririz.görselleştirerek.
"""
    pyplot yazmasaydık, matplotlib kütüphanesinin içindeki pyplot modülüne doğrudan erişemezdik.
    Bu durumda, pyplot modülünün sağladığı fonksiyonları (örneğin plot, show, xlabel, ylabel gibi) kullanamazdık. 
    
#Evet, pyplot, matplotlib modülünün bir üyesidir. Python'da modüller, içlerinde başka modüller, fonksiyonlar veya sınıflar barındırabilir.
# Bu yapıya modül hiyerarşisi denir. Örneğin:

matplotlib ana modüldür.

matplotlib.pyplot bu ana modülün içindeki bir alt modüldür.

pyplot modülünün içinde de plot, show, xlabel, ylabel gibi fonksiyonlar bulunur.

---------------------------------------------------------------------------
matplotlib bir ana modüldür ve içinde birçok alt modül bulunur. Örneğin:

matplotlib.pyplot (grafik çizim fonksiyonları)

matplotlib.figure (grafik figürleriyle ilgili sınıflar)

matplotlib.axes (eksenlerle ilgili sınıflar)

Bu alt modüller, ana modülün (matplotlib) içinde bulunur, ancak otomatik olarak içe aktarılmazlar. 
Yani, sadece import matplotlib dediğinizde, bu alt modüllere erişemezsiniz    
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)  # 0,1,2,3,4 # arange fonksiyonun içerisine girdiğimiz sayiya kadar sayi rüeten bir fonskiyondur.
 # print(x)
# print(type(x))   # <class 'numpy.ndarray'> ndarray , numpy modülünün bir sınıfıdır.np.array dedigimizde ndarray sınıfınınn bir örneğini nesnesini oluşturmuşuzdur demektir.
#yani aslinda ndarray sinifinin bir nesnesi örneği olan da numpy listesidir. çiktisi [0,1,2,3,4] şeklindedir.

y = x


#plt.plot(x,y,"o-") # plot fonksiyonu verileri görselleştirmek için 2d grafik çizer.
plt.show() #grafiği göstermek için bu fonksiyonu kullaniriz.
# eğerki biz düz çizgi değil de küçük o harfi ile çizilmesini istiyorsak plot fonksiyonunda üçüncü parametre olarka onu gönderiririz.
#hiçbir şey yazmazsak zaten düz çizer.
plt.plot(x,y,"o--")
#plt.show()

#aynı grafik üzerinde çizim yapıp farklı verileri kıyaslamak yorumlamak istersem ? 


plt.plot(x,-y)
plt.plot(-x,y,"o")
plt.title("y = x, y = -x") #grafiğimize ad koymak için
plt.show()