"""
Flask is a Python module that lets you develop web applications
easily.
"""
from flask import Flask
from flask import render_template
"""
The escape function is used for safely escaping HTML and other
special characters in order to prevent cross-site scripting (XSS)
attacks and ensure that user-generated content is displayed as
plain text rather than being interpreted as HTML or script code.
"""
from markupsafe import escape

app = Flask(__name__)
"""
 a route refers to a URL pattern that is defined within the framework to determine 
 how incoming requests are handled.
"""
@app.route("/")
def hello():
    """
    This is a function that returns a specified string when routing to /
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """
    This is a function that returns a specified string when routing to /hbnb
    """
    return "HBNB"

@app.route("/c/<text>")
def c_is_fun(text):
    """
    Thi sfunction returns the specified string when routing to /c showing
    the text in that directory
    """
    return f"C " + text.replace('_', ' ')

@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Templates can be used to generate any type of text file.
    """
    return f"Python " + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def is_a_num(n):
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes= False)
def number_template(n):
    return render_template("templates/5-number.html")

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        return render_template("templates/6-number_odd_or_even.html", Num=n)
    else:
        return render_template("templates/6-number_odd_or_even.html", Number=n)


if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0', port=5000)

