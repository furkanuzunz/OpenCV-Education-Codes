import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev3\\para2.jpg")
image = cv2.resize(image, (640, 480))
cv2.imshow("Orijinal grountu", image)

# Gri Tonlama
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Tonlama", gray_image)

# Gürültü azaltma
gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Eşikleme (Binary Threshold)
_, binary_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold (ikili esikleme)", binary_image)

# Morfolojik Açma İşlemi
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=5)
cv2.imshow("Morfolojik Acma", opening)

# Arka Plan (Dilatasyon)
sure_bg = cv2.dilate(opening, kernel, iterations=2)
cv2.imshow("Dilatasyon (Arka Plan)", sure_bg)

# Mesafe Dönüşümü
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
cv2.imshow("Mesafe donusumu", dist_transform / dist_transform.max())  # Normalleştirilmiş

# Ön Plan (Threshold Sonrası)
ret, sure_fg = cv2.threshold(dist_transform, 0.4 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
cv2.imshow("on Plan", sure_fg)

# Bilinmeyen Alan# Bilinmeyen Alan
unknown = cv2.subtract(sure_bg, sure_fg)
cv2.imshow("Bilinmeyen Alan", unknown)

# İşaretleme (Markers)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Watershed Algoritmasını Uygulama
markers = cv2.watershed(image, markers)
image[markers == -1] = [255, 0, 0]  # Kırmızı sınırlar çizilir
cv2.imshow("Watershed Sonucu", image)

# Tespit Edilen Para Sayısını Yazdırma
num_objects = len(np.unique(markers)) - 2  # Arka plan hariç tutulur
cv2.putText(image, f"Para Sayisi: {num_objects}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.waitKey(0)
cv2.destroyAllWindows()
