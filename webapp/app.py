from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint
# from gpiozero import MotionSensor
# from picamera import PiCamera
# import datetime
# from time import sleep

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')