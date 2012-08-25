'''
Created on Aug 12, 2012

@author: adetolaadewodu
'''
from __future__ import with_statement
from database import create_engine,MetaData,db_session
from flask import Flask, render_template, g
import models

#Using pymysql adapter to connect
engine = create_engine( "mysql+pymysql://root:@localhost/pydb")
metadata = MetaData(bind=engine)

# Create our application
app = Flask(__name__)
app.config.from_object(__name__)



@app.before_request
def before_request():
    g.db = engine.connect()
    db_session.configure()
    
    
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
    
@app.route('/countries')
def show_countries():
    cur = db_session.query(models.Country)
    countries = [dict(country=row.country, country_code=row.country_code) for row in cur]
    return render_template('show_countries.html', countries=countries)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()