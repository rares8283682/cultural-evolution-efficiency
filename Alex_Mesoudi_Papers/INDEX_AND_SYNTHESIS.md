# Alex Mesoudi Research Archive & Modeling Synthesis
## Grounding Cultural Evolution in Agent-Based Models, Acquisition Costs, Prestige Bias, and Cumulative Culture

**Curated for:** Cultural Evolution Master's Final Project (Prof. Alexey Koshevoy, PSAI / ENS-PSL)  
**Location:** `/Users/raresolteanu/Desktop/Cultural/Alex_Mesoudi_Papers/`  
**Date:** November 2026  

---

## 1. Archive Inventory

| # | Filename | Year | Title | Venue / Source | Key Contribution |
|---|---|---|---|---|---|
| 1 | `Mesoudi_Thornton_2018_What_is_Cumulative_Cultural_Evolution.md` | 2018 | *What is cumulative cultural evolution?* | *Proc. R. Soc. B* (PMC6015835) | The canonical 4-part benchmark definition of CCE (Transmission, Modification, Accumulation, Beyond Individual Discovery). |
| 2 | `Mesoudi_2011_Variable_Cultural_Acquisition_Costs.pdf` | 2011 | *Variable Cultural Acquisition Costs Constrain Cumulative Cultural Evolution* | *PLoS ONE* (617 KB) | **Mathematical Foundation:** Proof that when learning costs $C(z)$ scale with skill, cumulative culture halts unless specialization/division of labor emerges. |
| 3 | `Jimenez_Mesoudi_2019_Prestige_Biased_Social_Learning.pdf` | 2019 | *Prestige-biased social learning: Current evidence and outstanding questions* | *Nature Palgrave Comm.* (571 KB) | State-of-the-art review and model of prestige vs. dominance and informational efficiency. |
| 4 | `Atkisson_OBrien_Mesoudi_2012_Prestige_Biased_Learning.md` | 2012 | *Adult Learners in a Novel Environment Use Prestige-Biased Social Learning* | *Evolutionary Psychology* (PMC4885851) | Experimental validation that humans rely on prestige cues when entering uncertain/novel environments. |
| 5 | `Brand_Heap_Morgan_Mesoudi_2020_Emergence_Use_of_Prestige.pdf` | 2020 | *The emergence and adaptive use of prestige in an online social learning task* | *Nature Scientific Reports* (1.4 MB) | Behavioral experiment demonstrating how prestige hierarchies emerge endogenously as attention heuristics. |
| 6 | `Mesoudi_2021_Cultural_Selection_and_Biased_Transformation.md` | 2021 | *Cultural selection and biased transformation: two dynamics of cultural evolution* | *Phil. Trans. R. Soc. B* (PMC8059521) | Resolves the debate between Cultural Attraction Theory (biased transformation) and California School selection models. |
| 7 | `Acerbi_Mesoudi_2015_Cultural_Darwinians_Disagreements.pdf` | 2015 | *If we are all cultural Darwinians what’s the fuss about?* | *Biology & Philosophy* (522 KB) | Synthesizes population-genetics models with cognitive-attractor transmission models. |
| 8 | `Derex_Bonnefon_Boyd_Mesoudi_2019_Causal_Understanding_Technology.pdf` | 2019 | *Causal understanding is not necessary for the improvement of culturally evolving technology* | *Nature Human Behaviour* / OSF (289 KB) | Shows that cumulative technological complexity advances through selective transmission even without mechanistic causal understanding. |
| 9 | `Mesoudi_2018_Migration_Acculturation_Maintenance_Variation.pdf` | 2018 | *Migration, acculturation, and the maintenance of between-group cultural variation* | *PLoS ONE* / bioRxiv (5.6 MB) | Agent-based simulation of conformist vs. payoff-biased transmission maintaining group differences under migration. |
| 10 | `Acerbi_Mesoudi_Smolla_2022_IBM_Cultevo_Guide.md` | 2022 | *Individual-Based Models of Cultural Evolution: A Step-by-Step Guide using R* | Textbook Reference | Reference computational guide for cultural evolution ABMs (Chapters 7, 8, 9, 10, 12). |

---

## 2. Alex Mesoudi's Core Theoretical Frameworks

### A. The 4 Criteria for Cumulative Cultural Evolution (Mesoudi & Thornton 2018)
In *What is cumulative cultural evolution?*, Mesoudi and Alex Thornton formalize the standard diagnostic criteria that define cumulative culture:
1. **Repetitive Cultural Transmission:** Traits are transferred repeatedly through social learning across multiple individuals/generations.
2. **Directional Modification:** Inventions, modifications, or improvements are sequentially incorporated into the cultural lineage.
3. **Accumulation of Diversity / Complexity / Efficiency:** Traits exhibit monotonic or asymptotic gains in performance measures or structural complexity.
4. **Beyond Individual Discovery:** The accumulated technological trait possesses structural complexity such that **no single individual could discover it independently *de novo*** during a single lifetime.

> **Project Link:** Our simulation directly operationalizes this via Henrich's Gumbel transmission ($\Delta z = -\alpha + \beta(\gamma + \ln N)$) and the Rogers (1988) benchmark: Copiers maintain cultural traits far beyond individual trial-and-error limits, preventing cultural regression during harsh shocks.

---

### B. Variable Acquisition Costs & The Learning Trap (Mesoudi 2011)
In *Variable Cultural Acquisition Costs Constrain Cumulative Cultural Evolution* (*PLoS ONE* 2011), Mesoudi addressed a critical flaw in classical cumulative culture models (e.g. Boyd & Richerson 1996; Henrich 2004):
- Classical models assume cultural traits can accumulate indefinitely without accounting for the **time and cognitive energy required to learn them**.
- Mesoudi modeled agents with a finite lifetime $L$. In generation $t$, an agent must first acquire existing culture $z$ at cost $C(z) = c \cdot z$.
- **The Result:** If $C(z)$ scales linearly with $z$, agents spend their entire lives acquiring existing knowledge and have zero remaining time to innovate ($\Delta z \to 0$). Cumulative culture hits a hard ceiling.
- **The Solution:** Cumulative progress can only continue if:
  1. Social transmission fidelity increases (lowering the marginal cost of acquisition $c$).
  2. Cognitive labor is **divided** into specialized, polymorphic roles (some agents exploit/copy existing tools while others explore/innovate).

> **Project Link:** This provides the exact theoretical justification for our payoff function:
> $$\Pi_i(t) = z_i(t) - H(t) - C_i$$
> where $C_{\text{copier}} < C_{\text{innovator}}$, demonstrating why a polymorphic population with an adaptive division of cognitive labor resolves the learning trap.

---

### C. The Great Basin Projectile-Point Simulation (Mesoudi & O'Brien 2008)
In *American Antiquity* (2008), Mesoudi and Michael J. O'Brien tested cultural learning strategies on a multimodal adaptive landscape:
- **Guided Variation:** Agents innovate through individual trial-and-error hill climbing.
- **Indirect (Prestige) Bias:** Agents copy individuals with high prestige cues (attention, reputation).
- **Payoff Bias:** Agents directly inspect and copy high-payoff traits.
- **Core Findings:**
  - On rugged, multimodal fitness landscapes, guided variation frequently gets trapped on suboptimal local peaks.
  - Payoff-biased learning is optimal but requires high informational access costs (agents must accurately evaluate everyone's payoffs).
  - **Prestige bias acts as an adaptive, low-cost proxy:** Learners can easily identify prestigious individuals and copy their traits, outperforming random copying and avoiding the costs of full payoff audits.

> **Project Link:** This matches Prof. Koshevoy's blackboard prestige formula implemented in our simulation:
> $$W_j = P_j^\alpha \cdot F_j^\beta$$
> where agents weight candidates by both observable prestige attention ($P_j$) and observed skill ($F_j$).

---

### D. The Acerbi, Mesoudi, & Smolla (2020/2022) ABM Standards (`IBM-cultevo`)
The computational textbook co-authored by Mesoudi defines the exact simulation architectures used throughout Alexey Koshevoy's course:
- **Chapter 7: Neutral Copying & Bentley's Power Law:**
  - Random copying with continuous innovation ($\mu$) produces stationary power-law distributions ($\alpha \approx 0.1042 \ln(N\mu) + 1.48$).
- **Chapter 9: Content & Payoff Bias:**
  - Models direct selection where traits with higher payoff $w$ spread logistically through the population.
- **Chapter 10: Model-Based Biases (Prestige & Success):**
  - Agents select demonstrators based on social rank and track records.
- **Chapter 12: Interdependent Traits & Cultural Complexes:**
  - Traits are not independent scalars; acquiring trait $B$ requires prior acquisition of foundational trait $A$.
  - This directly connects Mesoudi's modeling to Mathieu Charbonneau's modular technological recipes and patent citation networks!

---

## 3. How to Cite Alex Mesoudi to Satisfy Prof. Koshevoy's Rubric

1. **In the Research Questions & Theoretical Rationale:**
   - Cite **Mesoudi & Thornton (2018)** to establish that our model measures genuine cumulative cultural evolution (accumulation beyond single-agent discovery).
   - Cite **Mesoudi (2011)** to defend the cost of learning $C_i$ as a structural acquisition constraint that prevents runaway scalar accumulation.
2. **In the Agent Architecture & Social Learning Mechanics:**
   - Cite **Atkisson, O'Brien, & Mesoudi (2012)** and **Brand et al. (2020)** for prestige-biased transmission in novel/uncertain environments.
   - Cite **Mesoudi & O'Brien (2008)** for why prestige heuristics outperform pure individual trial-and-error on multimodal landscapes.
3. **In the Discussion & Real-World Application (Patents / Technological Complexity):**
   - Cite **Acerbi, Mesoudi, & Smolla (2022, Chapter 12)** alongside **Mathieu Charbonneau (2016)** and **W. Brian Arthur (2009)**: Real-world cultural evolution is combinatorial; patent citations represent interdependent modular recipes.
