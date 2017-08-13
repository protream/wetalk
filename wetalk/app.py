"""
    wetalk.app
    ~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import Flask as _Flask
from werkzeug.datastructures import ImmutableDict


class Flask(_Flask):
    jinja_options = ImmutableDict(
        # 渲染模版时去除空行
        trim_blocks=True,
        lstrip_blocks=True,
        # Flask 的默认配置
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_']
    )
