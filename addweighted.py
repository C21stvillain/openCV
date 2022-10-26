import cv2
import numpy as np

resim1 = cv2.imread("1.jpg")
resim2 = cv2.imread("2.png")

toplam = cv2.add(resim1,resim2)
toplam2 = cv2.addWeighted(resim1,0.7,resim2,0.3,0)

cv2.imshow("t",toplam)
cv2.imshow("agir",toplam2)

cv2.waitKey(0)
cv2.destroyAllWindows