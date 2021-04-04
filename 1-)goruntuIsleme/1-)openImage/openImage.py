# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:13:55 2021

@author: fatih cihan
"""

import cv2

# içe aktarma
img = cv2.imread("messi5.jpg", 0) # 0 resmi gri yapar

# görselleştir
cv2.imshow("ilk Resim", img)

k = cv2.waitKey(0) & 0xFF # goruntuledikten sonra yapilacak islemi tanimlama

if (k ==27): # esc tuşunu alinca her seyi kapat
    cv2.destroyAllWindows()

elif(k == ord("s")): # s tusuna basilinca img kaydet
    cv2.imwrite("mess_gray.png", img)
    cv2.destroyAllWindows()










