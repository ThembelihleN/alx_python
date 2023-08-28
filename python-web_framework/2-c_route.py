from flask import Flask
'''
Flask is a web framework, it is a Python module that lets you develop web applications easily.
It has a small and easy-to-extend core: it is a microframework that doesn’t include an ORM 
(Object Relational Manager) or such features.
'''
app = Flask(__name__)

@app.route("/c/<text>")
def hello():
    return "C"


if __name__ == '__main__':
    app.run()