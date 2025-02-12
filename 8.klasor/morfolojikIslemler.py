# #erozyon yontemi resmi erozyona ugratior.
# Erozyon Nedir?
# Erozyon, bir resmin ön planındaki (beyaz pikseller) nesnelerin sınırlarını aşındırır.
# Beyaz piksellerden oluşan nesnelerin boyutu küçülür.
# Özellikle gürültüyü azaltmak veya nesne sınırlarını daraltmak için kullanılır.


import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"

img = cv2.imread(path,0)

# bir fonksiyon ile resmi erozyona ugraticaz. sorna onu bir degiskene aktaricaz.

#belli bir matris kullanarak resmi erozyon ugraticaz. (kernel)

kernel = np.ones((5,5),np.uint16) # 1lerden olusan matriis resim üzerine getirierek resmi bozcaz.
erosion = cv2.erode(img,kernel,iterations = 1) #iterations = 1 demek erozyon iişleminin sadece 1 kez uygulancagını belirtir.
cv2.imshow("erosion",erosion)


# bir diğer yöntem   dilation yöntemi

dilation = cv2.dilate(img,kernel,iterations= 4)
cv2.imshow("dilation yöntemi",dilation)
# 1. Dilatasyon Nedir?
# Dilatasyon, bir resimdeki beyaz piksellerin (ön plan ) sınırlarını genişletir. Bu işlem şu şekilde çalışır:

# Bir kernel , resim üzerinde kaydırılır.
# Kernel'in kapladığı alanda en az bir beyaz piksel (255) varsa, kernel'in merkezindeki piksel beyaz yapılır.
# Bu işlem sonucunda:

# Nesnelerin boyutları büyür.
# Küçük delikler kapanır.
# Beyaz pikseller arasındaki boşluklar dolar.


#bir diger yontem morfoloji ex yöntemi

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("ex yontemi",opening)

#bir diger yontem

closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("exin close yontemi",closing)
# Bu işlem, özellikle nesneler arasındaki boşlukları doldurmak veya küçük delikleri kapamak için kullanılır.
# Kapatma işlemi şu sırayla gerçekleşir:

# Önce dilatasyon uygulanır.
# Ardından erozyon uygulanır.
# Bu işlem, özellikle nesneler arasındaki küçük boşlukları doldurmak
# , delikleri kapamak ve nesne sınırlarını daha düzgün hale getirmek için kullanılır.


#bir diger

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# # Gradient = Dilatasyon - Erozyon
# Resme önce dilatasyon uygulanır.
# Sonra aynı resme erozyon uygulanır.
# İki sonuç arasındaki fark alınarak nesnelerin sınırları elde edilir.
cv2.imshow("gradientli yöntem",gradient)

#bu yöntemleri harfleri segmentelemde,öbeklemede kullanicaz.





#bir diger yöntem 

tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("tophat",tophat)
# # Tophat = Orijinal Resim - Açılma Sonucu
# Yani:

# Öncelikle resme açılma işlemi uygulanır.
# Ardından, orijinal resimden açılım sonucu çıkarılır.
# Bu işlem, özellikle küçük nesneleri , gürültüyü veya detayları ortaya çıkarmak için kullanılır.


#bir diger yontem

blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("blackhat",blackhat)



cv2.imshow("original img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()