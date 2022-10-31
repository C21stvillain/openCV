import cv2
import numpy as np
import datetime

kamera = cv2.VideoCapture(0) # burada 0 dersek varsayılan kamera. Eğer 1 dersek usbdeki olabilir. Eğer 2 dersek burada ki bir video olabilir gibi.

while True:
    ret,goruntu= kamera.read()
    datet = str(datetime.datetime.now())
    goruntu = cv2.putText(goruntu,datet,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("title",goruntu)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


kamera.release()

cv2.destroyAllWindows()