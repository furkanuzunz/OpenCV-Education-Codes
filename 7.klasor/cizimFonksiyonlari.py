import cv2
import numpy as np

canvas = np.zeros((512,512,3),np.uint8) + 255 # + 255 ile beyaz yaptık canvasi(tuvali)
#tüm değerlere 255 eklendi. ve [255,255,255] in BGR karsiliği beyazidr.
# np.zeros((512, 512, 3), np.uint8)
# Bu kısım, siyah bir tuval oluşturur.
# (512, 512, 3) boyutunda bir NumPy dizisi oluşturulur:
# 512: Görüntünün yüksekliği (satır sayısı)
# 512: Görüntünün genişliği (sütun sayısı)
# 3: Renk kanalları (Blue, Green, Red)
# np.uint8: Veri tipi olarak 8-bit işaretsiz tam sayı kullanılır. 
# # Piksel değerleri 0 ile 255 arasında olabilir.
# + 255 ifadesi, tüm piksellerin değerlerine 255 ekler.
# NumPy dizilerinde matematiksel işlemler element-wise (eleman bazlı) yapılır. Yani, dizideki her bir elemana 255 eklenir.
# Sonuç olarak, tüm piksellerin değerleri [255, 255, 255] olur.
# [255, 255, 255], BGR formatında beyaz rengi temsil eder.

cv2.line(canvas, (50,50), (512,512), (255,0,0), 5) #basit bir cizgi cizme fonksiyonu
#paramterleri anlamak icin , geometrik sekillerin paramterlerin anlamak lazim aslinda.
#bir cizginin başlangic noktasi,bitiş noktasi ve de bir kalinliği vardir mesela.
#sirasi ile paramterler, 
#-(cizim yapilacak tuval,baslangic koordinati,bitis koordinati,bgr olarak hangi renkte olmasini istedigimz,kalinlik)
#255,0,0 BGR yani bu blue = 255 dir. diğerleri ise yok.
# sadece mavi kanal aktif olduğu için çizgi saf mavi renkte olur.

cv2.line(canvas,(100,50),(200,250),(0,0,255),8)


#---dikdörtgen cizicez-----

cv2.rectangle(canvas,(20,20),(60,60),(0,255,0),2) 
#dikdörtgende bizim için önemli köşeler sol üst köşe ve sağ üst köşelerin koordinatari olur
#cunku oralar baslangic noktasi ve bitis noktasi diyebiliriz.o noktalari girdigimde aslinda enine ve boyuna uzunlugnu bildirmis oluyorum.

#dikdörtgenin icini dolu yapmak istersem kalınlık parametresine -1 degerini gireriz.
cv2.rectangle(canvas,(70,70),(100,100),(0,255,0),-1)



#----cember cizme---
cv2.circle(canvas,(250,250),100,(0,0,255),5)
#bir merkezi vardir ve de yaricap degeri vardir.parametre olarak onlari gircez.
# canvas,merkez noktası koordinati,yaricap,renk,kalinlik
#ayni sekilde daire olsuturmak istersek ici dolu yani, -1 koyariz
cv2.circle(canvas,(400,400),50,(255,200,145),-1)



#-----ucgen------
#bunun icin bir fonkisonumuz yok ama biz kendimiz cizebilirz farklı yöntemlerle.

#uc tane ayrı ayrı cizgi cekerek ucgen olusturmak.
# 3 noktanin kooridnati ile biz ucgen czebiliriz.


point1 = (100,200)
point2 = (50,50)
point3= (300,100)

cv2.line(canvas,point1,point2,(0,0,0),10) #ilk cizgimizi p1 den p2ye cektik
cv2.line(canvas,point2,point3,(0,100,200),10) #ikinci cizgimizi 2 den 3 e cektik
cv2.line(canvas,point3,point1,(0,255,0),10) #ucuncu cizgimizi de 3 ten bire cekerek ucgenimizi olusturduk.

#--- herhangi bir dikdörtgen----   yani aslidna bir besgen,bir yamuk vs. bunu nasil yapariz

#polyLines fonksiyonunun calisma ilkesi gereği,bir numpy arrayi olusturmma gerekiyo.
points = np.array([[ 110 , 175 ] , [ 330 , 200 ] , [ 290 , 220 ] , [ 100 , 100 ] ],np.int32)
# numpy da olusturdugmuz her sayi dizisinin veri tipini girmem gerekir.

cv2.polylines(canvas,[points],True,(0,0,100),5)#buradaki true kapali olmasini istiyorsak seklin diye
#bunun ile rastgele çizgiler olusturuluyor ve sonra birlesitirior ve kapalı bir sekil elde ediliyor.
#cizimlerde veri tipine dikkat ederiz,uint8 kullanilir mesela.


# elips icin cv2.elips fonksiyonunu kullaniriz.
#aslinda işin özü şui, geometrik şekillerin özelliklerini bilmek gerekir.
#bir elips icin
# img:
# Elipsin çizileceği görüntü (tuval). Bu, daha önce oluşturulan bir NumPy dizisidir.
# center:
# Elipsin merkez noktasının koordinatları. (x, y) şeklinde bir tuple olarak verilir.
# Örnek: (256, 256) → Elipsin merkezi, görüntünün tam ortasında olur.
# axes:
# Elipsin yarı eksen uzunlukları. (major_axis_length, minor_axis_length) şeklinde bir tuple olarak verilir.
# major_axis_length: Elipsin ana ekseninin uzunluğu (genişlik).
# minor_axis_length: Elipsin küçük ekseninin uzunluğu (yükseklik).
# Bu değerler, piksel cinsinden verilir ve her iki değerin yarısı alınır (çünkü OpenCV yarı eksen uzunluklarını bekler).
# angle:
# Elipsin döndürme açısı (derece cinsinden). Elipsin ana ekseni, yatay eksene göre saat yönünde döndürülür.
# Örnek: 45 → Elips 45 derece döndürülür.
# startAngle:
# Elipsin çizimine başlanacak açı (derece cinsinden). Genellikle 0 ile başlar.
# endAngle:
# Elipsin çiziminin biteceği açı (derece cinsinden). Tam bir elips çizmek için 360 kullanılır.
# Eğer sadece bir parça çizmek isterseniz, farklı bir değer verebilirsiniz (örneğin, 0 ile 180 arasında bir değer).
# color:
# Elipsin rengi. (B, G, R) formatında bir tuple olarak verilir.
# Örnek: (255, 0, 0) → Mavi renk.
# thickness (opsiyonel):
# Elipsin çizgi kalınlığı (piksel cinsinden).
# Eğer -1 verilirse, elips içi dolu olarak çizilir.
# lineType (opsiyonel):
# Çizginin türü. Örneğin:
# cv2.LINE_8 (varsayılan): 8-connected çizgi.
# cv2.LINE_AA: Anti-aliased (daha yumuşak kenarlar).
# shift (opsiyonel):
# Koordinatların ve eksen uzunluklarının hassasiyeti. Genellikle 0 kullanılır.

#kisacasi merkezi,merkezden yataya olan uzaklık ve dikeye olan uzaklıgı bilsek yeterli.
 #canvas,merkez,genislik,yükseklik,yatay eksenle yapilan aci,kac dereceden kac dereceye cizmi yapacagini gireriz,
cv2.ellipse(canvas,(400,400),(80,20),20,0,360,(255,255,0),-1)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
