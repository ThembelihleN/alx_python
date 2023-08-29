"""
Flask is a Python module that lets you develop web applications
easily.
"""
from flask import Flask

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
def hbnb():
    return "C"


if __name__ == '__main__':
    app.run(debug=True)

