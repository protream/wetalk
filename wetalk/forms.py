# -*- coding: utf-8 -*-
"""
    wetalk.forms
    ~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask import request
from werkzeug.datastructures import MultiDict
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Required, Length, Email, StopValidation
from wetalk.models import db, User


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


class RegisterForm(Form):
    username = StringField(validators=[
        Length(3, 24, message='用户名长度要在3~24个字符之间'),
    ])
    email = StringField(validators=[
        Email(message='请输入有效的邮箱地址'),
    ])
    password = PasswordField(validators=[
        Length(6, 24, message='密码长度要在6~24个字符之间')
    ])

    def create_user(self):
        user = User(
            username=self.username.data,
            email=self.email.data,
            password=self.password.data
        )
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(Form):
    email = StringField(validators=[
        Required('请输入您的邮箱'),
        Email(message='请输入有效的邮箱地址'),
    ])
    password = PasswordField(validators=[
        Required('请输入您的密码')
    ])

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise StopValidation('该邮箱还未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user and not user.verify_password(field.data):
            raise StopValidation('密码错误')
