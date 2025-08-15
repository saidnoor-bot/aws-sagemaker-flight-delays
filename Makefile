.PHONY: install lint format test run-local train pipeline clean

install:
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

lint:
flake8 src tests

format:
black src tests && isort src tests

test:
pytest -q

run-local:
python -m src.train --local --config config/params.yaml

train:
python -m src.train --config config/params.yaml

pipeline:
aws cloudformation deploy \
  --template-file infra/cloudformation/sagemaker-pipeline.yaml \
  --stack-name flight-delays-pipeline \
  --capabilities CAPABILITY_IAM

clean:
rm -rf .venv .pytest_cache **/__pycache__
