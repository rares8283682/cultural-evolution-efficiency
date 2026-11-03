"""
Cultural Evolution Simulation Engine: Harshness-Driven Learning & Division of Labor
Authors: Rares Olteanu (in dialogue with Prof. Alexey Koshevoy)
Institution: PSAI AI & Society Master's Program, PSL University / ENS-PSL

Standards:
- 100% Mass Computational Reproducibility (I4R / APS Standard)
- Vectorized NumPy Monte Carlo Engine (50-run ensembles with pointwise percentile ribbons)
- Single Environmental Harshness parameter H(t) (Pressure for Efficiency)
- Payoff Function: Pi = z - H - C(action)
- Core Strategies:
    1. Pure Copiers (100% Social Learners, Skill-Biased Selection, Henrich Gumbel Transmission)
    2. Pure Innovators (100% Individual Learners, Continuous Hatched-Zone Discovery)
    3. Homogeneous Adaptive Social Brain (Bandit Rescorla-Wagner Delta Rule + Softmax Gating)
    4. Static Exploration Baseline (Fixed 5% Innovation Heuristic Null)
    5. Heterogeneous Society (Division of Cognitive Labor: 80% Copiers, 10% Innovators, 10% Adaptive)
- Fixed-Mixture Sensitivity Sweep (5% to 100% exploration grid)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(context="paper", style="ticks", font_scale=1.1, palette="colorblind")


class HarshnessCulturalArena:
    def __init__(
        self,
        N: int = 100,
        generations: int = 100,
        shock_gen: int = 40,
        H_low: float = 2.0,
        H_high: float = 10.0,
        cost_copy: float = 1.0,
        cost_innov: float = 5.0,
        alpha_prestige: float = 4.0,
        gumbel_loss: float = 0.8,
        gumbel_beta: float = 0.3,
        innov_lambda: float = 1.5,
        eta: float = 0.35,
        tau: float = 1.0,
        seed: int = 101101,
    ):
        self.N = N
        self.T = generations
        self.T_shock = shock_gen
        self.H_low = H_low
        self.H_high = H_high
        self.cost_copy = cost_copy
        self.cost_innov = cost_innov
        self.alpha_prestige = alpha_prestige
        self.gumbel_loss = gumbel_loss
        self.gumbel_beta = gumbel_beta
        self.innov_lambda = innov_lambda
        self.eta = eta
        self.tau = tau
        self.seed = seed

    def simulate_single_run(
        self,
        strategy_mode: int,
        rng: np.random.Generator,
        fixed_innov_prob: float = None,
    ):
        """
        strategy_mode:
            0: Pure Copiers (100% Social Learners)
            1: Pure Innovators (100% Individual Learners)
            2: Homogeneous Adaptive Social Brain (Bandit Delta Rule + Softmax)
            3: Static Fixed Exploration Mixture (uses fixed_innov_prob, default 0.05)
            4: Heterogeneous Society (80% Copier, 10% Innovator, 10% Adaptive)
        """
        N = self.N
        # Initialize continuous technological skill z around 6.5
        z = rng.uniform(6.0, 7.0, size=N)

        # Q-values [Q_copy, Q_innov] for adaptive agents
        # For mode 2: all N agents are adaptive.
        # For mode 4: last 10 agents (indices 90..99) are adaptive.
        if strategy_mode == 2:
            n_adapt = N
            q_vals = np.zeros((N, 2))
            q_vals[:, 0] = 3.5  # Prior expectation for cheap copying
            q_vals[:, 1] = 0.0  # Prior expectation for costly innovation
        elif strategy_mode == 4:
            n_adapt = 10
            q_vals = np.zeros((10, 2))
            q_vals[:, 0] = 3.5
            q_vals[:, 1] = 0.0
        else:
            q_vals = None

        history = {
            "mean_payoff": np.zeros(self.T),
            "mean_skill": np.zeros(self.T),
            "diversity": np.zeros(self.T),
            "pct_innovating": np.zeros(self.T),
        }

        for t in range(self.T):
            # 1. Environmental Harshness parameter H(t) (Pressure for Efficiency)
            H = self.H_low if t < self.T_shock else self.H_high

            # 2. Action Selection
            actions = np.zeros(N, dtype=int)  # 0 = COPY, 1 = INNOVATE
            if strategy_mode == 0:
                actions[:] = 0
            elif strategy_mode == 1:
                actions[:] = 1
            elif strategy_mode == 2:
                # Softmax action selection over bandit Q-values
                delta_q = (q_vals[:, 1] - q_vals[:, 0]) / self.tau
                p_innov = 1.0 / (1.0 + np.exp(-np.clip(delta_q, -15, 15)))
                actions = (rng.random(N) < p_innov).astype(int)
            elif strategy_mode == 3:
                p_fixed = 0.05 if fixed_innov_prob is None else fixed_innov_prob
                actions = (rng.random(N) < p_fixed).astype(int)
            elif strategy_mode == 4:
                # Division of Cognitive Labor:
                # 0..79: Dedicated Copiers (80%)
                actions[:80] = 0
                # 80..89: Dedicated Innovators (10%)
                actions[80:90] = 1
                # 90..99: Adaptive Response Team (10%)
                delta_q = (q_vals[:, 1] - q_vals[:, 0]) / self.tau
                p_innov = 1.0 / (1.0 + np.exp(-np.clip(delta_q, -15, 15)))
                actions[90:] = (rng.random(10) < p_innov).astype(int)

            # 3. Transmission & Discovery Phase
            z_next = z.copy()
            costs = np.zeros(N)

            # --- A. Copiers (Social Learners) ---
            copy_idx = np.where(actions == 0)[0]
            if len(copy_idx) > 0:
                costs[copy_idx] = self.cost_copy
                # Skill-biased demonstrator selection proportional to z^alpha
                prestige_scores = (np.maximum(z, 0.01) / np.max(z)) ** self.alpha_prestige
                probs = prestige_scores / np.sum(prestige_scores)

                # Sample demonstrators with replacement
                models = rng.choice(N, size=len(copy_idx), p=probs)

                # Henrich (2004) Gumbel transmission noise
                gumbel_noise = rng.gumbel(
                    loc=-self.gumbel_loss, scale=self.gumbel_beta, size=len(copy_idx)
                )
                z_next[copy_idx] = np.maximum(0.0, z[models] + gumbel_noise)

            # --- B. Innovators (Hatched Zone Discovery) ---
            innov_idx = np.where(actions == 1)[0]
            if len(innov_idx) > 0:
                costs[innov_idx] = self.cost_innov
                dz = rng.exponential(scale=self.innov_lambda, size=len(innov_idx))
                z_next[innov_idx] = z[innov_idx] + dz

            # 4. Net Energetic Payoff: Pi = z - H - C
            payoffs = z_next - H - costs

            # 5. Phasic Rescorla-Wagner Bandit Updates
            if strategy_mode == 2:
                for act in [0, 1]:
                    mask = (actions == act)
                    if np.any(mask):
                        rpe = payoffs[mask] - q_vals[mask, act]
                        q_vals[mask, act] += self.eta * rpe
            elif strategy_mode == 4:
                adapt_actions = actions[90:]
                adapt_payoffs = payoffs[90:]
                for act in [0, 1]:
                    mask = (adapt_actions == act)
                    if np.any(mask):
                        rpe = adapt_payoffs[mask] - q_vals[mask, act]
                        q_vals[mask, act] += self.eta * rpe

            # Update population state
            z = z_next

            # Record metrics
            history["mean_payoff"][t] = np.mean(payoffs)
            history["mean_skill"][t] = np.mean(z)
            history["diversity"][t] = np.std(z)
            history["pct_innovating"][t] = np.mean(actions)

        return history

    def run_ensemble(self, n_runs: int = 50, seed: int = None):
        """Runs vectorized Monte Carlo ensembles across all main strategies."""
        rng = np.random.default_rng(self.seed if seed is None else seed)
        strategies = {
            "Pure Copiers": 0,
            "Pure Innovators": 1,
            "Homogeneous Adaptive": 2,
            "Static 5% Mixture": 3,
            "Heterogeneous (80/10/10)": 4,
        }
        ensemble_data = {s: [] for s in strategies}

        for s_name, s_mode in strategies.items():
            for _ in range(n_runs):
                run_hist = self.simulate_single_run(strategy_mode=s_mode, rng=rng)
                ensemble_data[s_name].append(run_hist)

        # Compute mean, cumulative payoff, and 2.5th-97.5th percentiles
        processed = {}
        for s_name in strategies:
            runs = ensemble_data[s_name]
            processed[s_name] = {}
            for metric in ["mean_payoff", "mean_skill", "diversity", "pct_innovating"]:
                arr = np.array([r[metric] for r in runs])  # shape: (n_runs, T)
                processed[s_name][metric] = {
                    "mean": np.mean(arr, axis=0),
                    "lower": np.percentile(arr, 2.5, axis=0),
                    "upper": np.percentile(arr, 97.5, axis=0),
                }
            # Cumulative payoff distribution across 50 runs
            cum_payoffs = np.array([np.sum(r["mean_payoff"]) for r in runs])
            processed[s_name]["cumulative_payoff"] = {
                "mean": float(np.mean(cum_payoffs)),
                "std": float(np.std(cum_payoffs, ddof=1)),
                "lower": float(np.percentile(cum_payoffs, 2.5)),
                "upper": float(np.percentile(cum_payoffs, 97.5)),
            }

        return processed

    def run_fixed_mixture_sweep(
        self,
        probs: list = [0.05, 0.20, 0.50, 0.70, 0.90, 1.00],
        n_runs: int = 50,
        seed: int = 2026,
    ):
        """Runs fixed innovation probability sweep to evaluate exploration sensitivity."""
        rng = np.random.default_rng(seed)
        sweep_results = []
        for p in probs:
            cum_runs = []
            fin_payoffs = []
            fin_skills = []
            for _ in range(n_runs):
                hist = self.simulate_single_run(
                    strategy_mode=3, rng=rng, fixed_innov_prob=p
                )
                cum_runs.append(np.sum(hist["mean_payoff"]))
                fin_payoffs.append(hist["mean_payoff"][-1])
                fin_skills.append(hist["mean_skill"][-1])
            sweep_results.append({
                "Fixed_Innov_Prob": p,
                "Mean_Cumulative_Payoff": float(np.mean(cum_runs)),
                "Std_Cumulative_Payoff": float(np.std(cum_runs, ddof=1)),
                "Mean_Final_Payoff": float(np.mean(fin_payoffs)),
                "Mean_Final_Skill": float(np.mean(fin_skills)),
            })
        return pd.DataFrame(sweep_results)

    def run_replicator_dynamics(
        self,
        n_runs: int = 50,
        init_props: list = [1 / 3, 1 / 3, 1 / 3],
        mu: float = 0.03,
        seed: int = 303303,
    ):
        """Simulates endogenous co-evolution of strategies via discrete replicator dynamics."""
        rng = np.random.default_rng(seed)
        props_history = np.zeros((n_runs, self.T, 3))
        payoff_history = np.zeros((n_runs, self.T))
        skill_history = np.zeros((n_runs, self.T))

        for r in range(n_runs):
            z = np.full(self.N, 1.0)
            q_vals = np.zeros((self.N, 2))
            counts = np.array([self.N // 3, self.N // 3, self.N - 2 * (self.N // 3)])
            props = counts / self.N

            for t in range(self.T):
                props_history[r, t] = props
                H = self.H_high if t >= self.T_shock else self.H_low
                c0, c1, c2 = counts

                actions = np.zeros(self.N, dtype=int)
                if c1 > 0:
                    actions[c0 : c0 + c1] = 1
                if c2 > 0:
                    ad_slice = slice(c0 + c1, self.N)
                    diff = (q_vals[ad_slice, 1] - q_vals[ad_slice, 0]) / self.tau
                    prob_innov = 1.0 / (1.0 + np.exp(-np.clip(diff, -10.0, 10.0)))
                    actions[ad_slice] = (rng.uniform(size=c2) < prob_innov).astype(int)

                costs = np.zeros(self.N)
                z_next = np.copy(z)

                copy_idx = np.where(actions == 0)[0]
                if len(copy_idx) > 0:
                    costs[copy_idx] = self.cost_copy
                    prestige = (np.maximum(z, 0.01) / np.max(z)) ** self.alpha_prestige
                    probs = prestige / np.sum(prestige)
                    models = rng.choice(self.N, size=len(copy_idx), p=probs)
                    gumbel_noise = rng.gumbel(
                        loc=-self.gumbel_loss, scale=self.gumbel_beta, size=len(copy_idx)
                    )
                    z_next[copy_idx] = np.maximum(0.0, z[models] + gumbel_noise)

                innov_idx = np.where(actions == 1)[0]
                if len(innov_idx) > 0:
                    costs[innov_idx] = self.cost_innov
                    dz = rng.exponential(scale=self.innov_lambda, size=len(innov_idx))
                    z_next[innov_idx] = z[innov_idx] + dz

                payoffs = z_next - H - costs

                if c2 > 0:
                    ad_slice = slice(c0 + c1, self.N)
                    for act in [0, 1]:
                        sub = (actions[ad_slice] == act)
                        if np.any(sub):
                            g_idx = np.where(actions[ad_slice] == act)[0] + (c0 + c1)
                            rpe = payoffs[g_idx] - q_vals[g_idx, act]
                            q_vals[g_idx, act] += self.eta * rpe

                z = z_next

                p0 = np.mean(payoffs[:c0]) if c0 > 0 else 0.0
                p1 = np.mean(payoffs[c0 : c0 + c1]) if c1 > 0 else 0.0
                p2 = np.mean(payoffs[c0 + c1:]) if c2 > 0 else 0.0

                gps = np.array([p0, p1, p2])
                fit = gps - np.min(gps) + 1.0

                rep = props * (fit / np.sum(props * fit))
                rep = (1.0 - mu) * rep + mu * (1.0 / 3.0)
                rep = rep / np.sum(rep)

                counts = rng.multinomial(self.N, rep)
                props = counts / self.N

                payoff_history[r, t] = np.mean(payoffs)
                skill_history[r, t] = np.mean(z)

        return {
            "props_history": props_history,
            "payoff_history": payoff_history,
            "skill_history": skill_history,
        }


if __name__ == "__main__":
    print("Executing 50-run Monte Carlo simulation with Division of Cognitive Labor...")
    arena = HarshnessCulturalArena(N=100, generations=100, shock_gen=40, seed=101101)
    results = arena.run_ensemble(n_runs=50)

    print("\n=== MONTE CARLO ENSEMBLE SUMMARY (50 RUNS) ===")
    print(f"{'Strategy':<26} | {'Pre-Shock (t=39)':<16} | {'Final Payoff':<12} | {'Cumulative Payoff':<18} | {'Final Skill':<11}")
    print("-" * 92)
    for name, data in results.items():
        pre_payoff = data["mean_payoff"]["mean"][39]
        final_payoff = data["mean_payoff"]["mean"][-1]
        cum_mean = data["cumulative_payoff"]["mean"]
        final_skill = data["mean_skill"]["mean"][-1]
        print(
            f"{name:<26} | {pre_payoff:+16.2f} | {final_payoff:+12.2f} | {cum_mean:+18.2f} | {final_skill:11.2f}"
        )

    print("\n=== FIXED MIXTURE SENSITIVITY SWEEP ===")
    sweep_df = arena.run_fixed_mixture_sweep()
    print(sweep_df.to_string(index=False))

    print("\n=== ENDOGENOUS REPLICATOR DYNAMICS (CO-EVOLVING SHARES) ===")
    rep_res = arena.run_replicator_dynamics(n_runs=50)
    mean_props = np.mean(rep_res["props_history"], axis=0)
    print(f"t=0  Proportions (Copiers/Innovators/Adaptive): {mean_props[0].round(3)}")
    print(f"t=39 Proportions (Pre-Shock):                  {mean_props[39].round(3)}")
    print(f"t=45 Proportions (Post-Shock):                 {mean_props[45].round(3)}")
    print(f"t=99 Proportions (Final ESS):                  {mean_props[99].round(3)}")
    print(f"Mean Cumulative Payoff under Replicator:       {np.mean(np.sum(rep_res['payoff_history'], axis=1)):.2f}")
