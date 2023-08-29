"""
Flask is a Python module that lets you develop web applications
easily.
"""
from flask import Flask, request
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
    return f"C {escape(text)}"

@app.route("/python/", defaults={"<text>, is cool"})
@app.route("/python/<text>")
def pyhton_is_cool(text):
    return f"Python <text>"

if __name__ == '__main__':
    app.run(debug=True)

