import cv2
import numpy as np

resim1 = cv2.imread("cat.jpg")
resim2 = cv2.imread("resim.jpg")

print(resim1[100,200])
print(resim2[300,200])

cv2.imshow("tit",resim1)
cv2.imshow("tit2",resim2)

print(resim1[100,200]+resim2[300,200])

cv2.waitKey(0)
cv2.destroyAllWindows()