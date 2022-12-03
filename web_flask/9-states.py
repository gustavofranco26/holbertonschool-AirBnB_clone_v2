#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models.state import State
from models import storage

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_int(n):
    """Module to display html page only if int"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """Module to display html page only if int odd or even"""
    odd_even = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_even=odd_even)


@app.teardown_appcontext
def tear_down_close(self):
    """Module to remove current SQLAlchemy and close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states_html():
    """Module to display html page where you look for ordered
    places to insert in html in the UL tag"""
    states_objs = storage.all("State")
    return render_template("7-states_list.html", states=states_objs)


@app.route('/cities_by_states', strict_slashes=False)
def html_states_cities():
    """Module to display html page where you look for ordered
    places and cities to insert in html in the LI tag"""
    states_objs = storage.all("State")
    return render_template("8-cities_by_states.html", states=states_objs)


@app.route("/states")
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for states in storage.all("State").values():
        if states.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
