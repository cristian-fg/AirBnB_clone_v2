#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """hello HBNB from flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Display text"""
    txt = text.replace('_', ' ')
    return "C {}".format(txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
