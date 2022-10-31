import numpy as np
import cv2

img = cv2.imread('2.png')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[80:100,120:140]

img[45:65,70:90] = ball

cv2.imshow("title", img)

cv2.waitKey(0)
cv2.destroyAllWindows()