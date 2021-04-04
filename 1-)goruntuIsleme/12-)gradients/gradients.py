# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:54:03 2021

@author: fatih cihan
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("original")


# X gradyan

sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5)
# (source, output derinligi, x yonunde gradyan, kutucuk boyutu)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("sobelx")

# Y gradyan
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("sobely")

# ikisi bir arada
twoInOne = sobelx + sobely
plt.figure(), plt.imshow(twoInOne, cmap = "gray"), plt.axis("off"), plt.title("twoInOne")

# Laplace gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)# hem x hem y yonunde gradyani alir
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("laplacian")































