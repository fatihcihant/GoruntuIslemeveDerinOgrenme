# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:02:17 2021

@author: fatih cihan
"""
import cv2
import numpy as np
# resmi ice aktarma
img = cv2.imread("lenna.png")
cv2.imshow("original", img)
cv2.waitKey(0) & 0xFF

# yatay (horizontal) ekleme
hor = np.hstack((img, img))
cv2.imshow("horizontal", hor)
cv2.waitKey(0) & 0xFF

# dikey(vertical) ekleme
ver = np.vstack((img, img))
cv2.imshow("vertical", ver)
cv2.waitKey(0) & 0xFF

   






















