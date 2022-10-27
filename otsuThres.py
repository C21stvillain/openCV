import cv2
import numpy as np

resim = cv2.imread("parmak.jpg",0)

ret,thres1 = cv2.threshold(resim,127,255,cv2.THRESH_BINARY)

ret1,thres2 = cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow("orj",resim)
cv2.imshow("simp",thres1)
cv2.imshow("otsu",thres2)
cv2.waitKey(0)
cv2.destroyAllWindows()