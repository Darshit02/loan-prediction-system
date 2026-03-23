import joblib
import mlflow
import mlflow.sklearn

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from data.data_loader import load_dataset
from data.preprocess import preprocess_data

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def train_model_pipeline():

    df = load_dataset()

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)

    models = {
        "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42),
        "XGBoost": XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=4)
    }

    best_model = None
    best_score = 0
    best_model_name = ""

    mlflow.set_experiment("loan_prediction")

    for name, model in models.items():

        with mlflow.start_run(run_name=name):
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            score = accuracy_score(y_test, preds)
            mlflow.log_metric("accuracy", score)
            mlflow.sklearn.log_model(model, name)
            print(f"{name} Accuracy: {score}")
            if score > best_score:
                best_score = score
                best_model = model
                best_model_name = name

    print("\nBest Model:", best_model_name)
    print("Best Accuracy:", best_score)

    joblib.dump(best_model, "models/train_model.pkl")
    joblib.dump(preprocessor, "models/preprocessor.pkl")

if __name__ == "__main__":
    train_model_pipeline()