import cv2
from cv2 import imread
import numpy as np

resim= cv2.imread("resim.jpg")
cv2.imshow("title", resim)

cv2.imwrite("yenisim.jpg",resim)

cv2.waitKey(0)
cv2.destroyAllWindows
