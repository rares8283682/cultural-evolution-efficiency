# Cultural Evolution: Master Course, Practicals, R Modeling & Project Context

This document is the comprehensive reference for the Cultural Evolution course taught by **Alexey Koshevoy** in the **PSAI AI & Society Master's Program** (PSL University, Autumn 2026–2027). It brings together:
1. **Course Lectures & Readings**: Theoretical foundations, evolutionary models, demography, and phylogenetics.
2. **Official Course Practicals (Python)**: Detailed code architectures and solved implementations from [`alexeykosh/cultural-evolution-2026-S3`](https://github.com/alexeykosh/cultural-evolution-2026-S3) (`S2` through `S5`).
3. **Reference Computational Textbook (R)**: Alberto Acerbi, Alex Mesoudi, & Marco Smolla, [*Individual-Based Models of Cultural Evolution* (IBM-cultevo)](https://albertoacerbi.github.io/IBM-cultevo/) with complete model catalog and R-to-Python mapping.
4. **Official Project Guidelines & Grading Rubric**: Requirements, 10-point evaluation criteria, and the 5 professor-suggested research project avenues.

---

## 1. Course Information & Master's Context

- **Program**: PSAI AI & Society Master's Program (Autumn Semester 2026–2027).
- **Program**: PSAI AI & Society Master's Program (Autumn Semester 2026–2027).
- **Instructor**: Alexey Koshevoy (Research Fellow at PR[AI]RIE - PSAI; Postdoctoral Researcher at École Normale Supérieure / ENS-PSL; PhD in Cognitive Science from Aix-Marseille Université & Institut Jean Nicod, supervised by Olivier Morin & Isabelle Dautriche; ENS Cogmaster alumnus).
- **Intellectual Core & Published Agenda**:
  - Focuses on Cultural Evolution, Computational Linguistics, Statistical Laws, and NeuroAI.
  - Core papers: *Cognition* (2023), *Topics in Cognitive Science* (2024), *PNAS Nexus* (2026), *CogSci* (2023, 2024), *OSF* (2025).
  - Key Themes: **The Pressure for Efficiency**, **The Principle of Least Effort (Zipfian dynamics)**, **Mechanistic Agent-Based Modeling (ABM)**, and **Neutral Drift vs. Directional Selection**.
- **Professor's Methodological Passions (from LinkedIn & Research Activity)**:
  1. **Strict End-to-End Computational Reproducibility**: Contributor to the *Institute for Replication (I4R)*; passionately insists that 100% of figures, tables, and statistics must be reproduced from raw data using fixed seeds (`np.random.default_rng`).
  2. **NeuroAI & Mathematical Learning Theory**: Enthusiastic about bridging neuroscience (Dopaminergic TD Q-learning, Prediction Errors) with formal artificial intelligence.
  3. **Anti-Functionalism & Equifinality**: Dislikes teleological hand-waving; demands explicit micro-level decision rules and comparisons against neutral / static baselines.
  4. **Interactive AI in Science**: Praises tools that turn static research into interactive, executable computational agents and transparent notebooks.
- **Grading Breakdown**:
  - **Final Project**: **50%**
  - **3 Quizzes**: **30%** (First quiz is 20 minutes, covering Lectures 1–3 concepts; not based on optional readings).
  - **Participation**: **20%**
- **Recommended Textbooks & Methodological References**:
  - Alberto Acerbi, Alex Mesoudi, & Marco Smolla, *Individual-Based Models of Cultural Evolution* ([IBM-cultevo](https://albertoacerbi.github.io/IBM-cultevo/)).
  - Paul E. Smaldino (2023), *Modeling Social Behavior: Mathematical and Agent-Based Models of Social Dynamics and Cultural Evolution*.
  - Bentley, Hahn & Shennan (2004), *Random drift and culture change*, Proc. R. Soc. Lond. B.
  - Youngblood, Baraghith & Savage (2021), *Phylogenetic reconstruction of the cultural evolution of electronic music via dynamic community detection (1975–1999)*, Evolution and Human Behavior.

---

## 2. Official Final Project Guidelines & Evaluation Rubric

### 2.1 Submission Requirements
- **Format**: Executable **Jupyter Notebook (`.ipynb`)**.
- **Mandatory Sections**:
  1. **Research Question**: Short introduction, motivation, theoretical framing, and clear hypothesis.
  2. **Analysis**: Implementation of simulations or empirical data processing, statistical validation, and clean figures.
  3. **Conclusions**: In-depth theoretical discussion engaging deeply with cultural evolution literature, assessing limitations, and outlining future work.
- **Repository**: Deposited on **GitHub** and **fully reproducible**.
  - All code must execute sequentially from top to bottom.
  - Open datasets must be included; proprietary/large datasets shared privately.
- **AI Disclosure**: Explicit statement at the end of the notebook disclosing AI tools used for writing, coding, or designing. (Note: Using AI for data annotation is explicitly encouraged).

### 2.2 Grading Criteria (Total: 10 Points)

| Criterion | Points | Evaluation Standard |
| :--- | :---: | :--- |
| **1. Fit & Novelty of Research Question** | **2 pts** | **0 pts**: Irrelevant to what was taught in class.<br>**1 pt**: Directly related to theory or data seen in class.<br>**2 pts**: Highly novel, original research question grounded in CE. |
| **2. Methods** | **3 pts** | **Lowest**: Low relevance to cultural evolution.<br>**Highest (3 pts)**: Methods standard in CE or recent publications (ABM / IBM, population genetics simulations, generative inference / BayesFlow, phylogenetics, network models). |
| **3. Originality** | **3 pts** | **Lowest**: Pure replication of an existing study without improvements.<br>**Highest (3 pts)**: Novel research question and/or new analytical framework and/or new dataset. |
| **4. Conclusions** | **2 pts** | **Lowest**: Simple summary of results without theoretical engagement.<br>**Highest (2 pts)**: Innovative discussion engaging deeply with theoretical debates (seen or unseen in class). |

---

## 3. Official Project Ideas Suggested by the Professor

### Idea 1: Foundation Time-Series Models for Drift vs. Selection (TimesFM)
- **Question**: Can zero-shot time-series foundation models like Google Research's **TimesFM** ([`google-research/timesfm`](https://github.com/google-research/timesfm)) reliably distinguish frequency changes produced by neutral drift from directional cultural selection?
- **Setup**:
  - Generate synthetic Wright-Fisher frequency trajectories with varying selection coefficients $s \in [0, 0.1]$, population sizes $N$, and temporal binning.
  - Benchmark TimesFM's classification/forecasting accuracy against **Karsdorp et al. (2020)** and the Frequency Increment Test (FIT).
- **Key Reference**: Feder et al. (2014); Karsdorp et al. (2020) [PMC10427472].

### Idea 2: Drift vs. Selection in Strategy Games (e.g., Bongcloud Attack in Chess)
- **Question**: Are unconventional strategies—such as the **Bongcloud Attack** (1. e4 e5 2. Ke2?!) in chess, or novel Go moves post-AlphaGo—driven by **prestige bias** (top grandmasters/streamers like Nakamura or Carlsen), frequency biases, or neutral drift?
- **Data & Methods**:
  - Lichess open database / Chess.com APIs across rating brackets and historical dates.
  - Fit neutral drift models (Bentley et al. 2004) vs. prestige/success-biased transmission models.
- **Key References**:
  - *Opening strategies in Go from feudalism to superhuman AI* (Cambridge Core, 2025).
  - *Evolution and Human Behavior* (2014).
  - *Proc. R. Soc. B* (2023, 10.1098/rspb.2023.1634).

### Idea 3: Critical Evaluation of Cultural Nestedness
- **Question**: Repertoire "nestedness" (subsets of skills) has been used to claim animals have cumulative culture. Can simulations prove that nestedness is an emergent artifact of demography, task constraints, or neutral drift rather than true cultural transmission?
- **Data & Methods**:
  - Bipartite network analysis and NODF nestedness metric.
  - Compare agent simulations against empirical "collection"-like data (e.g., Spotify/Last.fm album listening histories, language vowel inventories from PHOIBLE).
- **Key References**:
  - PNAS (2013, 10.1073/pnas.1313318110).
  - PubMed (2023, 37588550).

### Idea 4: Social Network Topologies vs. Population Size
- **Question**: Is cultural maintenance/loss genuinely driven by census population size (Henrich 2004), or is it determined by **interaction topology** (modularity, clustering, degree variance, scale-free bottlenecks) and *effective population size* ($N_e$)?
- **Data & Methods**:
  - Agent-based simulations replacing Henrich's well-mixed population with complex network structures (Erdős-Rényi, Watts-Strogatz small-world, Barabási-Albert scale-free).
  - Measure how network bottlenecks insulate complex skills against loss or cause fragmentation.
- **Key Reference**: *Cognitive Science* (2024, 10.1111/cogs.13439).

### Idea 5: Fitting Cultural Evolution Models via Generative Inference (BayesFlow / SBI)
- **Question**: Can we infer hidden cultural transmission parameters (selection strength $s$, innovation rate $\mu$, conformity parameter $D$) from empirical cultural datasets using amortized Bayesian inference?
- **Data & Methods**:
  - Use **BayesFlow** (`https://bayesflow.org/v2.0.14/index.html`) — deep generative neural networks (Invertible Neural Networks / Normalizing Flows) for simulation-based inference (SBI).
  - Take a canonical CE model (e.g., Henrich demographic skill model, or Acerbi conformity model) and estimate parameters from empirical cultural time-series.
- **Key References**:
  - Kandler & Powell (2018), *Generative inference for cultural evolution*, Phil. Trans. R. Soc. B.
  - *Proc. R. Soc. B* (2025, 10.1098/rspb.2025.1433); *PNAS Nexus* (2024, pgag258).

---

## 4. Deep Dive: Course Practicals & Code Architecture (Python)

The official course repository ([`alexeykosh/cultural-evolution-2026-S3`](https://github.com/alexeykosh/cultural-evolution-2026-S3)) contains four core seminar practicals:

```
cultural-evolution-2026-S3/
├── S2/
│   ├── 02-unbiased-copying.ipynb
│   └── 02-unbiased-copying-solved.ipynb
├── S3/
│   ├── 03-drift-detection.ipynb
│   └── 03-drift-detection-solved.ipynb
├── S4/
│   └── 04-Henrich-model.ipynb
├── S5/
│   ├── 05-linguistic-phylogenies.ipynb
│   ├── iecor-languages.csv
│   ├── iecor-parameters.csv
│   └── iecor-forms.csv
└── README.md
```

### 4.1 Global Visual & Coding Standards
All notebooks follow consistent styling:
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(context="paper", style="ticks", font_scale=1, palette="colorblind")
rng = np.random.default_rng(101101)
```

---

### 4.2 Practical S2: Unbiased Copying & Wright-Fisher Drift
#### 1. Agent-Based vs. Binomial Simulation
* **Agent-Based Generation Turnover**:
  ```python
  def simulate_run(N, p_init, t, rng):
      population = rng.choice(["A", "B"], size=N, p=[p_init, 1 - p_init])
      percent_A = [np.mean(population == "A")]
      for _ in range(t):
          population = rng.choice(population, size=N, replace=True)
          percent_A.append(np.mean(population == "A"))
      return percent_A
  ```
* **Binomial Shortcut (Exact Equivalence)**:
  Under unbiased copying with two variants, drawing $N$ individuals with replacement from a population with proportion $p$ is mathematically identical to a Binomial draw:
  ```python
  def simulate_run_binomial(N, p_init, t, rng):
      percent_A = [p_init]
      p_A = p_init
      for _ in range(t):
          p_A = rng.binomial(N, p_A) / N
          percent_A.append(p_A)
      return np.array(percent_A)
  ```

#### 2. Adding Mutation / Innovation
* **Agent-Based Mutation**:
  ```python
  def simulate_with_innovation(N, p_init, t, mu, rng):
      population = rng.choice(["A", "B"], size=N, p=[p_init, 1 - p_init])
      percent_A = [np.mean(population == "A")]
      for _ in range(t):
          population = rng.choice(population, size=N, replace=True)
          innovators = rng.random(N) < mu
          population[innovators] = np.where(population[innovators] == "A", "B", "A")
          percent_A.append(np.mean(population == "A"))
      return np.array(percent_A)
  ```
* **Binomial Mutation**:
  The expected frequency after symmetric mutation is $p' = p(1 - \mu) + (1 - p)\mu$:
  ```python
  def simulate_with_innovation_binomial(N, p_init, t, mu, rng):
      percent_A = [p_init]
      p_A = p_init
      for _ in range(t):
          p_A_after_innovation = p_A * (1 - mu) + (1 - p_A) * mu
          p_A = rng.binomial(N, p_A_after_innovation) / N
          percent_A.append(p_A)
      return np.array(percent_A)
  ```

---

### 4.3 Practical S3: Drift Detection & Multi-Variant Models
#### 1. Bentley et al. (2004) Multi-Variant Engine
Tracks infinite novel variants across generations:
```python
def simulate_with_innovation(N, k, t, mu, rng):
    population = rng.choice(np.arange(k), size=N)
    populations = [population.copy()]
    next_variant = k

    for _ in range(t):
        # Unbiased copying with replacement
        population = rng.choice(population, size=N, replace=True)

        # Innovation: assign unique incremental integer IDs
        innovators = rng.random(N) < mu
        for i in np.where(innovators)[0]:
            population[i] = next_variant
            next_variant += 1

        populations.append(population.copy())

    # Build full frequency matrix (t + 1, total_unique_variants)
    frequencies = np.zeros((t + 1, next_variant))
    for time_step, pop in enumerate(populations):
        for v in np.unique(pop):
            frequencies[time_step, v] = np.mean(pop == v)

    return frequencies
```

#### 2. Directional Selection Engine
Weighting variant probabilities by relative fitness ($1 + s$ vs. $1$):
```python
def simulate_run(N, p_init, t, selection, rng):
    items = ["A", "B"]
    population = rng.choice(items, size=N, p=[p_init, 1 - p_init])
    frequencies = [np.mean(population == "A")]

    for _ in range(t):
        weights = np.where(population == "A", 1 + selection, 1.0)
        weights = weights / weights.sum()
        population = rng.choice(population, size=N, replace=True, p=weights)
        frequencies.append(np.mean(population == "A"))

    return np.array(frequencies)
```

#### 3. Frequency Increment Test (FIT)
Computes normalized frequency increments and performs a one-sample t-test ($H_0: \mu = 0$):
```python
from scipy.stats import ttest_1samp

def fit(frequencies):
    previous = frequencies[:-1]
    valid = (previous > 0) & (previous < 1)
    increments = np.diff(frequencies)[valid]
    increments = increments / np.sqrt(2 * previous[valid] * (1 - previous[valid]))

    if len(increments) < 2:
        return np.nan, np.nan, increments

    result = ttest_1samp(increments, 0)
    return result.statistic, result.pvalue, increments
```

#### 4. Karsdorp et al. (2020) Temporal Binning Experiment
Demonstrates how temporal aggregation obscures selection:
```python
def bin_frequencies(frequencies, n_bins):
    frequencies = np.asarray(frequencies)
    bins = np.array_split(frequencies, n_bins)
    return np.array([b.mean() for b in bins])
```

---

### 4.4 Practical S4: Henrich (2004) Model of Demography & Cultural Loss
#### 1. One Generation of Imperfect Copying
```python
N = 80          # Population of learners
alpha = 5       # Transmission difficulty / degradation
beta = 1        # Copying noise / dispersion
z_model = 10    # Model skill level

# Individual learner skill draws
copies = z_model + rng.gumbel(loc=-alpha, scale=beta, size=N)
best_learner = copies.max()
```

#### 2. Multi-Generational Evolution (Solved Implementation)
```python
def simulate_henrich(N, alpha, beta, generations, rng):
    population = np.zeros(N)
    best_skill = [population.max()]

    for _ in range(generations):
        model = population.max()
        # All learners attempt to copy the best individual
        population = model + rng.gumbel(loc=-alpha, scale=beta, size=N)
        best_skill.append(population.max())

    return np.array(best_skill)
```

#### 3. Empirical Zero-Crossing Estimation of $N^*$ (Solved Implementation)
```python
N_values = [10, 20, 40, 60, 80, 100, 150, 200, 300]
num_runs = 10_000
comparison_rng = np.random.default_rng(4)
mean_changes = []

for N in N_values:
    # Estimate mean change after one generation from skill 0
    changes = []
    for _ in range(num_runs):
        copies = comparison_rng.gumbel(loc=-alpha, scale=beta, size=N)
        changes.append(copies.max())
    mean_changes.append(np.mean(changes))

# Zero-crossing indicates critical population size N*
```

---

### 4.5 Practical S5: Linguistic Phylogenies from Scratch
#### 1. Pipeline & Solved Code
```python
from itertools import combinations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, cophenet
from scipy.stats import spearmanr
from lingpy import LexStat

# 1. Filter present-day Romance varieties with full phonemic segments
romance = languages[(languages.Clade == "Italic;Roman") & ~languages.historical]
usable = forms[forms.Language_ID.isin(romance.index) & forms.Phonemic.notna() & forms.Phonemic_Segments.notna()]
romance = romance[romance.index.isin(usable.Language_ID)]

# 2. Retain meanings with exactly one form across all chosen varieties
counts = (usable.groupby(["Parameter_ID", "Language_ID"]).size()
          .unstack(fill_value=0).reindex(columns=romance.index, fill_value=0))
shared_meanings = counts.index[counts.eq(1).all(axis=1)]
selected = usable[usable.Parameter_ID.isin(shared_meanings)]

# 3. LingPy Sound-Class-Based Alignment (SCA) clustering
entries = {0: ["doculect", "concept", "ipa", "tokens"]}
for i, row in enumerate(selected.itertuples(index=False), 1):
    entries[i] = [romance.loc[row.Language_ID, "Name"], meanings.loc[row.Parameter_ID, "Name"], row.Phonemic, row.Phonemic_Segments.split()]

lex = LexStat(entries, no_bscorer=True)
lex.cluster(method="sca", threshold=0.6, ref="auto")

# 4. Cognate Matrix & Hamming Distance
cognates = pd.DataFrame(
    [(lex[i, "concept"], lex[i, "doculect"], lex[i, "auto"]) for i in lex],
    columns=["Meaning", "Language", "Cognate set"]
).pivot(index="Meaning", columns="Language", values="Cognate set")[romance.Name]

lexical_distances = pdist(cognates.T, metric="hamming")
lexical_matrix = pd.DataFrame(squareform(lexical_distances), index=cognates.columns, columns=cognates.columns)

# 5. UPGMA Tree Reconstruction
tree = linkage(lexical_distances, method="average")
tree_distances = 2 * cophenet(tree)

# 6. Haversine Geographic Distance Function
def great_circle_km(a, b):
    lat1, lon1 = np.radians(a)
    lat2, lon2 = np.radians(b)
    h = (np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371 * np.arcsin(np.sqrt(h))

locations = romance.set_index("Name").loc[cognates.columns, ["Latitude", "Longitude"]]
geographic_distances = pdist(locations.values, metric=great_circle_km)

# 7. Spatial vs. Phylogenetic Correlation
rho, p_val = spearmanr(geographic_distances, tree_distances)
```

---

## 5. Reference Computational Textbook: *IBM-cultevo* (Acerbi et al. in R)

Alberto Acerbi, Alex Mesoudi, & Marco Smolla's open textbook (*Individual-Based Models of Cultural Evolution*) provides the standard R modeling paradigms for cultural evolution. Below is the complete chapter catalog, mathematical specifications, and R implementations.

### 5.1 R Modeling Conventions & Idioms
- Built on `tidyverse` (`tibble`, `dplyr`, `ggplot2`).
- Discrete populations represented as `tibble(trait = ...)` or integer vectors.
- Stochastic transitions via `sample(x, size = N, replace = TRUE, prob = ...)`.

### 5.2 Chapter Catalog & Algorithmic Formulations

#### Chapter 1: Unbiased Transmission
- **Concept**: Wright-Fisher cultural drift with discrete non-overlapping generations.
- **R Implementation**:
  ```R
  library(tidyverse)
  N <- 100; t_max <- 200
  population <- tibble(trait = sample(c("A", "B"), N, replace = TRUE))
  output <- tibble(generation = 1:t_max, p = rep(NA, t_max))
  output$p[1] <- sum(population$trait == "A") / N

  for (t in 2:t_max) {
    previous_population <- population
    population <- tibble(trait = sample(previous_population$trait, N, replace = TRUE))
    output$p[t] <- sum(population$trait == "A") / N
  }
  ```

#### Chapter 2: Unbiased and Biased Mutation
- **Unbiased Mutation**:
  ```R
  mutate <- runif(N) < mu
  population$trait[mutate] <- sample(c("A", "B"), sum(mutate), replace = TRUE)
  ```
- **Biased (Directional) Mutation**:
  Asymmetric transformation probabilities: $\mu_{b \to a} > \mu_{a \to b}$.

#### Chapter 3: Direct (Content) Bias
- **Concept**: Individuals prefer variant A over B due to intrinsic memorability, psychological attractiveness, or payoff:
  $$p' = \frac{p(1 + s)}{p(1 + s) + (1 - p)}$$
- **R Implementation**:
  ```R
  p <- sum(previous_population$trait == "A") / N
  p_after_selection <- (p * (1 + s)) / (p * (1 + s) + (1 - p))
  population <- tibble(trait = sample(c("A", "B"), N, replace = TRUE, prob = c(p_after_selection, 1 - p_after_selection)))
  ```

#### Chapter 4: Frequency-Dependent Indirect Bias (Conformity)
- **Concept**: Boyd & Richerson (1985) cubic conformity formulation:
  $$p' = p + D p (1 - p)(2p - 1)$$
  - $D > 0$: **Conformist bias** (disproportionately favors majority trait, producing sigmoidal S-curves and fixation).
  - $D < 0$: **Anti-conformist / Novelty bias** (favors rare traits, maintaining polymorphism near $p = 0.5$).
- **R Implementation**:
  ```R
  p <- sum(previous_population$trait == "A") / N
  p_conform <- p + D * p * (1 - p) * (2 * p - 1)
  population <- tibble(trait = sample(c("A", "B"), N, replace = TRUE, prob = c(p_conform, 1 - p_conform)))
  ```

#### Chapter 5: Demonstrator-Based Indirect Bias (Prestige Bias)
- **Concept**: Models have observable cues or prestige scores $S_i$. Copiers sample models with probability proportional to score:
  $$P(\text{choose } j) = \frac{S_j}{\sum_k S_k}$$
- **R Implementation**:
  ```R
  model_indices <- sample(1:N, N, replace = TRUE, prob = previous_population$prestige / sum(previous_population$prestige))
  population$trait <- previous_population$trait[model_indices]
  ```

#### Chapter 6: Vertical, Horizontal, and Oblique Transmission
- **Vertical**: Direct copying of biological parents (1-to-1 linkage). Retards cultural diffusion.
- **Horizontal**: Copying peers within the same generation. Fast, fashion-like diffusion.
- **Oblique**: Copying older non-parent adults (e.g. teachers). Bridges generations with social institutions.

#### Chapter 7: Multiple Traits & Power Laws (Bentley Model)
- **Concept**: Infinite-alleles model where innovators introduce brand new integer IDs.
- **R Implementation**:
  ```R
  next_trait <- max(population$trait) + 1
  for (t in 2:t_max) {
    population$trait <- sample(previous_population$trait, N, replace = TRUE)
    mutate <- runif(N) < mu
    num_mutants <- sum(mutate)
    if (num_mutants > 0) {
      population$trait[mutate] <- next_trait:(next_trait + num_mutants - 1)
      next_trait <- next_trait + num_mutants
    }
  }
  ```
  Generates power-law distributions $P(v) \sim v^{-\alpha}$ matching Bentley et al. (2004).

#### Chapters 8 & 9: Rogers' Paradox & Critical Social Learners
- **Rogers' Paradox**: Pure social learners free-ride on individual learners in changing environments ($u = \text{prob of environmental change}$). At equilibrium, mean population fitness is identical to a population of solitary individual learners!
- **Solution (Critical Social Learning, Enquist et al. 2007)**:
  Agents learn socially first. If the acquired trait fails a payoff threshold, they switch to individual trial-and-error learning, breaking the paradox and raising average population fitness.

#### Chapter 10: Cultural Attraction & Convergent Transformation
- **Concept**: Dan Sperber & Nicolas Claidière's Cognitive Attractor Theory.
- Instead of exact copying, traits occupy continuous space $[0, 1]$ and undergo directional transformation toward cognitive attractors $C$:
  $$x^{t+1} = x^t + \lambda (C - x^t) + \epsilon$$
- Demonstrates that high cultural stability and uniformity can emerge **without high-fidelity copying**.

#### Chapter 11: Social Learning of Social Learning Rules
- Meta-evolution: Agents culturally transmit not just traits, but their own learning parameters (e.g., individual learning propensity vs. copying conservatism).

#### Chapter 12: Trait Interdependence & Cultural Complexes
- Prerequisite networks: Adopting trait $T_B$ requires prior mastery of trait $T_A$.
- Creates epistatic fitness landscapes, path dependency, and technological lock-in.

#### Chapter 13: Demography & Skill Maintenance
- Translates Henrich (2004) into R: Gumbel error draws around the maximum skill model, showing population collapse thresholds.

#### Chapter 14: Social Network Structure & Contagions
- Built with `igraph` in R.
- Compares simple contagion (contact suffices) vs. **complex contagion** (adoption requires multiple reinforcing exposures, e.g. Centola 2010) across small-world and scale-free topologies.

#### Chapter 15: Group-Structured Populations & Migration
- $M$ demes of size $N$. Agents copy locally with probability $1 - m$, or copy migrants from other demes with probability $m$.
- Foundation for **Cultural Group Selection (CGS)**: between-group cultural variance drives selection for cooperative institutions.

---

### 5.3 R-to-Python Translation Reference

| R Idiom (`tidyverse` / Base R) | Python Equivalent (`numpy` / `pandas`) |
| :--- | :--- |
| `tibble(trait = sample(c("A", "B"), N, replace = TRUE))` | `rng.choice(["A", "B"], size=N, replace=True)` |
| `rbinom(1, N, p) / N` | `rng.binomial(N, p) / N` |
| `sample(prev$trait, N, replace = TRUE, prob = weights)` | `rng.choice(prev_pop, size=N, replace=True, p=norm_weights)` |
| `runif(N) < mu` | `rng.random(N) < mu` |
| `rgumbel(N, loc = -alpha, scale = beta)` | `rng.gumbel(loc=-alpha, scale=beta, size=N)` |
| `igraph::sample_smallworld(1, N, nei, p)` | `networkx.watts_strogatz_graph(n=N, k=2*nei, p=p)` |
| `igraph::sample_pa(N, power = 1)` | `networkx.barabasi_albert_graph(n=N, m=m)` |
| `pdist(X, metric = "hamming")` | `scipy.spatial.distance.pdist(X, metric="hamming")` |
| `hclust(d, method = "average")` | `scipy.cluster.hierarchy.linkage(d, method="average")` |

---

## 6. Comprehensive Theoretical & Historical Summary

### 6.1 Epistemological Timeline
- **18th c.**: Monogenism vs. Polygenism (Voltaire); Stadial Progressivism (Adam Smith: *Hunting $\to$ Pasturage $\to$ Agriculture $\to$ Commerce*).
- **Early 19th c.**: Lamarckism (orthogenesis & soft inheritance).
- **1859/1871**: Darwinism (substrate-neutral selection, population thinking, no teleological ladder).
- **Late 19th c.**: Tylor ("complex whole") & Morgan (*Savagery $\to$ Barbarism $\to$ Civilization*).
- **Early 20th c.**: Franz Boas (cultural relativism, historical particularism).
- **1981–1985**: Modern Quantitative Cultural Evolution:
  - Cavalli-Sforza & Feldman (1981): Population genetics framework.
  - Boyd & Richerson (1985): Dual inheritance theory and transmission biases.

### 6.2 Animal Traditions vs. Human Cumulative Culture
- **ZLS Hypothesis (Tennie et al.)**: Animal traditions are latent solutions individually reinvented via social priming; Snyder et al. (2022) showed Oldowan tools can be reinvented de novo.
- **Human Uniqueness (Tomasello)**: High-fidelity imitation and language power the **ratchet effect**, allowing cumulative retention across millennia.

### 6.3 Demography & Linguistic Structure
- **Henrich (2004)**: Price equation proves cumulative skill maintenance requires $N > N^* = \exp(\frac{\alpha}{\beta} - \gamma)$.
- **Linguistic Evolution**:
  - Lupyan & Dale (2010): Esoteric vs. Exoteric languages.
  - Shcherbakova et al. (2023): Debunked simplistic claims; societies of strangers do not speak simpler languages across fusion and informativity metrics.

---

## 7. Formula & Equation Cheat-Sheet

| Model / Phenomenon | Canonical Formula | Key Parameters |
| :--- | :--- | :--- |
| **Instantaneous Neutral Equilibrium** | $P(v) = 2N\mu - 1 (1 - v)^{2N\mu - 1}$ | $N$: population, $\mu$: innovation, $v$: frequency |
| **Accumulated Power Law (Bentley 2004)** | $\alpha = 0.1042 \ln(N\mu) + 1.48$ | $\alpha$: slope on log-log plot |
| **Comparative Exponent Shift** | $\alpha_1 - \alpha_2 = 0.1042 \ln\left(\frac{N_1\mu_1}{N_2\mu_2}\right)$ | Relative population prediction |
| **Henrich Copying Draw** | $z_i \sim \text{Gumbel}(z_{\max} - \alpha, \beta)$ | $\alpha$: difficulty, $\beta$: dispersion |
| **Henrich Expected Skill Rate** | $\Delta z = -\alpha + \beta(\gamma + \ln N)$ | $\gamma \approx 0.5772$ (Euler-Mascheroni) |
| **Critical Population Threshold** | $N^* = \exp\left(\frac{\alpha}{\beta} - \gamma\right)$ | Minimum size to prevent degradation |
| **Frequency Increment Test (FIT)** | $Y_t = \frac{p_t - p_{t-1}}{\sqrt{2 p_{t-1}(1 - p_{t-1})}}$ | Tested against $\mathcal{N}(0, 1)$ via t-test |
| **Conformist Transmission Bias** | $p' = p + D p (1 - p)(2p - 1)$ | $D > 0$: conformity, $D < 0$: novelty |
| **Direct (Selection) Weight** | $w_A = 1 + s, \quad w_B = 1$ | $s$: selection coefficient |
| **Haversine Geographic Distance** | $d = 2R \arcsin\left(\sqrt{\sin^2(\frac{\Delta\phi}{2}) + \cos\phi_1\cos\phi_2\sin^2(\frac{\Delta\lambda}{2})}\right)$ | $R \approx 6371$ km, $\phi$: lat, $\lambda$: lon |
| **Cultural Attraction Step** | $x^{t+1} = x^t + \lambda(C - x^t) + \epsilon$ | $C$: cognitive attractor, $\lambda$: pull strength |
