'''
Links:
------
https://variable-scope.com/posts/storing-and-verifying-passwords-with-sqlalchemy
'''
from datetime import datetime
from passlib.hash import bcrypt
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id =  Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    update_at = Column(DateTime, default=datetime.now(), nullable=True)
    create_at = Column(DateTime, default=datetime.now(), nullable=True)

    def __init__(self, username, email, password, name, update_at=datetime.now(), create_at=datetime.now()):
        self.username = username
        self.email = email
        self.password = bcrypt.encrypt(password)
        self.name = name
        self.update_at = update_at
        self.create_at = create_at

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)
    def __repr__(self):
        return "<User(username='%s', name='%s', email='%s', password=*****, update_at=%s, create_at='%s')>" % (self.username, self.name, self.email, self.update_at, self.create_at)
