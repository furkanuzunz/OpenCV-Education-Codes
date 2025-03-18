import cv2
import numpy as np
from collections import deque ##bu fonksiyon sayesinde listeleme  işi yapicaz.
#bir çizgi çizerken aslidnda art arda noktalar çiziyoruz bu nktaları işte deque de saklicaz

# capture = cv2.VideoCapture(0)
# if not capture.isOpened():
#     capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#     if not capture.isOpened():
#         capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
#         if not capture.isOpened():
#             print("Error: Could not open video capture.")
#             exit()

capture = None
for i in range(100):
    capture = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if capture.isOpened():
        print(f"Camera opened with index {i}")
        break
    capture.release()

if not capture or not capture.isOpened():
    print("Error: Could not open any video capture.")
    exit()


kernel = ((5,5),np.uint8)

#mavi silgim icin
lower_blue = np.array([100,60,60])
upper_blue = np.array([140,255,255])

#cizdigimiz cizgilerin noktalairni saklamak icin listeleri olusturucaz
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]
#bunlarin indekslerine ihtiyacaimiz var birazdan while dongusu icerisinde indeksleri kullanicaz

blue_indeks = 0
green_indeks = 0
red_indeks = 0
yellow_indeks = 0

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
#colors[0] aslinda mavi ((255,0,0)) yani
color_indeks = 0

#paint windowu ayarlicaz

paintWindow = np.zeros((471,636,3)) + 255 # siyahti ama biz 255 ekledik 0lardan olusan matris 255ten olusmaya basladi ve beyaz oldu
#bunun uzerine ciizmler yapcaz
paintWindow = cv2.rectangle(paintWindow,(40,1),(140,65),(0,0,0),2)
#eğer mavi nesnem paintwindowuma cizdigim beyaz dikdörtgenimin koordinatlari içerisine girerse ekran temizlenecek.

#diğer düğmeleri de oluşturalim
paintWindow = cv2.rectangle(paintWindow,(160,1),(255,65),colors[0],-1)
paintWindow = cv2.rectangle(paintWindow,(275,1),(370,65),colors[1],-1)
paintWindow = cv2.rectangle(paintWindow,(390,1),(485,65),colors[2],-1)
paintWindow = cv2.rectangle(paintWindow,(505,1),(600,65),colors[3],-1)
#-1 olmasi kapali anlamina içi dolu  geliyor aslinda

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintWindow,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow("Paint") #beyaz bir cizim penceremiz olcak bu
#aslinda olustrudgumuz seyi bu pencere işine yerleştiricem


while 1:
    ret,frame = capture.read()
    frame = cv2.flip(frame,1) 
    
    #nesneyi yakalicaz hsv,mask islemleri
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #HEM CİZİM PENCERESİ OLSUTURUCAZ HEM DE FRAMELER ÜZERİNE CİSİM YAPCAZ
    
    frame = cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame = cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame = cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame = cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame = cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)
    
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    
    if ret is False:
        break

    
    mask = cv2.inRange(hsv,lower_blue,upper_blue) #nesnemizi yakalicaz.
    
    mask = cv2.erode(mask,(5,5),iterations=2)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,(5,5))
    mask = cv2.dilate(mask,(5,5),iterations=1)
    
    
    #artık konturlarımızı bulucaz
    
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #diğer renklerden ayırdıgımız o nesneye bir cember cizicez yani o mavi silgimize
    #bu cemberin merkezi ne zaman o renklerin koordinatına girerse o renkle işlem yapcaz
    
    center = None
    
    if len(contours) > 0:
        max_contours = sorted(contours,key = cv2.contourArea,reverse = True)[0]  #büükten kucuge siraladk 0ıncıs en buyuk oldu 
        
        ((x,y),radius) = cv2.minEnclosingCircle(max_contours)
        cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,124),3)
        
        #merkez nktmiza ihtiyacımız var
        M = cv2.moments(max_contours)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        #x ve y değerleri sriasiyla

        #centerin bulundugu renk degerlerine göre renk degerlerimizi değişçez
        #yani silginin centerina göre vs aslinda
        
                
        if center[1] <= 65:#  #yani ekranın 65inden yukarsıı cizgisne#      ##ise düğmelerin hepsinin y degeri 65ten yuksek deemek ki center şuan oralarda ama şimdi x değerine göre hangi renkte ona bakca
            if 40<=center[0]<=140:
                #clear all
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_indeks=0
                green_indeks=0
                red_indeks=0
                yellow_indeks=0

                paintWindow[67:,:,:]=255

            elif 160<=center[0]<=255:
                color_indeks = 0
                #indeksimizi ayarladik blueay 

            elif 275<=center[0]<=370:
                color_indeks = 1
                #green

            elif 390<=center[0]<=485:
                color_indeks = 2
                #red
            elif 505<=center[0]<=600:
                color_indeks = 3
                #yellow
        else: #eğer 65ten buyukse artik cizim yapicamiz kısma gelmis oluyoruz alt kısıma
            #unutma bu silgi oynuyo ya sürekli o yüzden guncelleniyo center surekli
            if color_indeks == 0:
                blue_points[blue_indeks].appendleft(center)
                #centerim silgimin centeri, cizimde onunla beraber butun noktalarimizi eklicezç
                #deque sayesainde bu silgiyi oynattikca o noktalar sakliyoruz centerimiz mesela aşağıda bir yerde cizdi nokta öyle onlari sakliyoruz
                
            elif color_indeks == 1:    
                green_points[green_indeks].appendleft(center)
                
            elif color_indeks == 2:
                red_points[red_indeks].appendleft(center)
                
            elif color_indeks == 3:
                yellow_points[yellow_indeks].appendleft(center)
    else:
        blue_points.append(deque(maxlen=512))
        blue_indeks+=1
        
        green_points.append(deque(maxlen=512))
        green_indesk+=1
        
        red_points.append(deque(maxlen=512))
        red_indeks+=1
        
        yellow_points.append(deque(maxlen=512))
        yellow_indeks+=1
    
    points = [blue_points,green_points,red_points,yellow_points]
    #noktaarimi tutuvcak
    #blue points mesela x,y tutuyo o yüzden bu points dizisinin degerlerini dongu ile aliriz.
    
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range (len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame,points[i][j][k - 1],points[i][j][k],colors[i],2)
                cv2.line(paintWindow,points[i][j][k - 1],points[i][j][k],colors[i],2)
    
    
    cv2.imshow("frame",frame)
    cv2.imshow("Paint",paintWindow)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

