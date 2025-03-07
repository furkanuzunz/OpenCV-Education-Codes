import cv2
import numpy as np

# Siyah bir görüntü oluştur
image = np.zeros((400, 400), dtype=np.uint8)

# Beyaz dikdörtgenler çiz (farklı iç içe geçmiş şekiller oluşturacağız)
cv2.rectangle(image, (50, 50), (350, 350), 255, -1)  # Büyük dikdörtgen
cv2.rectangle(image, (100, 100), (300, 300), 0, -1)  # İçerideki küçük siyah dikdörtgen

# Konturları bul
contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Hierarchy’yi yazdır
print("Hierarchy:\n", hierarchy)

# Konturları çiz ve göster
image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image_bgr, contours, -1, (0, 255, 0), 2)

cv2.imshow("Konturlar", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
