#!/usr/bin/python3
"""
A sript that starts a Flask web application.
listens on 0.0.0.0, port 5000.
Has the following routes:
    - / : displays "Hello HBNB!"
    - /hbnb : displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
