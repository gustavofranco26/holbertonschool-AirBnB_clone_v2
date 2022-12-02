#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Module that display"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Module that display"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Module that display"""
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth_on(text="is cool"):
    """Module that display"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def text_int(n):
    """Module that display"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
