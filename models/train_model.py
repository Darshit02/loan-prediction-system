import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.training_pipeline import train_model_pipeline

if __name__ == "__main__":
    train_model_pipeline()