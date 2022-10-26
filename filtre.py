from statistics import median
import cv2

import numpy as np

resim = cv2.imread("kotu.jpg")

meanFilter= cv2.blur(resim,(3,3))
Median = cv2.medianBlur(resim,3)
gauss= cv2.GaussianBlur(resim,(3,3),0)


cv2.imshow("tit",resim)
cv2.imshow("filt",meanFilter)
cv2.imshow("med",Median)
cv2.imshow("gaus",gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()