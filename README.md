# ✈️ Flight Delay Risk — ML to Cloud
[![CI](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml/badge.svg)](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A production-grade machine learning project that predicts the probability of U.S. flight delays.  
Designed and implemented with a strong focus on **model accuracy, scalability, and cloud deployment best practices**.

This repository is part of my professional portfolio as a **Cloud Security & AI/ML Engineer**, demonstrating applied skills in:
- **AWS Services**: SageMaker, S3, CloudFormation, CloudWatch, IAM
- **Machine Learning**: Feature engineering, model training, and evaluation (RandomForest, sklearn)
- **Security**: Secure data handling, IAM least-privilege policies, audit logging
- **MLOps**: CI/CD automation, reproducible pipelines, deployment to production

## 🧠 Project Goals
- **Business Impact:** Reduce costly flight delays and improve airline operational efficiency.
- **Engineering Value:** Show end-to-end ML workflow from raw data ingestion to production-ready deployment.
- **Recruiter Insight:** Highlights cloud-native ML engineering with security-conscious design.

## 🏗 Architecture
```mermaid
flowchart LR
  A[Raw Flight Data] --> B[Preprocess (pandas/sklearn)]
  B --> C[Train (RandomForest)]
  C --> D[Evaluate (AUC, PR, ROC)]
  D --> E[Artifacts (model + metrics)]
  E --> F{Deploy?}
  F -->|Batch| G[Batch Inference (AWS Batch/S3)]
  F -->|Realtime| H[SageMaker Endpoint]

