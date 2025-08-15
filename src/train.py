from __future__ import annotations
import argparse, yaml, json
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support
from src.preprocess import build_features
import joblib

def load_params(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/params.yaml")
    parser.add_argument("--local", action="store_true")
    args = parser.parse_args()

    params = load_params(args.config)

    df = pd.read_csv("data/sample.csv")
    if params.get("sample_rows"):
        df = df.head(params["sample_rows"])

    X, y = build_features(df)

    clf = RandomForestClassifier(**params["model"]["params"], random_state=params["random_state"])
    clf.fit(X, y)

    # quick self-eval on same data (demo)
    y_hat = clf.predict_proba(X)[:, 1]
    auc = roc_auc_score(y, y_hat)
    precision, recall, f1, _ = precision_recall_fscore_support(y, (y_hat > 0.5).astype(int), average="binary")

    metrics = {
        "auc": round(float(auc), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1": round(float(f1), 4),
    }

    Path("artifacts").mkdir(exist_ok=True)
    with open("artifacts/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    # save model for inference demo
    joblib.dump(clf, "artifacts/model.joblib")

    print("METRICS:", metrics)
