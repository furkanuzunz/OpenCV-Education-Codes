import cv2
import numpy as np
import math

vid = cv2.VideoCapture(0)

while 1:
    try:
        ret,frame = vid.read()
        frame = cv2.flip(frame,1)
        
        kernel = np.ones((3,3),np.uint8)
        
        roi = frame[100:300,100:300]
        
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),1) 
        hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV) #mask islemlerinde hsv daha iyi oldugu icin ceviriyoruz.
        
        lower_skin = np.array([0,20,70],dtype=np.uint8)
        upper_skin = np.array([20,255,255],dtype=np.uint8)
        
        mask = cv2.inRange(hsv,lower_skin,upper_skin)
        mask = cv2.dilate(mask,kernel,iterations=4) # beyazlatır aslında
        mask = cv2.GaussianBlur(mask,(5,5),100)
        
        contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        cnt = max(contours,key = lambda x: cv2.contourArea(x))
        
        epsilon_for_approx = 0.0005 * cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon_for_approx,True)
        
        hull = cv2.convexHull(cnt) #elimizin dışınd adış bükey bi örtü oluşturuyoruz.
        
        area_hull = cv2.contourArea(hull) #dış örtünün alani
        area_cnt = cv2.contourArea(cnt) #elimizin alani
        
        area_ratio = ((area_hull- area_cnt)/area_cnt)*100 #elimizin olmadıgı alan.
        
        hull = cv2.convexHull(approx,returnPoints=False)  #indeksleri dönderir.
        #guncel https://chatgpt.com/share/67cde47e-f910-800b-bfd2-1dc41349a7df
        #indeks mevzulari
        defects = cv2.convexityDefects(approx,hull)
        #defects dediğimiz aslinda girintiler
        l = 0 #girinti sayisi aslinda parmak sayiisi icin
        
        for i in range(defects.shape[0]):   #bu dongu , iç bükey sayilari sayisi kadar döner.
            s,e,f,d = defects[i][0] #gereksiz boyuttan kurtulduk gibi düşünebiliriz.chatgt sohbetinde anlattirdim.
            
            #sohbette ilk sonucb yazan yere kadar kısımda aşağıdaki tupleli kısmı analrsın onun da altında defectsi anlarsin.
            start = tuple(approx[s][0]) #cv2.line gibi fonksiyonlar [] şeklinde değill () şeklinde alır ondan tuplye cevirdik
            end = tuple(approx[e][0])
            farth = tuple(approx[f][0]) #en derin nokta gibi düşün.
            
            ##https://chatgpt.com/share/67cde8cc-a4c4-800b-b446-cb9083fcf12e
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((farth[0] - start[0])**2 + (farth[1] - start[1])**2)
            c = math.sqrt((end[0] - farth[0])**2 + (end[1] - farth[1])**2)
            
            yari_cevre = (a + b + c)/2
            alan = math.sqrt(yari_cevre*(yari_cevre - a)*(yari_cevre - b)*(yari_cevre - c))
            
            derinlik = (2 * alan )/ a
            
            angle = math.acos((b**2 + c**2 - a**2) /  ( 2 * b * c )) * (180/math.pi)
            #cosinüs teoremi
            if angle <= 90 and derinlik > 30:
                l+=1
                cv2.circle(roi,farth,3,[255,0,0],-1) #girintinin orayı circle aldık.
            
            cv2.line(roi,start,end,[0,255,0],2) #parmak uclarini birlestirdik.
            
        #https://chatgpt.com/share/67cde8cc-a4c4-800b-b446-cb9083fcf12e
        l += 1 #şöyle yani aslinda ifin icine iki kez girince iki girinti vardrı ama 3 parmak vardır o yüzden fiten sonra arttirriz.
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==1:
            if alan<2000:
                cv2.putText(frame,'Put your hand in the box',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            else:
                if area_ratio<12:
                    cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                elif area_ratio<17.5:
                    cv2.putText(frame,'Best luck',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                   
                else:
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
        elif l==2: #girinti 1 di l sonra 2 oldu hani artttırdık ya dışında o yüzden 2 parmak olur
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==3:
         
              if area_ratio<27:
                    cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
              else:
                    cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==4:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==6:
            cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        else :
            cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)            
        
        
        
        
    except:
        pass
    
    
    if cv2.waitKey(40) & 0xFF==ord('q'):
            break

cv2.destroyAllWindows()
vid.release()
        




# Burada ne oluyor?

# l → bulunan parmak sayısıdır.
# Parmak sayısına göre farklı metinler ekrana yazılır:
# Örneğin:
# Eğer hiç parmak yoksa (l=1 ve areaRatio < 12) → ekrana "0" yazılır.
# 1 parmak işareti varsa "1",
# 2 parmak işareti varsa "2", vb.
# Bazı özel durumlar var:
# Alan (areaCnt) çok küçükse → "Elini kutunun içine koy" mesajı yazılır.
# Parmaklar farklı şekillerde açıldığında (areaRatio) "Best luck" veya "ok" gibi mesajlar yazılır.
# 📌 areaRatio Nedir?
# Önceden şu hesap yapılmıştı:

# python
# Kopyala
# Düzenle
# areaRatio = ((areaHull - areaCnt) / areaCnt) * 100
# Buradaki mantık:

# areaHull: Convex Hull'un alanıdır (parmak aralarını kapatan dış alan).
# areaCnt: Gerçek el kontürünün alanıdır.
# Yani:

# Alan farkı (areaHull - areaCnt), parmakların arasındaki boşlukların büyüklüğünü gösterir.
# Bu oran büyüdükçe, parmaklar daha fazla açılmış veya ayrılmış demektir.
# Bu orana göre bazı özel durumlar ayrılır:

# Parmaklar hiç ayrılmamışsa → küçük oran (areaRatio<12)
# Parmaklar hafif açık → orta değerler (12 ile 17.5 arası gibi)
# Parmaklar oldukça açık → büyük değerler (17.5 üzeri)
