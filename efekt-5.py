import cv2
import numpy as np

resim= cv2.imread("cat.jpg")

resim[300:500,600:900,0] = 255

cv2.imshow("title",resim)

cv2.waitKey(0)
cv2.destroyAllWindows