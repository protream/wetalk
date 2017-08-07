# -*- coding: utf-8 -*-
"""
    wetalk.models.base
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True, unique=True)
    text = Column(String(10000), nullable=False)
