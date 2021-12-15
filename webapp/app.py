'''
Title: Ace Animal Detector
Course: CST 205
Date: Dec. 15, 2021
Authors: Jason Casareno, Chris Johnson, & Monica Aguilar
Abstract: This program will take photographs of animals in a non-envasive way via Raspberry Pi,
            Flask, and OPenCV. In addition, the project will display images taken via user's local website.
            Displays an interactive search bar that allows user's of this project to search for specific
            animals that the Raspberry Pi has taken or other existing images.

GitHub Link: https://github.com/MasonJason23/CST-205-Final-Project

Contributions:
> Jason Casareno
    - app.py and routes, GitHub & Trello setup, search bar in nav bar
> Chris Johnson
    - hardware/Raspberry Pi setup, use of OpenCV for animal identification
> Monica Aguilar
    - design elements, including the CSS file, HTML file layouts and partials, and elements (buttons and carousel)
'''

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import requests, json
from pprint import pprint
# from gpiozero import MotionSensor
# from picamera import PiCamera
# import datetime
# from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

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

class List(FlaskForm):
    search = StringField(
        'Search an animal', 
        validators=[DataRequired()]
    )

'''
HOME page; selects 3 random images and displays them in the carousel
'''
@app.route('/', methods=['GET', 'POST'])
def home():
    form = List()
    if form.validate_on_submit():
        return results(form.search.data)
    
    images = data['hits']
    random.shuffle(images)
    im_info1 = images[0]
    im_info2 = images[1]
    im_info3 = images[2]
    return render_template('index.html', form=form, imInfo1 = im_info1, imInfo2 = im_info2, imInfo3 = im_info3)

'''
ABOUT page; displays some README.md information, and provides a link to our GitHub
'''
@app.route('/about')
def about():
    return render_template('about.html')

'''
RESULTS page; displays results of search
'''
@app.route('/results')
def results(search):
    img_list = []
    images = data['hits']
    image_limit = 10

    for image in images:
        if (image_limit == 0):
            break
        tags = image['tags'].split(",")
        for tag in tags:
            if (tag == search):
                img_list.append(image)
                image_limit -= 1

    return render_template('results.html', animal=search, list=img_list)