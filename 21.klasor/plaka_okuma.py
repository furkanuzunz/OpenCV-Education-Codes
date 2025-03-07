from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import imutils#buda aslinda bir dzi görüntü işleme fonksiyonlari içerir
import cv2
import numpy as np


image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\21.klasor\\licence_plate.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray,6,250,250)#amacımız plaka harici yerlerin gürültüsünü kaybetmek.plaka dışındaki yerlerin keskin hatlarını azaltmaya calsııyoruz.
#resim,çap,sigma color,sigma space,

edges = cv2.Canny(filtered,30,200)
#min,max değer
#min , zayıf kenarları tanımlamak için , max ise güçlü kenarları tanımlar.


#contourları yapıcaz simdi.
contours = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
####3print("kontour",contours)
#SİMDİ İMTUİLS KÜTÜPÜ İLE UYGUN KONTURLARI CEKİCEZ.

cnts = imutils.grab_contours(contours)
#uygun konturları yakala
#bunları sıralicaz şimd,yani uygun koordinatlı konturları sıralıcaz.
#biz art arda sıralanmıs noktalara bakıcam, eğer dikdörtgen görürsem onu alıcam gibi düşümn
#cunku biz diğer gürültüleri engelledik baya, plaka harici dikdörtgen yoktur.
####print("imutils grab contours",cnts)


cnts = sorted(cnts,key = cv2.contourArea,reverse = True)[:10] #0 dan 10 a kadar olan degerler için.ilk 10 büyük kontoru al.
#ikinci paramete = alana göre sıralama,reverrse true ise girdiğimiz değerleri tersten sıralıyo
###print("sorted contours",cnts)


screen = None #bunu sunun icin kullanıyoruz eğer o kapalı dikdörtgen alanını sıraladıgımız yerlerden birind bulursak bu none luktan cıkcak artık

#simdi biz kapalı bir alan dikdörtgen aricaz.
for c in cnts:
    #böyle mesela eğri bir karenin konturlarını bulmak icin bir yaklasım uygulicaz.
    epsilon = 0.018* cv2.arcLength(c,True)
#arclenght konturların yay uzunlugunu bulur.oradaki True boslugun olup olmadıgıdr.eğer bosluk yoksa bu koordinatlar arasında devam et demek.
    
    #approx şuan ne tutuyor,konturların daha köşelere yaklaşılmış halini tutuyor.
    #eğer 4 tane ise noktalar,burada bir dikdörtgen vardır.
    approx = cv2.approxPolyDP(c,epsilon,True) #approx mevzusu en aşağıda analttıld.
    if len(approx)==4:
        screen = approx
        break

#simdi algıladıgımız bu bölgeye mask uygulicaz.
mask = np.zeros(gray.shape,np.uint8) #suan mesela siyah ekran olustu demi aynı boyutlarda imagemizle.
#az sonra mevzu söyle işleyecek , bu siyah ekran , normal gray imagemizin üstüne gelicek ve gezicek,bir tek plaka alanımız siyah olmayacak .

new_image = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
#lk gireceğimiz değer mask , cunku buldugumuz dikdörtgeni aslinda birnevi o siyah ekranda gösteriez.
#screen de zaten koordinatları tutuyor.

#simdi ise o plaka bölgesindeki yazıyı kontur üzerine yapıştıalım
new_image2 = cv2.bitwise_and(image,image,mask = mask) #mask alanına imageyi yapıştırıyo aslında bu.
# cv2.bitwise_and fonksiyonu, genellikle iki görüntü üzerinde mantıksal "AND" işlemi yapmak için kullanılır. Bu işlem, her pikselin her iki görüntüde de belirli bir koşulu sağlaması durumunda bir sonuç üretir. Bu, görüntü üzerinde bir maske kullanarak sadece belirli bir bölgeyi seçmek için oldukça faydalıdır.

# bitwise_and Fonksiyonu:
# Parametreler:
# image1: İlk görüntü (bu genellikle orijinal görüntü olur).
# image2: İkinci görüntü (bu genellikle maske olur).
# mask: Maskeyi uygular. Maskede beyaz (255) olan pikselleri kabul eder, siyah (0) olanları göz ardı eder.
# Nasıl Çalışır:
# Her iki görüntüde de aynı konumda olan piksellerin değerlerine bakılır.
# Eğer maskenin değeri 255 ise, bu pikseller orijinal görüntü ile işleme alınır.
# Maskenin değeri 0 ise, bu pikseli tamamen yok sayar.
# Örneğin, eğer bir maske sadece belirli bir bölgede beyazsa, bitwise işlemi ile bu beyaz bölgedeki piksellerin değerleri korunur, diğer bölgeler sıfırlanır.
# Kullanım Senaryosu:
# Bu işlem, özellikle bir bölgenin (örneğin, plaka alanı gibi) maskelenip, sadece o bölgenin çıkarılması veya işlenmesi gerektiğinde çok yaygındır. Maskenin beyaz olan kısımları, orijinal görüntüden alınan piksellerle birleşir, siyah kısımlar ise yok sayılır.

# Kodunuzda:

# new_image2 = cv2.bitwise_and(image, image, mask = mask)
# Burada, image iki kez kullanılıyor. Bu, orijinal görüntünün maskeyle birleştirilmesini sağlıyor.
# mask değişkeni, plaka alanını (dikdörtgen alanı) gösteren bir maskedir.
# Maskenin beyaz olan kısımlarında orijinal görüntü, diğer bölgelerde ise siyah (yok) pikseller oluşur.
# Özetle:
# Bu işlem, yalnızca belirli bir bölgeyi, burada plaka bölgesini seçmek için kullanılır.
# Maskede beyaz olan bölgeler korunur ve orijinal görüntüyle birleştirilir.


#simdi en son kalan resmi kırpıp yazıyı k-okuyalım

#bu where bize aslinda bir liste döndürür.[241,244,22,4,3],[456,4678,653,] gibi x,y bunlari ttuar
(x,y) = np.where(mask ==255) #eğer beyaz bölgelerin oldugu yerse  -o koordinatları tut demek.
(topx,topy) = (np.min(x),np.min(y)) #miny dedik cuunku max istiyoruz ama o da en yukarda zaten
#aynı sekil minx de öyle en soldai x lazım.sol köşeyi almak için
(bottomx,bottomy) = (np.max(x),np.max(y))
# np.where(mask == 255) fonksiyonu, mask değişkenindeki beyaz piksellerin x ve y koordinatlarını döndüren iki NumPy dizisi oluşturur. 
# Yani, maskede 255 (beyaz) olan tüm piksellerin (x, y) koordinatları, bu iki dizide tutulur.

# Örneğin, diyelim ki bir mask görüntüsü şu şekilde:

# lua
# Kopyala
# Düzenle
# [[  0,   0, 255,  0, 255],
#  [255,  0, 255,  0,  0],
#  [  0,   0,  0,  0,  0],
#  [255,  0,   0,  0, 255]]
# Bu durumda, np.where(mask == 255) çıktısı şu şekilde olacaktır:

# Çıktı:
# python
# Kopyala
# Düzenle
# x, y = np.where(mask == 255)

# print(x)  # x koordinatları (yatay)
# # [0 0 1 1 3 3]

# print(y)  # y koordinatları (dikey)
# # [2 4 0 2 0 4]
# Bu örnekte:

# x dizisi, beyaz piksellerin yatay (x) koordinatlarını tutar: 0, 0, 1, 1, 3, 3
# y dizisi, beyaz piksellerin dikey (y) koordinatlarını tutar: 2, 4, 0, 2, 0, 4
# Açıklama:
# İlk beyaz piksel (0, 2) olduğu için x[0] = 0, y[0] = 2
# İkinci beyaz piksel (0, 4) olduğu için x[1] = 0, y[1] = 4
# Üçüncü beyaz piksel (1, 0) olduğu için x[2] = 1, y[2] = 0
# Dördüncü beyaz piksel (1, 2) olduğu için x[3] = 1, y[3] = 2
# Beşinci beyaz piksel (3, 0) olduğu için x[4] = 3, y[4] = 0
# Altıncı beyaz piksel (3, 4) olduğu için x[5] = 3, y[5] = 4
# Yani, mask görüntüsündeki tüm beyaz piksellerin yatay ve dikey koordinatları x ve y dizilerinde sırasıyla saklanır.

# Daha Somut Bir Örnek:
# Eğer mask görüntüsü çok daha büyük ve kompleksse, bu dizilerdeki değerler daha fazla olur. Örneğin, bir 5x5'lik bir görüntüde her beyaz pikselin koordinatları bu dizilerde saklanır.





kirpilmis = gray[topx:bottomx + 1, topy:bottomy+1]

#simdi bunu okicaz
text = pytesseract.image_to_string(kirpilmis,lang="eng")
print("detected text",text)

# cv2.imshow("yazılı hal",new_image2)
# cv2.imshow("maskeye cizildi",mask)

# cv2.imshow("1.image",image)
# cv2.imshow("2.gray",gray)
# cv2.imshow("3.filtered",filtered)
# cv2.imshow("4.edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()



# #*mask islemi
# Evet, mask işlemi genellikle başka şekillerde de kullanılır, ancak burada kullanılan örnek belirli bir işleme yönelik. Şöyle açıklayayım:

# python
# Kopyala
# Düzenle
# mask = np.zeros(gray.shape, np.uint8)
# Bu satırda mask değişkeni şu şekilde oluşturuluyor:

# np.zeros(gray.shape, np.uint8):
# Bu, sıfırlardan oluşan bir NumPy dizisi oluşturur. gray.shape ifadesi, gray adlı gri tonlamalı görüntünün boyutlarını alır. Örneğin, eğer gray görüntüsü 500x500 piksel boyutlarında ise, mask da 500x500 boyutlarında olacaktır.
# np.uint8 tipi, her pikselin 0-255 arası bir değeri temsil edeceği 8 bit tamsayı tipi olduğunu belirtir. Yani, bu mask dizisi bir görüntü maskesi olacaktır.
# Mask Kullanımı:
# Maskeler, genellikle görüntü işleme işlemlerinde belirli bölgeleri seçmek veya gizlemek için kullanılır. Örneğin:

# Region of Interest (ROI) Seçimi: Maskeler, bir görüntünün sadece belirli kısımlarını seçmek için kullanılabilir. Sıfır olan pikseller maskelenmiş olur, diğer pikseller seçilmiş olur.
# Yüzey veya Kontur Tanımlaması: Kontur tespiti, nesne tanıma gibi işlemler için maskeler oluşturulabilir. Belirli bir nesne veya alan, sıfırlarla maskelenip, diğer her şey işlemeye alınabilir.
# Örnek Kullanım:
# Sıfırlardan Oluşan Maskeyle Görüntü Üzerinde İşlem: Maskeyi oluşturduktan sonra, bir alanı beyaz (255) yapıp, gerisini siyah (0) bırakabilirsiniz. Örneğin, yalnızca belirli bir kontur üzerinde işlem yapabilirsiniz:

# python
# Kopyala
# Düzenle
# mask = np.zeros(gray.shape, np.uint8)  # Sıfırlardan oluşan bir maske
# cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)  # Konturları beyazla çiz
# result = cv2.bitwise_and(image, image, mask=mask)  # Maskeyi görüntü üzerinde uygula
# Görüntüyü Maskeye Uygulamak: Burada, mask üzerinde yalnızca beyaz alanları (konturların olduğu yer) tutarak, sadece bu bölgeleri image üzerinde işlem yapabilirsiniz.


# #****************approx işlemi ****************
# cv2.approxPolyDP fonksiyonunun ne yaptığına bakalım.

# cv2.approxPolyDP ve approx:
# cv2.approxPolyDP fonksiyonu, konturların daha düzgün bir şekilde, yaklaşık bir poligon haline getirilmesi için kullanılır. Yani, bir konturun tüm köşelerini daha az sayıda, daha belirgin noktalarla temsil etmek amacıyla kullanılır.
# Bu işleme "kontur nokta sayısını azaltma" denebilir.

# Parametreler:
# c: Kontur (bu, cv2.findContours ile elde edilen bir dizi noktadır).
# epsilon: Bu, yaklaşık doğruluk değeridir. Yüksek bir değer, daha az köşe ile birleştirilmiş şekiller oluşturur, düşük bir değer ise daha fazla köşe ile daha ayrıntılı bir şekil oluşturur.
# True: Bu, konturun kapalı olup olmadığını belirtir. Eğer True verilirse, şekil sonrasında da kapanır.
# Örneğin, bir dairesel şekil verildiğinde, approxPolyDP onu dörtgen gibi bir şekle yaklaştırabilir. Bu durumda da 4 köşe elde edilebilir.

# Nasıl Çalışır?
# Şimdi, approx değişkenine odaklanalım. approx içinde şunlar bulunur:

# approx, cv2.approxPolyDP fonksiyonu kullanılarak oluşturulan yaklaşık köşeler listesini tutar.
# Eğer bir konturun köşe sayısı 4 ise, bu, dörtgen olduğunu belirtir. Bu durumda, plaka gibi dikdörtgen bir şekil bulmayı amaçlıyoruz, ve len(approx) değeri 4 olursa, bu konturun dörtgen olduğu anlamına gelir.
# Örneğin, aşağıdaki adımlarda:

# Eğri bir şekil (örneğin bir elips) verildiğinde, cv2.approxPolyDP fonksiyonu bu şekli daha az köşe ile (örneğin dörtgen) yaklaştırabilir.
# Eğer bu şekil dörtgen (4 köşe) ise, approx içinde 4 nokta olacaktır.
# Kodda, eğer len(approx) == 4 ise, bu şekli dörtgen olarak kabul ediyoruz.
# Örnek:
# 
# epsilon = 0.018 * cv2.arcLength(c, True)
# approx = cv2.approxPolyDP(c, epsilon, True)
# cv2.arcLength(c, True) fonksiyonu, konturun çevresini hesaplar.
# epsilon = 0.018 * çevre uzunluğu ifadesi, bu çevrenin 0.018 katı kadar bir yaklaşık doğruluk değeri belirler.
# cv2.approxPolyDP(c, epsilon, True) fonksiyonu, bu doğruluğa göre konturun noktalarını azaltarak daha düzgün bir şekil oluşturur.
# approx ve len(approx):
# Eğer dört köşe varsa (len(approx) == 4), bu şekil dörtgen olarak kabul edilir.
# Şayet approx içinde 4 nokta varsa, plaka gibi bir dikdörtgen olduğunda bu noktayı bulabiliriz ve işlemi bitiririz (screen = approx).
# Kodda approx ile Ne Yapılıyor?
# Kontur tespiti sonrası, approx ile yaklaşık köşeler elde ediliyor. Bu köşeler 4 tane olduğunda (yani dikdörtgen olduğunda), plaka bölgesini bulmuş oluyoruz. Sonrasında bu bölgeyi maskeleyerek orijinal görüntüde yalnızca plakanın olduğu alanı seçmiş oluyoruz.

# Özet:
# approx: Bu, cv2.approxPolyDP fonksiyonu ile elde edilen konturun yaklaşık köşelerini tutar.
# 4 köşe olması (len(approx) == 4) durumunda, bu şekil dikdörtgen olarak kabul edilir. Bu durumda, plakanın bulunduğu bölgeyi işaret edebileceğiz.