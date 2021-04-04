# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:51:19 2021

@author: fatih cihan
"""

import cv2
import matplotlib.pyplot as plt



img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # tum pikseller gri skalaya cekildi 0-255 arasi degerler
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()

# esikleme

_ , thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)
# bu islem 2 sey return eder ilki isimize yaramiyor
# (source, sinir degeri, skala max degeri, islem tipi) 
# sinir deger ustunde degerleri 0 degerini atiyor
plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()


_ , thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY_INV)
# islem tipi THRESH_BINARY_INV secildi
plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()


# adaptif threshhold
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
# (source, skalanin max degeri, adaptif algoritmasi, islem tipi, esik deger hesabi icin blok boyutu,c sabiti ortalamayla alakali)
# yukarida thresh degerimiz sabit olarak biz belirlemistik burada bu deger algoritmalarla adaptif olarak belirlencek
# bu sayede image icinde objelerin kismi goruntu kaybi olmayacak
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis()
plt.show()
























