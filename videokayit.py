import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

width = int(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
Writer = cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height))

while True:
    ret,frame = kamera.read()
    Writer.write(frame)
    cv2.imshow("video",frame)

    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

kamera.realease()
Writer.release()
cv2.destroyAllWindows()