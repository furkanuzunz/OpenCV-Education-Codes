import cv2
import numpy as np

canvas = np.zeros((512,512,3),np.uint8) #np.uint8 cizim yaptigimizda kullanacagimiz veri tipidir. 
#np zeros fonksiyonunun amaci belirli bir alanda siyah bir tuval oluşturmaktir.
#canvas aslinda tuvalin ingilizcesidir.cizim ekranidir aslinda yani.
# 512x512 boyutunda 3 kanalli (RGB) bir tuval olusturduk.
# (512,512,3) üç boyutlu bir dizi oluşturur aslinda genişlik,yükseklik ve renk kanallari
# np.zeros fonksiyonu ile 0'lardan olusan bir dizi olusturuyoruz. 0 siyah rengi temsil eder.
# np.uint8 ise 0-255 arasinda deger alabilen 8 bitlik bir tam sayi veri tipidir.
#goruntu islemede piksel degerlerini temsil etmek icin kullanilir.
# 0 siyah 255 beyaz rengi temsil eder. ve goruntu islemede genellikle 0-255 arasinda degerler kullanilir.

# print(canvas) #sifirlardan olusan bir matris elde ettik. O ın bgr karisliği siyahtir.
# cv2.imshow("Canvas",canvas) #siyah bir tuval elde edicez.
# cv2.waitKey(0) #0 olunca ekranda bekler ve kapatilana kadar bekler.
# cv2.destroyAllWindows() #pencereleri kapatir.

#normalde (255,255,255) beyazdir demi dizide.
# bunun icin de matristeki tüm degerlere 255 eklicem.
 #ister bunu diretk np.zeros ifadesinden sonra + 255 diyerek yap ya da alttaki gibi
canvas[:] = [255,255,255] #bunu yaparak da ayni islemi yapabiliriz.
print(canvas) # 255lerden olusan bir matris elde etttik

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()