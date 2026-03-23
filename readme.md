<div align="center">

<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-189ABA?style=for-the-badge&logo=xgboost&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

# 💳 Loan Prediction System

### End-to-End ML + MLOps — Predict Loan Approval in Real Time  
**Random Forest · XGBoost · MLflow · FastAPI · Streamlit · Docker**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/Experiment%20Tracking-MLflow-0194E2?logo=mlflow)](https://mlflow.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-project-architecture)
- [Pipeline Flow](#-pipeline-flow)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Training](#-run-training-pipeline)
- [MLflow UI](#-run-mlflow-ui)
- [API Server](#-run-fastapi-server)
- [Dashboard](#-run-streamlit-dashboard)
- [API Usage](#-api-usage)
- [Model Performance](#-model-performance)
- [Docker](#-docker-deployment)
- [Testing](#-testing)
- [Future Roadmap](#-future-roadmap)
- [Disclaimer](#-disclaimer)
- [Contributing](#-contributing)

---

## 🔬 Overview

**Loan Prediction System** is a production-style, end-to-end machine learning application that predicts whether a loan application should be **Approved** or **Rejected** based on financial and demographic data.

The project demonstrates the complete ML lifecycle — from raw data ingestion and feature engineering, through model training and experiment tracking with MLflow, to a live REST API and interactive Streamlit dashboard. Built with MLOps best practices from the ground up.

> ⚠️ **For educational purposes only.** Not intended for real financial decision-making.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Full ML Pipeline** | Data ingestion → preprocessing → training → evaluation → serving |
| 🤖 **Model Comparison** | Random Forest vs XGBoost with automatic best-model selection |
| 📈 **MLflow Tracking** | Log parameters, metrics, artifacts; full experiment history & model versioning |
| 🔌 **FastAPI Backend** | RESTful prediction endpoint with Pydantic schema validation |
| 📊 **Streamlit Dashboard** | Upload applicant data and get instant predictions via browser UI |
| 🐳 **Dockerized** | Full Docker + Docker Compose setup for one-command production deployment |
| 🧪 **Test-Ready** | pytest-compatible structure for unit and integration tests |

---

## 🏗️ Project Architecture

```
loan-prediction-system/
│
├── app/
│   └── streamlit_app.py            # 📊 Streamlit prediction dashboard
│
├── data/
│   ├── raw/                        # 📁 Raw CSV dataset
│   ├── data_loader.py              #    Load & split data
│   └── preprocess.py               #    Feature engineering & encoding
│
├── mlruns/                         # 📈 MLflow experiment tracking data
├── mlflow.db                       #    MLflow SQLite backend
│
├── models/
│   ├── train_model.py              # 🤖 RF & XGBoost training logic
│   ├── predict.py                  #    Load model + run inference
│   ├── preprocessor.pkl            #    Saved preprocessing pipeline
│   └── train_model.pkl             #    Saved best model artifact
│
├── pipelines/
│   └── training_pipeline.py        # ⚙️  Orchestrates full training flow
│
├── notebooks/
│   └── eda.ipynb                   # 📓 Exploratory Data Analysis
│
├── src/                            # 🔌 Core API backend
│   ├── api/                        #    FastAPI route handlers
│   ├── config/                     #    App configuration & constants
│   ├── schema/                     #    Pydantic request/response models
│   ├── utils/                      #    Helper functions & logging
│   └── main.py                     #    API entrypoint
│
├── tests/
│   └── sent_data.py                # 🧪 Test payload & assertions
│
├── artifacts/                      # 💾 Additional saved outputs
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Pipeline Flow

```
                     ┌──────────────────────────────────────────────┐
                     │              RAW DATA INGESTION               │
                     │    CSV → data_loader.py → Train/Test Split    │
                     └────────────────────┬─────────────────────────┘
                                          │
                     ┌────────────────────▼─────────────────────────┐
                     │            FEATURE ENGINEERING                │
                     │  Encoding · Scaling · Imputation · Selection  │
                     └────────────────────┬─────────────────────────┘
                                          │
                     ┌────────────────────▼─────────────────────────┐
                     │           MODEL TRAINING & COMPARISON         │
                     │       Random Forest  ↔  XGBoost              │
                     └──────────┬─────────────────────┬─────────────┘
                                │                     │
                    ┌───────────▼──────────┐ ┌────────▼──────────────┐
                    │   Model Evaluation   │ │   MLflow Experiment   │
                    │ Accuracy · F1 · AUC  │ │  Params · Metrics ·   │
                    │  Best Model Selected │ │  Artifacts · Versions │
                    └───────────┬──────────┘ └───────────────────────┘
                                │
                     ┌──────────▼───────────────────────────────────┐
                     │          SAVED MODEL (.pkl)                   │
                     │     models/train_model.pkl                    │
                     └──────────┬────────────────────┬──────────────┘
                                │                    │
               ┌────────────────▼──────┐  ┌──────────▼──────────────┐
               │    FastAPI REST API   │  │  Streamlit Dashboard    │
               │   POST /predict       │  │  Form → Predict → Show  │
               └───────────────────────┘  └─────────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **ML Models** | Random Forest · XGBoost |
| **Data Processing** | Pandas · NumPy · Scikit-learn |
| **Experiment Tracking** | MLflow (SQLite backend) |
| **Backend API** | FastAPI · Uvicorn · Pydantic |
| **Frontend** | Streamlit |
| **Containerization** | Docker · Docker Compose |
| **Testing** | pytest |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip / conda
- Docker *(optional, for containerized deployment)*

### 1. Clone the Repository

```bash
git clone https://github.com/Darshit02/loan-prediction-system.git
cd loan-prediction-system
```

### 2. Create a Virtual Environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Dataset

Place your raw dataset in the `data/raw/` directory:

```
data/
└── raw/
    └── loan_data.csv       # Your training dataset
```

Recommended: [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)

---

## 🧠 Run Training Pipeline

```bash
python pipelines/training_pipeline.py
```

This will:

1. ✅ Load and clean data from `data/raw/`
2. ✅ Run feature engineering and preprocessing
3. ✅ Train Random Forest and XGBoost models
4. ✅ Compare performance and select the best model
5. ✅ Log all experiments, metrics, and artifacts to MLflow
6. ✅ Save the winning model to `models/train_model.pkl`

---

## 📈 Run MLflow UI

```bash
mlflow ui
```

Open your browser at **http://127.0.0.1:5000**

You'll see:
- 📋 All experiment runs with parameters and metrics
- 📊 Side-by-side model comparison charts
- 📦 Saved model artifacts per run
- 🏷️ Model versioning history

---

## 🔌 Run FastAPI Server

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Interactive API docs available at:
- **Swagger UI** → http://localhost:8000/docs
- **ReDoc** → http://localhost:8000/redoc

---

## 📊 Run Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

Open your browser at **http://localhost:8501**

Features:
- 📝 Fill in applicant details via form inputs
- 🤖 Instant prediction with confidence score
- 📊 Feature importance visualization
- 📈 Model performance summary panel

---

## 📌 API Usage

### Endpoint

```
POST /predict
```

### Request Payload

```json
{
  "income": 50000,
  "loan_amount": 200000,
  "credit_score": 750,
  "employment_status": "Salaried"
}
```

### Response

```json
{
  "loan_status": "Approved",
  "confidence": 0.87,
  "model_used": "XGBoost"
}
```

### Example with curl

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"income": 50000, "loan_amount": 200000, "credit_score": 750, "employment_status": "Salaried"}'
```

---

## 📊 Model Performance

Models are evaluated on a held-out test set. The best-performing model is automatically selected by the training pipeline.

| Metric | Random Forest | XGBoost |
|---|---|---|
| **Accuracy** | ~85% | ~88% |
| **Precision** | ~84% | ~87% |
| **Recall** | ~83% | ~86% |
| **F1-Score** | ~83% | ~86% |
| **AUC-ROC** | ~0.91 | ~0.93 |

> Metrics vary based on dataset, hyperparameters, and train/test split. All runs are logged in MLflow for full reproducibility.

---

## 🐳 Docker Deployment

### Build & Run (Single Container)

```bash
docker build -t loan-prediction .
docker run -p 8000:8000 loan-prediction
```

### Multi-Service with Docker Compose

```bash
docker-compose up --build
```

This spins up:
- `api` service → FastAPI on port `8000`
- `dashboard` service → Streamlit on port `8501`
- `mlflow` service → MLflow UI on port `5000`

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# With coverage report
pytest tests/ --cov=src --cov-report=term-missing
```

Test coverage includes:
- `tests/sent_data.py` — API payload validation and response assertions
- Preprocessing pipeline correctness
- Model loading and inference checks

---

## 🔮 Future Roadmap

- [ ] 📊 **Feature importance visualization** — SHAP values in Streamlit
- [ ] 🧠 **AutoML integration** — Optuna / FLAML hyperparameter search
- [ ] 🏪 **Feature store** — Feast or Hopsworks integration
- [ ] ✅ **Data validation** — Great Expectations for schema & drift checks
- [ ] 🔁 **CI/CD pipeline** — GitHub Actions for automated test + deploy
- [ ] 🔄 **Automated retraining** — scheduled model refresh on new data
- [ ] 📦 **MLflow Model Registry** — staging → production promotion workflow
- [ ] 📡 **Drift monitoring** — Evidently AI or Whylogs integration
- [ ] ☁️ **Cloud deployment** — AWS SageMaker / GCP Vertex AI

---

## ⚠️ Disclaimer

> This project is developed **strictly for educational and research purposes**.  
> It is **not validated for real financial decision-making** and must **not** be used to approve or deny actual loan applications.  
> Always consult a licensed financial professional for credit-related decisions.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "feat: add your feature"

# 4. Push to your fork
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ for the ML & MLOps community

⭐ **Star this repo** if you found it useful!

</div>