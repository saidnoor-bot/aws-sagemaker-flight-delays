# ✈️ Flight Delay Risk — ML to Cloud

## 📌 Project Overview
This project takes a Machine Learning model from concept to deployment (cloud-friendly).
It predicts whether a U.S. domestic flight will arrive late using historical flight and route features.

**Business Relevance:** Airlines/logistics/travel apps can use this to optimize ops & customer experience.  
**Engineering Focus:** Maintainability, automation, and scalability.

## 🏗 Architecture
```mermaid
flowchart LR
  A[Raw Flight Data] --> B[Preprocess (pandas/sklearn)]
  B --> C[Train (RandomForest)]
  C --> D[Evaluate (AUC/PR, ROC)]
  D --> E[Artifacts (model + metrics)]
  E --> F{Deploy?}
  F -->|Batch| G[Batch Inference]
  F -->|Realtime| H[SageMaker Endpoint]
```

## ✅ Results (local quick run)
| Metric     | Value |
|-----------:|:-----:|
| AUC        | 1.0 |
| Precision  | 1.0 |
| Recall     | 1.0 |
| F1         | 1.0  |

![ROC Curve](artifacts/roc.png)

## 🚀 Quick Demo
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.evaluate
```

Artifacts are saved to `artifacts/` and metrics printed to console.

## 🔧 Dev Helpers
Make targets:
```bash
make demo     # venv + install + evaluate (writes artifacts)
make eval     # re-run evaluation only
make clean    # clean caches/venv/artifacts
```

---
