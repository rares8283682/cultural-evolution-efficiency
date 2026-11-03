.PHONY: all test figures sim dashboard notebook clean help

help:
	@echo "Available commands:"
	@echo "  make test       - Run unit test suite with pytest"
	@echo "  make figures    - Generate all publication-grade 300 DPI figures"
	@echo "  make sim        - Run 50-run Monte Carlo ensemble simulation"
	@echo "  make dashboard  - Open interactive HTML5 simulation sandbox"
	@echo "  make notebook   - Rebuild and execute master Jupyter notebook"
	@echo "  make clean      - Remove bytecode and cache files"

test:
	pytest -v

figures:
	python generate_figures.py

sim:
	python simulate.py

dashboard:
	python -m webbrowser docs/index.html || open docs/index.html

notebook:
	python build_project_notebook.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
