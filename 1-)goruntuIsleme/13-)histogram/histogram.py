# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:01:37 2021

@author: fatih cihan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.figure(), plt.imshow(img_vis)


print(img.shape)
imgHist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])# channel = [0] kirmizi
print(imgHist.shape)
plt.figure(), plt.plot(imgHist)

color = ("b", "g", "r")
plt.figure()
for i, c, in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)


goldenGate = cv2.imread("goldenGate.jpg")
goldenGateVis = cv2.cvtColor(goldenGate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(goldenGateVis)

print(goldenGate.shape)

mask = np.zeros(goldenGate.shape[:2], np.uint8)# maske olusturuldu
plt.figure(), plt.imshow(mask, cmap = "gray")

mask[1500:2000, 1000:2000] = 255
plt.figure(), plt.imshow(mask, cmap = "gray") # maskedek delik actik gorselin uzerine koydugumuzda bize calisacak alani verecek

maskedİmgVis = cv2.bitwise_and(goldenGateVis, goldenGateVis, mask = mask)
plt.figure(), plt.imshow(maskedİmgVis, cmap = "gray")

maskedİmg = cv2.bitwise_and(goldenGate, goldenGate, mask = mask)# original resim maskelendi
maskedİmgHist = cv2.calcHist([goldenGate], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(maskedİmgHist) # piksellerin kirmizi renklerini gosterir channel = [0]


# histogram esitleme - kontrast artirma

img2 = cv2.imread("hist_equ.jpg", 0)
plt.figure(), plt.imshow(img2, cmap = "gray"), plt.title("normal")

img2Hist = cv2.calcHist([img2], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img2Hist)

eqHist = cv2.equalizeHist(img2)
plt.figure(), plt.imshow(eqHist, cmap = "gray"),plt.title("equalized histogram")

eqImageHist = cv2.calcHist([eqHist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eqImageHist),plt.title("equalized histogram table")













