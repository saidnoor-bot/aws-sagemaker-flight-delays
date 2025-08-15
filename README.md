---

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

