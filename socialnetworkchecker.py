#import os
from flask import Flask
from flask import render_template
from flask import jsonify
from twitter import *
import ConfigParser


app = Flask(__name__)


config = ConfigParser.RawConfigParser()
config.read('config.ini')


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/<handle>')
def check_handle(handle):
    # show the user profile for that user
    return render_template('handle.html', handle=handle)


@app.route('/twitter/<handle>')
def check_handle_twitter(handle):
    t = Twitter(auth=OAuth(
        '12113422-S0iECIb7BayxpIt8u4ss1nzXjcvdW1b3E3eI8ISEs',
        'VuLql7ImZgppO44dzBIltuPYfcPhBd3KPZxnvLY8J4Q',
        '8hHKUUzTaIVfZNQAFzkw',
        'XxxYJCwgwWbvgEN7jCWdOuQdMBhtkgWW91uSXPWFU'
    ))
    try:
        lookup = t.users.lookup(screen_name=handle)
        found = True
    except TwitterHTTPError:
        lookup = None
        found = False
    return jsonify(found=found, user=lookup)
    # statuses = []
