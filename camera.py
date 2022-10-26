import cv2
import numpy as np

kamera = cv2.VideoCapture(0) # burada 0 dersek varsayılan kamera. Eğer 1 dersek usbdeki olabilir. Eğer 2 dersek burada ki bir video olabilir gibi.

while True:
    ret,goruntu= kamera.read()

    cv2.imshow("title",goruntu)
    
    if cv2.waitKey(30) & 0xFF == ('q'):
        break


kamera.release()

cv2.destroyAllWindows()