# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:35:34 2021

@author: fatih cihan
"""

import cv2
import matplotlib.pyplot as plt

#karistirma

img1 = cv2.imread("img1.jpg")# image default olarak bi renk skalasiyla tanimlaniyor
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # bu durumu degistirip image orijinal rengiyle olusturduk

img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)
print(img1.shape, img2.shape)# boyutlar farkli cikti birlestirmek icin ayni boyutta olmalilar

img1 = cv2.resize(img1, (600,600))
img2 = cv2.resize(img2, (600,600))

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karistirma denklemi = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)
# resim oranlari alpha beta katsayilariyla belirlenir

plt.figure()
plt.imshow(blended)

























