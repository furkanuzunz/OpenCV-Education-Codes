import numpy as np
import matplotlib.pyplot as plt 

#nesne tespitinde önemli bir yer tutar kontur kavramı.

#kontur nedir?
#örneğin üçgenin konturlarını buldugumuzda onun çevreleyen sınırlayan çizgilier buluruz
 #şeklin sınırıları boyunca art arda devam eden ve benzer renk özelliğine sahip olan noktalar bütünüdür.
 
 
 #kurmamız gereken temel algoritma
 #1- resimleri binary formatlara cevirmek
 #2-cv2.cvtColor() ile gri formata çeviricez.
 #3-daha sonrada thresh hold ile binary formata cevircez. cv2.threshold()
 #4- daha sonra bu şekli çevreleyen sınır çizgiliernin koordinatlarını yani konturlarının koordinatlarını
 #bulmak icin cv2.findContours() kullanicaz.
 #5-bulunan noktaların cizimi icin de cv2.drawContours() fonksiyonunu kullanicaz.
 
 #bu konturların bazı özellikleri vardır
 # **> bu kontur koordinatları ile üçgenn alanı,çevres,geometri merkezini,çevreleyici geometrilerini bulabiliriz.
 
 #---------------------------------------
 #convex hull nedir = convex = dış bükey demektir., hull ise örtü
 #dış bükey örtü anlamına gelir.
#mesela beşgen dış bükeydir. yıldız ise iç bükeydir.

#convex hullun teriminin temel amacı iç bükey şekiller üzerinde dış bükey konturlar(örtüler) çizmektir.
 
 #--------------------------------
 #convexity defects ise dış bükey kusurlar anlamına gelir.
 #dış bükey kusur dedigimiz sey , nesnenin örtüden saptığı yerlerdir.
 #mesela elimiz iç bükeydir , parmak araralarımızın o içi.dk-8 de resim var
 #dış bükey kusurlarına göre mesela elimizle kaç parmak işareti yaptığımız anlamına gelir.
 #2 kusur varsa mesela 3 parmak yapmısıdır.
 
 
 
 
 