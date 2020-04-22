#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """app context"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display all states objects"""
    data = storage.all('State')
    data_1 = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', data=data, data_1=data_1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
