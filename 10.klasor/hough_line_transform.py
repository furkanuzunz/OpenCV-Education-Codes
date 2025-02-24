import numpy as np
import matplotlib.pyplot as plt
import cv2

#arabalar belli bir şeridi nsıl tutturup gidecek, işte bu yöntemle



path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\10.klasor\\h_line.png"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#canny fonksiyonunun görevi resimlerdeki köşeleri tespit etmk

edges = cv2.Canny(gray,75,150)

#line ları tespit et.ez
#cv2.HoughLines cok fazla cpu kullandıgı icin önrlmez
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200) #maxline gap çizgilerin tamamini doldurmmaıza yarıyo
print(lines) # lines 4 adet deger tutuyor


for line in lines:
    x1,y1,x2,y2 = line[0]
    #bunlar aslinda linelarin baslangic ve bitis noktalari
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) #imgye cizidk

#https://chatgpt.com/share/67b8e4d3-d5d4-800b-aefa-78bed59f1a0b
#mevzuyu anla
    

cv2.imshow("org",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print(lines)dedigimizde cıkan sonuc tan hasediyoruz ve neden lines[0] kullandik
# Bu çıktı aslında `lines` dizisinin tamamını gösteriyor. Her satır bir çizgiyi temsil ediyor. İşte detaylı açıklama:

# - Her satır `[x1, y1, x2, y2]` formatında koordinat çiftlerini içeriyor
# - Örneğin ilk satır: `[[ 46  57 408  57]]`
#   - x1 = 46
#   - y1 = 57
#   - x2 = 408
#   - y2 = 57

# İşte neden `line[0]` kullandığımızı gösteren örnek kod:

# ```python
# # Her bir line'ın yapısını görmek için:
# for i, line in enumerate(lines):
#     print(f"Line {i}:")
#     print(f"Complete line data: {line}")        # [[[x1 y1 x2 y2]]]
#     print(f"Accessing coordinates: {line[0]}")  # [x1 y1 x2 y2]
#     print("---")
# ```

# Çıktı şöyle olacaktır:
# ```
# Line 0:
# Complete line data: [[ 46  57 408  57]]
# Accessing coordinates: [ 46  57 408  57]
# ---
# ```

# Yani:
# - `lines`: Tüm çizgileri içeren ana dizi
# - `line`: Tek bir çizgi verisi (3 boyutlu dizi formatında)
# - `line[0]`: O çizginin koordinat değerleri (x1, y1, x2, y2)

# Bu yapı OpenCV'nin Hough dönüşümü implementasyonundan kaynaklanıyor ve 
# bu yüzden koordinatlara erişmek için `line[0]` kullanmamız gerekiyor.