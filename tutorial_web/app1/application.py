from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hellow World!!!"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome</h1>"
