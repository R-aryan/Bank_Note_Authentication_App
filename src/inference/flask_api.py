from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

from src.inference.predict import NotePredictor

app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Welcome All"


nap = NotePredictor()


@app.route('/predict', methods=["Get"])
def predict_note_authentication():

    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")

    result = ""

    prediction = nap.predict(variance, skewness, curtosis, entropy)

    if prediction:
        result = "The note is Authentic"

    else:
        result = "The note is not authentic"

    return result

#
# if __name__ == '__main__':
#     app.run(debug=True)
