#!/usr/bin/python3
""" Start a flask web application
Listens on 0.0.0.0 and port 5000

Routes:
    /: displays Hello HBNB!
    /hbnb: displays HBNB
    /c/<text>: display “C ” followed value of the text variable
"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=1)
