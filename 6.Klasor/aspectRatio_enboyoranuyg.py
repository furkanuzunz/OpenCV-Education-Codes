import cv2


path = "C:\\Users\\Furkan\\Desktop\\resim_okuma_gosterme_kaydetme\\klon.jpg"

# inter = cv2.INTER_AREA çakişmalari önlemek icindir.
def resizeWithAspectRatio(img,width = None,height = None,inter = cv2.INTER_AREA):
    yeniBoyut = None
    (boy,en) = img.shape[:2] # iki girmemizin sebebi Bir görüntü OpenCV'de cv2.imread() ile okunduğunda bir NumPy dizisi (numpy.ndarray) olarak saklanır. Eğer görüntü renkli (RGB veya BGR) ise, img.shape üç bileşenden oluşur.(height, width, channels) = img.shape.
    #biz height ve width e ihtiyacımız var.
    #shape fonksiyonu bize boy,en olarak verir. ama resize fonksiyonu en,boy şeklindedir.
    if width is None and height is None:
        return img
    
    if width is None:
        oran = height/float(boy) #orijinal en boy oranını korumak icin, cunku width degeri girilmedi kullanici tarafindan.
#simdi kullanici en girmemişse Width none ise , ama height yani yükseklik girdi ise.biz orijinal en(genislik)degerini girersek orantisiz olcak.
#o yüzden kullanicinin giirdigi yüksekliki orijinal yüksekliğe bölerek oran buluyoruz.sonra orijinal en degerini bu oran ile carparak yeni genislik degerini(en)degerini elde ediyoruz.
        yeniBoyut = (int(en*oran),height)
#resmin orijinal en değeri ile hesapladıgım r degerini carpıyorum ve inte cevirdikten sonra bu yeni en degerimiz(genislik) oluyor.
    
    else:
        oran = width/float(en)
#parametre sirasina dikkat et.ilk width sonra height.
        yeniBoyut = (width,(int(boy*oran)))
        
        
    return cv2.resize(img,yeniBoyut,interpolation=inter)

img = cv2.imread(path)
img1 = resizeWithAspectRatio(img,None,600,cv2.INTER_AREA)

cv2.imshow("original",img)
cv2.imshow("resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()