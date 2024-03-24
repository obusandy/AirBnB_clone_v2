#!/usr/bin/python3
"""This script launches a Flask web application
with a friendly greeting.
on port 5000
- Visitors are welcomed with a cheerful "Hello HBNB!" message.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Extends a warm welcome to those
    who visit the application
    main point of entry

    """
    return "Hello HBNB!"

    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
