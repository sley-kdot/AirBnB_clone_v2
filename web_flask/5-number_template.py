#!/usr/bin/python3
""" Start a flask web application
Listens on 0.0.0.0 and port 5000

Routes:
    /: displays Hello HBNB!
    /hbnb: displays HBNB
    /c/<text>: display “C ” followed value of the text variable
    /python/<text>: display “Python ”, followed by the value of the text var
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Handles application URL """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Handles application URL """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hbnb_c(text):
    """ display “C ” followed by the value of the text var
    replace underscore _ symbols with a space"""
    text_with_space = text.replace('_', ' ')
    return "C {}".format(text_with_space)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb_python(text="is cool"):
    """ display “Python ” followed by the value of the text var
    replace underscore _ symbols with a space"""
    text_with_space = text.replace('_', ' ')
    return "Python {}".format(text_with_space)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display 'n is a number' only if n is an integer """
    return "n is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=1)
