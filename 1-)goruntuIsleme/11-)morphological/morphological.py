# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:14:12 2021

@author: fatih cihan
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"),plt.axis("off"), plt.title("original")


# Erozyon
"""
Erozyon: on plandaki nesnenin sinirlarini asindirir.
        Bir kutucuk(kernel) image uzerinde dolasip sinirlari asindiracak
"""
kernel = np.ones((5,5), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"),plt.axis("off"), plt.title("erozyon")

# Genisleme
"""
Genisleme: Erozyonun tam tersi
"""
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"),plt.axis("off"), plt.title("genisleme")

# white noise olusturma
whiteNoise = np.random.randint(0, 2, img.shape[:2]) # image icin white noise olusturulcak 
whiteNoise = whiteNoise * 255 # white noise normalize durumda o yuzden istedigimiz skalaya cektik
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"),plt.axis("off"), plt.title("whiteNoise")

noiseImage = whiteNoise + img # white noise image icine eklendi simdi bu sorunu cozucez
plt.figure(), plt.imshow(noiseImage, cmap = "gray"),plt.axis("off"), plt.title("noıseImage")


# Acilma 
"""
Beyaz gurultu azalmada kullanilir
Erozyon + genisleme islemidir.
"""
opening = cv2.morphologyEx(noiseImage.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"),plt.axis("off"), plt.title("fixedImage")

# Black noise olusturma

blackNoise = np.random.randint(0, 2, img.shape[:2]) # image icin white noise olusturulcak 
blackNoise = blackNoise * -255 # white noise normalize durumda o yuzden istedigimiz skalaya cektik
plt.figure(), plt.imshow(blackNoise, cmap = "gray"),plt.axis("off"), plt.title("blackNoise")

blackNoiseImage = blackNoise + img
blackNoiseImage[blackNoiseImage <= -245] = 0 # daaha net gozukebilmesi icin
plt.figure(), plt.imshow(blackNoiseImage, cmap = "gray"),plt.axis("off"), plt.title("blackNoise2")

# kapatma 
"""
Siyah gurultu azalmada kulanilir.
Genisleme + erozyon
"""
closing = cv2.morphologyEx(blackNoiseImage.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"),plt.axis("off"), plt.title("closing")

# gradient
"""
Goruntunun genislemesi ve erozyonu arasindaki farkin alinmasidir
"""
gradient = cv2.morphologyEx( img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"),plt.axis("off"), plt.title("gradient")









 







