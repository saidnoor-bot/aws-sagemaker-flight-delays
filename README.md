# ✈️ Flight Delay Risk — ML to Cloud
[![CI](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml/badge.svg)](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A clean, recruiter-ready ML portfolio project that predicts U.S. flight delay risk.
Built for clarity, reproducibility, and **AWS-ready MLOps**.

## 🧠 Why it matters
- **Business impact:** Reduce delays & improve customer satisfaction.
- **Engineering value:** Modeling, evaluation, automation, cloud readiness.

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

