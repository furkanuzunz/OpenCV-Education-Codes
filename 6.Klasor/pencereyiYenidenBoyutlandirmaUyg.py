import cv2


# Burada bir pencere oluşturuyoruz ve bu pencereye "Orijinal resim" adını veriyoruz.
# # Bu pencere, ileride görüntüyü göstermek için kullanılacak.
cv2.namedWindow("Orijinal resim") 
path = "C:\\Users\\Furkan\\Desktop\\resim_okuma_gosterme_kaydetme\\klon.jpg"
img = cv2.imread(path)
# cv2.imread() fonksiyonu ile belirtilen dosya yolundaki resmi okuyoruz ve 'img' değişkenine atıyoruz.
# Eğer resim başarıyla yüklenirse, img değişkeni NumPy dizisi olarak saklanır.


img = cv2.resize(img,(640,480))#kendimiz boyutlandirdik
#bu boyutların original resimle aynı oranlarda olmasına dikkat etmeliyiz.




cv2.imshow("Orijinal resim",img)
cv2.waitKey(0) # herhangi bir tuş basılana kadar bekler.bit tuşa basıldıgıktan sonra tum peneeler destroyAllWindows sayesine kapanir.
# cv2.waitKey() fonksiyonu, bir tuşa basılmasını bekler.
# Parametre olarak verilen değer milisaniye cinsindendir. 
# 0 değeri, herhangi bir tuşa basılana kadar beklemeyi sağlar.  


cv2.destroyAllWindows()
