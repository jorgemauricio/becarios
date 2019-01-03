import datetime
import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tablas=[]
    for i in range(1,11):
        for j in range(1, 11):
            tablas.append("{} x {} = {}".format(i,j,i*j))
    return render_template("index.html", tablas=tablas)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)
