"""
Empirical Analysis Module: Benchmark Validation against Najar et al. (2020) Dataset.
"""

from typing import Dict, Tuple, Optional
import os
import pandas as pd
import numpy as np


def load_najar_dataset(data_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load and clean empirical two-armed bandit trials from Najar et al. (2020) PLoS Biology.

    Parameters
    ----------
    data_path : str, optional
        Path to task1.csv dataset file. If None, resolves relative to repository root.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe containing participant trials.
    """
    if data_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_path = os.path.join(base_dir, "data", "task1.csv")

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Empirical dataset not found at: {data_path}")

    df = pd.read_csv(data_path)
    # Filter for valid participant choices
    if "condition.obs" in df.columns:
        df_choice = df[df["condition.obs"] == "Choice"].copy()
    else:
        df_choice = df.copy()

    return df_choice


def evaluate_empirical_comparison(df: pd.DataFrame) -> Dict[str, float]:
    """
    Compute summary metrics on participant choices across skilled vs novice demonstrator conditions.

    Parameters
    ----------
    df : pd.DataFrame
        Empirical dataset.

    Returns
    -------
    Dict[str, float]
        Dictionary of empirical choice statistics and imitation fidelity metrics.
    """
    # Clean reaction times and outcomes
    valid_trials = df[df["cgb"].notna() & (df["cgb"] != "NA")].copy()
    valid_trials["cgb"] = pd.to_numeric(valid_trials["cgb"], errors="coerce")

    # Proportion of optimal choices (cgb == 1 corresponds to choosing the high-reward arm)
    mean_optimal_choice = float(valid_trials["cgb"].mean())

    # Disaggregate by skilled demonstrator condition if present
    if "condition.demskill" in valid_trials.columns:
        skilled_trials = valid_trials[valid_trials["condition.demskill"] == "skilled.dem"]
        skilled_optimal = float(skilled_trials["cgb"].mean()) if len(skilled_trials) > 0 else mean_optimal_choice
    else:
        skilled_optimal = mean_optimal_choice

    return {
        "total_trials": len(valid_trials),
        "mean_optimal_choice": mean_optimal_choice,
        "skilled_dem_optimal_choice": skilled_optimal,
    }
