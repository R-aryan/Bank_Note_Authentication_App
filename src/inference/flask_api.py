from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Welcome All"

