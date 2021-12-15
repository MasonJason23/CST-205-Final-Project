import cv2
import numpy as np
import glob

casc_class = 'haarcascade_frontalcatface.xml'

face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

images = np.array(glob.glob('static/img/*.jpg'))

grays = np.array([cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY) for i in images])
faces = np.array([face_cascade.detectMultiScale(i, 1.1, 9) for i in grays])

results = []
for i in range(len(faces)):
    if len(faces[i]) != 0:
        results.append(images[i])
print(results)
