"""
    wetalk.app
    ~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import Flask as _Flask
from werkzeug.datastructures import ImmutableDict


class Flask(_Flask):
    jinja_options = ImmutableDict(
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_']
    )
