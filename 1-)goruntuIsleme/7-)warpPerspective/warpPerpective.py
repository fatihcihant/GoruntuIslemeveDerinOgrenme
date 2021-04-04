# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:09:45 2021

@author: fatih cihan
"""

import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("kart", img)
cv2.waitKey(0) & 0xFF

#image degerleri
width = 400
height = 500

# point1 dondurulmek istenen koselerin o anki indisi sol ust, sag ust ...
# point2 dondurulmek istenen koselerin yeni indisleri
point1 = np.float32([[230,1], [1,472], [540,150], [338,617]])
point2 = np.float32([[0,0], [0, height], [width,0], [width,height]])

# bu indislerle bir dondurme matrixi olsuturuz
matrix = cv2.getPerspectiveTransform(point1, point2)
print(matrix)
# yeni image dondurme matrisi ile dondurulur
imageOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("son hali", imageOutput)
cv2.waitKey(0) & 0xFF






























