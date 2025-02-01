import cv2

path = "C:\\Users\\Furkan\\Desktop\\Yeniklasör\\calisma.mp4"
#bu videoyu kaydedelim.

capture = cv2.VideoCapture(path)
kaydedilecekYer = "C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\6.Klasor\\istenilenAndakiFrame.jpg"

while True:
    ret,frame = capture.read()
    if(ret == 0):
        print("video bitti")
        break
    cv2.imshow("dersVideosu",frame)
    if (cv2.waitKey(1) & 0xFF == ord("s")):
        cv2.imwrite(kaydedilecekYer,frame)
        print("frame kaydedildi",{kaydedilecekYer}) #s ye basarsam o anki frameyi kaydeder.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
capture.release()
cv2.destroyAllWindows()#tüm pencereleri kapatır.




    