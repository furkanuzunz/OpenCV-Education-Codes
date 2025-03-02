import cv2


path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\smile.mp4"

capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_smile.xml")


while True:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(640,480))
    
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        roi_smile_gray = gray_frame[x:x+w,y:y+h]
        roi_smile_img = frame[x:x+w,y:y+h]
    
    smiles = smile_cascade.detectMultiScale(roi_smile_gray,1.3,7)
    
    
    for (ex,ey,ew,eh) in smiles:
        cv2.rectangle(roi_smile_img,(ex,ey),(ex + ew, ey + eh),(0,255,0),2)
        
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()