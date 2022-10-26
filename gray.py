import cv2
from cv2 import imshow
import numpy as np

resim = cv2.imread("resim.jpg")

resimgri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

height,wight,kanalsayisi = resim.shape
height2,wight2 = resimgri.shape

print("orj", height,wight,kanalsayisi)
print("gri", height2,wight2)
imshow("tit",resimgri)

cv2.waitKey(0)
cv2.destroyAllWindows