import cv2
import numpy as np
from test.test_itertools import minsize

img = cv2.imread("face.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
path = ".//face_recognition//haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)
#print(face_cascade.detectMultiScale.__doc__)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.55, minNeighbors=5, minSize=(40,40))
print(len(faces))

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()