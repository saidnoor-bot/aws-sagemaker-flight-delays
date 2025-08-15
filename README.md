cat > README.md <<'EOF'
# ✈️ Flight Delay Risk — ML to Cloud
![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange) ![AWS-SageMaker](https://img.shields.io/badge/AWS-SageMaker-success) ![MLOps](https://img.shields.io/badge/MLOps-CI%2FCD-green)
[![CI](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml/badge.svg)](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A production-grade machine learning project that predicts the probability of U.S. flight delays.  
Built for real-world deployment with a focus on **scalability, security, and maintainability**.

## Why this project
- **Business impact:** Anticipate delays to improve scheduling and customer satisfaction.
- **Engineering value:** End-to-end ML: data → features → model → metrics → deploy.
- **Recruiter insight:** Cloud-native ML with security-conscious design.

## Architecture
```mermaid
flowchart LR
  A[Raw Data] --> B[Preprocess: pandas & scikit-learn]
  B --> C[Train: RandomForest]
  C --> D[Evaluate: AUC, Precision, Recall, F1]
  D --> E[Artifacts: model + metrics]
  E --> F{Deploy?}
  F -->|Batch| G[Batch Inference]
  F -->|Realtime| H[AWS SageMaker Endpoint]


![ROC Curve](assets/roc_curve.png)

## Project structure
cat > Makefile <<'EOF'
.PHONY: demo eval clean

demo: ## Create venv, install deps, run evaluation (writes artifacts)
python -m venv .venv && . .venv/bin/activate && \
python -m pip install --upgrade pip && \
pip install -r requirements.txt && \
MPLBACKEND=Agg python -m src.evaluate

eval: ## Re-run evaluation (refresh metrics + ROC)
MPLBACKEND=Agg python -m src.evaluate

clean: ## Remove venv and generated artifacts
rm -rf .venv artifacts/*.png artifacts/*.json __pycache__ */__pycache__

**One-liner to run everything:** `make demo`
