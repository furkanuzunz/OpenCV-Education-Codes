import cv2
import numpy as np

capture = cv2.VideoCapture(0)
windowName = "Live Video"
cv2.namedWindow(windowName)


#cozunurluklere bakalim
print("witdh: "+str(capture.get(3))) #3 yazdgiimzida capteki goruntunun enini verir.
#4 yazdigimzida ise yuksekligini verir.
print("heigh: "+str(capture.get(4)))#str yazmamizin sebebi strye cevirip printte heightin devamina yazdirmakicin

#set ile de aslinda cozunurlukleri degisebilirm.

capture.set(3,1280) #eni düzenliyoruz
capture.set(4,720)

print("width: "+str(capture.get(3)))
print("height: "+str(capture.get(4)))

while True:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    
    cv2.imshow(windowName,frame)
    
    if cv2.waitKey(1) == 27:
        break
capture.release()
cv2.destroyAllWindows()