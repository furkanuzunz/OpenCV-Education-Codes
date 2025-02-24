import numpy as np
import cv2

#son 2parametre threshold araligi aslinda
#cv2.Canny(input,minThreshold,maxThreshold)

path2 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\contour.png"
path1 = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\8.klasor\\text.png"
img2 = cv2.imread(path2)
img1 = cv2.imread(path1)

#webcamden aldigimiz goruntuuy islicez.


capture = cv2.VideoCapture(0)

while 1:
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)
    
    edges = cv2.Canny(frame,100,200)
    
    cv2.imshow("org frame",frame)
    cv2.imshow("edges",edges)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows() 
