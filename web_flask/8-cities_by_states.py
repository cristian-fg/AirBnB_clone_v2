#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """app context"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def Display_cities_states():
    """Display all states objects"""
    data = storage.all('State')
    return render_template('8-cities_by_states.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
