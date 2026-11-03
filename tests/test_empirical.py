"""
Unit tests for Empirical analysis module.
"""

import pytest
import os
from src.cultural_evolution.empirical import load_najar_dataset, evaluate_empirical_comparison


def test_empirical_loader_and_evaluation():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "task1.csv")
    if not os.path.exists(data_path):
        pytest.skip("task1.csv not present in test environment")

    df = load_najar_dataset(data_path)
    assert len(df) > 0

    metrics = evaluate_empirical_comparison(df)
    assert "total_trials" in metrics
    assert "mean_optimal_choice" in metrics
    assert 0.0 <= metrics["mean_optimal_choice"] <= 1.0
