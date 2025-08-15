import pandas as pd
from src.preprocess import build_features

def test_build_features_shapes():
    df = pd.read_csv("data/sample.csv")
    X, y = build_features(df)
    assert len(X) == len(y)
    assert y.isin([0, 1]).all()
