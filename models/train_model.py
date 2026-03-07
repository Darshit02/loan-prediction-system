import joblib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from data.data_loader import load_dataset
from data.preprocess import preprocess_data

def train_models():
    df = load_dataset()
    X_train, X_test, y_train, y_test, preprocessing = preprocess_data(df)

    models = {
    "RandomForest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        colsample_bytree=0.8
    )
    }

    best_model = None
    best_score = 0
    best_model_name = ""

    for name ,model in  models.items():
        model.fit(X_train,y_train)
        preds = model.predict(X_test)
        score = accuracy_score(y_test ,preds)

        print(f"{name} Accurecy : {score}")

        if score > best_score:
            best_score = score
            best_model = model
            best_model_name = name

        print("\nBest Model:", best_model_name)


if __name__ == "__main__":
    train_models()