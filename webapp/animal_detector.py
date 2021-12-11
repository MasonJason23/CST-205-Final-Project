import cv2
import numpy as np
from pprint import pprint

casc_class = 'haarcascade_frontalcatface.xml'

face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

img = cv2.imread('fillon.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 9)

pprint(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('newface2.png', img)
