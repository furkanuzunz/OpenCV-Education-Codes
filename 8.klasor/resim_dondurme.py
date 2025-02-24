import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"

img = cv2.imread(path,0)

row,col = img.shape

#2 boyutta rotassyon degisme
Matris = cv2.getRotationMatrix2D((col / 2,row / 2),90,1)
# #argümanlar:  sütun,satir,hangi yonde dondurmek,olcek(gosterim sekli aslinda)
# Bir resmi döndürmek için, önce dönüşümün etrafında döneceği bir merkez noktası belirlemek gerekir.
# Bu merkez noktası genellikle resmin merkezi olarak seçilir.
# # Resmin merkezini bulmak için, resmin genişliğini (col) ve yüksekliğini (row) 2'ye böleriz.
# col: Resmin genişliği (sütun sayısı).
# row: Resmin yüksekliği (satır sayısı).
# Resmin merkezi, genişliğin ve yüksekliğin yarısıdır. Bu nedenle her ikisini de 2'ye böleriz.


dst = cv2.warpAffine(img,Matris,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


