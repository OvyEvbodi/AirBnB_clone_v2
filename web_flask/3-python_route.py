#!/usr/bin/python3

"""This modiule starts a Flask web application,
    that returns text based on the route
"""

from flask import Flask

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

    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is_cool'):
    """Renders `Python` followed by the text passed in the route"""

    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
