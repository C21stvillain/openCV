import cv2
import numpy as np

ayResmi = cv2.imread("moon.jpg")

cv2.imshow("title", ayResmi)

print(ayResmi[(230,80)])
print("Resmin boyutu: "+str(ayResmi.size))
print("REsmin özellikleri: "+str(ayResmi.shape))
print("Resmin veri tipi: "+str(ayResmi.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()

