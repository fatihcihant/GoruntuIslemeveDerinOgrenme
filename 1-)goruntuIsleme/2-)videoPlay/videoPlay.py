# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:38:39 2021

@author: fatih cihan
"""
import cv2
import time

video_name = "MOT17-04-DPM.mp4"


# video ice aktar
cap = cv2.VideoCapture(video_name)

print("genislik ", cap.get(3)) # 3. indis genislik
print("yükseklik ", cap.get(4)) # 4. indis yukseklik
print(cap)

if (cap.isOpened == False): # videonun yuklenme hatasini cok onceden saptamak icin
    print("hata")



while True: # frameleri belli bir hızda oynatip videoya gorunumune cekeriz
    ret, frame = cap.read() # ilk parametre islemin basarisini dondurur, 2. parametre videodaki resimleri
    if (ret == True):
        time.sleep(0)
        cv2.imshow("Video",frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord ("q"): # video oynatimini q ile kapat
        break

cap.release() # video yakalamayi durdurur
cv2.destroyAllWindows()

















