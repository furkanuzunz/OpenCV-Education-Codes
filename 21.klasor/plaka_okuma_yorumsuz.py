from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import imutils
import cv2
import numpy as np


image = cv2.imread("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\21.klasor\\licence_plate.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray,6,250,250)
edges = cv2.Canny(filtered,30,200)



contours = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(contours)



cnts = sorted(cnts,key = cv2.contourArea,reverse = True)[:10] 

screen = None 
for c in cnts:
    
    epsilon = 0.018* cv2.arcLength(c,True)

    approx = cv2.approxPolyDP(c,epsilon,True) 
    if len(approx)==4:
        screen = approx
        break

mask = np.zeros(gray.shape,np.uint8) 

new_image = cv2.drawContours(mask,[screen],0,(255,255,255),-1)


new_image2 = cv2.bitwise_and(image,image,mask = mask) 

(x,y) = np.where(mask ==255)
(topx,topy) = (np.min(x),np.min(y)) #
(bottomx,bottomy) = (np.max(x),np.max(y))



kirpilmis = gray[topx:bottomx + 1, topy:bottomy+1]

#simdi bunu okicaz
text = pytesseract.image_to_string(kirpilmis,lang="eng")
print("detected text",text)

# cv2.imshow("yazılı hal",new_image2)
# cv2.imshow("maskeye cizildi",mask)

# cv2.imshow("1.image",image)
# cv2.imshow("2.gray",gray)
# cv2.imshow("3.filtered",filtered)
# cv2.imshow("4.edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


