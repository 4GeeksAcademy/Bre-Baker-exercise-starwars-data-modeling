import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    addresses = relationship('Address', back_populates='user')
    blog_posts = relationship('BlogPost', back_populates='user')
    comments = relationship('Comment', back_populates='user')

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='addresses')

class BlogPost(Base):
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='blog_posts')
    comments = relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='comments')
    post_id = Column(Integer, ForeignKey('blog_post.id'))
    post = relationship('BlogPost', back_populates='comments')

    def to_dict(self):
        return {}

# Draw the ER diagram using SQLAlchemy base
render_er(Base, 'diagram.png')