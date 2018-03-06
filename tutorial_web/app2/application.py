from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hellow World!!!"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/<string:name>')
def hello(name):
    return "Hello, {}".format(name)
