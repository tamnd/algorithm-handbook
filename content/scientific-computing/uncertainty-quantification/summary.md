## What to remember

- **Monte Carlo** estimates $\mathbb{E}[Q]$ with the standard error $\sigma/\sqrt N$, independent of the number of inputs. A probability $p$ needs about $(1-p)/(p\,\delta^2)$ samples for a relative error $\delta$. [Quasi-Monte Carlo](/quasi-monte-carlo-integration/) has the [Koksma-Hlawka](/koksma-hlawka-inequality/) bound $V(f)\,D_N^*$ for integrands of bounded variation.
- **Multilevel Monte Carlo.** If the bias decays like $2^{-\alpha l}$, the level variance like $2^{-\beta l}$ and the cost grows like $2^{\gamma l}$, with $\alpha \ge \frac12\min(\beta, \gamma)$, the cost for root mean square error $\varepsilon$ is $O(\varepsilon^{-2})$ if $\beta > \gamma$, $O(\varepsilon^{-2}(\log\varepsilon)^2)$ if $\beta = \gamma$ and $O(\varepsilon^{-2-(\gamma-\beta)/\alpha})$ if $\beta < \gamma$. The bounds hold only under these rate assumptions.
- **Polynomial chaos.** The mean is $c_0$ and the variance $\sum_{\alpha \ne 0} c_\alpha^2$ for an orthonormal basis; a total degree $p$ in $d$ inputs has $\binom{d+p}{p}$ terms. The coefficients decay fast, spectrally, only when the output depends smoothly on the inputs; a kink or a jump slows them to an algebraic rate.
- **Sparse grids** replace the $m^d$ nodes of a tensor rule by $O(2^L L^{d-1})$ nodes. They reduce the curse of dimension but do not remove it, and their fast rates are again for smooth dependence.
- **Reliability.** FORM gives $P_f \approx \Phi(-\beta)$ with $\beta$ the distance from the origin to the most probable failure point in standard normal space. It is exact for a linear limit state; the HL-RF iteration is not guaranteed to converge. Subset simulation needs about $\log P_f/\log p_0$ levels.
- **Sobol indices.** For independent inputs the Hoeffding-Sobol decomposition is unique, $0 \le S_i \le S_{Ti} \le 1$ and $\sum_i S_i \le 1 \le \sum_i S_{Ti}$. The Saltelli scheme estimates all $S_i$ and $S_{Ti}$ from $N(d+2)$ runs; the results are estimates with sampling error, and the decomposition fails for dependent inputs.
- **Reduced models.** POD keeps the modes with the largest eigenvalues, and the snapshot error is $\sum_{i>r}\lambda_i$. The reduced basis method gives a certified error bound relative to the finite element solution, with an online cost independent of $n$ for affine problems. The weak greedy algorithm inherits polynomial or exponential decay of the Kolmogorov width.
- **Bayesian calibration.** With a Gaussian prior, Gaussian noise and a forward map that satisfies the growth conditions of the theorem, the posterior exists and is locally Lipschitz in the data in the Hellinger distance. Without a discrepancy term, a calibrated parameter can be overconfident and wrong.

## The methods side by side

| Method | Runs of the model | Error | Needs |
|---|---|---|---|
| [Monte Carlo](/forward-uncertainty-propagation/) | $N$ | $\sigma/\sqrt N$ | only samples |
| [Multilevel Monte Carlo](/multilevel-monte-carlo/) | $N_l$ on each level | cost $\varepsilon^{-2}$ to $\varepsilon^{-2-(\gamma-\beta)/\alpha}$ | a hierarchy with rates $\alpha$, $\beta$, $\gamma$ |
| [Multifidelity Monte Carlo](/multifidelity-monte-carlo/) | $m_i$ of model $i$ | unbiased, smaller variance | correlated cheap models |
| [Spectral projection](/non-intrusive-spectral-projection/) | $m^d$ | truncation plus aliasing | smooth dependence, small $d$ |
| [Stochastic collocation](/stochastic-collocation-method/) | $O(2^L L^{d-1})$ | interpolation exact for total degree $L$, quadrature for $2L+1$ | smooth dependence |
| [Regression chaos](/regression-polynomial-chaos/) | $N \ge P$, often $2P$ to $3P$ | least squares | $P = \binom{d+p}{p}$ terms |
| [Stochastic Galerkin](/stochastic-galerkin-method/) | one coupled system | best in the energy norm | access to the solver |
| [FORM](/first-order-reliability-method/) | $K$ gradient steps | exact for linear $G$ | a smooth limit state |
| [Subset simulation](/subset-simulation/) | $N + (m-1)(1-p_0)N$ | coefficient of variation measured | MCMC in each level |

: Costs and errors as the entries state them. $P$ is the number of chaos terms, $m$ the number of Gauss points per input or of subset levels, and $K$ the number of HL-RF iterations. The rule of $2P$ to $3P$ runs is a heuristic.

## Choosing a method

If the model is cheap or the inputs are many and rough, use Monte Carlo, with quasi-Monte Carlo points when the integrand is smooth enough. If the model is an SDE or a PDE solved on a grid, use multilevel Monte Carlo; if cheaper models of the same quantity exist, use multifidelity Monte Carlo. For a small failure probability, start with FORM to find the design point, and check it with subset simulation or importance sampling there.

When the output depends smoothly on a few inputs, a polynomial chaos expansion or a sparse grid surrogate gives the mean, the variance and the Sobol indices from far fewer runs. Screen many inputs first with the Morris method, and keep only those that matter. When the same parametrized PDE is solved many times, build a reduced basis or a POD-Galerkin model offline, with empirical interpolation for its nonlinear terms.
