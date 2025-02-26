import cv2
import numpy as np
import math

#simdi aslinda yuz ozellikleirni tanımlama derken aslinda yapacağiğmiz şey,
#önce yüzümüzü belli bir bölgeye getirip o bölgede yüzün bazı özelliklerini aramak olucak.
#o bölgeyi getirmeden önce o bölgeyi bir roi etmem gerekiyor
#roi etmeyi öğrenmiştik

capture = cv2.VideoCapture(0)




def findMaxContour(contours):
    max_i = 0
    max_area = 0
    for i in range(len(contours)):
        contour_area_face = cv2.contourArea(contours[i])
        
        if max_area < contour_area_face:
            max_area = contour_area_face
            max_i = i #indeksini de eşitliyoruz hangi contourda ise
        try:
            c = contours[max_i]
        except:
            contours = [0]
            c = contours[0]
        return c
 
while 1:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250,200:400]#frame[y1:y2,x1:x2]
#     50:250 ifadesi, frame matrisinin satırlarını belirtir. Yani, 50. satırdan 250. satıra kadar olan kısmı seçer.
# 250:450 ifadesi ise, frame matrisinin sütunlarını belirtir. Yani, 250. sütundan 450. sütuna kadar olan kısmı seçer.
    #50.satirdan asagi gittikce işte y degerlerin aliriz ya.öyle düşün
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),0)
    #rectangeli kalınlıgını 0 yapmalıyız ki maskeleme isine dahil olmasın
    
    #yüzümü o bölgelerdeki nesnelerden ayırmak için roi'yi hsvye cevirmem lazim
    hsv_frame = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    #SİMDİ yüz için belirlediğimiz hsv araliğini belirlemeliyz.
    lower_color = np.array([0,45,79],dtype= np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)
    # HSV renk uzayında, renk bilgisi (Hue) ve ışık/parlaklık (Value) birbirinden
    # ayrıldığı için renk tespiti ve nesne takibi daha kararlı olur.
    #bu belirlediğimiz hsv degerleri ile mask uygulicaz.
    mask_frame = cv2.inRange(hsv_frame,lower_color,upper_color)
    # mask üzerinde biraz karıncalanma var.önce dilate edicez.sonra  bi kernel olusturup onu gezdirip blurlicaz frameleri
    kernel = np.ones((3,3),np.uint8) # kernelimiz 1 lerden oluşsun ki ben beyaz noktalardaki siyah noktali karincalanmalari yok etmek istiyorum
    mask_frame = cv2.dilate(mask_frame,kernel,iterations=2)
    
    contours,hierarcy = cv2.findContours(mask_frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
         
             #simdi tmam contourslarda değerler var , ama bu contourlsardaki değerler
             #söyle de olabilir işte yüzünün arkasindaki byeaaz karıncalanmalar olabilir.
             # yüzüm roideki en büyük nesne olucak demi.
             #o zaman ben o bölgedeki maximum kontourları bulsamv ve işlemlerimi de ona göre yapsam
             #maximum contourun tutuldugu deger 'c' olsun
             c = findMaxContour(contours)#böyle bir fpnksiyonumuz olsun.
             #artık görüntüdeki maximum alanlı contorumu bulduguma göre en sağ,en sol,en üst,en alt noktalarını hesaplamaya başlayabiliriz.
             
             #mesela en sol left için x koordinatı en kucuk olan noktayı bulucaz.ama tabi her biri (x,y) li olucak
             extreme_left = tuple(c[c[:,:,0].argmin()][0])
             #bu mevzuyu en sol en alt aciklama txtinde bulursun.
             extreme_right = tuple(c[c[:,:,0].argmax()][0])#o ise aslinda (x,y) den 0 olan x i çektiğini ifade eder
             extreme_top = tuple(c[c[:,:,1].argmin()][0])  # 1 ise y yi .
             extreme_down = tuple(c[c[:,:,1].argmax()][0])
             #bunlarin her birinden (x,y) li koordinatlar doncek
             
             #buldugumuz noktalara çemberler koyalim
             cv2.circle(roi,extreme_left,5,(0,255,0),2)
             cv2.circle(roi,extreme_right,5,(0,255,0),2)
             cv2.circle(roi,extreme_top,5,(0,255,0),2)
             cv2.circle(roi,extreme_down,5,(0,255,0),2)
             
             cv2.line(roi,extreme_left,extreme_top,(255,0,0),2)
             cv2.line(roi,extreme_top,extreme_right,(255,0,0),2)
             cv2.line(roi,extreme_right,extreme_down,(255,0,0),2)
             cv2.line(roi,extreme_down,extreme_left,(255,0,0),2)
             
             a = math.sqrt((extreme_right[0] - extreme_top[0])**2 + (extreme_right[1] - extreme_top[1])**2)
             b = math.sqrt((extreme_down[0] - extreme_right[0])**2 + (extreme_down[1] - extreme_right[1])**2)
             c = math.sqrt((extreme_down[0] - extreme_top[0])**2 + (extreme_down[1] - extreme_top[1])**2)
             
             try:
                 #acilari hesaplicaz.cos teoremi ile
                 angle_ab = int(math.acos((a**2 + b**2 - c**2) / (2*a*b))*57)
                 cv2.putText(roi,str(angle_ab),(extreme_right[0] - 100 + 50,extreme_right[1]),cv2.FONT_HERSHEY_SIMPLEX,1,
                             (0,255,0),2,cv2.LINE_AA)
             except:
                 cv2.putText(roi," ? ",
                (extreme_right[0]-100 + 50,extreme_right[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
                 
                 
             
             
             
        
    else:
        pass
    
    
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask_frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()






#önce döngümüzü olusturduk
#roimizi belirledik ve dikdörtgenimizi çizidirdik
#kullanacagımız roiyi hsv formatına dönderdik
#maskeleme için alt ve üst hsv degerlerini bulduk
#maskeledik
#karıncalanma tespit ettik kernel ile onları temizledik.
#temizleme işlemini dilate ile yaptık.
#dilate beyaz alanları genisletir,gürültü temizler,kenar kalınlatştırır,boşluk kapatır
#------sıra contourlarımızı bulmada---------
#findcontour ile bulucaz.ve yüzümüzün en sağ , en sol ve en üst noktalarını aricaz.
#deger gelmezse eğer contor yoksa hiç yani
