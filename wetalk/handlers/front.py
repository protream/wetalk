"""
    wetalk.front
    ~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import Blueprint
from flask import render_template

bp = Blueprint('front', __name__)


@bp.route('/')
def home():
    return render_template('index.html', msg='Hello, world!')
