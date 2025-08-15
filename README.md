# ✈️ Flight Delay Risk — ML to Cloud

A project that predicts U.S. flight delays using Python + AWS SageMaker.  
It’s built to be **real**, secure, and easy to scale.

## Why this project
- Predict delays → better schedules & happy customers.
- Shows skills from raw data → model → cloud.
- Recruiters see cloud-native + security focus.

## Architecture
```mermaid
flowchart LR
  A[Raw Data] --> B[Preprocess (pandas + scikit-learn)]
  B --> C[Train (RandomForest)]
  C --> D[Evaluate (AUC Precision Recall F1)]
  D --> E[Artifacts (model + metrics)]
  E --> F{Deploy?}
  F -->|Batch| G[Batch Inference]
  F -->|Realtime| H[AWS SageMaker Endpoint]

