'''
Created on Aug 12, 2012

@author: adetolaadewodu
'''
from sqlalchemy import Column, MetaData, Table, Integer, Float, String
from sqlalchemy.orm import mapper, relation, relationship
from sqlalchemy.schema import ForeignKey
from database import metadata, db_session


schema = MetaData()

# Create Tables

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True))


preference_table = Table('taste_preferences', schema,
                            Column('user_id', Integer, primary_key=True),
                            Column('item_id', Integer, primary_key=True),)

recommendation_table = Table('recommendations', schema,
                            Column('user_id', Integer, primary_key=True),
                            Column('item_id', Integer, primary_key=True),
                            Column('item_value', Integer))

country_table = Table('countries', schema,
                            Column('id', Integer, \
                                    ForeignKey('recommendations.item_id'), \
                                    ForeignKey('taste_preferences.item_id'), \
                                    primary_key=True),
                            Column("country_code", String),
                            Column("latitude", Float),
                            Column("longitude", Float),
                            Column("country", String))


#Create Objects

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
    
class Preference(object):
    def __init__(self, user_id, item_id):
        self.user_id = user_id
        self.item_id = item_id
        self.country = relationship(Country, backref="taste_preferences")
    
class Recommendation(object):
    def __init__(self, user_id, item_id, item_value):
        self.user_id = user_id
        self.item_id = item_id
        self.item_value = item_value
        self.country = relationship(Country, backref="recommendation")
        
        
class Country(object):
    def __init__(self, country_code, latitude, longitude, country):
        self.id = id
        self.country_code = country_code
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
    
    def __str__(self):
        return self.country
    
    def __unicode__(self):
        return self.country

# Map Objects to Tables
mapper(User, users)
mapper(Preference, preference_table,properties={"countries":relation(Country,backref="taste_preferences")})
mapper(Recommendation, recommendation_table,  properties={"countries":relation(Country,backref="recommendation")})
mapper(Country, country_table)