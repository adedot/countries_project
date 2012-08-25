'''
Created on Aug 12, 2012

@author: adetolaadewodu
'''

from database import init_db
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table

init_db()


engine = create_engine( "mysql+pymysql://root:@localhost/pydb")
metadata = MetaData(bind=engine)
users = Table('users', metadata, autoload=True)