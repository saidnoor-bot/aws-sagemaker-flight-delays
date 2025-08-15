import pandas as pd
from src.train import load_params
from src.preprocess import build_features
from sklearn.ensemble import RandomForestClassifier

def test_train_baseline_runs():
    params = load_params("config/params.yaml")
    df = pd.read_csv("data/sample.csv")
    X, y = build_features(df)
    clf = RandomForestClassifier(**params["model"]["params"], random_state=params["random_state"])
    clf.fit(X, y)
    assert hasattr(clf, "feature_importances_")
