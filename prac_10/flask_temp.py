"""Cp1404 prac week 10 intro to flask."""
from flask import Flask

app = Flask(__name__)


def main():
    """
    CP1404/CP5632 - Practical
    Pseudocode for temperature conversion
    """


def get_celsius(celsius_value):
    return "{:.2f}".format(celsius_value * 9.0 / 5 + 32)


def get_fahrenheit(fahrenheit_value):
    return "{:.2f}".format(5 / 9 * (fahrenheit_value - 32))


@app.route('/c/')
@app.route('/c/<c>')
def celsius(c="0"):
    try:
        str(get_celsius(float(c)))
        return "{} Celsius = {} Fahrenheit".format(c, str(get_celsius(float(c))))
    except:
        return "Enter valid Celsius value to convert to Fahrenheit"


@app.route('/f/')
@app.route('/f/<f>')
def fahrenheit(f="-17.7778"):
    try:
        str(get_fahrenheit(float(f)))
        return "{} Fahrenheit = {} Celsius".format(f, str(get_fahrenheit(float(f))))
    except:
        return "Enter valid Celsius value to convert to Fahrenheit"

if __name__ == '__main__':
    app.run()