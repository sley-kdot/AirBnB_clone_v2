#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """displays content on the webpage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays content on the webpage"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """displays content of the webpage from the subpath"""
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
