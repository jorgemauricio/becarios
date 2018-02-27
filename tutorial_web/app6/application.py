import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ["Pablo", "Juan", "Antonio", "Pedro"]
    return render_template("index.html", names=names)
