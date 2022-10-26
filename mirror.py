import cv2
import numpy as np

resim = cv2.imread("moon.jpg")

mirrorimage = cv2.copyMakeBorder(resim, 100,100,100,100,cv2.BORDER_REFLECT)
uzatilanresim = cv2.copyMakeBorder(resim, 120,120,120,120, cv2.BORDER_REPLICATE)
tekrar = cv2.copyMakeBorder(resim,150,150,150,150,cv2.BORDER_WRAP)
sarilan= cv2.copyMakeBorder(resim, 75,75,50,50,cv2.BORDER_CONSTANT,
    value=(0,0,255))

cv2.imshow("çerçeve",sarilan)
cv2.imshow("loop",tekrar)
cv2.imshow("mirror", mirrorimage)
cv2.imshow("expand", uzatilanresim)


cv2.waitKey(0)
cv2.destroyAllWindows