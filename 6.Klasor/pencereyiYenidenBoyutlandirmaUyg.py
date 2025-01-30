import cv2

cv2.namedWindow("Orijinal resim") 
path = "C:\\Users\\Furkan\\Desktop\\resim_okuma_gosterme_kaydetme\\klon.jpg"
img = cv2.imread(path)

img = cv2.resize(img,(640,480))#kendimiz boyutlandirdik
#bu boyutların original resimle aynı oranlarda olmasına dikkat etmeliyiz.




cv2.imshow("Orijinal resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
