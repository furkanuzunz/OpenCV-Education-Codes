import cv2
import numpy as np

image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\odev3\\para2.jpg")
image = cv2.resize(image,(640,480))
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray_image = cv2.GaussianBlur(gray_image,(5,5),0)

_,binary_image = cv2.threshold(gray_image,50,255,cv2.THRESH_BINARY)



#WATERSHEDDE MORFOLOJİK İŞLEMLERİ UYGULAMAK FAYDALI
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(binary_image,cv2.MORPH_OPEN,kernel,iterations=5)

# contours,hierarchy = cv2.findContours(opening,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# for cnt in contours:
#     if cv2.contourArea(cnt)>300:
#         (x,y),r = cv2.minEnclosingCircle(cnt)
#         center = (int(x),int(y)) 
#         r =  int(r)
#         cv2.drawContours(image,[cnt],-1,(0,255,0),2)


sure_bg = cv2.dilate(opening,kernel,iterations=2)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg = cv2.threshold(dist_transform,0.4*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

ret,markers = cv2.connectedComponents(sure_fg)

markers = markers + 1

markers[unknown == 255] = 0

markers = cv2.watershed(image,markers)
#image[markers == -1] = [255,0,0]

num_objects = len(np.unique(markers)) - 2  # Arka plan hariç tutulur
cv2.putText(image, f"Para Sayisi: {num_objects}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


circles = cv2.HoughCircles(gray_image,cv2.HOUGH_GRADIENT,1,image.shape[0]/4,param1 = 145,param2 = 38,minRadius=10,maxRadius=120)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Dış daire




cv2.imshow("image",image)
cv2.waitKey()