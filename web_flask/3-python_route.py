#!/usr/bin/python3
"""This Flask web application provides several
routes for dynamic responses:
The root path (`/`) welcomes visitors
with a friendly "Hello HBNB!" message.
The `/hbnb` path shows a concise "HBNB" response.
The `/c/<text>` path allows customization.
It shows the letter 'C' followed by the provided text value.
Any underscores(_) in the text are replaced with spaces.
The `/python` and `/python/<text>`
    
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays  a warm fiendly welcome
    'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the welcome
    'HBNB'.
    Returns:
        A string containing the greeting message "Hello HBNB!".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Handles requests to the `/hbnb` path.

    Returns:
        A string containing the message "HBNB".
    
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ 
    Args:
        text (str): The text value provided in the URL.
    Replaces any underscores in <text> with slashes.
     Args:
        text (str, optional): The text value provided in the URL (defaults to "is cool").

    Returns:
        A string containing 'Python' followed by the processed text value. 
        Underscores in the text are replaced with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
