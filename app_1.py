from flask import Flask, jsonify 

 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,inspect

base = automap_base()

engine = create_engine(f'sqlite:///chinook.sqlite')
base.prepare(autoload_with=engine)
session = Session(bind=engine)

app = Flask(__name__)

@app.route('/')
def home():
    tables_name = base.classes.keys()

    session.close()
    return tables_name

@app.route('/column_names')

def col_names():

    inspector = inspect(engine)
    tabels_info = {}
    table_names = base.classes.keys()

    for table_name in table_names:
        column_names = inspector.get_columns(table_name)

        col_names = [col['name'] for col in column_names]

        tabels_info[table_name] = col_names

        session.close()

    return jsonify(tabels_info)





if __name__ == '__main__':
    app.run(debug=True)