import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

ikikat = cv2.pyrUp(resim)
kucuk = cv2.pyrDown(resim)

cv2.imshow("title",resim)
cv2.imshow("boyk",ikikat)
cv2.imshow("kck",kucuk)

print("orj",resim.shape)
print("kck", kucuk.shape)


cv2.waitKey(0)
cv2.destroyAllWindows
