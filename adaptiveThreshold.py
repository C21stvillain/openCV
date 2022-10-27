import cv2
import numpy as np

resim = cv2.imread("parmak.jpg",0)
#simple
ret,thres = cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
#adaptive
thres2 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY,11,2)

thres3 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    cv2.THRESH_BINARY,11,2)

cv2.imshow("orj",resim)
cv2.imshow("simp",thres)
cv2.imshow("adap",thres2)
cv2.imshow("adap2",thres3)
cv2.waitKey(0)
cv2.destroyAllWindows()