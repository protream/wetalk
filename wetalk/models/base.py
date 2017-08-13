"""
    wetalk.models.base
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime


db = SQLAlchemy()


class Base(db.Model):
    """ 所有 model 的一个基类，默认添加了时间戳
    """
    # 表示不要把这个类当作 Model 类
    __abstract__ = True
    # 设置了 defautl 和 onupdate 这俩个时间戳都不需要自己去维护
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
