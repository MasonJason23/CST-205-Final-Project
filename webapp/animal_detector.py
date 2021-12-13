import cv2
import numpy as np
# from pprint import pprint
# from PIL import Image
import glob

casc_class = 'haarcascade_frontalcatface.xml'

face_cascade = cv2.CascadeClassifier(casc_class)

if face_cascade.empty():
    print('WARNING: Cascade did not load')

images = np.array(glob.glob('static/img/*.jpg'))

print(images)

grays = np.array([cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY) for i in images])
faces = np.array([face_cascade.detectMultiScale(i, 1.1, 9) for i in grays])

print(len(faces))

count = 0
for image in faces:
    if len(image) != 0:
        count += 1
print(f'Found {count} cats')
