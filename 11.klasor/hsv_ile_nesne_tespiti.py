import numpy as np
import cv2

path = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\11.klasor\\hsv.mp4"
capture = cv2.VideoCapture(path)

def nothing(x):
    pass

cv2.namedWindow("trackbar")
cv2.createTrackbar("LH","trackbar",0,179,nothing)
cv2.createTrackbar("LS","trackbar",0,255,nothing)
cv2.createTrackbar("LV","trackbar",0,255,nothing)
cv2.createTrackbar("UH","trackbar",0,179,nothing)
cv2.createTrackbar("US","trackbar",0,255,nothing)
cv2.createTrackbar("UV","trackbar",0,255,nothing)

while(1):
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(500,350))
    
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("LH","trackbar")
    ls = cv2.getTrackbarPos("LS","trackbar")
    lv = cv2.getTrackbarPos("LV","trackbar")
    uh = cv2.getTrackbarPos("UH","trackbar")
    us = cv2.getTrackbarPos("US","trackbar")
    uv = cv2.getTrackbarPos("UV","trackbar")
    
    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,us,uv])
    
    mask_frame = cv2.inRange(hsv_frame,lower_blue,upper_blue)
    bitwise_frame = cv2.bitwise_and(frame,frame,mask=mask_frame)
    #     bitwise_and ile Renk İzolasyonu
    # bitwise = cv2.bitwise_and(frame, frame, mask=mask)
    # 👉 Burada bitwise_and'in rolü ne?

        # Maske ile orijinal görüntüyü birleştirir.
    # Sadece maskede beyaz (255) olan pikseller, orijinal görüntüde korunur.
    # Maskede siyah (0) olan yerler görüntüde siyah yapılır.
    # 💡 Neden bitwise_and?

    # AND işlemi, sadece hem maske hem de görüntüde uygun piksellerin kalmasını sağlar.
    # Böylece, seçilen renk aralığına sahip nesneler izole edilir ve kolayca analiz edilebilir.
    # 🖼️ Sonuç Görseller:
    # frame: Orijinal video karesi.
    # mask: Seçilen renklerin beyaz olduğu ikili görüntü.
    # bitwise: Sadece seçilen renklerin orijinal görüntüde kaldığı izolasyon sonucu.
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask_frame)
    cv2.imshow("bitwise",bitwise_frame)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()