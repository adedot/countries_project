'''
Created on Aug 12, 2012

@author: adetolaadewodu
'''

from database import init_database
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table

init_database()

engine = create_engine( "mysql+pymysql://root:@localhost/pydb")
metadata = MetaData(bind=engine)
# Create database
user = Table('user', metadata, autoload=True)