import cv2

capture = cv2.VideoCapture(2)

while 1:
    ret,frame = capture.read()
    cv2.imshow("frame",frame)
    
    