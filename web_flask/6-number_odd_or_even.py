#!/usr/bin/python3
"""
starts a Flask web application.
listens on 0.0.0.0, port 5000.
Has the following routes:
    - / : displays "Hello HBNB!"
    - /hbnb : displays "HBNB"
    - /c/<text> : display "C" followed by the value of the text
    - /python/(<text>): display "Python" followed by the value of the text
    - /number/<n>: display "n is a number" only if n is an integer
    - /number_template/<n>: display an HTML page only if n is an integer
    - /number_odd_or_even/<n>: display an HTML page only if n is an integer
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns C followed by the value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Returns Python followed by the value of the text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns n is a number only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns an HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
