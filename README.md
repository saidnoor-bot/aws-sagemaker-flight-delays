
# ✈️ Flight Delay Risk — ML to Cloud
[![CI](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml/badge.svg)](https://github.com/saidnoor-bot/aws-sagemaker-flight-delays/actions/workflows/ci.yml) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange) ![AWS SageMaker](https://img.shields.io/badge/AWS--SageMaker-success) ![MLOps](https://img.shields.io/badge/MLOps-CI%2FCD-green)


  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)  
![AWS SageMaker](https://img.shields.io/badge/AWS--SageMaker-success)  
![MLOps](https://img.shields.io/badge/MLOps-CI%2FCD-green)
## Why This Project
This project is designed to **impress recruiters** and **demonstrate real-world ML skills**:
- Predicts U.S. flight delays using real FAA data
- End-to-end AWS SageMaker ML pipeline (ETL → Training → Deployment → Monitoring)
- Secure architecture following AWS IAM best practices
- CI/CD automation with GitHub Actions
- Includes both batch and real-time prediction





## 📊 Metrics & Results
![ROC Curve](assets/roc_curve.png)
![Precision-Recall Curve](assets/pr_curve.png)

## 📦 Installation & Usage
```bash
# Clone the repository
git clone https://github.com/saidnoor-bot/aws-sagemaker-flight-delays.git
cd aws-sagemaker-flight-delays

# (Optional) Create and activate virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run evaluation
MPLBACKEND=Agg python -m src.evaluate

## 📸 Demo & Screenshots

Below are example outputs and diagrams from the project:

### Model ROC Curve
![ROC Curve](assets/roc_curve.png)

### Architecture Diagram
(See diagram above in the Architecture section)

---

## 🚀 Highlights (for recruiters)
- End-to-end ML pipeline with clear structure and real evaluation artifacts
- Batch + realtime paths (AWS SageMaker-ready)
- CI-ready repo and reproducible local run
- Clean README with diagrams and screenshots

## 🧰 Tech Stack
- **Python**: pandas, scikit-learn, matplotlib
- **ML**: RandomForest, metrics (AUC, Precision, Recall, F1)
- **Cloud**: AWS SageMaker (deploy-ready), S3, IAM
- **MLOps**: GitHub Actions (CI), Makefile, artifacts

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/saidnoor-bot/aws-sagemaker-flight-delays.git
   cd aws-sagemaker-flight-delays

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

MPLBACKEND=Agg python -m src.evaluate


Clone the repository and run the demo in one command:

```bash
git clone https://github.com/saidnoor-bot/aws-sagemaker-flight-delays.git
cd aws-sagemaker-flight-delays
make demo

