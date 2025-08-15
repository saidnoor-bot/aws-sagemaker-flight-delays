from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support, roc_curve
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import build_features
import matplotlib.pyplot as plt

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def train_and_eval(csv_path="data/sample.csv",
                   metrics_path=ARTIFACTS/"metrics.json",
                   roc_path=ARTIFACTS/"roc.png"):
    df = pd.read_csv(csv_path)
    X, y = build_features(df)
    clf = RandomForestClassifier(n_estimators=120, max_depth=10, random_state=42)
    clf.fit(X, y)
    y_prob = clf.predict_proba(X)[:, 1]
    auc = roc_auc_score(y, y_prob)
    prec, rec, f1, _ = precision_recall_fscore_support(y, (y_prob > 0.5).astype(int), average="binary")
    metrics = {"auc": round(float(auc), 4),
               "precision": round(float(prec), 4),
               "recall": round(float(rec), 4),
               "f1": round(float(f1), 4)}
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)

    fpr, tpr, _ = roc_curve(y, y_prob)
    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC (AUC={metrics['auc']})")
    plt.plot([0,1],[0,1], linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve — Flight Delay Risk")
    plt.legend(loc="lower right")
    plt.savefig(roc_path, bbox_inches="tight")
    return metrics

if __name__ == "__main__":
    m = train_and_eval()
    print("METRICS:", m)
