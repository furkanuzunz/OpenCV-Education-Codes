#bu kisimda resimler üzerindeki gürüültüleri pürüzleri azaltmayi amacliyorız
#yummusatmayi amacliyoruz.

import cv2
import numpy as np

path_filter = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\filter.png"
path_median = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\median.png"
path_bilateral = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\bilateral.png"


img_filter = cv2.imread(path_filter)
img_median = cv2.imread(path_median)#uzerine tuz serpilmis gibi olan.
img_bilateral = cv2.imread(path_bilateral)

img_blur = cv2.blur(img_filter,(5,5))#burda girdigmiz deger ile resmin yumusama degerini attirabiliriz.
img_blurGaus = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow("blur_filter",img_filter)
# cv2.imshow("original_Filter",img_blur)
# cv2.imshow("blur 2",img_blurGaus)

median_blur = cv2.medianBlur(img_median,9)
# cv2.imshow("original median",img_median)
# cv2.imshow("median_blur",median_blur)

bilateral_blur = cv2.bilateralFilter(img_bilateral,9,95,95)
cv2.imshow("bilateral blur",bilateral_blur)
cv2.imshow("original image",img_bilateral) 



# cv2.imshow("Filter",img_filter)
# cv2.imshow("Median",img_median)
# cv2.imshow("Bilateral",img_bilateral)






cv2.waitKey(0)
cv2.destroyAllWindows()