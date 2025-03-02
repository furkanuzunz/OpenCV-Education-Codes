import cv2

path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\eye.mp4"

capture = cv2.VideoCapture(path1)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\eye.xml")

while 1:
    ret,frame = capture.read()
    frame = cv2.resize(frame,(640,480))
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
    
    #Eğer webcam ile canlı görüntü alıyorsak, her yeni karede yüzün yeri değişebilir.
    #eğer webcamle kullanıcaksak, roilerimizi üstteki for içinde tanımlamamız lazım.
    roi_grayFr = gray_frame[y:y+h,x:x+w]
    roi_imgFr = frame[y:y+h,x:x+w]
    
    #sira eye cascade işleminde
    
    eyes = eye_cascade.detectMultiScale(roi_grayFr,1.3,5)
    
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_imgFr,(ex,ey),(ex + ew,ey + eh),(0,0,255),2)
    
    cv2.imshow("video",frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

