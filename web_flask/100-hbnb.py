#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """app context"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_task():
    """Display all states objects"""
    state = storage.all('State')
    ameni = storage.all('Amenity')
    citi = storage.all('City')
    place = storage.all('Place')
    return render_template('100-hbnb.html', state=state, ameni=ameni,
                           citi=citi, place=place)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
