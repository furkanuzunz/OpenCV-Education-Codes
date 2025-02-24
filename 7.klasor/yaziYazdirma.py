import cv2
import numpy as np

canvas = np.zeros((512,512,3),np.uint8) + 255
# yerleseceği koordinati aslinda hani mesela "canvas" ya "c"nin sol alt köşesini seçeriz.

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX



#ekran,yazacağimiz metin,mtnin yerleseceği koordinat,yazi fontu,fontun buyuklugu,rengi,yazı tipi
cv2.putText(canvas, "OpenCV ",(30,100),font3,4,(0,0,0),lineType=cv2.LINE_AA)








cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
