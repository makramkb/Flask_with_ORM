import sqlalchemy
from sqlalchemy import create_engine,inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from flask import Flask , jsonify 
import pandas as pd

base = automap_base()
engine = create_engine(f'sqlite:///titanic.sqlite')
base.prepare(autoload_with=engine)
connection = engine.connect()


app = Flask(__name__)

@app.route('/')

def home_page():

    return ('This is the home page')

@app.route('/table_names')

def tables():
    
    session = Session(bind=engine)

    all_tables = base.classes.keys()

    session.close()


    return jsonify(all_tables)

@app.route('/passengers_name')

def passenger__names():

    session = Session(bind=engine)

    Passenger = base.classes.passenger 

    query = session.query(Passenger)

    passenger_names = [i.name for i in query]

    session.close()

    return passenger_names



if __name__ == '__main__':
    app.run(debug=True)

        





    



