from flask import Flask, render_template, request
from flask.templating import render_template_string
from flask_bootstrap import Bootstrap
# from gpiozero import MotionSensor
# from picamera import PiCamera
# import datetime
# from time import sleep

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('results', methods="GET, POST")
def search():
    # this needs to pass info from search into the html file
    return render_template('displayResults.html')