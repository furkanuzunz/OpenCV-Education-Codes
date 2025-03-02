import cv2


path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\smile.jpg"

image = cv2.imread(path1)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_smile.xml")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,5)

smiles = smile_cascade.detectMultiScale(gray,1.4,7)

for (x,y,w,h) in smiles:
    cv2.rectangle(image,(x,y),(x + w, y + h),(0,255,0),2)
    roi_smile_gray = gray[x:x+w,y:y+h]
    roi_smile_img = image[x:x+w,y:y+h]
    
    
    smiles = smile_cascade.detectMultiScale(roi_smile_gray,1.4,7)

    for (ex,ey,ew,eh) in smiles:
        cv2.rectangle(roi_smile_img,(x,y),(x + w, y + h),(0,255,0),2)
    
    cv2.imshow("image",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
