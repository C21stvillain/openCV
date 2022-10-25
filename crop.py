import cv2
import numpy as np

resim= cv2.imread("cat.jpg")

Crop = resim[50:150,300:500]

resim[0:100,0:200] = Crop     

cv2.imshow("kedi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows