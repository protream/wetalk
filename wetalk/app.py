"""
    wetalk.app
    ~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from datetime import datetime
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from werkzeug.datastructures import ImmutableDict


class JSONEncoder(_JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        return super(JSONEncoder, self).default(obj)


class Flask(_Flask):
    json_encoder = JSONEncoder
    jinja_options = ImmutableDict(
        # 渲染模版时去除空行
        trim_blocks=True,
        lstrip_blocks=True,
        # Flask 的默认配置
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_']
    )
