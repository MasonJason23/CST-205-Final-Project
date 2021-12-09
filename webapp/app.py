from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint
import random
# from gpiozero import MotionSensor
# from picamera import PiCamera
# import datetime
# from time import sleep

my_key = '24730070-074e9d5f350c21a172695576f'

payload = {
    'key': my_key,
    'category': 'animals'
}
endpoint = 'https://pixabay.com/api/'
try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    # pprint(data['hits'])
except:
    print('please try again')

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    images = data['hits']
    random.shuffle(images)
    im_info1 = images[0]
    im_info2 = images[1]
    im_info3 = images[2]
    return render_template('index.html', imInfo1 = im_info1, imInfo2 = im_info2, imInfo3 = im_info3)

