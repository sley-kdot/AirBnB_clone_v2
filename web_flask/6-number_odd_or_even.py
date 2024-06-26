#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """displays content on the webpage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays content on the webpage"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays content of the webpage from the subpath"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """displays content of the webpage from the subpath"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays content on the webpage from the subpath if it's an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    displays content on the webpage if it's an integer
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def number_odd_or_even(num):
    """
    displays content on the webpage if an integer is even or odd
    """
    return render_template('6-number_odd_or_even.html', num_var=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
