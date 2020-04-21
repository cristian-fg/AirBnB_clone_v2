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


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_2(text):
    """Display python"""
    txt = text.replace('_', ' ')
    return "Python {}".format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display number only if it is"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
