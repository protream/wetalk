"""
    wetalk.front
    ~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import Blueprint
from flask import render_template

front = Blueprint('front', __name__)


@front.route('/')
@front.route('/about')
def home():
    return render_template('index.html')


@front.route('/p/<path:name>')
def other(name):
    return render_template('index.html')
