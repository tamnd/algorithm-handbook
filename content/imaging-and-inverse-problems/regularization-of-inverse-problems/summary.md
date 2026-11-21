## What to remember

- **Compact operators have unbounded inverses.** A [Fredholm integral equation of the first kind](/fredholm-integral-equation-first-kind/) with a square-integrable kernel is compact, and its singular values tend to 0. The error $\delta u_k$ in the data becomes $(\delta/\sigma_k) v_k$ in the solution, so the third condition of a [well-posed problem](/well-posed-problem/) fails.
- **The singular value expansion explains everything linear.** $Ax = \sum_k \sigma_k\langle v_k, x\rangle u_k$. By the [Picard condition](/picard-condition/), $Ax = y$ has a solution exactly when $y$ lies in the closure of the range and $\sum_k |\langle u_k, y\rangle|^2/\sigma_k^2 < \infty$. The [degree of ill-posedness](/degree-of-ill-posedness/) is the decay rate of the $\sigma_k$: polynomial decay is mild or moderate, exponential decay is severe.
- **Linear methods differ only in their filter.** The estimate is $\sum_k f(\sigma_k)\,\langle u_k, y\rangle/\sigma_k\, v_k$. [Truncated SVD](/truncated-svd/) keeps or drops, Tikhonov uses $\sigma^2/(\sigma^2 + \alpha)$ and [Landweber iteration](/landweber-iteration/) uses $1 - (1 - \omega\sigma^2)^k$, which behaves like Tikhonov with $\alpha \approx 1/(\omega k)$.
- **The parameter trades bias against noise.** The noise part of a Tikhonov solution is at most $\delta/(2\sqrt\alpha)$, and the bias grows with $\alpha$. Iterative methods show [semi-convergence](/semi-convergence/): the error first falls and then rises as the iterates fit the noise.
- **Rates need smoothness.** Under a [source condition](/source-condition/) $x^\dagger = (A^*A)^\nu w$ with $\|w\| \le \rho$, the best possible worst-case error is of order $\rho^{1/(2\nu+1)}\delta^{2\nu/(2\nu+1)}$. A method reaches it only up to its [qualification](/qualification-of-regularization/): 1 for Tikhonov, which saturates at $\delta^{2/3}$, and infinite for truncated SVD and Landweber.
- **Rules that know the noise level converge; rules that do not cannot always.** The [discrepancy principle](/morozov-discrepancy-principle/) uses $\delta$ and gives convergence; with Tikhonov it is order optimal only for $\nu \le 1/2$. The [Bakushinskii veto](/bakushinskii-veto/) proves that no rule that ignores $\delta$ converges for every ill-posed problem, so [GCV](/generalized-cross-validation/), the [L-curve](/l-curve-method/) and the [quasi-optimality criterion](/quasi-optimality-criterion/) are heuristics that fail on some data.
- **Krylov methods are the fast iterative choice.** [CGLS](/cgls/) and [LSQR](/lsqr/) are equal in exact arithmetic. With the discrepancy principle CGLS is order optimal for every $\nu > 0$ and stops after $O(\delta^{-1/(2\nu+1)})$ steps, against $O(\delta^{-2/(2\nu+1)})$ for Landweber.
- **The Bayesian view gives Tikhonov back, and more.** In the [linear Gaussian inverse problem](/linear-gaussian-inverse-problem/) the posterior mean is a weighted Tikhonov solution, with $\alpha = \sigma^2/\gamma^2$ for white noise and a white prior. [pCN](/preconditioned-crank-nicolson-mcmc/) samples other posteriors with an acceptance rate that does not fall as the mesh is refined.

| Method | Filter $f(\sigma)$ | Parameter | Qualification | Best rate with the discrepancy principle | Main cost |
|:--|:--|:--|:--|:--|:--|
| Truncated SVD | 1 if $\sigma \ge \sigma_k$, else 0 | index $k$ | $\infty$ | $\delta^{2\nu/(2\nu+1)}$ for all $\nu$ | one SVD |
| Tikhonov | $\sigma^2/(\sigma^2 + \alpha)$ | $\alpha > 0$ | 1 | $\delta^{1/2}$ (a priori choice: $\delta^{2/3}$) | one solve per $\alpha$ |
| Iterated Tikhonov, $j$ steps | $1 - (\alpha/(\sigma^2 + \alpha))^j$ | $\alpha$, $j$ | $j$ | depends on the rule | $j$ solves per $\alpha$ |
| Landweber | $1 - (1 - \omega\sigma^2)^k$ | steps $k$ | $\infty$ | $\delta^{2\nu/(2\nu+1)}$ for all $\nu$ ($\tau$ large enough) | $k$ products with $A$ and $A^*$ |
| CGLS, LSQR | data dependent polynomial | steps $k$ | not a linear filter | $\delta^{2\nu/(2\nu+1)}$ for all $\nu$ | $k$ products, far fewer steps |

: The main linear and Krylov regularization methods. The rates hold under the source condition with exponent $\nu$ and are orders in $\delta$; constants are in the entries.

## Choosing a method

- **The SVD is affordable and the problem is linear.** Use [truncated SVD](/truncated-svd/) or Tikhonov, after a look at the Picard plot.
- **The noise level is known.** Use the [discrepancy principle](/morozov-discrepancy-principle/) with $\tau$ a little above 1. For Tikhonov with a smooth solution, the [Lepskii balancing principle](/lepskii-balancing-principle/) reaches higher orders.
- **The noise variance is known and the noise is white.** [UPRE](/unbiased-predictive-risk-estimator/) and [SURE](/stein-unbiased-risk-estimate/) estimate the risk without bias, but a wrong variance can make them fail badly.
- **The noise level is unknown.** Try [GCV](/generalized-cross-validation/) and the [L-curve](/l-curve-method/), and compare their answers. By the Bakushinskii veto they fail on some data; in the [comparison of rules](/regularization-parameter-choice/) GCV is 25 times worse than the best on one noise draw.
- **The operator is large and only products are available.** Use [CGLS](/cgls/) or [LSQR](/lsqr/) and stop by the discrepancy principle. [Hybrid Krylov regularization](/hybrid-krylov-regularization/) makes the stopping index less critical.
- **The forward operator is nonlinear.** Use the [iteratively regularized Gauss-Newton method](/iteratively-regularized-gauss-newton/).
- **Uncertainty is wanted, not one image.** Use the [linear Gaussian](/linear-gaussian-inverse-problem/) formulas if they apply. Otherwise sample with [pCN](/preconditioned-crank-nicolson-mcmc/), or with [randomize-then-optimize](/randomize-then-optimize/) when a least squares solver is at hand.
- **A local average with a stated resolution is the goal.** Use the [Backus-Gilbert method](/backus-gilbert-method/) or the [approximate inverse](/approximate-inverse/).
