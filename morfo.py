from contextlib import closing
import cv2
from cv2 import imshow
from cv2 import MORPH_CLOSE
from cv2 import morphologyEx
from cv2 import MORPH_GRADIENT
from cv2 import MORPH_TOPHAT
from cv2 import MORPH_BLACKHAT
import numpy as np

resim = cv2.imread("yazi.jpg")

kernel=np.ones((5,5),np.uint8)
dilation= cv2.dilate(resim,kernel,iterations=1)
ero= cv2.erode(resim,kernel,iterations=1)
dilation1 = cv2.dilate(resim,kernel,iterations=2)


opening = cv2.morphologyEx(resim,cv2.MORPH_OPEN,kernel)
clos = cv2.morphologyEx(resim,MORPH_CLOSE,kernel)
tophat= morphologyEx(resim,MORPH_TOPHAT,kernel)
blackhat = morphologyEx(resim,MORPH_BLACKHAT,kernel)



cv2.imshow("rir",resim)
cv2.imshow("dil",dilation)
cv2.imshow("ero",ero)
imshow("dil2",dilation1)
imshow("op",opening)
imshow("clo",clos)
imshow("top",tophat)
imshow("blc",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()