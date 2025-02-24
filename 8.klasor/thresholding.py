# Thresholding aslında resimleri segmentlendirmedir.
# Resimleri öbeklendirmedir yani.
# Threshold yöntemi ile resimleri gruplandırabiliriz.
# Threshold ile resmi binary (ikili) formata çeviririz: 1'ler ve 0'lar.
# Resmin siyah beyaz olması sağlanır.

# Thresholding, bir görüntüyü siyah-beyaz veya belirli bir eşik değerine göre gruplandırmak için kullanılan bir görüntü işleme tekniğidir. 
# Bu işlem, özellikle nesne tespiti, metin çıkarma veya arka plan-ön plan ayrımı gibi görevlerde kullanılır.

import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\smile.jpg"
img = cv2.imread(path, 0)  # Görüntüyü gri tonlamalı (grayscale) oku

# Şimdi threshold ile resmi ölçeklendireceğiz ve bazı özelliklerini ortaya çıkaracağız.

# Threshold yapma yöntemi 1 (Basit thresholding)
ret, threshold1 = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY)
cv2.imshow("Image with Threshold 1", threshold1)

# Başka bir yöntem (Adaptive Mean Thresholding)
threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Image with Threshold 2", threshold2)

# Bir diğer yöntem (Adaptive Gaussian Thresholding)
threshold3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Image with Threshold 3", threshold3)

cv2.waitKey(0)
cv2.destroyAllWindows()
