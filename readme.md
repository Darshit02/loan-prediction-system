# 🏦 Loan Prediction System (End-to-End ML Project)

An end-to-end **Machine Learning application** that predicts whether a loan application will be **approved or rejected** based on applicant information.

This project demonstrates a **complete ML engineering workflow**, including:

- Data preprocessing
- Feature engineering
- Model training and selection
- Experiment tracking
- API deployment
- Interactive dashboard
- Containerization

The system allows users to enter loan details through a **web dashboard** and receive a prediction instantly.

---

# 🚀 Features

- End-to-End ML pipeline
- Multiple model training (Random Forest + XGBoost)
- Automated best model selection
- Experiment tracking with MLflow
- REST API using FastAPI
- Interactive dashboard with Streamlit
- Docker container deployment
- Clean modular project structure

---

# 🧠 Machine Learning Workflow

```
EDA
 ↓
Data Preprocessing
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Model Evaluation
 ↓
Best Model Selection
 ↓
Model Deployment
```

---

# 🏗️ System Architecture

```
                User
                 │
                 ▼
        Streamlit Dashboard
                 │
                 ▼
            FastAPI API
                 │
                 ▼
         Prediction Module
                 │
                 ▼
        Data Preprocessor
                 │
                 ▼
            ML Model
                 │
                 ▼
            Prediction
```

---

# 📂 Project Structure

```
loan-prediction-model
│
├── app
│   └── streamlit_app.py
│
├── data
│   ├── raw
│   ├── data_loader.py
│   └── preprocess.py
│
├── models
│   ├── predict.py
│   ├── train_model.py
│   ├── train_model.pkl
│   └── preprocessor.pkl
│
├── notebooks
│   └── eda.ipynb
│
├── pipelines
│   └── training_pipeline.py
│
├── src
│   ├── api
│   ├── config
│   ├── schema
│   └── utils
│
├── tests
│   └── sent_data.py
│
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── mlflow.db
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/loan-prediction-system.git
cd loan-prediction-system
```

Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

```
python src/models/train_model.py
```

This will:

- preprocess data
- train models
- select the best model
- save model artifacts

---

# 🔌 Run API

```
uvicorn src.api.main:app --reload
```

Open API docs:

```
http://localhost:8000/docs
```

---

# 📊 Run Dashboard

```
streamlit run app/streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Run with Docker

Build image

```
docker build -t loan-api .
```

Run container

```
docker run -p 8000:8000 loan-api
```

Or with docker compose

```
docker compose up --build
```

---

# 📈 Experiment Tracking

Run MLflow UI

```
mlflow ui
```

Open:

```
http://localhost:5000
```

Track:

- model accuracy
- parameters
- experiments
- artifacts

---

# 📊 Example Input

```
{
 "Gender": "Male",
 "Married": "Yes",
 "Dependents": "0",
 "Education": "Graduate",
 "Self_Employed": "No",
 "ApplicantIncome": 5000,
 "CoapplicantIncome": 2000,
 "LoanAmount": 150,
 "Loan_Amount_Term": 360,
 "Credit_History": 1,
 "Property_Area": "Urban"
}
```

---

# 🛠 Tech Stack

Machine Learning

- Scikit-learn
- XGBoost

Backend

- FastAPI

Frontend

- Streamlit

MLOps

- MLflow
- Docker
- Docker Compose

---

# 📌 Future Improvements

- Model monitoring
- Feature store
- CI/CD pipeline
- Cloud deployment (AWS/GCP)

---

# 👨‍💻 Author

Darshit

Machine Learning & AI Developer

