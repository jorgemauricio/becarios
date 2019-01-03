import datetime
import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv("../../data/coor_est.csv")
    nombres = np.array(data["Nombre"])
    return render_template("index.html", nombres=nombres)
