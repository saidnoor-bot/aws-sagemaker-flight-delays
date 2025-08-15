# Flight Delays — Predictive ML with Amazon SageMaker

Production-style ML project that builds, evaluates, and (optionally) deploys a model to predict US flight arrival delays using Amazon SageMaker. Includes reproducible code, tests, CI, and infra-as-code.

![CI](https://img.shields.io/github/actions/workflow/status/saidnoor-bot/aws-sagemaker-flight-delays/ci.yml)

## Highlights
- **End-to-end**: data prep → training → evaluation → (optional) batch inference
- **Reproducible**: `Makefile`, `requirements.txt`, and CI tests
- **Cloud-native**: SageMaker-ready code + optional Pipeline skeleton
- **Quality**: pre-commit (Black, isort, Flake8) and unit tests

## Quickstart (Local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make test
make run-local   # runs a quick baseline on sample data

That’s it. Your repo will now look professional with CI, tests, structure, and a clean README recruiters love. 

Want me to add:
- a 30–45s demo GIF command (ffmpeg) + instructions,
- a results badge pulled from `artifacts/metrics.json`,
- or switch your remote to SSH so future pushes are passwordless?

Tell me which and I’ll drop the exact commands.
cd ~/flight-project

# 1) Fix requirements (add joblib used by inference)
cat > requirements.txt <<'EOF'
boto3
sagemaker
pandas
numpy
scikit-learn
pyyaml
matplotlib
joblib
pytest
flake8
black
isort
pre-commit
