'''
Created on Aug 12, 2012

@author: adetolaadewodu
'''
from sqlalchemy import Column, MetaData, Table, Integer, Float, String, Unicode
from sqlalchemy.orm import mapper, relation, relationship
from sqlalchemy.schema import ForeignKey
from database import metadata, db_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, ForeignKey('recommendations.item_id'), ForeignKey('preferences.item_id'),primary_key=True, )
    country_code = Column(Unicode, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)
    country = Column(Unicode, unique=True)
    
    
    
    
class Preference(Base):
    __tablename__ = 'preferences'
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    item_id = Column(Integer, primary_key=True)
    country = relationship(Country, backref="preferences")
    
    def __str__(self):
        return self.country
    
class Recommendation(Base):
    __tablename__ = 'recommendations'
    user_id = Column(Integer,ForeignKey('user.id'), primary_key=True)
    item_id = Column(Integer,primary_key=True)
    item_value = Column(Float)
    country = relationship(Country, backref="recommendations")

    def __str__(self):
        return self.country

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(130), unique=True)
    preferences = relationship(Preference, backref='user')
    recommendations = relationship(Recommendation, backref='user')
