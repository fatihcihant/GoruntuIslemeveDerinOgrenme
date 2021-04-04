# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:37:15 2021

@author: fatih cihan
"""

import cv2
import numpy as np

# resim olsuturma

img = np.zeros((512, 512, 3), np.uint8)# 0'dan olusan piksellerle siyah bir resim olusturcaz
print(img.shape)
cv2.imshow("Siyah", img)
cv2.waitKey(0) & 0xFF

# cizgi

# (resim, baslangic noktasi, bitis noktasi, renk, kalinlik)
cv2.line(img, (00,00), (512,512), (0,255,0), 3) # BGR = (0,255,0) yesil kodlamasi
k = cv2.waitKey(0) & 0xFF
cv2.imshow("cizgi", img)# yukarida cizgi tanimlandi gormek icin gorsellestiririz
cv2.waitKey(0) & 0xFF

# dikdortgen

# (resim, başlangıç, bitiş, renk )
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED) # BGR (255,0,0) mavi, son parametre ici doldurur
cv2.imshow("dikdortgen",img)
cv2.waitKey(0) & 0xFF

# cember

# (resim, merkez, yarı cap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("cember", img)
cv2.waitKey(0) & 0xFF

# metin

# (resim, baslangic noktasi, font, kalinlik, renk)
cv2.putText(img, "hello world", (250,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("metin", img)
cv2.waitKey(0) & 0xFF






