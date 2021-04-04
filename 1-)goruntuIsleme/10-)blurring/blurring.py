import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
"""
Ortalama Bulaniklastirma:
    Goruntu normallestirilmis kutu filtresiyle sarmalanir.
    Belirli boyuttaki bu kutu icindeki piksellerin degerlerinin ortalamasini alip merkezdeki piksele onu atar.
    
Gauss Bulaniklastirma:
    Kutu filtresi yerine Gauss cekirdegi kullanilir.
    Cekirdek genisligi ve yuksekligi belirtilir
    Bizim tarafimizdan belirlenen degere gore islem yapar.
    
Medyan Bulaniklastirma:
    Kutucuk icindeki piksel degerlerinin medyanını baz alır.
"""

# blurring

img = cv2.imread("NYC.jpg")
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()


# 1-) Ortalama bulaniklastirma

dst2 = cv2.blur(img, ksize = (3,3)) # "dst" opencv dokumaninda boyle geciyor, ksize kutunun boyutu
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ort bulaniklastirma"),plt.show()

# 2-) Gauss Bulaniklastirma

gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gaussian"),plt.show()

# 3-) Medyan Bulaniklastirma

mb = cv2.medianBlur(img, ksize = 3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Median"),plt.show()


# Gauss noisy olusturma

def gaussianNoise(image):
    row, col, ch = image.shape # chanel resmin hangi renkte okundugu bilgisi
    mean = 0
    var = 0.05 # variance
    sigma = var**(0.5)
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss    
    
    return noisy
    
# ice aktarip normalize etme

img = cv2.imread("NYC.jpg")
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/ 255
# noisy degerlerimiz kucuk oldugu icin image icinde gorunsun diye piksel degerlerini normalize ettik /255 ile
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinalNormalizePixel"),plt.show()

gaussianNoiseImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoiseImage),plt.axis("off"),plt.title("gaussianNoiseImage"),plt.show()



# Gauss Bulaniklastirma ile cozum

gb2 = cv2.GaussianBlur(gaussianNoiseImage, ksize = (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with GaussianBlur"),plt.show()

# Tuz Karabiber Gurultu cozumu

def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5 # salt versus pepper
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt (beyaz noktaciklar eklendi)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape] # rastgele pixel secimi
    noisy[coords] = 1 # pixele beyaz degeri atanir
    
    # pepper (siyah noktaciklar eklendi)
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape] # rastgele pixel secimi
    noisy[coords] = 0 # pixele siyah degeri eklenir
    
    return noisy
       
spImage = saltPepperNoise(img)   
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

# Median Bulaniklastirma ile cozum
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3) # opencv float32 formatinda istiyor
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Median Blur")











