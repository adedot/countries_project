from flask import Flask
from sqlalchemy import Column, Date, DateTime, Float, Integer, Unicode, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.restless import APIManager
from Finder.Type_Definitions import preferences
from models import *

app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:@localhost/pydb', convert_unicode=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = scoped_session(Session)


Base.metadata.bind = engine

### Create the database tables.
Base.metadata.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, session=Session)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST'])
manager.create_api(Preference, methods=['GET', 'POST'])
manager.create_api(Recommendation, methods=['GET'])
manager.create_api(Country, methods=['GET'])

# start the flask loop
app.run()
