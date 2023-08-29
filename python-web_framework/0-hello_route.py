'''
Flask is a web framework, it is a Python module that lets you develop web applications easily.
It has a small and easy-to-extend core: it is a microframework that doesn’t include an ORM 
(Object Relational Manager) or such features.
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """
    This is a function that returns a specifies string when routing to /
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()