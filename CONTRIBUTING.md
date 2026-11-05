# Contributing to Cultural Evolution & Efficiency

Thank you for your interest in contributing to this project! We welcome contributions from researchers, computational social scientists, cognitive scientists, and students.

## Academic & Reproducibility Standards

This project adheres to the **Institute for Replication (I4R)** and **American Psychological Society (APS)** standards for computational reproducibility. Any proposed pull request modifying the model architecture or empirical benchmarks must maintain:
1. **Deterministic Random Seeding**: All stochastic simulations must use NumPy's modern Generator API (`np.random.default_rng(seed)`).
2. **Vectorized Implementations**: Model iterations across the agent population must remain vectorized in NumPy/SciPy for computational efficiency.
3. **Equifinality Preemption**: Parameter modifications must include null model baselines (e.g., Rogers 1988 static mixed-strategy, neutral drift) to rule out parameter-tuning artifacts.
4. **Complete Unit Test Coverage**: Any new feature or module in `src/cultural_evolution/` must be paired with corresponding unit tests in `tests/`.

## Local Development Workflow

### 1. Clone & Set Up Environment

```bash
git clone https://github.com/rares8283682/cultural-evolution-efficiency.git
cd cultural-evolution-efficiency
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest
```

### 2. Running Test Suite

```bash
pytest -v
```

### 3. Re-generating Figures

```bash
python generate_figures.py
```

### 4. Running the Interactive Simulation Dashboard

Simply open `docs/index.html` in any modern web browser or serve it locally:

```bash
python -m http.server 8000
# Open http://localhost:8000/docs/index.html
```

## Pull Request Guidelines

1. Create a feature branch (`git checkout -b feature/novel-transmission-bias`).
2. Commit your modifications with descriptive commit messages.
3. Ensure `pytest` passes with 100% success rate.
4. Open a Pull Request on GitHub against `main`.
