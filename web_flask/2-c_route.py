#!/usr/bin/python3
"""This Flask web application serves two simple routes:
The root path (`/`) welcomes visitors
with a friendly "Hello HBNB!" message.
The `/hbnb` path displays a
concise "HBNB" response.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a warm welcome
    'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'.
    main point of entry"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
