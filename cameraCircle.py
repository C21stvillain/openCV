import cv2
from cv2 import waitKey
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.rectangle(goruntu,(100,100),(200,200),(0,0,255),3)
    cv2.line(goruntu,(0,0),(100,100),(0,255,0),2)

    cv2.circle(goruntu,(150,150),5,(255,0,0),3)
    cv2.putText(goruntu,"Deniz",(220,220),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)
    cv2.imshow("tit",goruntu)

    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

kamera.release()

cv2.destroyAllWindows()