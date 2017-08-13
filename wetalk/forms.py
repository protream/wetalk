# -*- coding: utf-8 -*-
"""
    wetalk.forms
    ~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import request
from werkzeug.datastructures import MultiDict
from flask_wtf import FlaskForm


class Form(FlaskForm):
    """ 所有表单的基类，在 SPA 中我们用 JSON 通信，使用 Form
        主要是做数据验证，当然也有一些专门验证 JSON 数据的库，
        但是用习惯了这个库还是觉得比较方便的
    """
    @classmethod
    def create_from_json(cls, obj=None):
        """ 用 json 数据初始化 form，想一想在留言板项目中的
            使用方法，留言板中只有的一个 form，这里抽象到基
            类中以给所有 form 使用
        """
        formdata = MultiDict(request.get_json())
        form = cls(formdata=formdata, obj=obj, csrf_enabled=False)
        return form
