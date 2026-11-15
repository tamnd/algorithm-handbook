## What to remember

- A **credible interval** is a statement about the parameter given the data and the prior. Averaged over a proper prior, its coverage is exactly $1 - \alpha$; at a fixed parameter it can be far from that. The two agree in the limit under the conditions of the [Bernstein-von Mises theorem](/bernstein-von-mises-theorem/), which fail at a boundary, for Uniform$(0, \theta)$, and for a prior with no mass near the truth.
- **The loss picks the estimate.** Squared loss gives the posterior mean, absolute loss the median, and a linear loss with costs $c_1$ for underestimating and $c_2$ for overestimating the quantile of order $c_1/(c_1 + c_2)$. The posterior mode, like a [highest posterior density region](/highest-posterior-density-interval/), changes with the parametrization; quantiles do not.
- An **improper prior** is usable only when the posterior is proper; proper full conditionals do not prove it. Bayes factors with an improper prior on a parameter that only one model has are not defined.
- The **Jeffreys prior** is invariant under reparametrization but depends on the sampling design: binomial and negative binomial data with the same likelihood get different posteriors. With one parameter the [reference prior](/reference-prior/) is the Jeffreys prior.
- In a **hierarchical model** given $\mu$ and $\tau$, each group estimate is pulled toward $\mu$ by the factor $\sigma_j^2/(\sigma_j^2 + \tau^2)$. The prior $1/\tau$ gives an improper posterior for every data set. [Empirical Bayes](/empirical-bayes/) plugs in $\hat\tau$, which can be 0, and then hides the uncertainty about $\tau$.
- The **Bayes factor** depends on the prior under the alternative, even when the posterior hardly does. With $z$ fixed and $n$ growing, it favours a point null that a fixed-level test rejects ([Lindley paradox](/lindley-paradox/)). For every prior $B_{01} \ge e^{-z^2/2}$, so at even prior odds $z = 1.96$ never puts the null's posterior probability below $0.128$.
- **Every computation here is approximate or random.** Markov chains converge only in the limit. ABC targets the posterior given the summaries within a tolerance, which is the posterior only with a sufficient summary and tolerance zero.
- **Checking a model and checking a computation are different tasks.** The p-value of a [posterior predictive check](/posterior-predictive-check/) is not uniform: under the prior predictive law it has mean $1/2$ and only $P(p_B \le \alpha) \le 2\alpha$. [Simulation-based calibration](/simulation-based-calibration/) assumes the model and tests the sampler.

## The computing methods side by side

| Method | Gives | Accuracy | Time |
|---|---|---|---|
| [Laplace approximation](/laplace-approximation/) | normal posterior, $\log Z$ | relative error $O(1/n)$ for $Z$ in regular models | one optimization |
| [INLA](/integrated-nested-laplace-approximation/) | posterior marginals | exact for a Gaussian likelihood only | $\Theta(KGIC)$ per marginal |
| [Bridge sampling](/bridge-sampling/) | ratio of normalizing constants | Monte Carlo error | $\Theta(nT)$ |
| [Nested sampling](/nested-sampling/) | $\log Z$ and weighted draws | error about $\sqrt{H/N}$, a heuristic | $\Theta(N(H + K)C)$ |
| [ABC rejection](/abc-rejection-sampling/) | independent draws | targets the $\varepsilon$-posterior | $\Theta(NC/A)$ expected |
| [ABC-SMC](/abc-sequential-monte-carlo/) | weighted draws | targets the $\varepsilon_T$-posterior | $\Theta(T(N^2 + NC/A))$ expected |
| [PSIS-LOO](/pareto-smoothed-importance-sampling-loo/) | $\mathrm{elpd}_{\mathrm{loo}}$ and $\hat k$ | Monte Carlo; trusted when $\hat k$ is small | $\Theta(nS\log S)$ |
| Simulation-based calibration | a test of a sampler | necessary, not sufficient | $\Theta(N(S + C + L))$ |

: Methods for computing and checking posteriors. The symbols in the time column are defined in each entry.

## Choosing a method

- **One parameter, conjugate model.** Use the closed form, and [Bayesian linear regression](/bayesian-linear-regression/) for a normal linear model.
- **Many groups of similar units.** Fit a [hierarchical model](/hierarchical-bayesian-model/) with a proper prior on the spread, such as a half-Cauchy. Empirical Bayes is close to it when there are many groups.
- **Two models, one nested in the other.** Compute the Bayes factor with the [Savage-Dickey density ratio](/savage-dickey-density-ratio/) when the priors are compatible, and report how it moves with the prior.
- **Two models that are not nested.** Estimate each marginal likelihood by bridge sampling or nested sampling. Avoid the harmonic mean estimator, whose variance is often infinite. For prediction, compare by PSIS-LOO or average with [Bayesian model averaging](/bayesian-model-averaging/).
- **Many coefficients, few of them large.** Use a [spike-and-slab prior](/spike-and-slab-prior/) for inclusion probabilities, a [horseshoe prior](/horseshoe-prior/) for a continuous shrinkage rule.
- **A latent Gaussian field with a few hyperparameters.** Use INLA; prefer Monte Carlo for binary data with one observation per latent value.
- **A simulator without a likelihood.** Use ABC rejection when the prior is narrow, ABC-SMC when it is wide, and check the result with simulation-based calibration.
- **New sampler code.** Run simulation-based calibration first, then a posterior predictive check on the model.
