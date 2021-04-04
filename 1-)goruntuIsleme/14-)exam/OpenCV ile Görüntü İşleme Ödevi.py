# opencv kütüphanesini içe aktaralım
import cv2

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("odev1.jpg", 0)

# resmi çizdirelim
cv2.imshow("original", img)
cv2.waitKey(0) & 0xFF

# resmin boyutuna bakalım
print(img.shape)
# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
imgResized = cv2.resize(img, (int(img.shape[0] * 4/5), int(img.shape[1] * 4/5)))
cv2.imshow("imgResized", imgResized)
cv2.waitKey(0) & 0xFF

# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv2.putText(img, "kopek", (35,25), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))
cv2.imshow("img with text", img)
cv2.waitKey(0) % 0xFF

# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
x, threshImg = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
cv2.imshow("threshold", threshImg)
cv2.waitKey(0) & 0xFF

# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
cv2.imshow("gaussian", gb)
cv2.waitKey(0) & 0xFF

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0) & 0xFF


# orijinal resmin histogramını çizdirelim
imgHist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(imgHist)

















