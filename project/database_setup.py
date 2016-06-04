from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
# New imports for this step
from flask import session as login_session
import random
import string 

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User) 
 
class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key = True)
    title =Column(String(80), nullable = False)
    content = Column(String(5000), nullable = False)
    summary = Column(String(500))
    picture = Column(String(250))
    comment = Column(Boolean, default=True)
    tag = Column(String(300))
    author = Column(String(50))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

engine = create_engine('mysql://root:admin@localhost:3306/marriedtochinese1')
Base.metadata.create_all(engine)