import pandas as pd
import numpy as np
import pickle

# df = pd.read_csv('../dataset/TestFile.csv')
# print(df.head())


class NotePredictor:

    def __init__(self):
        self.pickle_in = open("../training/note_classifier.pkl", "rb")
        self.classifier = pickle.load(self.pickle_in)

    def predict(self,variance,skewness,curtosis,entropy):


