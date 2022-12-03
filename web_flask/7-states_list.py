#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
