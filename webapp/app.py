from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint
# from gpiozero import MotionSensor
# from picamera import PiCamera
# import datetime
# from time import sleep

my_key = '24730070-074e9d5f350c21a172695576f'

payload = {
  'key': my_key,
  'category': 'food'
}
endpoint = 'https://pixabay.com/api/'
try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data)
except:
  print('please try again')

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')