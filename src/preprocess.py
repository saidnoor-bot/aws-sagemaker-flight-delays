from __future__ import annotations
import pandas as pd
from typing import Tuple

FEATURES = ["dep_delay", "distance"]
LABEL = "is_late"

def build_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    # Ensure required columns exist; light cleanup
    for col in FEATURES + [LABEL]:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    X = df[FEATURES].copy()
    y = df[LABEL].astype(int)
    # Basic NA handling
    X = X.fillna(0)
    return X, y
