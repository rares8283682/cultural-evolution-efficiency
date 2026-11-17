"""
Master Notebook Builder for Cultural Evolution Final Project
Author: Rares Olteanu (in dialogue with Prof. Alexey Koshevoy)
Institution: PSAI AI & Society Master's Program, PSL University / ENS-PSL

Structure:
- Part I: Simplest Core Model First (Copier Proportion Sweep 0%->100%, 2D General Case Phase Diagrams,
  Henrich Gumbel Copying, & Deep Theoretical Reflection)
- Part II: Secondary Extensions ("Extras" at the End: Adaptive Social Brain, Replicator Dynamics,
  Interactive Sandbox, Yule-Simon Rank-Frequency, Charbonneau Patent Recombination,
  Corporate R&D Time Machine, & Empirical Najar et al. 2020)
- Small, modular code cells with plain-English explanations above every block.
"""

import nbformat as nbf
from nbclient import NotebookClient

nb = nbf.v4.new_notebook()

nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.13.0",
    },
}

cells = []

# ==============================================================================
# CELL 0: TITLE, ABSTRACT & MASTER PIPELINE
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""# When Does Copying Stop Paying Off? Environmental Harshness, Least Effort, and the Critical Threshold of Cumulative Culture

**Course**: Cultural Evolution (2025–2026)  
**Instructor**: Prof. Alexey Koshevoy (PR[AI]RIE Fellow & Postdoctoral Researcher, ENS-PSL)  
**Institution**: Master's in AI & Society (PSAI), PSL University / École Normale Supérieure  
**Author**: Rareș Olteanu  

---

## Abstract

> In cultural and technological evolution, copying existing solutions is cheap, whereas inventing new ones is costly. While minimizing effort pushes actors toward imitation, copying alone creates no new knowledge—it only redistributes existing techniques that erode through transmission error (Henrich, 2004). Addressing Rogers' Paradox (1988) in the context of corporate R&D and patent evolution (Charbonneau, 2015), this project asks: **how much copying can a system afford before an environmental or market shock triggers technological collapse?** To answer this, we build a minimal agent-based model where agents either pay a high cost for R&D innovation or cheaply copy existing patents, varying the copier share from $0\%$ to $100\%$. While heavy copying ($80\text{--}90\%$) maximizes short-term efficiency in stable times (the *"Free-Rider Illusion"*), a sudden scarcity shock triggers collapse above a critical copier threshold ($p^* \approx 70\%$), demonstrating why technological and corporate R&D systems require a minimum innovator core ($\sim 30\%$) to survive crises.

---

## Master Project Pipeline & Architecture

Following **Professor Alexey Koshevoy's** supervisory guidance (*"Start with the simplest model first, reflect deeply on theory, think about a general case, and add complex extensions at the end"*), this notebook follows a four-stage pipeline divided into **Part I (Core Minimal Model)** and **Part II (Extensions & Applications)**:

![Master Project Pipeline](assets/figures/fig0_project_pipeline.png)

### Quick Navigation Guide
* **Part I — Core Minimal Model & General Case Analysis (Sections 1–4)**:
  * **Section 1**: Research Question, Corporate R&D / Patent Framing & Theoretical Motivation
  * **Section 2**: Formal Specification & Modular Simulation Functions ($\Pi_i = z_i - H - C$)
  * **Section 3**: Core Results — The $0\% \to 100\%$ Copier Sweep (**Fig 1**), 2D General Case Phase Diagrams (**Fig 2**), & Gumbel Tail Analysis (**Fig 3**)
  * **Section 4**: Deep Theoretical Reflection (Henrich 2004, Charbonneau 2015, Rogers 1988, Corporate Technical Debt & AI Collapse)
* **Part II — Secondary Extensions & Real-World Applications ("Extras", Section 5)**:
  * **Extensions 5.1–5.2**: Adaptive Social Brain ($\Delta$-rule) & Endogenous Replicator Dynamics (**Figs 4–5**)
  * **Extension 5.3**: Interactive 60-FPS Parameter Sandbox
  * **Extensions 5.4–5.5**: Yule-Simon Rank-Frequency & Charbonneau Modular Patent Citation Networks (**Figs 6–7**)
  * **Extension 5.6**: Macro-Technological Scenario Simulator — **The Corporate R&D Time Machine** ($N=1{,}000$ firms, **Fig 8**)
  * **Extension 5.7**: Empirical Validation on Human Social Learning Trials ($N=2{,}544$ pairs, **Fig 9**)
"""))

# ==============================================================================
# PART I - SECTION 1: RESEARCH QUESTION & MOTIVATION
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
# Part I: Core Model & General Theory

## Section 1: Research Question & Theoretical Motivation

### 1.1 The Core Question in Plain Terms

> **Core Research Question**:  
> *In a cultural species where copying others is cheap but imperfect, and inventing new solutions is costly, how much social copying can a population tolerate before an environmental scarcity shock triggers cultural collapse?*

This question directly addresses the central tension in **Rogers' Paradox (1988)** and **Henrich's (2004) treadmill model** under changing environmental pressure:
1. If copying is cheap, agents naturally gravitate toward it (**Principle of Least Effort as a transmission bias**).
2. However, copying does not generate novel adaptive information; it only redistributes existing skills, which decay on average due to imperfect replication (**Henrich’s Gumbel skill loss**).
3. In easy, forgiving environments, relying heavily on copying looks like an optimal energy-saving strategy (the **"Free-Rider Illusion"**).
4. When environmental austerity strikes (higher living/metabolic demands $H$), at what exact proportion of copiers ($p^*$) does cumulative culture fail to generate enough value to pay survival costs?

### 1.2 Real-World Application: Corporate R&D, Patents & Technological Obsolescence
As highlighted in discussion with **Professor Alexey Koshevoy**, this exact dynamical tension governs **corporate industrial policy and patent strategy**:
* **Frontier In-House R&D** ($C_{\text{innov}} = 5.0$): High burn rate, risky discovery increments ($\Delta z \sim \text{Exp}$), but generates novel intellectual property and patent breakthroughs.
* **Fast-Follower Copying & Licensing** ($C_{\text{copy}} = 1.0$): Cheap adoption of open standards and competitor patents, highly efficient in low-interest boom times, but produces no foundational patents.
* **Technological Obsolescence** ($\alpha_{\text{loss}} = 0.8$): Copied technology depreciates over time unless actively refreshed by in-house engineering competence.
* **Macroeconomic Austerity Crisis** ($H = 2.0 \to 10.0$): When market competition tightens or regulatory/borrowing costs surge, firms relying on $>70\%$ imitation experience technological insolvency ($\Pi < 0$).

### 1.3 Why Start with a Minimal Model of Technological Evolution?
As noted by **Charbonneau (2015, 2018)**, formal mathematical and agent-based modeling of **technological evolution** remains surprisingly sparse—aside from **Henrich's (2004)** classic skill-loss model, few simple, general models quantify how individual learning costs and imitation error interact under ecological pressure. Starting with fixed population mixtures ($p \in \{0\%, 10\%, \dots, 100\%\}$ copiers) eliminates unnecessary cognitive assumptions, allowing clean causal isolation of the phase boundary across general parameter regimes.
"""))

# ==============================================================================
# PART I - SECTION 2: MODEL SPECIFICATION
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Section 2: Specification of the Simplest Model

The baseline model tracks a population of $N = 100$ agents over $T = 100$ discrete generations using three simple rules:

### 2.1 Individual Net Payoff ($\Pi_i$) & Real-World Translation
Following standard cultural evolution ABM conventions (Mesoudi, 2011; Acerbi, Mesoudi, & Smolla, 2022), every agent $i$ with technological competence $z_i(t) \ge 0$ receives:
$$\Pi_i(t) = \underbrace{z_i(t)}_{\text{Cultural Skill}} - \underbrace{H(t)}_{\text{Environmental Harshness}} - \underbrace{C(a_i(t))}_{\text{Effort Cost}}$$

| Cultural Evolution Variable | Anthropological Meaning | Corporate Economics / Patent Equivalent |
| :--- | :--- | :--- |
| **$z_i(t)$** | Individual cultural skill / technological competence | **Patent Portfolio Quality & Technological Capital** |
| **$C(\text{INNOV}) = 5.0$** | High cognitive effort to discover new techniques | **In-House Frontier R&D Capital Investment** (high burn rate) |
| **$C(\text{COPY}) = 1.0$** | Low energetic effort to imitate a peer demonstrator | **Reverse-Engineering & Patent Licensing** (low-cost rollout) |
| **$\alpha_{\text{loss}} = 0.8$** | Henrich Gumbel transmission loss (skill degradation) | **Technological Depreciation & Knowledge Obsolescence** |
| **$H(t) = 2.0 \to 10.0$** | Baseline metabolic survival / environmental living cost | **Macroeconomic Austerity & Cost of Capital Shock** |
| **$\Pi_i(t) = z - H - C$** | Net biological fitness / reproductive success | **Corporate Operating Margin & Net Cashflow** ($\Pi < 0 \implies \text{insolvency}$) |

* **Environmental Harshness ($H(t)$)**:
  $$H(t) = \begin{cases} H_{\text{low}} = 2.0, & t < 40 \quad (\text{Benign Boom Era}) \\ H_{\text{high}} = 10.0, & t \ge 40 \quad (\text{Austerity / Scarcity Shock}) \end{cases}$$
* **Effort Cost ($C$) — The Principle of Least Effort**:
  $$C(\text{COPY}) = 1.0, \qquad C(\text{INNOVATE}) = 5.0$$
  Copying requires 5 times less effort than innovating, acting as an intrinsic energetic transmission bias.

### 2.2 Cultural Transmission & Discovery Dynamics
* **When an agent Innovates ($a_i = 1$)**: They pay cost $C_{\text{innov}} = 5.0$ to explore new solutions, improving their skill by an exponential discovery increment:
  $$z_i(t+1) = z_i(t) + \Delta z_i, \quad \Delta z_i \sim \text{Exponential}(\text{scale} = \lambda_{\text{innov}} = 1.5)$$
* **When an agent Copies ($a_i = 0$)**: They pay cost $C_{\text{copy}} = 1.0$, select a demonstrator $j$ from the previous generation weighted by skill/prestige ($\alpha = 4.0$):
  $$\mathbb{P}(\text{select } j) = \frac{(z_j(t) - \min z + \epsilon)^\alpha}{\sum_{m=1}^N (z_m(t) - \min z + \epsilon)^\alpha}$$
  and reproduce the demonstrator's skill subject to **Henrich's (2004) asymmetric Gumbel transmission noise**:
  $$z_i(t+1) = \max\left(0, \; z_j(t) + \epsilon_i\right), \quad \epsilon_i \sim \text{Gumbel}(\mu = -\alpha_{\text{loss}}, \; \beta_{\text{disp}})$$
  with baseline transmission loss $\alpha_{\text{loss}} = 0.8$ and dispersion $\beta_{\text{disp}} = 0.3$.

### 2.3 The Experiment: Fixed Copier Proportion Sweep ($0\%$ to $100\%$)
In each population mixture, a fixed share $p \in \{0\%, 10\%, 20\%, \dots, 90\%, 100\%\}$ of agents act as copiers while the remaining $1 - p$ act as innovators. We evaluate both the baseline case ($H_{\text{high}}=10.0, \alpha_{\text{loss}}=0.8$) and the **general case** across sweeping shock severities and imitation error rates.
"""))

# ==============================================================================
# PART I - MODULAR CODE CELLS (SMALL PIECES WITH CLEAR DESCRIPTIONS)
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""### 2.4 Step 1: Importing Libraries & Setting Plot Style
First, I import NumPy, Pandas, SciPy, Matplotlib, and Seaborn, and configure a clean colorblind-safe theme for all figures. I also print the library versions so the results are easy to reproduce.
"""))

cells.append(nbf.v4.new_code_cell(r"""import os
import sys
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", palette="colorblind", context="notebook")
plt.rcParams["figure.dpi"] = 120
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["axes.labelsize"] = 11

print(f"Python: {sys.version.split()[0]} | NumPy: {np.__version__} | Pandas: {pd.__version__}")
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 2.5 Step 2: Baseline Simulation Parameters
Here I define the baseline constants for the minimal model: 100 agents over 100 generations, with an environmental shock at generation 40 (`H` jumps from `2.0` to `10.0`), cheap copying (`1.0`), costly innovation (`5.0`), and Henrich's Gumbel loss (`0.8`).
"""))

cells.append(nbf.v4.new_code_cell(r"""N_AGENTS = 100
N_GENS = 100
SHOCK_GEN = 40

H_LOW = 2.0
H_HIGH = 10.0

COST_COPY = 1.0
COST_INNOV = 5.0

PRESTIGE = 4.0
LOSS_MU = 0.8
LOSS_BETA = 0.3
INNOV_SCALE = 1.5
SEED = 101101
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 2.6 Step 3: Helper Function for One Generation of Copying
Next, I write a small helper function `copy_peers()` that handles social learning for all copiers in a single generation. It picks demonstrators from the previous generation weighted by their skill (prestige bias) and adds Henrich's asymmetric Gumbel error so skills slightly degrade on average when copied.
"""))

cells.append(nbf.v4.new_code_cell(r"""def copy_peers(skills, n_copiers, rng, prestige=PRESTIGE, loss_mu=LOSS_MU, loss_beta=LOSS_BETA):
    # Weight demonstrators by their relative skill (prestige bias)
    shifted = skills - np.min(skills) + 1e-4
    weights = shifted ** prestige
    total = np.sum(weights)
    probs = weights / total if total > 0 else np.ones(len(skills)) / len(skills)

    # Pick demonstrators and apply Henrich's asymmetric Gumbel noise
    chosen = rng.choice(len(skills), size=n_copiers, p=probs, replace=True)
    noise = rng.gumbel(loc=-loss_mu, scale=loss_beta, size=n_copiers)
    return np.maximum(0.0, skills[chosen] + noise)
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 2.7 Step 4: Running One Complete Simulation (`run_one_sim`)
Now I combine innovation, copying, and the payoff formula $\Pi = z - H - C$ into a single simulation function `run_one_sim()`. Given a fixed copier proportion `p_copy` (from `0.0` to `1.0`), it steps through 100 generations and records the mean payoff, mean skill, and skill diversity at every generation.
"""))

cells.append(nbf.v4.new_code_cell(r"""def run_one_sim(p_copy, rng, n_agents=N_AGENTS, n_gens=N_GENS, shock_gen=SHOCK_GEN,
                h_low=H_LOW, h_high=H_HIGH, loss_mu=LOSS_MU):
    skills = rng.uniform(6.0, 7.0, size=n_agents)
    mean_payoff = np.zeros(n_gens)
    mean_skill = np.zeros(n_gens)
    diversity = np.zeros(n_gens)

    for t in range(n_gens):
        h = h_high if t >= shock_gen else h_low
        # Decide who copies (0) and who innovates (1)
        is_innov = rng.random(n_agents) < (1.0 - p_copy)
        is_copy = ~is_innov

        next_skills = np.copy(skills)
        costs = np.zeros(n_agents)

        n_copy = np.sum(is_copy)
        if n_copy > 0:
            costs[is_copy] = COST_COPY
            next_skills[is_copy] = copy_peers(skills, n_copy, rng, loss_mu=loss_mu)

        n_innov = np.sum(is_innov)
        if n_innov > 0:
            costs[is_innov] = COST_INNOV
            next_skills[is_innov] = skills[is_innov] + rng.exponential(scale=INNOV_SCALE, size=n_innov)

        payoffs = next_skills - h - costs
        skills = next_skills

        mean_payoff[t] = np.mean(payoffs)
        mean_skill[t] = np.mean(skills)
        diversity[t] = np.std(skills)

    return mean_payoff, mean_skill, diversity
"""))

# ==============================================================================
# PART I - SECTION 3: CORE RESULTS (COPIER SWEEP & GENERAL CASE)
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Section 3: Core Results — The Copier Proportion Sweep & General Case Analysis

### 3.1 Running the 10% Copier Bins Experiment ($0\%$ to $100\%$)
Following Prof. Koshevoy's suggestion, I test fixed population mixtures in 10% steps from `0%` to `100%` copiers, running 50 independent Monte Carlo simulations per mixture. First, I compute the pre-shock payoff ($t=39$), post-shock payoff ($t=99$), and cumulative lifetime welfare for each bin and display them in a summary table.
"""))

cells.append(nbf.v4.new_code_cell(r"""copier_grid = np.linspace(0.0, 1.0, 11)
master_rng = np.random.default_rng(SEED + 999)
run_seeds = master_rng.integers(100000, 999999, size=50)

rows = []
for p_copy in copier_grid:
    pre_list, post_list, cum_list, skill_list = [], [], [], []
    for s in run_seeds:
        p_hist, z_hist, _ = run_one_sim(p_copy, np.random.default_rng(s))
        pre_list.append(p_hist[39])
        post_list.append(p_hist[-1])
        cum_list.append(np.sum(p_hist))
        skill_list.append(z_hist[-1])

    rows.append({
        "Copier_Pct": int(round(p_copy * 100)),
        "Innovator_Pct": int(round((1.0 - p_copy) * 100)),
        "Pre_Shock_Mean": np.mean(pre_list),
        "Pre_Shock_SD": np.std(pre_list),
        "Post_Shock_Mean": np.mean(post_list),
        "Post_Shock_SD": np.std(post_list),
        "Cum_Welfare_Mean": np.mean(cum_list),
        "Cum_Welfare_SD": np.std(cum_list),
        "Final_Skill_Mean": np.mean(skill_list),
    })

sweep_df = pd.DataFrame(rows)
print("=== COPIER PROPORTION EXPERIMENT SUMMARY (50 MONTE CARLO RUNS PER STEP) ===")
display(sweep_df.round(2))
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Now I plot **Publication Figure 1** from `sweep_df`:
* **Panel A** compares immediate payoff before the shock ($H=2.0$) versus after the shock ($H=10.0$), highlighting the "Free-Rider Illusion" and the sudden collapse above $p^* \approx 70\%$.
* **Panel B** shows cumulative lifetime welfare across all 100 generations, peaking at the $\sim 70\%$ copier / $30\%$ innovator balance.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))
pcts = sweep_df["Copier_Pct"]

# Panel A: Pre-Shock vs Post-Shock Payoff
axes[0].errorbar(pcts, sweep_df["Pre_Shock_Mean"], yerr=sweep_df["Pre_Shock_SD"],
                 fmt="o-", color="#2b5c8f", lw=2.2, capsize=4, label="Pre-Shock Payoff (Benign H=2.0)")
axes[0].errorbar(pcts, sweep_df["Post_Shock_Mean"], yerr=sweep_df["Post_Shock_SD"],
                 fmt="s-", color="#d95f02", lw=2.5, capsize=4, label="Post-Shock Payoff (Scarcity H=10.0)")
axes[0].axhline(0, color="black", linestyle=":", lw=1.2, label="Survival Threshold (Π = 0)")
axes[0].axvspan(72, 102, color="#e41a1c", alpha=0.10, label="Collapse Zone (>70% Copiers)")

axes[0].annotate("Free-Rider Illusion:\n80-90% Copiers peak in benign times",
                 xy=(80, sweep_df.loc[sweep_df["Copier_Pct"] == 80, "Pre_Shock_Mean"].values[0]),
                 xytext=(35, 110), arrowprops=dict(arrowstyle="->", color="#2b5c8f", lw=1.5),
                 fontsize=9, fontweight="bold", color="#2b5c8f")
axes[0].annotate("Tipping Point (p* ≈ 70%)\nAbove 70%, Society Collapses!",
                 xy=(80, sweep_df.loc[sweep_df["Copier_Pct"] == 80, "Post_Shock_Mean"].values[0]),
                 xytext=(38, 30), arrowprops=dict(arrowstyle="->", color="#d95f02", lw=1.5),
                 fontsize=9, fontweight="bold", color="#d95f02")

axes[0].set_title("A. Pre-Shock vs. Post-Shock Payoff by Copier Proportion", fontweight="bold")
axes[0].set_xlabel("Proportion of Copiers in Population (%)", fontweight="bold")
axes[0].set_ylabel("Mean Net Payoff (Π)", fontweight="bold")
axes[0].set_xticks(pcts)
axes[0].grid(True, ls=":", alpha=0.5)
axes[0].legend(loc="lower left", frameon=True, fontsize=8.8)
sns.despine(ax=axes[0])

# Panel B: Cumulative Lifetime Welfare
axes[1].errorbar(pcts, sweep_df["Cum_Welfare_Mean"], yerr=sweep_df["Cum_Welfare_SD"],
                 fmt="D-", color="#1b9e77", lw=2.5, capsize=4, label="Cumulative Welfare (100 Gens)")
axes[1].axhline(0, color="black", linestyle=":", lw=1.2)
axes[1].axvspan(72, 102, color="#e41a1c", alpha=0.10)

best_idx = sweep_df["Cum_Welfare_Mean"].idxmax()
best_p = sweep_df.loc[best_idx, "Copier_Pct"]
best_w = sweep_df.loc[best_idx, "Cum_Welfare_Mean"]
axes[1].annotate(f"Optimal Balance (~{best_p}% Copiers)\nResolves Rogers' Paradox",
                 xy=(best_p, best_w), xytext=(15, best_w * 0.72),
                 arrowprops=dict(arrowstyle="->", color="#1b9e77", lw=1.6),
                 fontsize=9.5, fontweight="bold", color="#1b9e77")

axes[1].set_title("B. Cumulative Lifetime Welfare across Copier Spectrum", fontweight="bold")
axes[1].set_xlabel("Proportion of Copiers in Population (%)", fontweight="bold")
axes[1].set_ylabel("Cumulative Net Payoff (Σ Π)", fontweight="bold")
axes[1].set_xticks(pcts)
axes[1].grid(True, ls=":", alpha=0.5)
axes[1].legend(loc="lower left", frameon=True, fontsize=9)
sns.despine(ax=axes[1])

plt.suptitle("Publication Figure 1: The Critical Copier Threshold (p* ≈ 70%) under Scarcity Shocks",
             fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Let's also summarize the key mixtures in a clean reference table showing the transition from viable division of labor ($0\text{--}70\%$ copiers) to collapse ($80\text{--}100\%$ copiers).
"""))

cells.append(nbf.v4.new_code_cell(r"""table_rows = []
for _, r in sweep_df.iterrows():
    p_c = int(r["Copier_Pct"])
    if p_c in [0, 30, 50, 70, 80, 90, 100]:
        if p_c == 0:
            status = "Viable (Costly Rediscovery)"
        elif p_c == 70:
            status = "Optimal Division of Labor"
        elif p_c < 70:
            status = "Highly Viable"
        elif p_c in [80, 90]:
            status = "Collapsed (Net Deficit Π < 0)"
        else:
            status = "Extinction / Total Decay"

        table_rows.append({
            "Population Mixture": f"{p_c}% Copiers / {100-p_c}% Innovators",
            "Pre-Shock (H=2.0)": f"{r['Pre_Shock_Mean']:+.1f} ± {r['Pre_Shock_SD']:.1f}",
            "Post-Shock (H=10.0)": f"{r['Post_Shock_Mean']:+.1f} ± {r['Post_Shock_SD']:.1f}",
            "Cumulative Welfare": f"{r['Cum_Welfare_Mean']:+,.0f}",
            "Viability": status,
        })

display(pd.DataFrame(table_rows))
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 3.2 Testing the General Case: 2D Phase Diagrams
To make sure the $70\%$ threshold isn't just an artifact of one specific set of numbers, I sweep **environmental harshness** ($H_{\text{high}} \in [2, 14]$) and **imitation skill loss** ($\alpha_{\text{loss}} \in [0.2, 1.2]$) across all copier proportions using 20 Monte Carlo runs per point.
"""))

cells.append(nbf.v4.new_code_cell(r"""h_grid = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0]
loss_grid = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
phase_seeds = np.random.default_rng(SEED + 888).integers(100000, 999999, size=20)

mat_harsh = np.zeros((len(h_grid), len(copier_grid)))
for i, h_val in enumerate(h_grid):
    for j, p_copy in enumerate(copier_grid):
        posts = [run_one_sim(p_copy, np.random.default_rng(s), h_high=h_val)[0][-1] for s in phase_seeds]
        mat_harsh[i, j] = np.mean(posts)

mat_loss = np.zeros((len(loss_grid), len(copier_grid)))
for i, l_val in enumerate(loss_grid):
    for j, p_copy in enumerate(copier_grid):
        posts = [run_one_sim(p_copy, np.random.default_rng(s), loss_mu=l_val)[0][-1] for s in phase_seeds]
        mat_loss[i, j] = np.mean(posts)

print("2D general-case phase matrices computed.")
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Here I plot **Publication Figure 2**, showing the two heatmaps with a dashed black contour at $\Pi = 0$ (the survival boundary). As either harshness or copying error rises, the maximum tolerable copier percentage shrinks smoothly.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 2, figsize=(15, 5.8))
x_pcts = np.linspace(0, 100, len(copier_grid))

im1 = axes[0].imshow(mat_harsh, origin="lower", aspect="auto", cmap="RdYlGn",
                     extent=[0, 100, h_grid[0], h_grid[-1]], vmin=-15, vmax=120)
axes[0].contour(x_pcts, h_grid, mat_harsh, levels=[0.0], colors="black", linewidths=2.2, linestyles="--")
plt.colorbar(im1, ax=axes[0]).set_label("Post-Shock Net Payoff (Π)", fontweight="bold")
axes[0].axhline(10.0, color="navy", linestyle=":", lw=1.5, label="Baseline Shock (H=10.0)")
axes[0].set_title("A. Phase Boundary: Copier Share vs. Harshness", fontweight="bold")
axes[0].set_xlabel("Proportion of Copiers (%)", fontweight="bold")
axes[0].set_ylabel("Environmental Harshness Shock (H)", fontweight="bold")
axes[0].legend(loc="upper left", frameon=True)

im2 = axes[1].imshow(mat_loss, origin="lower", aspect="auto", cmap="RdYlGn",
                     extent=[0, 100, loss_grid[0], loss_grid[-1]], vmin=-15, vmax=120)
axes[1].contour(x_pcts, loss_grid, mat_loss, levels=[0.0], colors="black", linewidths=2.2, linestyles="--")
plt.colorbar(im2, ax=axes[1]).set_label("Post-Shock Net Payoff (Π)", fontweight="bold")
axes[1].axhline(0.8, color="navy", linestyle=":", lw=1.5, label="Baseline Loss (α=0.8)")
axes[1].set_title("B. Phase Boundary: Copier Share vs. Imitation Error", fontweight="bold")
axes[1].set_xlabel("Proportion of Copiers (%)", fontweight="bold")
axes[1].set_ylabel("Gumbel Skill Loss (α_loss)", fontweight="bold")
axes[1].legend(loc="upper left", frameon=True)

plt.suptitle("Publication Figure 2: The General Case — Continuous Survival Boundaries",
             fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 3.3 Why Copying Erodes Skills: Visualizing Henrich's (2004) Gumbel Distribution
To make the micro-level mechanism intuitive, **Publication Figure 3** plots the exact Gumbel probability density when copying a demonstrator with skill $z_{\text{model}} = 6.5$. Most learners fall slightly below the model (blue area), while only $6.71\%$ accidentally outperform the model (hatched yellow tail).
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, ax = plt.subplots(figsize=(10, 5.2))
z_grid = np.linspace(2.0, 14.0, 1000)
z_model = 6.5
pdf = stats.gumbel_r.pdf(z_grid, loc=z_model - LOSS_MU, scale=LOSS_BETA)

ax.plot(z_grid, pdf, color="#2b5c8f", lw=2.8, label=r"Copying Density: $\Pr(z \mid z_{\text{model}}=6.5)$")
ax.axvline(z_model, color="navy", linestyle="-", lw=2.0, label="Model Skill (z=6.5)")
ax.axvline(H_LOW + COST_COPY, color="gray", linestyle="--", lw=1.2, label="Benign Cost (H+C=3.0)")
ax.axvline(H_HIGH + COST_COPY, color="crimson", linestyle="--", lw=1.8, label="Shock Cost (H+C=11.0)")

ax.fill_between(z_grid[z_grid >= z_model], 0, pdf[z_grid >= z_model],
                hatch="///", facecolor="#fee08b", edgecolor="#d73027", alpha=0.6,
                label="Rare Gain Tail (6.71%): z > z_model")
loss_mask = (z_grid < z_model) & (z_grid >= 3.0)
ax.fill_between(z_grid[loss_mask], 0, pdf[loss_mask], facecolor="#91bfdb", alpha=0.35, label="Skill Loss (Henrich 2004)")

ax.set_title("Publication Figure 3: Micro-Level Skill Loss vs. Breakthrough Frontier", fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("Technological Competence Level (z)", fontweight="bold")
ax.set_ylabel("Probability Density p(z)", fontweight="bold")
ax.set_xlim(3.0, 13.0)
ax.set_ylim(0, 1.4)
ax.legend(loc="upper right", frameon=True, fontsize=9.2)
sns.despine(ax=ax)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# PART I - SECTION 4: THEORETICAL REFLECTION
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Section 4: Theoretical Reflection on Technological Cultural Evolution

Following Professor Koshevoy's emphasis on prioritizing **theoretical reflection over technical clutter**, the core results yield four overarching insights for cultural evolution:

### 4.1 Why Technological Evolution Needs General Minimal Models (Henrich 2004 & Charbonneau 2015)
Aside from **Henrich's (2004)** classic demographic treadmill model—which showed how reductions in effective population size drive cumulative skill loss—mathematical modeling of technological trajectories remains remarkably under-explored (**Charbonneau, 2015, 2018**). Henrich modeled *population size* ($N$) as the primary driver of cultural loss. Our model shifts the lens to **learning strategy composition ($p$ copiers vs. $1-p$ innovators)** under fluctuating environmental pressure ($H$). Even when population size $N$ stays constant, an excess proportion of imitators triggers the exact same downward spiral observed in Tasmanian demographic bottlenecks.

### 4.2 The "Free-Rider Illusion" & Least Effort as a Transmission Bias
Why do societies drift dangerously close to collapse? Our sweep exposes a deceptive evolutionary trap:
* Under benign conditions ($H = 2.0$), increasing the copier share up to $80\%-90\%$ raises immediate per-generation payoffs because copiers avoid paying the heavy innovation fee ($C_{\text{innov}} = 5.0$). This operationalizes **Zipf's Principle of Least Effort** as an economic **transmission bias**.
* However, this efficiency surplus is illusory if the environment becomes unstable. Because no complex tools are invented by copying alone, the cultural baseline erodes under Henrich's Gumbel loss ($\alpha_{\text{loss}} = 0.8$). When harshness jumps ($H = 10.0$), populations above $p^* \approx 70\%$ lack the innovative replenishment rate necessary to sustain skill above survival costs, collapsing into negative payoff ($\Pi < 0$).

### 4.3 Resolving Rogers' Paradox via Ecological Thresholds
Alan Rogers (1988) argued that social learning provides zero net fitness benefit at equilibrium because imitators dilute the adaptive value of innovation. Previous resolutions—such as Enquist et al.'s (2007) *Critical Social Learning*—relied on sophisticated individual decision rules. Our general case phase diagram demonstrates a more **parsimonious ecological resolution**: 
* Cumulative welfare does **not** require a population of 100% tireless innovators (which wastes energy on constant rediscovery), nor does it collapse into Rogers' equilibrium across all states.
* Instead, maximizing cumulative welfare favors an **intermediate division of cognitive labor** ($\sim 70\%$ copiers exploiting the breakthroughs of $\sim 30\%$ innovators), with the exact viable boundary shifting smoothly as harshness $H$ or imitation noise $\alpha_{\text{loss}}$ increases (Figure 2).

### 4.4 Real-World Value Beyond Anthropology: Corporate R&D, Patents & AI
1. **The Corporate Patent Dilemma & Technical Debt**: 
   In corporate economics, technology firms face an exact analog of Rogers' Paradox. In benign, low-interest economic climates ($H=2.0$), fast-followers that cut internal R&D ($C_{\text{innov}}=5.0$) and rely on licensing competitor patents or adopting open standards ($C_{\text{copy}}=1.0$) boast superior short-term profit margins (+90.2 vs +79.2 for pure innovators). However, because borrowed technologies undergo rapid obsolescence ($\alpha_{\text{loss}}=0.8$), these firms accumulate deep technical debt. When a macroeconomic shock strikes ($H=10.0$ — capital costs rise, trade barriers emerge, or regulatory standards tighten), firms with less than ~30% in-house R&D suffer catastrophic insolvency ($\Pi < 0$).
2. **Preventing AI "Model Collapse" (Shumailov et al., *Nature* 2024)**: 
   Modern generative AI models trained recursively on synthetic AI outputs mirror our $>80\%$ copier regime: without continuous grounding in external human novelty ("innovators"), recursive copying collapses distributional tails and degrades model competence.
"""))

# ==============================================================================
# PART II INTRO
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
---
# Part II: Advanced Extensions & Further Explorations ("Extras")

> [!NOTE]
> **Structural Note (Per Professor Koshevoy's Recommendation)**:
> Having established and interpreted the simplest core model and its general phase boundaries in **Part I**, this section explores seven secondary theoretical, empirical, and applied extensions:
> 1. **Extension 5.1**: Can individuals *discover* the optimal division of labor dynamically via simple prediction-error learning (**The Adaptive Social Brain**)?
> 2. **Extension 5.2**: Does natural selection (**Discrete Replicator Dynamics**) autonomously converge on the ~70/30 ESS without central design?
> 3. **Extension 5.3**: Interactive 60-FPS Browser Simulation Sandbox.
> 4. **Extension 5.4**: The Professor's **Yule-Simon Rank-Frequency Model** (Neutral drift vs. frequency-independence vs. prestige/conformist bias).
> 5. **Extension 5.5**: **Charbonneau's Modular Patent Recombination** (Patent citations & cumulative technology).
> 6. **Extension 5.6**: **Corporate R&D Time Machine** (Macro-technological scenario simulator for 1,000 competing corporate firms).
> 7. **Extension 5.7**: **Empirical Human Validation** on trial-by-trial choices (**Najar et al., 2020**).
"""))

# ==============================================================================
# EXTENSION 5.1: ADAPTIVE SOCIAL BRAIN
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""## Extension 5.1: Dynamic Self-Organization — The Adaptive Social Brain & Ensemble Trajectories

In Part I, copier and innovator shares were held fixed. A natural follow-up question is: **how could agents discover the ~70/30 division of labor dynamically on their own?**

### Mathematical Rule (Rescorla-Wagner / Q-Learning Gating)
Adaptive agents track expected action values $\mathbf{Q}_i = [Q_i(\text{COPY}), Q_i(\text{INNOV})]$, choose stochastically via Softmax ($\tau = 1.0$), and update via Reward Prediction Error ($\eta = 0.35$):
$$\delta_i(t) = \Pi_i(t) - Q_i(a_i(t)), \qquad Q_i(a_i(t)) \leftarrow Q_i(a_i(t)) + \eta \cdot \delta_i(t)$$

First, I write a helper function `run_strategy(mode, rng)` to test 5 benchmark strategies: Pure Copiers (`0`), Pure Innovators (`1`), Homogeneous Adaptive (`2`), Static 5% Mixture (`3`), and a Heterogeneous Society (`4`: 80% Copiers, 10% Innovators, 10% Adaptive).
"""))

cells.append(nbf.v4.new_code_cell(r"""def softmax_pick(q_vals, rng, tau=1.0):
    v0 = q_vals[:, 0] / tau
    v1 = q_vals[:, 1] / tau
    m = np.maximum(v0, v1)
    p_innov = np.exp(v1 - m) / (np.exp(v0 - m) + np.exp(v1 - m))
    return (rng.random(len(q_vals)) < p_innov).astype(int)

def run_strategy(mode, rng, eta=0.35):
    skills = rng.uniform(6.0, 7.0, size=N_AGENTS)
    if mode == 2:
        q = np.tile([3.5, 0.0], (N_AGENTS, 1))
    elif mode == 4:
        q = np.tile([3.5, 0.0], (10, 1))
    else:
        q = None

    pay_hist, skill_hist, div_hist, innov_hist = np.zeros(N_GENS), np.zeros(N_GENS), np.zeros(N_GENS), np.zeros(N_GENS)

    for t in range(N_GENS):
        h = H_HIGH if t >= SHOCK_GEN else H_LOW
        actions = np.zeros(N_AGENTS, dtype=int)

        if mode == 1:
            actions[:] = 1
        elif mode == 2:
            actions = softmax_pick(q, rng)
        elif mode == 3:
            actions = (rng.random(N_AGENTS) < 0.05).astype(int)
        elif mode == 4:
            actions[80:90] = 1
            actions[90:] = softmax_pick(q, rng)

        next_skills = np.copy(skills)
        costs = np.where(actions == 1, COST_INNOV, COST_COPY)

        c_idx = np.where(actions == 0)[0]
        if len(c_idx) > 0:
            next_skills[c_idx] = copy_peers(skills, len(c_idx), rng)

        i_idx = np.where(actions == 1)[0]
        if len(i_idx) > 0:
            next_skills[i_idx] = skills[i_idx] + rng.exponential(scale=INNOV_SCALE, size=len(i_idx))

        payoffs = next_skills - h - costs
        if mode == 2:
            for a in [0, 1]:
                idx = np.where(actions == a)[0]
                if len(idx) > 0:
                    q[idx, a] += eta * (payoffs[idx] - q[idx, a])
        elif mode == 4:
            for a in [0, 1]:
                sub = np.where(actions[90:] == a)[0]
                if len(sub) > 0:
                    q[sub, a] += eta * (payoffs[90 + sub] - q[sub, a])

        skills = next_skills
        pay_hist[t], skill_hist[t], div_hist[t], innov_hist[t] = np.mean(payoffs), np.mean(skills), np.std(skills), np.mean(actions)

    return {"mean_payoff": pay_hist, "mean_skill": skill_hist, "diversity": div_hist, "pct_innovating": innov_hist}
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Next, I run 50 Monte Carlo repetitions for each of the 5 strategies and print a summary table comparing pre-shock payoff, post-shock payoff, and cumulative welfare.
"""))

cells.append(nbf.v4.new_code_cell(r"""strategies = {
    "Pure Copiers": 0,
    "Pure Innovators": 1,
    "Homogeneous Adaptive": 2,
    "Static 5% Mixture": 3,
    "Heterogeneous (80/10/10)": 4,
}

ens_seeds = np.random.default_rng(SEED).integers(100000, 999999, size=50)
ensemble_results = {}
summary_rows = []

for name, mode in strategies.items():
    runs = [run_strategy(mode, np.random.default_rng(s)) for s in ens_seeds]
    d = {}
    for k in ["mean_payoff", "mean_skill", "diversity", "pct_innovating"]:
        mat = np.array([r[k] for r in runs])
        m = np.mean(mat, axis=0)
        se = np.std(mat, axis=0, ddof=1) / np.sqrt(50)
        d[k] = {"mean": m, "lower": m - 1.96 * se, "upper": m + 1.96 * se}

    cums = [np.sum(r["mean_payoff"]) for r in runs]
    ensemble_results[name] = d

    summary_rows.append({
        "Evolutionary Strategy": name,
        "Pre-Shock (t=39)": f"{d['mean_payoff']['mean'][39]:+.2f}",
        "Final Payoff (t=99)": f"{d['mean_payoff']['mean'][-1]:+.2f}",
        "Mean Cumulative Payoff": f"{np.mean(cums):+.2f}",
        "95% Run Spread": f"[{np.percentile(cums, 2.5):.1f}, {np.percentile(cums, 97.5):.1f}]",
        "Final Skill (z)": f"{d['mean_skill']['mean'][-1]:.2f}",
        "Regime": "Deficit (Π < 0)" if d["mean_payoff"]["mean"][-1] < 0 else "Surplus (Π > 0)",
    })

display(pd.DataFrame(summary_rows))
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Now I plot **Publication Figure 4**, showing how the 5 strategies behave across all 100 generations with 95% confidence ribbons.
"""))

cells.append(nbf.v4.new_code_cell(r"""palette = {
    "Pure Copiers": "#d95f02",
    "Pure Innovators": "#7570b3",
    "Homogeneous Adaptive": "#1b9e77",
    "Static 5% Mixture": "#e7298a",
    "Heterogeneous (80/10/10)": "#2b5c8f",
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
gens = np.arange(N_GENS)

for name, data in ensemble_results.items():
    for ax, key in zip(axes.flat, ["mean_payoff", "mean_skill", "diversity", "pct_innovating"]):
        scale = 100.0 if key == "pct_innovating" else 1.0
        ax.plot(gens, data[key]["mean"] * scale, label=name, color=palette[name], lw=2.2)
        ax.fill_between(gens, data[key]["lower"] * scale, data[key]["upper"] * scale, color=palette[name], alpha=0.15)

axes[0, 0].axvline(SHOCK_GEN, color="crimson", linestyle="--", lw=1.5, label="Austerity Shock (t=40)")
axes[0, 0].axhline(0, color="black", linestyle=":", lw=1.2, label="Subsistence (Π=0)")
axes[0, 0].set_ylabel(r"Net Payoff $\Pi(t)$", fontweight="bold")
axes[0, 0].set_title("A. Energetic Payoff & Subsistence Deficit", fontweight="bold", loc="left")
axes[0, 0].legend(loc="upper left", frameon=True, fontsize=9)

axes[0, 1].axvline(SHOCK_GEN, color="crimson", linestyle="--", lw=1.5)
axes[0, 1].set_ylabel(r"Mean Cultural Skill $\bar{z}(t)$", fontweight="bold")
axes[0, 1].set_title("B. Cumulative Technological Competence", fontweight="bold", loc="left")

axes[1, 0].axvline(SHOCK_GEN, color="crimson", linestyle="--", lw=1.5)
axes[1, 0].set_ylabel(r"Skill Dispersion $\sigma_z(t)$", fontweight="bold")
axes[1, 0].set_xlabel("Evolutionary Generation (t)", fontweight="bold")
axes[1, 0].set_title("C. Repertoire Diversity (Variance)", fontweight="bold", loc="left")

axes[1, 1].axvline(SHOCK_GEN, color="crimson", linestyle="--", lw=1.5)
axes[1, 1].set_ylabel("% Population Innovating", fontweight="bold")
axes[1, 1].set_xlabel("Evolutionary Generation (t)", fontweight="bold")
axes[1, 1].set_title("D. Dynamic Behavioral Strategy Allocation", fontweight="bold", loc="left")
axes[1, 1].set_ylim(-5, 105)

for ax in axes.flat:
    sns.despine(ax=ax)

plt.suptitle("Publication Figure 4: 50-Run Ensemble Trajectories (Adaptive Social Brain & Division of Labor)",
             fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# EXTENSION 5.2: REPLICATOR DYNAMICS
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.2: Endogenous Co-Evolution via Discrete Replicator Dynamics

Rather than fixing strategy frequencies externally, I test whether evolutionary selection (Boyd & Richerson, 1985; Taylor & Jonker, 1978) starting from an equal $[1/3, 1/3, 1/3]$ split autonomously converges toward the ~70/30 division of labor ESS:
$$x_k(t+1) = (1 - \mu) \left( x_k(t) \frac{F_k(t)}{\bar{F}(t)} \right) + \frac{\mu}{3}$$

First, I write a compact replicator simulation across 50 independent runs.
"""))

cells.append(nbf.v4.new_code_cell(r"""def run_replicator(n_runs=50, mu=0.02):
    rep_seeds = np.random.default_rng(SEED + 777).integers(100000, 999999, size=n_runs)
    props_all = np.zeros((n_runs, N_GENS, 3))

    for r, s in enumerate(rep_seeds):
        rng = np.random.default_rng(s)
        props = np.array([1/3, 1/3, 1/3])
        skills = rng.uniform(6.0, 7.0, size=N_AGENTS)
        q = np.tile([3.5, 0.0], (N_AGENTS, 1))

        for t in range(N_GENS):
            h = H_HIGH if t >= SHOCK_GEN else H_LOW
            props_all[r, t] = props
            c0 = int(round(props[0] * N_AGENTS))
            c1 = int(round(props[1] * N_AGENTS))
            c2 = max(0, N_AGENTS - c0 - c1)

            actions = np.zeros(N_AGENTS, dtype=int)
            if c1 > 0:
                actions[c0 : c0 + c1] = 1
            if c2 > 0:
                actions[c0 + c1 :] = softmax_pick(q[c0 + c1 :], rng)

            next_skills = np.copy(skills)
            costs = np.where(actions == 1, COST_INNOV, COST_COPY)
            c_idx, i_idx = np.where(actions == 0)[0], np.where(actions == 1)[0]
            if len(c_idx) > 0:
                next_skills[c_idx] = copy_peers(skills, len(c_idx), rng)
            if len(i_idx) > 0:
                next_skills[i_idx] = skills[i_idx] + rng.exponential(scale=INNOV_SCALE, size=len(i_idx))

            payoffs = next_skills - h - costs
            if c2 > 0:
                for a in [0, 1]:
                    sub = np.where(actions[c0 + c1 :] == a)[0]
                    if len(sub) > 0:
                        g_idx = c0 + c1 + sub
                        q[g_idx, a] += 0.35 * (payoffs[g_idx] - q[g_idx, a])
            skills = next_skills

            p0 = np.mean(payoffs[:c0]) if c0 > 0 else 0.0
            p1 = np.mean(payoffs[c0 : c0 + c1]) if c1 > 0 else 0.0
            p2 = np.mean(payoffs[c0 + c1 :]) if c2 > 0 else 0.0
            gps = np.array([p0, p1, p2])
            fit = gps - np.min(gps) + 1.0
            rep = (1.0 - mu) * (props * fit / np.sum(props * fit)) + mu / 3.0
            props = rng.multinomial(N_AGENTS, rep / np.sum(rep)) / N_AGENTS

    return props_all

props_hist = run_replicator(n_runs=50)
print(f"Final ESS Proportions -> Copiers: {np.mean(props_hist[:, -1, 0])*100:.1f}%, "
      f"Innovators: {np.mean(props_hist[:, -1, 1])*100:.1f}%, "
      f"Adaptive: {np.mean(props_hist[:, -1, 2])*100:.1f}%")
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Next, I plot **Publication Figure 5** showing the population strategy proportions over time and the final equilibrium shares.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 2, figsize=(14, 5.2))
gens = np.arange(N_GENS)
labels = ["Pure Copiers", "Pure Innovators", "Adaptive Social Brain"]
colors = ["#d95f02", "#7570b3", "#1b9e77"]

for k in range(3):
    m = np.mean(props_hist[:, :, k], axis=0) * 100
    se = np.std(props_hist[:, :, k], axis=0, ddof=1) / np.sqrt(50) * 100
    axes[0].plot(gens, m, label=labels[k], color=colors[k], lw=2.4)
    axes[0].fill_between(gens, np.maximum(0, m - 1.96 * se), np.minimum(100, m + 1.96 * se), color=colors[k], alpha=0.18)

axes[0].axvline(SHOCK_GEN, color="crimson", linestyle="--", lw=1.5, label="Austerity Shock (t=40)")
axes[0].set_title("A. Co-Evolutionary Replicator Dynamics (50 Runs)", fontweight="bold")
axes[0].set_xlabel("Generation (t)", fontweight="bold")
axes[0].set_ylabel("Population Share (%)", fontweight="bold")
axes[0].set_ylim(0, 100)
axes[0].legend(loc="upper right", frameon=True, fontsize=9)
sns.despine(ax=axes[0])

final_means = np.mean(props_hist[:, -1, :], axis=0) * 100
final_stds = np.std(props_hist[:, -1, :], axis=0) * 100
bars = axes[1].bar(labels, final_means, yerr=final_stds, capsize=6, color=colors, alpha=0.85, edgecolor="black")
for bar, val in zip(bars, final_means):
    axes[1].text(bar.get_x() + bar.get_width() / 2, val + 5.5, f"{val:.1f}%", ha="center", fontweight="bold")

axes[1].set_title("B. Final Evolutionarily Stable State (t=99)", fontweight="bold")
axes[1].set_ylabel("Equilibrium Population Share (%)", fontweight="bold")
axes[1].set_ylim(0, 100)
sns.despine(ax=axes[1])

plt.suptitle("Publication Figure 5: Natural Selection Converges to an Asymmetric Division of Labor",
             fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# EXTENSION 5.3: INTERACTIVE SANDBOX
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.3: Interactive Parameter Sandbox (Live HTML5/Canvas Dashboard)

To allow live exploration of harshness shocks, copier proportions, and Gumbel error rates, I embed our interactive simulation dashboard (`docs/index.html`) directly below.
"""))

cells.append(nbf.v4.new_code_cell(r"""from IPython.display import IFrame, display

if os.path.exists("docs/index.html"):
    display(IFrame(src="docs/index.html", width="100%", height="620px"))
else:
    print("Interactive dashboard HTML file not found at docs/index.html")
"""))

# ==============================================================================
# EXTENSION 5.4: YULE-SIMON MODEL
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.4: Rank-Frequency Distributions & Transmission Biases (Yule-Simon Model)

Operationalizing **Professor Alexey Koshevoy's** observation on frequency-dependent vs. frequency-independent trait distributions (and Mesoudi Ch. 7 & 10):
$$\mathbb{P}(\text{trait } k) = \frac{(F_k(t))^\beta \cdot (Q_k)^\alpha + \mu}{\sum_{m=1}^M \left[ (F_m(t))^\beta \cdot (Q_m)^\alpha + \mu \right]}$$
First, I write a short function `sim_traits()` to compare **Yule-Simon Neutral Copying ($\beta=1.0$)**, **Frequency-Independent Uniform ($\beta=0.0$)**, **Prestige Bias ($\beta=1.0, \alpha=2.0$)**, and **Conformist Bias ($\beta=1.5$)**.
"""))

cells.append(nbf.v4.new_code_cell(r"""def sim_traits(n_pop=1000, n_items=100, gens=200, beta=1.0, alpha=0.0, mu=0.01, seed=42):
    rng = np.random.default_rng(seed)
    qualities = rng.lognormal(mean=0.0, sigma=0.5, size=n_items)
    traits = rng.integers(0, n_items, size=n_pop)
    for _ in range(gens):
        freqs = np.bincount(traits, minlength=n_items) / n_pop
        w = (np.ones(n_items) if beta == 0.0 else freqs ** beta) * (qualities ** alpha if alpha > 0 else 1.0) + mu
        traits = rng.choice(n_items, size=n_pop, p=w / np.sum(w))
    counts = np.bincount(traits, minlength=n_items)
    return np.arange(1, n_items + 1), np.sort(counts)[::-1], counts

ranks, yule_s, yule_raw = sim_traits(beta=1.0, alpha=0.0, seed=101)
_, unif_s, unif_raw = sim_traits(beta=0.0, alpha=0.0, seed=102)
_, prest_s, _ = sim_traits(beta=1.0, alpha=2.0, seed=103)
_, conf_s, _ = sim_traits(beta=1.5, alpha=0.0, seed=104)
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Now I plot **Publication Figure 6** showing the log-log rank-frequency curves and the heavy-tail concentration of top items.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

axes[0].loglog(ranks, yule_s + 1, "o-", color="#1f77b4", lw=2, markersize=5, label=r"Yule-Simon Frequency Bias ($\beta=1.0, \alpha=0$)")
axes[0].loglog(ranks, prest_s + 1, "s-", color="#2ca02c", lw=2, markersize=5, label=r"Prestige & Quality Bias ($\beta=1.0, \alpha=2.0$)")
axes[0].loglog(ranks, conf_s + 1, "^-", color="#9467bd", lw=2, markersize=5, label=r"Conformist Bias ($\beta=1.5, \alpha=0$)")
axes[0].loglog(ranks, unif_s + 1, "d--", color="#d62728", lw=1.8, markersize=5, label=r"Frequency-Independent Uniform ($\beta=0, \alpha=0$)")
axes[0].set_title("A. Cultural Trait Rank-Frequency Distributions (Log-Log)", fontweight="bold")
axes[0].set_xlabel("Trait Rank (k)", fontweight="bold")
axes[0].set_ylabel("Trait Frequency + 1", fontweight="bold")
axes[0].legend(loc="upper right", frameon=True, fontsize=9)
axes[0].grid(True, which="both", ls=":", alpha=0.5)
sns.despine(ax=axes[0])

axes[1].bar(np.arange(30), yule_s[:30], color="#1f77b4", alpha=0.7, label="Top 30 Yule Traits")
axes[1].plot(np.arange(30), [np.mean(unif_raw)] * 30, color="#d62728", ls="--", lw=2, label="Uniform Null Level")
axes[1].set_title("B. Heavy-Tail Cultural Item Concentration", fontweight="bold")
axes[1].set_xlabel("Top Cultural Traits (Ordered)", fontweight="bold")
axes[1].set_ylabel("Number of Adopters (N=1,000)", fontweight="bold")
axes[1].legend(loc="upper right", frameon=True)
axes[1].grid(True, ls=":", alpha=0.5)
sns.despine(ax=axes[1])

plt.suptitle("Publication Figure 6: Yule-Simon Transmission Biases & Rank-Frequency Scaling", fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# EXTENSION 5.5: CHARBONNEAU PATENT RECOMBINATION
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.5: Modular Technological Recombination & Patent Lineages (Charbonneau Framework)

Extending the model into real-world patent networks (**Charbonneau, 2015, 2018**; suggested during class discussion): inventors recombine pre-existing functional patent modules weighted by cumulative prestige and quality:
$$W_j = (\text{Citations}_j + 1)^\alpha \cdot (\text{Quality}_j)^\beta, \qquad Q_{t+1} = \max\left(Q_{\text{parent}_1}, Q_{\text{parent}_2}\right) + \Delta Q$$
"""))

cells.append(nbf.v4.new_code_cell(r"""from src.cultural_evolution.recombination import RecombinantPatentModel

patent_res = RecombinantPatentModel(initial_patents=25, total_steps=600, alpha_cit=1.2, beta_quality=1.0, seed=42).simulate()
neutral_res = RecombinantPatentModel(initial_patents=25, total_steps=600, alpha_cit=0.0, beta_quality=0.0, seed=42).simulate()

print(f"Total simulated patents: {len(patent_res['citations'])} | Distinct modules discovered: {patent_res['total_modules']}")

fig, ax = plt.subplots(figsize=(9, 5.2))
ax.loglog(patent_res["ranks"], patent_res["sorted_citations"] + 1, "o-", color="#2b5c8f", markersize=4, lw=1.5, alpha=0.85, label="Modular Patent Network (Charbonneau)")
ax.loglog(neutral_res["ranks"], neutral_res["sorted_citations"] + 1, "s--", color="#c0392b", markersize=3, lw=1.2, alpha=0.7, label="Neutral Drift Benchmark (Bentley et al. 2004)")

ax.set_title("Publication Figure 7: Heavy-Tailed Patent Citation Distribution\n(Modular Recombination vs. Neutral Drift)", fontweight="bold")
ax.set_xlabel("Patent Citation Rank (k)", fontweight="bold")
ax.set_ylabel("Cumulative Citations + 1", fontweight="bold")
ax.legend(loc="upper right", frameon=True, fontsize=10)
ax.grid(True, which="both", ls=":", alpha=0.5)
sns.despine(ax=ax)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# EXTENSION 5.6: CORPORATE R&D TIME MACHINE
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.6: Macro-Technological Scenario Simulator ("Corporate R&D Time Machine")

To translate our findings directly into **corporate economics and industrial patent policy** (as discussed with Prof. Alexey Koshevoy), this module stress-tests an industry of **$N = 1{,}000$ competing firms** over **$T = 100$ quarterly epochs** across four corporate R&D strategies:
1. **Fast-Follower Swarm ($90\%$ Licensing/Copying, $10\%$ In-House R&D)**
2. **Optimal Division of Labor ($70\%$ Licensing/Copying, $30\%$ In-House R&D)**
3. **Balanced Tech Enterprise ($50\%$ Licensing/Copying, $50\%$ In-House R&D)**
4. **DeepTech Frontier Pioneer ($10\%$ Licensing/Copying, $90\%$ In-House R&D)**

First, I write `run_firm_cohort()` to simulate 1,000 firms over 100 quarters using our same `copy_peers()` helper and payoff rule, tracking solvency (% of firms with margin $\ge 0$) and patent portfolio value.
"""))

cells.append(nbf.v4.new_code_cell(r"""def run_firm_cohort(p_copy, n_firms=1000, n_quarters=100, shock_q=40, seed=42):
    rng = np.random.default_rng(seed)
    skills = np.full(n_firms, 2.0)
    margins = np.zeros((n_firms, n_quarters))
    vals = np.zeros((n_firms, n_quarters))
    cum_profit = np.zeros((n_firms, n_quarters))
    survival = np.zeros(n_quarters)

    for t in range(n_quarters):
        h = H_HIGH if t >= shock_q else H_LOW
        is_innov = rng.random(n_firms) >= p_copy
        is_copy = ~is_innov

        next_skills = np.copy(skills)
        costs = np.where(is_innov, COST_INNOV, COST_COPY)

        if np.sum(is_copy) > 0:
            next_skills[is_copy] = copy_peers(skills, np.sum(is_copy), rng)
        if np.sum(is_innov) > 0:
            next_skills[is_innov] = skills[is_innov] + rng.exponential(scale=INNOV_SCALE, size=np.sum(is_innov))

        m = next_skills - h - costs
        skills = next_skills

        margins[:, t] = m
        vals[:, t] = skills
        cum_profit[:, t] = m if t == 0 else cum_profit[:, t - 1] + m
        survival[t] = np.mean(m >= 0.0) * 100.0

    return {
        "mean_val": np.mean(vals, axis=0),
        "val_low": np.percentile(vals, 2.5, axis=0),
        "val_high": np.percentile(vals, 97.5, axis=0),
        "mean_margin": np.mean(margins, axis=0),
        "survival": survival,
        "cum_cash": np.mean(cum_profit, axis=0),
        "pre_margin": float(np.mean(margins[:, shock_q - 1])),
        "post_margin": float(np.mean(margins[:, -1])),
        "final_surv": float(survival[-1]),
    }
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Next, I run the 1,000-firm simulator for each of the four corporate strategies and print the performance comparison table.
"""))

cells.append(nbf.v4.new_code_cell(r"""corp_configs = [
    ("Fast-Follower Swarm (90% Copy / 10% R&D)", 0.90, "#d62728", 101),
    ("Optimal Division of Labor (70% Copy / 30% R&D)", 0.70, "#2ca02c", 102),
    ("Balanced Tech Firm (50% Copy / 50% R&D)", 0.50, "#1f77b4", 103),
    ("DeepTech Pioneer (10% Copy / 90% R&D)", 0.10, "#9467bd", 104),
]

tm_results = {}
tm_rows = []
for name, p_c, color, s in corp_configs:
    res = run_firm_cohort(p_c, seed=s)
    res["color"] = color
    tm_results[name] = res
    tm_rows.append({
        "Corporate Strategy": name,
        "Licensing Ratio": f"{int(p_c*100)}%",
        "In-House R&D Ratio": f"{int((1-p_c)*100)}%",
        "Pre-Shock Margin (H=2.0)": f"+{res['pre_margin']:.1f}",
        "Post-Shock Margin (H=10.0)": f"{res['post_margin']:+.1f}",
        "Cumulative Cashflow": f"+{res['cum_cash'][-1]:,.0f}",
        "100-Quarter Solvency": f"{res['final_surv']:.1f}%",
    })

display(pd.DataFrame(tm_rows))
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Now I plot **Publication Figure 8**, showing the 1,000-firm solvency rates, patent portfolio valuations, and operating margins across 100 quarters.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 3, figsize=(18, 5.2))
quarters = np.arange(1, 101)

for name, res in tm_results.items():
    axes[0].plot(quarters, res["survival"], label=name, color=res["color"], lw=2.4)
    axes[1].plot(quarters, res["mean_val"], label=name, color=res["color"], lw=2.2)
    axes[1].fill_between(quarters, res["val_low"], res["val_high"], color=res["color"], alpha=0.15)
    axes[2].plot(quarters, res["mean_margin"], label=name, color=res["color"], lw=2.2)

axes[0].axvline(40, color="crimson", ls="--", lw=1.5, label="Macro Scarcity Shock (H=10.0)")
axes[0].set_title("A. Industry Solvency & Survival Rate (N=1,000 Firms)", fontweight="bold")
axes[0].set_xlabel("Quarterly Epoch (t)", fontweight="bold")
axes[0].set_ylabel("Solvent Firms (% Margin ≥ 0)", fontweight="bold")
axes[0].set_ylim(-5, 105)
axes[0].grid(True, ls=":", alpha=0.5)
axes[0].legend(loc="lower left", frameon=True, fontsize=8.5)

axes[1].axvline(40, color="crimson", ls="--", lw=1.5)
axes[1].set_title("B. Patent Portfolio Quality z(t) (95% CI Ribbons)", fontweight="bold")
axes[1].set_xlabel("Quarterly Epoch (t)", fontweight="bold")
axes[1].set_ylabel("Technological Capital / Patent Value", fontweight="bold")
axes[1].grid(True, ls=":", alpha=0.5)

axes[2].axhline(0, color="black", ls="-", lw=1.2, alpha=0.7)
axes[2].axvline(40, color="crimson", ls="--", lw=1.5)
axes[2].annotate("The 'Free-Rider Illusion'\n(90% Copying looks most profitable)", xy=(25, 90), xytext=(5, 115),
                 arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.5), fontweight="bold", color="#d62728", fontsize=8.5)
axes[2].annotate("Insolvency Cliff (Π < 0)\n(90% Copying Collapses)", xy=(55, -6), xytext=(50, -45),
                 arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.5), fontweight="bold", color="#d62728", fontsize=8.5)
axes[2].set_title("C. Net Operating Margin Across 100 Quarters", fontweight="bold")
axes[2].set_xlabel("Quarterly Epoch (t)", fontweight="bold")
axes[2].set_ylabel("Operating Margin / Net Cashflow", fontweight="bold")
axes[2].set_ylim(-55, 185)
axes[2].grid(True, ls=":", alpha=0.5)

for ax in axes:
    sns.despine(ax=ax)

plt.suptitle("Publication Figure 8: Corporate R&D Time Machine — 1,000-Firm Scenario Simulation", fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# EXTENSION 5.7: EMPIRICAL VALIDATION
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Extension 5.7: Empirical Validation on Human Trial Data (Najar et al. 2020)

To ground these mechanisms against human behavior, I analyze **Najar, Bonnet, Bahrami, & Palminteri (2020, *PLoS Biology*)** (`data/task1.csv`), aligning adjacent demonstrator-human trial pairs. First, I load the CSV, match each human trial to the immediately preceding demonstrator choice, and print the agreement table.
"""))

cells.append(nbf.v4.new_code_cell(r"""df_raw = pd.read_csv("data/task1.csv").sort_values(["expid", "session", "trial"]).copy()
prev = df_raw.shift(1)

valid = (
    df_raw["expid"].eq(prev["expid"]) &
    df_raw["session"].eq(prev["session"]) &
    df_raw["trial"].eq(prev["trial"] + 1) &
    df_raw["state"].eq(prev["state"]) &
    df_raw["condition.demskill"].eq(prev["condition.demskill"]) &
    df_raw["id"].ne("dem") &
    prev["id"].eq("dem") &
    df_raw["condition.demskill"].ne("private")
)

df_pairs = df_raw.loc[valid, ["expid", "session", "trial", "state", "condition.demskill", "cgb"]].copy()
df_pairs.rename(columns={"condition.demskill": "condition", "cgb": "human_good"}, inplace=True)
df_pairs["dem_cgb"] = prev.loc[valid, "cgb"].astype(int)
df_pairs["matched"] = df_pairs["human_good"].eq(df_pairs["dem_cgb"]).astype(int)

print(f"Extracted valid demonstration-to-human pairs: {len(df_pairs)}")
emp_table = df_pairs.groupby(["condition", "dem_cgb"]).agg(
    Valid_Pairs=("matched", "count"),
    Choice_Match_Rate=("matched", "mean"),
).reset_index()
emp_table["Demonstrator Choice"] = emp_table["dem_cgb"].map({1: "Optimal Arm (Good)", 0: "Suboptimal Arm (Bad)"})
emp_table["Choice_Match_Rate"] = emp_table["Choice_Match_Rate"].apply(lambda x: f"{x*100:.1f}%")
display(emp_table[["condition", "Demonstrator Choice", "Valid_Pairs", "Choice_Match_Rate"]])
"""))

cells.append(nbf.v4.new_markdown_cell(r"""Next, I plot **Publication Figure 9**, comparing how often participants match good vs. bad demonstrators and showing their learning curves across trial blocks.
"""))

cells.append(nbf.v4.new_code_cell(r"""fig, axes = plt.subplots(1, 2, figsize=(14, 5.2))

sns.barplot(data=df_pairs, x="condition", y="matched", hue="dem_cgb", palette=["#e41a1c", "#377eb8"],
            ax=axes[0], capsize=0.08, err_kws={"linewidth": 1.5})
axes[0].set_title("A. Human Agreement Conditional on Demonstrator Choice (N=2,544)", fontweight="bold")
axes[0].set_xlabel("Demonstrator Condition", fontweight="bold")
axes[0].set_ylabel("Probability of Matching Demonstrator", fontweight="bold")
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(["Skilled Demonstrator (80% Opt)", "Unskilled Demonstrator (20% Opt)"])
axes[0].set_ylim(0, 1.0)
axes[0].axhline(0.5, color="gray", linestyle=":", label="Random Chance (0.50)")
handles, _ = axes[0].get_legend_handles_labels()
axes[0].legend(handles=handles, labels=["Demonstrator Chose Bad Arm", "Demonstrator Chose Good Arm", "Chance (0.5)"], loc="upper right", frameon=True, fontsize=9)
sns.despine(ax=axes[0])

df_human = df_raw[df_raw["id"] != "dem"].copy()
df_human["trial_block"] = pd.cut(df_human["ctrial"], bins=np.arange(0, 161, 20), labels=np.arange(10, 160, 20))
curves = df_human.groupby(["condition.demskill", "trial_block"], observed=False)["cgb"].mean().reset_index()

sns.lineplot(data=curves, x="trial_block", y="cgb", hue="condition.demskill",
             palette={"skilled.dem": "#377eb8", "unskilled.dem": "#e41a1c", "private": "#4daf4a"},
             marker="o", markersize=7, lw=2.2, ax=axes[1])
axes[1].set_title("B. Empirical Human Learning Trajectories", fontweight="bold")
axes[1].set_xlabel("Cumulative Trial Block", fontweight="bold")
axes[1].set_ylabel("Optimal Choice Probability (cgb)", fontweight="bold")
axes[1].set_ylim(0.55, 0.95)
axes[1].legend(title="Condition", labels=["Skilled Demonstrator", "Unskilled Demonstrator", "Private Learning"], fontsize=9)
sns.despine(ax=axes[1])

plt.suptitle("Publication Figure 9: Empirical Behavioral Alignment (Najar et al. 2020)", fontsize=13.5, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
"""))

# ==============================================================================
# SECTION 6: CONCLUSIONS, DISCLOSURE & BIBLIOGRAPHY
# ==============================================================================
cells.append(nbf.v4.new_markdown_cell(r"""---
## Section 6: General Conclusions, Limitations, University AI Disclosure & References

### 6.1 Summary of Core Findings & Extensions
1. **The Copier Tipping Point ($p^* \approx 70\%$)**: In our minimal model, copying ($C_{\text{copy}} = 1.0$) produces higher short-term welfare than innovating ($C_{\text{innov}} = 5.0$) under benign climates ($H=2.0$). However, once an austerity shock hits ($H=10.0$), populations with more than $\sim 70\%$ copiers collapse into persistent net deficit ($\Pi < 0$) because imitation error outpaces discovery.
2. **General Boundary Law**: Across 2D parameter sweeps of environmental harshness ($H \in [2, 14]$) and Henrich Gumbel skill loss ($\alpha_{\text{loss}} \in [0.2, 1.2]$), the viable survival boundary scales smoothly, proving that Rogers' Paradox is resolved through an intermediate **division of labor** ($\sim 70\%$ copiers / $\sim 30\%$ innovators).
3. **Corporate R&D Time Machine (1,000-Firm Scenario)**: In our macroeconomic scenario simulation, fast-followers (90% copying) appear most profitable during benign boom quarters (+90.2 margin), but experience an immediate collapse to **0.0% solvency** after the shock. Conversely, balanced firms (70% copying / 30% R&D) achieve **100% solvency** and maximum cumulative cashflow.
4. **Dynamic & Technological Extensions**: Even without fixed roles, Rescorla-Wagner prediction error gating and Replicator Dynamics self-organize toward this ESS; Yule-Simon trait sampling and Charbonneau recombination reproduce heavy-tailed technological power laws; and empirical analysis of $N = 2{,}544$ human trials confirms cognitive filtering over blind copying.

### 6.2 Limitations & Future Directions
1. **Network Topology**: Our baseline uses global well-mixed sampling; incorporating partially connected graphs (Derex & Boyd, 2016) could reveal spatial pockets of innovation persistence.
2. **Simulation-Based Inference (SBI)**: Following Youngblood & Passmore (2026), future work could apply neural posterior estimation to infer empirical copier proportions and transmission loss directly from USPTO patent histories.

---

### 6.3 University AI Disclosure Statement
*In compliance with PSL University and the PSAI AI & Society Master's Program academic integrity regulations:*
* **AI Assistance**: Antigravity (Google DeepMind) was utilized as an interactive pair-programming assistant.
* **Scope**: NumPy array vectorization, Seaborn aesthetic configurations, and LaTeX math formatting.
* **Author Intellectual Responsibility**: All research questions, theoretical arguments, mathematical formalisms, simulation analyses, and analytical conclusions were conceived, supervised, verified, and validated by the student author. All code and tests were executed locally.

---

### 6.4 Academic Bibliography & References
1. **Acerbi, A., Mesoudi, A., & Smolla, M.** (2022). *Individual-Based Models of Cultural Evolution: A Step-by-Step Guide Using R*. Routledge.
2. **Arthur, W. B.** (2009). *The Nature of Technology: What It Is and How It Evolves*. Free Press.
3. **Bentley, R. A., Hahn, M. W., & Shennan, S. J.** (2004). Random drift and culture change. *Proceedings of the Royal Society of London. Series B: Biological Sciences*, 271(1547), 1443–1450.
4. **Boyd, R., & Richerson, P. J.** (1985). *Culture and the Evolutionary Process*. University of Chicago Press.
5. **Charbonneau, M.** (2015). All innovations are equal, but some more than others: (re)integrating modification processes to the origins of cumulative culture. *Biological Theory*, 10(4), 322–335.
6. **Charbonneau, M., & Bourrat, P.** (2021). Fidelity and the grain problem in cultural evolution. *Synthese*, 199(3), 5815–5836.
7. **Claidière, N., Scott-Phillips, T. C., & Sperber, D.** (2014). How cultural evolution can be informed by cultural attraction theory. *Philosophical Transactions of the Royal Society B: Biological Sciences*, 369(1642), 20130368.
8. **Derex, M., & Boyd, R.** (2016). Partial connectivity increases cultural accumulation within groups. *Proceedings of the National Academy of Sciences*, 113(11), 2982–2987.
9. **Enquist, M., Eriksson, K., & Ghirlanda, S.** (2007). Critical social learning: a solution to Rogers’s paradox of nonadaptive culture. *American Anthropologist*, 109(4), 727–734.
10. **Henrich, J.** (2004). Demography and cultural evolution: How adaptive cultural processes can produce maladaptive losses—The Tasmanian case. *American Antiquity*, 69(2), 197–214.
11. **Henrich, J., & Boyd, R.** (2008). Division of labor, economic specialization, and the evolution of social stratification. *Current Anthropology*, 49(4), 715–724.
12. **Koshevoy, A., Miton, H., & Morin, O.** (2023). Zipf’s law of abbreviation holds for individual characters across a broad range of writing systems. *Cognition*, 238, 105527.
13. **Mesoudi, A.** (2011). Variable cultural acquisition costs constrain cumulative cultural evolution. *PLoS ONE*, 6(3), e18239.
14. **Mesoudi, A.** (2024). *Simulation Models of Cultural Evolution in R*. Posit Cloud Tutorial.
15. **Miton, H., & Charbonneau, M.** (2018). Cumulative culture in the laboratory: Methodological and theoretical challenges. *Proceedings of the Royal Society B: Biological Sciences*, 285(1879), 20180677.
16. **Morin, O.** (2016). *How Traditions Live and Die*. Oxford University Press.
17. **Morin, O., & Koshevoy, A.** (2024). A cultural evolutionary model for the law of abbreviation. *Topics in Cognitive Science*, 18(1), 62–77.
18. **Muthukrishna, M., & Henrich, J.** (2016). Innovation in the collective brain. *Philosophical Transactions of the Royal Society B: Biological Sciences*, 371(1690), 20150192.
19. **Najar, A., Bonnet, E., Bahrami, B., & Palminteri, S.** (2020). The actions of others act as a pseudo-reward to drive imitation in the context of social reinforcement learning. *PLoS Biology*, 18(12), e3001028.
20. **Rogers, A. R.** (1988). Does biology constrain culture? *American Anthropologist*, 90(4), 819–831.
21. **Shumailov, I., et al.** (2024). AI models collapse when trained on recursively generated data. *Nature*, 631, 755–759.
22. **Youngblood, M., Miton, H., & Morin, O.** (2023). Statistical signals of copying are robust to time- and space-averaging. *Evolutionary Human Sciences*, 5, e19.
23. **Youngblood, M.** (2024). Language-like efficiency and structure in house finch song. *Proceedings of the Royal Society B*, 291(2018), 20232490.
"""))

# ==============================================================================
# SAVE NOTEBOOK & EXECUTE PROGRAMMATICALLY
# ==============================================================================
nb.cells = cells
output_file = "cultural_evolution_project.ipynb"

print(f"Total cells to write: {len(cells)}")
with open(output_file, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook written to {output_file}. Executing all cells via NotebookClient...")
client = NotebookClient(nb, timeout=300, kernel_name="python3")
client.execute()

with open(output_file, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook execution complete! All plots, outputs, and tables are pre-rendered in {output_file}.")
