import cv2

# 
img = cv2.imread("lenna.png")
print("Resim boyutu: ", img.shape)
cv2.imshow("Orijinal", img)
cv2.waitKey(0) & 0xFF

# resized
imgResized = cv2.resize(img, (800,800)) # yeniden boyutlandirdik
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Img Resized",imgResized)
cv2.waitKey(0) & 0xFF

# kırp
imgCropped = img[:200,:300] # width height -> height width 
cv2.imshow("Kirpik Resim",imgCropped)
cv2.waitKey(0) & 0xFF