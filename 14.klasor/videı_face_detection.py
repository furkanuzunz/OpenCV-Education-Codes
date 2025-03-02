import cv2

path1 = "C:\\Users\\Furkan\\Desktop\\haar_cascade\\test_images\\faces.mp4"

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Furkan\\Desktop\\haar_cascade\\haar_cascades\\haarcascade_frontalface_default.xml")

'''
face_cascade, aslında cv2.CascadeClassifier sınıfından oluşturduğumuz bir örnek (instance). Yani kütüphaneye ait bir sınıfın nesnesi olduğu için nokta (.) ile ilgili metotlarına erişebiliyoruz.
# '''
# # cv2.CascadeClassifier, OpenCV’de tanımlanmış bir sınıftır.
# # face_cascade değişkeni ise bu sınıftan üretilmiş bir nesnedir (instance).
# Bir sınıfın nesnesini oluşturduğumuzda, o sınıfa ait fonksiyon (metot) veya özellik (property) lere nesne_adi.metot_adi() şeklinde erişiriz.


while 1:
    ret,frame = video.read()
    frame = cv2.flip(frame,1)
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 1 olan aslinda iterasyon degeri,suanki son parametre ben belli bi bölgede yüz bulursam orayı çizeyim,emin olayım yuz oldugundan.onu arttırırsak 5 tane yuz arar aslinda ve yuz bulduguna emin olur.yani öyle tişörtümüzün üstünde yüz gördüğünde onu cizmesin bi zahmet.
    faces = face_cascade.detectMultiScale(gray_frame,1.4,1)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        
    cv2.imshow("image",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()