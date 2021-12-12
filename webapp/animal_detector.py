from typing import Any

import cv2
import numpy as np
from pprint import pprint
from PIL import Image
import glob

casc_class = 'haarcascade_frontalcatface.xml'

face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

# images = np.array([cv2.imread(i) for i in glob.glob('static/*.jpeg')])
# img = cv2.imread('fillon.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
images = np.array([cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY) for i in glob.glob('static/*.jpeg')])

faces = np.array([face_cascade.detectMultiScale(i, 1.1, 9) for i in images])

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('newface2.png', img)
