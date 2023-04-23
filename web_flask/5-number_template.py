#!/usr/bin/python3

"""This modiule starts a Flask web application,
    that returns text based on the route
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Renders ``hello HBNB`` for the root route"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Renders ``HBNB`` for the ``hbnb`` route"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_path(text):
    """Renders `C` followed by the text passed in the route"""

    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is_cool'):
    """Renders `Python` followed by the text passed in the route"""

    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """Renders n is a number, if it is"""

    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Renders a html template from the ``templates`` directory"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
