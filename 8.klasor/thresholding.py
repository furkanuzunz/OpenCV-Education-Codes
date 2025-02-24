#thresholding aslında resimleri segmentlendirmedir.
#resimleri öbeklendirmedir yani
#thresh hold yöntemi ile resimleir gruplandırarabiliriz.
#thresh hold ile resmi binaryye ceviririz. 1 ler ve 0 lar işte

#resmin siyah beyaz olalı.

# Thresholding, bir görüntüyü siyah-beyaz veya belirli bir eşik değerine göre gruplandırmak için kullanılan bir görüntü işleme tekniğidir. 
# Bu işlem, özellikle nesne tespiti,
# metin çıkarma veya arka plan ön plan ayrımı gibi görevlerde kullanılır.

import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"

img = cv2.imread(path,0)

#simdi thresh hol ile resmi ölçeklendiricez ve bazı özelliklerini ortaya cikaricaz.







# ret degisken ismi aslinda returndan gelen birşey
# # threshold yapma yöntemi 1
ret, threshold1 = cv2.threshold(img,127,200,cv2. THRESH_BINARY)
cv2.imshow("img with thresh1",threshold1)

#baska bir yontem

threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("img with thres2",threshold2)


#bir diğer yöntem

threshold3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("img with thresh 3",threshold3)



# cv2.imshow("img",mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()
