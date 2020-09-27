from flask import Flask, request
import pandas as pd

from src.inference.predict import NotePredictor

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome All"


nap = NotePredictor()


@app.route('/predict', methods=["GET"])
def predict_note_authentication():
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


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = nap.predict_file(df_test)

    return str(list(prediction))

#
# if __name__ == '__main__':
#     app.run(debug=True)
