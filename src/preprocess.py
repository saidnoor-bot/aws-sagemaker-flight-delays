from __future__ import annotations
import pandas as pd

TARGET_COL = "arr_delay"

def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    y = (df[TARGET_COL] > 15).astype(int)
    X = df.drop(columns=[TARGET_COL])
    # One-hot encode categoricals
    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)
    return X, y
