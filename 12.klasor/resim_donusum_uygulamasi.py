import cv2
import numpy as np

img1_path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\aircraft.jpg"
img2_path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\12.klasor\\balls.jpg"

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

img1 = cv2.resize(img1,(640,480))

img2 = cv2.resize(img2,(640,480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
#her iki resmi eşit oranda birleştirdik ve outputa atadik

windowName = "Transition Program"
cv2.namedWindow(windowName)

def nothing():
    pass

cv2.createTrackbar("Alpha-Beta",windowName,0,1000,nothing)

while True:
    cv2.imshow(windowName,output)
    alpha = cv2.getTrackbarPos("Alpha-Beta",windowName)/1000
    beta = 1- alpha
    #en basta balls cıkıyor cunku alpha 0 dan basliyor.0/1000 sıfırdır.1 - 0 1dir.yani ballsun yogunlugu 1 dir ondan o gorunur.
    output = cv2.addWeighted(img1,alpha,img2,beta,0)
    print(alpha,beta)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()