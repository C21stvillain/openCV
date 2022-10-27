import cv2
import numpy as np

daire = cv2.imread("daire.jpg")
yari = cv2.imread("yari.jpg")

xor1 = cv2.bitwise_xor(daire,yari)

cv2.imshow("ilk",daire)
cv2.imshow("iki",yari)
cv2.imshow("islenmis",xor1)


cv2.waitKey(0)
cv2.destroyAllWindows()