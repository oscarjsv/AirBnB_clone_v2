#!/usr/bin/python3
''' flask comment'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbnb():
    ''' module flask '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' module flask '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace('_', " ")


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p(text):
    return "Python " + text.replace('_', " ")


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return"{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_ood_or_even(n):
    """render template"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
