"""
    wetalk.models.user
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from .base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    email = Column(String(50), unique=True)
    _password = Column('password', String(255))

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def verify_password(self, orig_password):
        return check_password_hash(self._password, orig_password)

    def to_dict(self):
        return {'id': self.id,
                'email': self.email,
                'username': self.username}
