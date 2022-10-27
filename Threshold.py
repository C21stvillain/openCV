import cv2
from cv2 import imread
from cv2 import THRESH_BINARY
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import THRESH_BINARY_INV
from cv2 import imshow
from cv2 import THRESH_TRUNC
from cv2 import threshold
from cv2 import THRESH_TOZERO
import numpy as np

resim = imread("resim.jpg")

ret,thresh1=cv2.threshold(resim,127,255,THRESH_BINARY)

ret,thresh2 = cv2.threshold(resim,127,255,THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(resim,127,255,THRESH_TRUNC)

ret,thresh4 = threshold(resim,127,255,THRESH_TOZERO)

cv2.imshow("orj",resim)
cv2.imshow("th",thresh1)
imshow("inv",thresh2)
waitKey(0)
destroyAllWindows()