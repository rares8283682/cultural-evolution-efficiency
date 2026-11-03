"""
Unit tests for HarshnessCulturalArena simulation engine.
"""

import pytest
import numpy as np
from src.cultural_evolution.arena import HarshnessCulturalArena


def test_arena_initialization():
    arena = HarshnessCulturalArena(N=50, generations=20, shock_gen=10)
    assert arena.N == 50
    assert arena.T == 20
    assert arena.T_shock == 10
    assert arena.cost_copy < arena.cost_innov


@pytest.mark.parametrize("mode", [0, 1, 2, 3, 4])
def test_simulate_single_run_modes(mode):
    arena = HarshnessCulturalArena(N=40, generations=25, shock_gen=12, seed=42)
    rng = np.random.default_rng(12345)
    hist = arena.simulate_single_run(strategy_mode=mode, rng=rng)

    assert "mean_payoff" in hist
    assert "mean_skill" in hist
    assert "diversity" in hist
    assert "pct_innovating" in hist

    assert len(hist["mean_payoff"]) == 25
    assert not np.any(np.isnan(hist["mean_payoff"]))
    assert not np.any(np.isnan(hist["mean_skill"]))

    # Pure copiers (mode 0) should have 0% innovating
    if mode == 0:
        assert np.all(hist["pct_innovating"] == 0.0)
    # Pure innovators (mode 1) should have 100% innovating
    elif mode == 1:
        assert np.all(hist["pct_innovating"] == 100.0)


def test_run_ensemble_keys_and_shapes():
    arena = HarshnessCulturalArena(N=30, generations=15, shock_gen=8, seed=99)
    results = arena.run_ensemble(n_runs=3)

    assert len(results) == 5
    for label, data in results.items():
        assert "mean_payoff" in data
        assert "mean" in data["mean_payoff"]
        assert len(data["mean_payoff"]["mean"]) == 15
        assert "cumulative_payoff" in data
        assert "mean" in data["cumulative_payoff"]


def test_replicator_dynamics():
    arena = HarshnessCulturalArena(N=30, generations=15, shock_gen=8, seed=123)
    rep = arena.run_replicator_dynamics(n_runs=3)

    assert "props_history" in rep
    assert rep["props_history"].shape == (3, 15, 3)

    # Check proportions sum to 1.0 within numerical precision
    sums = np.sum(rep["props_history"], axis=2)
    assert np.allclose(sums, 1.0, atol=1e-2)
