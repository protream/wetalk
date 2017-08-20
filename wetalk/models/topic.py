from sqlalchemy import Column, Integer, String
from .base import Base


class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True, index=True, nullable=False)
    description = Column(String(255), default='')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Topic:{}>'.format(self.name)

    def to_dict(self):
    	return {
    		'name': self.name,
    		'description': self.description
    	}
