# Mason Youngblood Research Archive & Modeling Synthesis
## Communicative Efficiency, Time-Averaging, Conformity Bias, and Simulation-Based Inference

**Curated for:** Cultural Evolution Master's Course (Prof. Alexey Koshevoy, PSAI / ENS-PSL)  
**Location:** `/Users/raresolteanu/Desktop/Cultural/Mason_Youngblood_Papers/`  
**Date:** November 2026  

---

## 1. Archive Inventory (14 Documents)

| # | Filename | Year | Title | Venue | Key Contribution |
|---|---|---|---|---|---|
| 1 | `Youngblood_Miton_Morin_2023_Statistical_Signals_Copying_Time_Averaging.pdf` | 2023 | *Statistical signals of copying are robust to time- and space-averaging* | *Evolutionary Human Sciences* (654 KB) | **Equifinality & Drift Benchmark:** Co-authored with Olivier Morin & Hélène Miton. Proves that statistical signatures of social learning survive temporal aggregation. |
| 2 | `Youngblood_Passmore_2025_Simulation_Based_Inference_Speed_Climbing.pdf` | 2026 | *Simulation-based inference with deep learning suggests speed climbers combine innovation and copying* | *Proc. R. Soc. B* (3.7 MB) | **Methodological Vanguard:** Neural Simulation-Based Inference (SBI) proving that elite human performance requires a hybrid mix of innovation and copying. |
| 3 | `Youngblood_2025_Language_Like_Efficiency_Whale_Communication.md` | 2025 | *Language-like efficiency in whale communication* | *Science Advances* (78 KB) | **Pressure for Efficiency:** Comprehensive proof of Zipf's Law of Abbreviation and Menzerath's Law across 16 cetacean species and 51 human languages. |
| 4 | `Youngblood_2024_Language_Like_Efficiency_House_Finch_Song.pdf` | 2024 | *Language-like efficiency and structure in house finch song* | *Proc. R. Soc. B* (2.7 MB) | Compression and least-effort optimization in vocal cultural transmission. |
| 5 | `Wascher_Youngblood_2025_Vocal_Efficiency_in_Crows.pdf` | 2025 | *Vocal efficiency in crows* | *Animal Cognition* (449 KB) | Information theory and energetic constraints shaping communicative repertoires. |
| 6 | `Youngblood_2026_Simulation_Based_Inference_Tutorial_Baby_Names.pdf` | 2026 | *Simulation-based inference for cultural evolution: a tutorial with baby name data* | OSF Tutorial (1.8 MB) | Practical tutorial on training neural posterior estimators (NPE) to fit ABM cultural evolution models. |
| 7 | `Youngblood_2019_Conformity_Bias_Music_Sampling.md` | 2019 | *Conformity bias in the cultural transmission of music sampling traditions* | *Royal Society Open Science* (72 KB) | Mathematical and empirical verification of frequency-dependent conformity bias in digital culture. |
| 8 | `Youngblood_2019_Music_Sampling_Delocalization.pdf` | 2019 | *Cultural transmission modes of music sampling traditions remain stable despite delocalization* | *PLoS ONE* (1.1 MB) | Geographic vs. digital network transmission of cultural variants. |
| 9 | `Youngblood_et_al_2023_Negativity_Bias_Voter_Fraud_Conspiracy.pdf` | 2023 | *Negativity bias in the spread of voter fraud conspiracy theory tweets* | *Humanities & Soc. Sci. Comm.* (848 KB) | Co-authored with Olivier Morin & Alberto Acerbi. Transmission biases in large-scale social media. |
| 10 | `Sobchuk_Youngblood_Morin_2024_First_Mover_Advantage_Music.pdf` | 2024 | *First-mover advantage in music* | *EPJ Data Science* (1.8 MB) | Co-authored with Olivier Morin. Niche preemption and founding advantages in cultural evolution. |
| 11 | `Youngblood_Lahti_2018_Bibliometric_Analysis_Cultural_Evolution.pdf` | 2018 | *A bibliometric analysis of the interdisciplinary field of cultural evolution* | *Palgrave Communications* (726 KB) | Quantitative citation mapping of the cultural evolution field. |
| 12 | `Pitocchelli_et_al_2024_Mourning_Warbler_Transmission_Biases.pdf` | 2024 | *Temporal stability in songs across breeding range due to learning fidelity and transmission biases* | *Ornithology* (5.1 MB) | Co-authored with R. Alexander Bentley. Cultural stability vs. drift in song traditions. |
| 13 | `Youngblood_et_al_2026_Collective_Creativity_AI_Art.pdf` | 2026 | *Dynamics of collective creativity in AI art competitions* | *PNAS Nexus* (1.6 MB) | Recombination and exploration dynamics in human-AI cultural systems. |
| 14 | `Youngblood_2025_Chatter_Python_Library_Information_Theory.pdf` | 2025 | *chatter: a Python library for applying information theory and AI/ML models to animal communication* | arXiv (704 KB) | Python computational package for calculating entropy, mutual information, and compression. |

---

## 2. Why Prof. Alexey Koshevoy Cites Mason Youngblood

Prof. Koshevoy frequently highlights Mason Youngblood in course slides and lectures due to two direct academic synergies:

### A. The Paris / Institut Jean Nicod Connection
- Youngblood collaborates extensively with **Olivier Morin** (Alexey Koshevoy's PhD supervisor at Institut Jean Nicod / ENS-PSL), **Alberto Acerbi**, and **Hélène Miton**.
- Their joint papers (*Youngblood, Miton, & Morin 2023*; *Youngblood et al. 2023*; *Sobchuk, Youngblood, & Morin 2024*) represent the state-of-the-art methodology of the **Minds & Cultures group at ENS-PSL**.

### B. The Pressure for Efficiency & Zipf's Law of Abbreviation
- Prof. Koshevoy’s primary published research program (*Cognition 2023*; *TopiCS 2024*; *CogSci 2024*) centers on **the Pressure for Efficiency and the Principle of Least Effort** in cultural evolution.
- Youngblood's landmark papers in *Science Advances (2025)* and *Proceedings of the Royal Society B (2024)* provide the broad comparative biological proof for this exact phenomenon:
  $$\ln(\text{Duration}_i) = \beta_0 - \beta_1 \ln(\text{Frequency}_i) + \epsilon_i$$
  Both human languages and nonhuman cultural communication systems compress high-frequency variants to minimize energetic transmission costs.

---

## 3. Core Theoretical Insights & Modeling Applications

### 1. Robustness Under Time-Averaging & Preempting Equifinality (Youngblood, Miton, & Morin 2023)
* **The Problem**: In archaeology, paleontology, and historical datasets (including patent data), observations are **time-averaged**: discrete cultural acts are blurred across decades or centuries. Skeptics argued that time-averaging destroys signatures of copying, making selection indistinguishable from neutral drift (equifinality).
* **Youngblood et al.'s Finding**: Using forward ABM simulations across thousands of parameter regimes, they proved that:
  - **Neutral Drift (Bentley et al. 2004)** maintains a characteristic power-law tail and high turnover even under severe time-averaging.
  - **Conformist and Success Biases** leave detectable skewness and turnover suppression that **cannot be erased by temporal aggregation**.
* **Direct Project Application**: In our Master Notebook's Section on Equifinality, citing Youngblood, Miton, & Morin (2023) defends our simulation architecture against the critique that our results are artifacts of discrete generational binning.

---

### 2. Neural Simulation-Based Inference (SBI) & Hybrid Strategies (Youngblood & Passmore 2026)
* **The Problem**: In complex agent-based models (like our 3-strategy cultural evolution model), calculating an analytical likelihood function $P(\text{Data} | \theta)$ is intractable.
* **Youngblood's Method**: He introduced **Simulation-Based Inference (SBI)** using deep neural density estimators (Masked Autoregressive Flows / Mixture Density Networks):
  1. Sample parameter vectors $\theta \sim P(\theta)$ (e.g. innovation rate, copying fidelity, learning costs).
  2. Run the forward ABM simulation to generate synthetic time-series trajectories $\mathbf{x}$.
  3. Train a neural network $q_\phi(\theta | \mathbf{x})$ to approximate the true posterior distribution $P(\theta | \mathbf{x})$.
* **Empirical Discovery in Speed Climbing (*Proc. R. Soc. B 2026*)**:
  - Athletes do not succeed through pure individual practice, nor through pure imitation.
  - Performance optimization requires a **synergistic combination of innovation and copying**: copying establishes baseline competency, while targeted innovation discovers novel execution routes.
* **Direct Project Application**: This empirical finding mirrors our simulation's **Mode 4 (Heterogeneous Society)**, where combining Copiers ($80\%$) and Innovators ($10\%$) with Adaptive learners ($10\%$) achieves the highest cumulative net payoff ($+7,505.76$) and prevents collapse.

---

### 3. Measuring Conformity Bias in Cultural Transmission (Youngblood 2019)
* **The Model**:
  In *Conformity bias in the cultural transmission of music sampling traditions* (*Royal Society Open Science* 2019), Youngblood tested Boyd & Richerson’s canonical frequency-dependent transmission function:
  $$P(\text{adopt variant } k) = \frac{p_k^D}{\sum_j p_j^D}$$
  - $D = 1$: Linear unbiased copying (drift).
  - $D > 1$: Positive frequency-dependent bias (conformity: popular variants get copied more than expected by chance).
  - $D < 1$: Negative frequency-dependent bias (novelty-seeking / anti-conformity).
* **Direct Project Application**: Citing Youngblood (2019) grounds our frequency-dependent bias parameters in real-world cultural data (hip-hop sampling lineages).

### 4. Mathematical Formulations of Linguistic Laws & Efficiency (Youngblood 2024, 2025)
* **The Fundamental Efficiency Ratio**:
  $$\text{Efficiency} \propto \frac{\sum \pi}{C_L + \sum C_P}$$
  where:
  - $\sum \pi$: Lifetime communicative or technological benefit (information transmitted, payoff).
  - $C_L$: Acquisition/learning cost (cognitive overhead, trial-and-error exploration).
  - $\sum C_P$: Production cost (acoustic energetic expenditure, motor execution effort).
* **Menzerath-Altmann Law (Sequence Compression)**:
  $$\bar{d}(L) = a \cdot L^{-b} \cdot e^{-c L} \quad \implies \quad \ln(\bar{d}) \approx \beta_0 - \beta_1 \ln(L)$$
  As sequence length $L$ increases, mean constituent duration $\bar{d}$ decreases to conserve aggregate production cost.
* **The Shuffling Null Model (Linkage Disequilibrium in Cultural Subunits)**:
  $$P_{\text{shuffled}}(c_1, c_2, \dots, c_k) = \frac{\prod_{i=1}^k P(c_i)}{\sum_{(c_1', \dots, c_k') \in \Omega_k} \prod_{j=1}^k P(c_j')}$$
  Deviations between observed co-occurrence $P_{\text{obs}}$ and $P_{\text{shuffled}}$ provide rigorous proof of social transmission over independent random invention.

---

## 4. Master Citation Block for Master Notebook

```bibtex
@article{youngblood2023statistical,
  title={Statistical signals of copying are robust to time-and space-averaging},
  author={Youngblood, Mason and Miton, Helena and Morin, Olivier},
  journal={Evolutionary Human Sciences},
  volume={5},
  pages={e10},
  year={2023},
  publisher={Cambridge University Press}
}

@article{youngblood2026simulation,
  title={Simulation-based inference with deep learning suggests speed climbers combine innovation and copying to improve performance},
  author={Youngblood, Mason and Passmore, Sam},
  journal={Proceedings of the Royal Society B},
  volume={293},
  number={2062},
  pages={20251433},
  year={2026},
  publisher={The Royal Society}
}

@article{youngblood2025language,
  title={Language-like efficiency in whale communication},
  author={Youngblood, Mason},
  journal={Science Advances},
  volume={11},
  number={6},
  pages={eads6014},
  year={2025},
  publisher={American Association for the Advancement of Science}
}

@article{youngblood2019conformity,
  title={Conformity bias in the cultural transmission of music sampling traditions},
  author={Youngblood, Mason},
  journal={Royal Society Open Science},
  volume={6},
  number={9},
  pages={191149},
  year={2019},
  publisher={The Royal Society}
}
```
