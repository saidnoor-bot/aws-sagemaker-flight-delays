.PHONY: demo train eval test lint fmt clean

demo: ## Create venv, install deps, run quick evaluation
python -m venv .venv && . .venv/bin/activate && \
python -m pip install --upgrade pip && \
pip install -r requirements.txt && \
MPLBACKEND=Agg python -m src.evaluate

eval: ## Re-run evaluation (writes ROC plot + metrics)
MPLBACKEND=Agg python -m src.evaluate

clean: ## Remove caches and venv
rm -rf .venv .pytest_cache **/__pycache__ */__pycache__ artifacts/*.png artifacts/*.json
