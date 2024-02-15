#!/usr/bin/python3
""" Start a flask web application
Listens on 0.0.0.0 and port 5000

Routes:
    /: displays Hello HBNB!
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Handles application URL """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=1)
