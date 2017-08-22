from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='posts', uselist=False)
    topic_id = Column(Integer, ForeignKey('topic.id'), nullable=False)
    topic = relationship('Topic', backref='posts', uselist=False)

    def __repr__(self):
        return '<Post:{}>'.format(self.title)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'user': self.user.to_dict(),
            'topic': self.topic.to_dict()
        }
