from fastapi import FastAPI
from src.schema.validate import LoanRequest
from models.predict import predict_loan

app = FastAPI()

@app.get("/")
def root_route():
    return{
        "Result" : "Hello world"
    }

@app.post("/predict")
def predict(data: LoanRequest):
    result = predict_loan(data.dict())
    return {
        "loan_prediction": result
    }