from flask import Flask
'''
This is a documentation for the flask web application. 
'''
app = Flask(__name__)

@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run()
