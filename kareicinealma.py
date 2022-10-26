import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

cv2.rectangle(resim,(680,250),(910,200),[0,0,255],3)
cv2.imshow("title",resim)

cv2.waitKey(0)
cv2.destroyAllWindows
