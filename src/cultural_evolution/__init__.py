"""
Cultural Evolution & Efficiency Package
=======================================
A research-grade agent-based simulation toolkit for studying cumulative cultural
evolution under environmental harshness, transmission costs, and cognitive division of labor.

Key Components:
- HarshnessCulturalArena: Vectorized Monte Carlo agent-based model.
- RecombinantPatentModel: Modular technological evolution & citation dynamics (Charbonneau 2015).
- EmpiricalBanditAnalysis: Benchmark comparison against human behavioral trials (Najar et al. 2020).
"""

from .arena import HarshnessCulturalArena
from .recombination import RecombinantPatentModel
from .empirical import load_najar_dataset, evaluate_empirical_comparison

__version__ = "1.0.0"
__author__ = "Rares Olteanu (in collaboration with Prof. Alexey Koshevoy)"
__all__ = [
    "HarshnessCulturalArena",
    "RecombinantPatentModel",
    "load_najar_dataset",
    "evaluate_empirical_comparison",
]
