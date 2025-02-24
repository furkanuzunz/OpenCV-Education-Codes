import numpy as np
import matplotlib.pyplot as plt 
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\9.klasor\\contour.png"

img = cv2.imread(path)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#UNUTMA RESMİ BİNARİZE ETME ÖNCE GRİYE SONRA TRESHLEME İLE OLUR
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)


contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]
area = cv2.contourArea(contour)
print(area) #bana verdiği değer aslinda momenti yazdirinca "m00" ın karşısındaki ile aynı değer
moment = cv2.moments(contour)#burada buldugumuz alan momentı kullanarak yukarıda ise contorlaı kulllanarak idi.
print(moment["m00"])
print(moment)

#perimeter cevre demek
perimeter = cv2.arcLength(contour,True)
print(perimeter)

#print(contours[0])
# moment = cv2.moments(contour1)
# print(moment)







# cv2.imshow("original",img)
# cv2.imshow("gray",gray)
# cv2.imshow("thresh",thresh)

# cv2.waitKey(0)
# cv2.destroyAllWindows()