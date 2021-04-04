# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:59:25 2021

@author: fatih cihan
"""


import cv2

# capture
cap = cv2.VideoCapture(0) # hangi kameranin secilecegini belirtir 0

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # kameranin ozelliklerini cektik

print(width, height)

# video kayit
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),24,(width, height))
# bu nesneyi frameleri kaydetmek icin olustururuz
# 2. parametre windows icin video kodegidir,3. prmt saniyedeki frame sayisi

while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break


cap.release()
writer.release()
cv2.destroyAllWindows()









