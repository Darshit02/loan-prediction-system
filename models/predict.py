import joblib
import pandas as pd

model = joblib.load("models/train_model.pkl")
preprocessing = joblib.load("models/preprocessor.pkl")

def predict_loan(data: dict):

    df = pd.DataFrame([data])
    processed_data = preprocessing.transform(df)
    prediction = model.predict(processed_data)
    return prediction[0]