"""
Harshness Cultural Arena: Agent-Based Simulation of Cumulative Cultural Evolution.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd


class HarshnessCulturalArena:
    """
    Agent-based model simulating cumulative cultural transmission under environmental
    harshness shocks and cognitive transmission costs.

    Parameters
    ----------
    N : int, default=100
        Total population size of cultural agents.
    generations : int, default=100
        Number of discrete cultural transmission generations.
    shock_gen : int, default=40
        Generation at which environmental harshness shock H(t) occurs.
    H_low : float, default=2.0
        Baseline environmental harshness level (pre-shock).
    H_high : float, default=10.0
        Post-shock environmental harshness level (scarcity regime).
    cost_copy : float, default=1.0
        Cognitive/energetic cost of social learning (imitation).
    cost_innov : float, default=5.0
        Cognitive/energetic cost of individual learning (asocial discovery).
    alpha_prestige : float, default=4.0
        Softmax temperature / exponent governing prestige bias in model selection.
    gumbel_loss : float, default=0.8
        Expected fidelity loss in Henrich's Gumbel transmission process.
    gumbel_beta : float, default=0.3
        Scale parameter (variance/noise) of Gumbel copying error.
    innov_lambda : float, default=1.5
        Scale parameter of exponential skill gains via individual innovation.
    eta : float, default=0.35
        Learning rate for dopaminergic Reward Prediction Error (RPE) Q-updates.
    tau : float, default=1.0
        Softmax temperature governing exploration vs. exploitation in strategy gating.
    seed : int, default=101101
        Master random seed for computational reproducibility.
    """

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
    ) -> None:
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
        fixed_innov_prob: Optional[float] = None,
    ) -> Dict[str, np.ndarray]:
        """
        Execute a single generation-by-generation simulation run.

        Parameters
        ----------
        strategy_mode : int
            0: Pure Copiers (100% Social Learners)
            1: Pure Innovators (100% Individual Learners)
            2: Homogeneous Adaptive Social Brain (Bandit Delta Rule + Softmax)
            3: Static Fixed Exploration Mixture (uses fixed_innov_prob, default 0.05)
            4: Heterogeneous Society (80% Copier, 10% Innovator, 10% Adaptive)
        rng : np.random.Generator
            NumPy random number generator instance.
        fixed_innov_prob : float, optional
            Fixed innovation probability for strategy_mode 3.

        Returns
        -------
        Dict[str, np.ndarray]
            Trajectory dictionary containing mean_payoff, mean_skill, diversity, pct_innovating.
        """
        N = self.N
        z = rng.uniform(6.0, 7.0, size=N)

        if strategy_mode == 2:
            q_vals = np.zeros((N, 2))
            q_vals[:, 0] = 3.5  # Prior expectation for copying
            q_vals[:, 1] = 0.0  # Prior expectation for innovation
        elif strategy_mode == 4:
            n_copier = int(0.80 * N)
            n_innov = int(0.10 * N)
            n_adapt = N - (n_copier + n_innov)
            q_vals = np.zeros((n_adapt, 2))
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
            H = self.H_high if t >= self.T_shock else self.H_low
            actions = np.zeros(N, dtype=int)  # 0: copy, 1: innovate

            if strategy_mode == 0:
                actions[:] = 0
            elif strategy_mode == 1:
                actions[:] = 1
            elif strategy_mode == 2:
                v_copy = q_vals[:, 0] / self.tau
                v_innov = q_vals[:, 1] / self.tau
                max_v = np.maximum(v_copy, v_innov)
                exp_c = np.exp(v_copy - max_v)
                exp_i = np.exp(v_innov - max_v)
                p_innov = exp_i / (exp_c + exp_i)
                actions = (rng.random(size=N) < p_innov).astype(int)
            elif strategy_mode == 3:
                p_inv = fixed_innov_prob if fixed_innov_prob is not None else 0.05
                actions = (rng.random(size=N) < p_inv).astype(int)
            elif strategy_mode == 4:
                n_copier = int(0.80 * N)
                n_innov = int(0.10 * N)
                n_adapt = N - (n_copier + n_innov)
                actions[:n_copier] = 0
                actions[n_copier : n_copier + n_innov] = 1
                if n_adapt > 0:
                    v_copy = q_vals[:, 0] / self.tau
                    v_innov = q_vals[:, 1] / self.tau
                    max_v = np.maximum(v_copy, v_innov)
                    exp_c = np.exp(v_copy - max_v)
                    exp_i = np.exp(v_innov - max_v)
                    p_innov = exp_i / (exp_c + exp_i)
                    actions[n_copier + n_innov :] = (rng.random(size=n_adapt) < p_innov).astype(int)

            z_next = np.copy(z)
            costs = np.zeros(N)

            copy_idx = np.where(actions == 0)[0]
            if len(copy_idx) > 0:
                costs[copy_idx] = self.cost_copy
                z_shifted = z - np.min(z) + 1e-4
                weights = z_shifted**self.alpha_prestige
                denom = np.sum(weights)
                probs = (
                    weights / denom
                    if denom > 0
                    else np.ones(N) / N
                )
                models = rng.choice(N, size=len(copy_idx), p=probs, replace=True)
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

            # Update Q-values
            if strategy_mode == 2:
                for act in [0, 1]:
                    mask = actions == act
                    if np.any(mask):
                        rpe = payoffs[mask] - q_vals[mask, act]
                        q_vals[mask, act] += self.eta * rpe
            elif strategy_mode == 4:
                adapt_idx = slice(n_copier + n_innov, N)
                sub_actions = actions[adapt_idx]
                sub_payoffs = payoffs[adapt_idx]
                for act in [0, 1]:
                    mask = sub_actions == act
                    if np.any(mask):
                        rpe = sub_payoffs[mask] - q_vals[mask, act]
                        q_vals[mask, act] += self.eta * rpe

            z = z_next

            history["mean_payoff"][t] = np.mean(payoffs)
            history["mean_skill"][t] = np.mean(z)
            history["diversity"][t] = np.std(z)
            history["pct_innovating"][t] = np.mean(actions == 1) * 100.0

        return history

    def run_ensemble(self, n_runs: int = 50) -> Dict[str, Dict]:
        """
        Run 50-run Monte Carlo ensembles for all 5 core strategies.
        """
        strategy_labels = [
            "Pure Copiers (100% Social)",
            "Pure Innovators (100% Individual)",
            "Adaptive Social Brain (Delta Rule)",
            "Static Fixed Mixture (5% Innov)",
            "Heterogeneous Society (Labor Division)",
        ]

        master_rng = np.random.default_rng(self.seed)
        run_seeds = master_rng.integers(100000, 999999, size=n_runs)

        results = {}
        metrics = ["mean_payoff", "mean_skill", "diversity", "pct_innovating"]

        for s_idx, s_label in enumerate(strategy_labels):
            raw_data = {m: np.zeros((n_runs, self.T)) for m in metrics}
            for r, r_seed in enumerate(run_seeds):
                r_rng = np.random.default_rng(r_seed)
                run_hist = self.simulate_single_run(s_idx, r_rng)
                for m in metrics:
                    raw_data[m][r, :] = run_hist[m]

            stats = {}
            for m in metrics:
                arr = raw_data[m]
                stats[m] = {
                    "mean": np.mean(arr, axis=0),
                    "lower_95": np.percentile(arr, 2.5, axis=0),
                    "upper_95": np.percentile(arr, 97.5, axis=0),
                }

            cum_payoffs = np.sum(raw_data["mean_payoff"], axis=1)
            stats["cumulative_payoff"] = {
                "mean": float(np.mean(cum_payoffs)),
                "std": float(np.std(cum_payoffs)),
            }
            results[s_label] = stats

        return results

    def run_fixed_mixture_sweep(
        self,
        sweep_grid: Optional[List[float]] = None,
        n_runs: int = 50,
    ) -> pd.DataFrame:
        """
        Execute parametric sweep across fixed copier proportions (0% to 100% in 10% steps),
        directly implementing Prof. Alexey Koshevoy's requested experiment.
        """
        if sweep_grid is None:
            # Sweeping Copier Proportion: 0%, 10%, 20%, ..., 90%, 100%
            sweep_grid = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]

        master_rng = np.random.default_rng(self.seed + 777)
        run_seeds = master_rng.integers(100000, 999999, size=n_runs)

        records = []
        for p_copier in sweep_grid:
            p_innov = 1.0 - p_copier
            cums, pre_payoffs, post_payoffs, final_skills = [], [], [], []
            for r_seed in run_seeds:
                r_rng = np.random.default_rng(r_seed)
                hist = self.simulate_single_run(3, r_rng, fixed_innov_prob=p_innov)
                cums.append(np.sum(hist["mean_payoff"]))
                pre_payoffs.append(hist["mean_payoff"][self.T_shock - 1])
                post_payoffs.append(hist["mean_payoff"][-1])
                final_skills.append(hist["mean_skill"][-1])

            mean_post = float(np.mean(post_payoffs))
            status = "Resilient (Payoff > 0)" if mean_post > 0 else "Collapsed (Payoff < 0)"

            records.append({
                "Copier_Proportion": f"{int(round(p_copier * 100))}%",
                "Innovator_Proportion": f"{int(round(p_innov * 100))}%",
                "Pre_Shock_Payoff": float(np.mean(pre_payoffs)),
                "Post_Shock_Payoff": mean_post,
                "Cumulative_Payoff": float(np.mean(cums)),
                "Std_Cumulative_Payoff": float(np.std(cums, ddof=1)),
                "Final_Skill": float(np.mean(final_skills)),
                "Survival_Status": status,
            })

        return pd.DataFrame(records)

    def run_general_case_phase_diagram(
        self,
        copier_grid: Optional[List[float]] = None,
        harshness_grid: Optional[List[float]] = None,
        loss_grid: Optional[List[float]] = None,
        n_runs: int = 20,
    ) -> Dict[str, Any]:
        """
        Compute general 2D phase boundaries across:
        1) Copier proportion vs. Post-Shock Environmental Harshness (H_high)
        2) Copier proportion vs. Henrich Gumbel Transmission Loss (gumbel_loss)
        """
        if copier_grid is None:
            copier_grid = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
        if harshness_grid is None:
            harshness_grid = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0]
        if loss_grid is None:
            loss_grid = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]

        master_rng = np.random.default_rng(self.seed + 888)
        run_seeds = master_rng.integers(100000, 999999, size=n_runs)

        # Matrix 1: Harshness (rows) x Copier Proportion (cols)
        orig_H_high = self.H_high
        orig_loss = self.gumbel_loss

        mat_harshness = np.zeros((len(harshness_grid), len(copier_grid)))
        for i, h_val in enumerate(harshness_grid):
            self.H_high = h_val
            for j, p_copier in enumerate(copier_grid):
                p_innov = 1.0 - p_copier
                posts = []
                for r_seed in run_seeds:
                    r_rng = np.random.default_rng(r_seed)
                    hist = self.simulate_single_run(3, r_rng, fixed_innov_prob=p_innov)
                    posts.append(hist["mean_payoff"][-1])
                mat_harshness[i, j] = float(np.mean(posts))
        self.H_high = orig_H_high

        # Matrix 2: Gumbel Loss (rows) x Copier Proportion (cols) at baseline H_high
        mat_loss = np.zeros((len(loss_grid), len(copier_grid)))
        for i, l_val in enumerate(loss_grid):
            self.gumbel_loss = l_val
            for j, p_copier in enumerate(copier_grid):
                p_innov = 1.0 - p_copier
                posts = []
                for r_seed in run_seeds:
                    r_rng = np.random.default_rng(r_seed)
                    hist = self.simulate_single_run(3, r_rng, fixed_innov_prob=p_innov)
                    posts.append(hist["mean_payoff"][-1])
                mat_loss[i, j] = float(np.mean(posts))
        self.gumbel_loss = orig_loss

        return {
            "copier_grid": copier_grid,
            "harshness_grid": harshness_grid,
            "loss_grid": loss_grid,
            "payoff_vs_harshness": mat_harshness,
            "payoff_vs_loss": mat_loss,
        }

    def run_replicator_dynamics(
        self,
        n_runs: int = 50,
        mu: float = 0.02,
    ) -> Dict[str, np.ndarray]:
        """
        Simulate endogenous frequency-dependent replicator dynamics with mutation mu.
        """
        master_rng = np.random.default_rng(self.seed + 999)
        run_seeds = master_rng.integers(100000, 999999, size=n_runs)

        props_history = np.zeros((n_runs, self.T, 3))
        payoff_history = np.zeros((n_runs, self.T))
        skill_history = np.zeros((n_runs, self.T))

        for r, r_seed in enumerate(run_seeds):
            rng = np.random.default_rng(r_seed)
            props = np.array([1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0])
            z = rng.uniform(6.0, 7.0, size=self.N)
            q_vals = np.zeros((self.N, 2))
            q_vals[:, 0] = 3.5
            q_vals[:, 1] = 0.0

            for t in range(self.T):
                props_history[r, t] = props
                H = self.H_high if t >= self.T_shock else self.H_low

                counts = np.round(props * self.N).astype(int)
                counts[2] = self.N - (counts[0] + counts[1])
                c0, c1, c2 = counts[0], counts[1], counts[2]

                actions = np.zeros(self.N, dtype=int)
                if c1 > 0:
                    actions[c0 : c0 + c1] = 1

                if c2 > 0:
                    ad_slice = slice(c0 + c1, self.N)
                    v_copy = q_vals[ad_slice, 0] / self.tau
                    v_innov = q_vals[ad_slice, 1] / self.tau
                    max_v = np.maximum(v_copy, v_innov)
                    exp_c = np.exp(v_copy - max_v)
                    exp_i = np.exp(v_innov - max_v)
                    p_innov = exp_i / (exp_c + exp_i)
                    actions[ad_slice] = (rng.random(size=c2) < p_innov).astype(int)

                z_next = np.copy(z)
                costs = np.zeros(self.N)

                copy_idx = np.where(actions == 0)[0]
                if len(copy_idx) > 0:
                    costs[copy_idx] = self.cost_copy
                    z_shifted = z - np.min(z) + 1e-4
                    weights = z_shifted**self.alpha_prestige
                    denom = np.sum(weights)
                    probs = weights / denom if denom > 0 else np.ones(self.N) / self.N
                    models = rng.choice(self.N, size=len(copy_idx), p=probs, replace=True)
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
                        sub = actions[ad_slice] == act
                        if np.any(sub):
                            g_idx = np.where(actions[ad_slice] == act)[0] + (c0 + c1)
                            rpe = payoffs[g_idx] - q_vals[g_idx, act]
                            q_vals[g_idx, act] += self.eta * rpe

                z = z_next

                p0 = np.mean(payoffs[:c0]) if c0 > 0 else 0.0
                p1 = np.mean(payoffs[c0 : c0 + c1]) if c1 > 0 else 0.0
                p2 = np.mean(payoffs[c0 + c1 :]) if c2 > 0 else 0.0

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
