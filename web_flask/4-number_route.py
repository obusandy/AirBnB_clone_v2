#!/usr/bin/python3
"""
Starts a Flask web application.
This application demonstrates dynamic routing
The root path (`/`) welcomes visitors with a friendly "Hello HBNB!" message.
The `/hbnb` path displays a concise "HBNB" response.
The `/c/<text>` path allows customization. It displays the letter 'C'
followed by the provided text value, replacing any underscores with spaces.
The `/python` and `/python/<text>` paths handle requests related to Python.
The `/number/<int:n>` path validates user input.
It displays a message indicating whether the provided value `<n>` is an integer.
If not, an error is returned.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays  warm welcome
    'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns:
        A string containing the greeting message "Hello HBNB!".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Handles requests to the `/number/<int:n>` path and validates the input.
    Main point of entry."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
