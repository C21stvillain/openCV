import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(0,0,255),3)

cv2.circle(resim,(150,150),25,(0,255,0),3)

cv2.putText(resim,"deneme",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(25,64,35),5)

cv2.imshow("d",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()