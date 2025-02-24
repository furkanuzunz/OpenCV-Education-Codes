
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)
plt.plot(x, [y**2 for y in x]) # () kullanirsan tuple olur.elemanlari sonradan degisemezler.listelere göre daha hızldırılar.
plt.plot(x,[y**3 for y in x])   #küpünü aldik.
plt.plot(x,[y*2 for y in x]) # iki ile çarpilmiş hal
plt.plot(x,[y*5.2 for y in x])

#hangi grafiğin hangisinin kodu oldugunu anlayabiliriz
plt.legend(["x**2","x**3","x*2","x*5.2"],loc = "upper center") #bunun yerini değiştirmek için 6 noktamız var. üst vs. bunu da bir parametre ile yapıyoruz. loc anahtar kelimesi ile
# upper center = üst orta


#grafik üzerine bazı eklemelr yapcaz. bir grafikte onları incelerken ızgaralar bize yardımcı olurlar.
# bunun icin de bir fonksiyon vardır. grid fonksiyonu
plt.grid(True)



#x ve y eksenleirne ad koymak?
#x = np.arange ile geldi
# y yi ise biz hallettik
plt.xlabel("x = np.arange")
plt.ylabel("y = f(x)")


# print(plt.axis()) #bu bize x ve y eksenlerindeki max ve min noktalari verir.
#bu max ve minleri düzeltmek istersek
plt.axis([0,2,0,10]) #x ekseni 0 dan 2 ye. y ekseni ise 0 dan 10 a gitsin degerleri.
plt.title("Simple plot")

#kaydetmek hepsini
plt.savefig("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\kaydedilenler\\grafik")


plt.show()