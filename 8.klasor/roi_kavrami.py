import cv2
import numpy as np
#roi --> region of interest --> ilgi alani(resim üzerinde ilgilendiğimiz alan gibi)
#mesela resimde yüz ile ilgileniyoruz.bunun koordinatlarini buluruz daha sonra bu koordinatlar ile
# yüzü ayiririz ve roimizi elde ederiz.
#mesela bir goruntudeki kişinin gözlerinin acik olup olmadigini tespit etmeye  calisiyo olalim
#bunun iicn koskoca resmi islemeye gerek yok.
#önce bu kisinin gozlerini ayirirz resimden ve o kismi islemeye aliriz.iste roinin önemi budur.



img = cv2.imread("c:/Users/Furkan/Desktop/OpenCVegitim/8.klasor/klon1.jpg")
#burada roimiz askerin kafasi olsun ve bunu ayırmaya calisalim.
dimension = img.shape[:2] # suan kanal degeri ile ilgilenmiyorum.normalde bize [piksel1,piksel2,kanalsayisi] seklinde ver,r. [:2] ile sadece ,lk iki yani piksel degerlerini aliriz.
#print(dimension)

#roi mizi yazicaz
roi = img[30:200,200:400] #dikey(y_ekseni),yatay(x_ekseni)
#dikeyde 30 pikselinden 200 pikseline kadar aldik gibisinden.
cv2.imshow("ROI",roi)


















cv2.imshow("Klon1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()