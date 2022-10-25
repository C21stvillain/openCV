import cv2
import numpy as np

resim= cv2.imread("resim2.jpg")
cv2.imshow("title", resim)

print(resim.size)
print(resim.dtype)
print(resim.shape)

cv2.waitKey(0)
cv2.destroyAllWindows
