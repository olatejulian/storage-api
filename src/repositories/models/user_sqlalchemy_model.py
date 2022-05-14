from datetime import datetime
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id =  Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    create_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return "<User(username='%s', name='%s', email='%s', password=*****, create_at='%s')>" % (self.username, self.name, self.email, self.create_at)
