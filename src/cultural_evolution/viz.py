"""
Visualization styling and figure generation helpers.
Adheres to Prof. Alexey Koshevoy's palette and style specifications:
- seaborn colorblind palette
- paper context
- tick style with spine despine
- 300 DPI figure outputs
"""

import matplotlib.pyplot as plt
import seaborn as sns


def set_publication_style():
    """Configure matplotlib and seaborn globally for publication-standard figures."""
    sns.set_theme(
        context="paper",
        style="ticks",
        font_scale=1.15,
        palette="colorblind",
        rc={
            "font.family": "sans-serif",
            "axes.edgecolor": "#333333",
            "axes.linewidth": 1.1,
            "grid.linestyle": "--",
            "grid.alpha": 0.4,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        },
    )
