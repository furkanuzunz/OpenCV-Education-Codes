import cv2

path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\body.jpg"

image = cv2.imread(path1)



body_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_fullbody.xml")

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray_image,1.05,3)

for (x,y,w,h) in bodies:
    cv2.rectangle(image,(x,y),(x + w, y + h),(0,255,0),2)
    
cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
