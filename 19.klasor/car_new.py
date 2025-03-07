
import cv2


path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\car.mp4"

capture = cv2.VideoCapture(path1)


car_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\car_cascade.zip\\car_cascade\\car_trained_cascade.xml")

while 1:
    ret,frame = capture.read()
    #frame = cv2.resize(frame,(640,480))
    
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray_frame,1.1,3)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows() 
    
