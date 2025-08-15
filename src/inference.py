from __future__ import annotations
import pandas as pd
import joblib
from src.preprocess import build_features

def predict(csv_path: str, model_path: str = "artifacts/model.joblib") -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    X, _ = build_features(df)
    model = joblib.load(model_path)
    preds = model.predict_proba(X)[:, 1]
    out = df.copy()
    out["delay_score"] = preds
    return out
