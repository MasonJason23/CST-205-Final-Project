import cv2
import numpy as np

casc_class = 'haarcascade_frontalcatface.xml'
face_cascade = cv2.CascadeClassifier(casc_class)
img = cv2.imread('group.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 9)
for (x,y,w,h) in faces:
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite('newgroup.png', img)
