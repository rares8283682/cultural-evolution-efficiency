"""
Unit tests for RecombinantPatentModel.
"""

import pytest
import numpy as np
from src.cultural_evolution.recombination import RecombinantPatentModel


def test_patent_model_simulation():
    model = RecombinantPatentModel(initial_patents=10, total_steps=50, seed=42)
    res = model.simulate()

    assert "citations" in res
    assert "qualities" in res
    assert "ranks" in res
    assert "sorted_citations" in res

    total = 10 + 50
    assert len(res["citations"]) == total
    assert len(res["ranks"]) == total
    # Check that sorted citations are monotonically non-increasing
    assert np.all(np.diff(res["sorted_citations"]) <= 0)
    # Check modules exist
    assert len(res["patent_modules"]) == total
