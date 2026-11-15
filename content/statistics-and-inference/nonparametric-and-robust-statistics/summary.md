## What to remember

- The [empirical distribution function](/empirical-distribution-function/) $F_n$ of an independent sample converges to $F$ uniformly, almost surely ([Glivenko-Cantelli](/glivenko-cantelli-theorem/)). The [DKW inequality](/dkw-inequality/) gives $P(\sup_t |F_n(t) - F(t)| > \varepsilon) \le 2e^{-2n\varepsilon^2}$ for every $n$, so $F_n \pm \sqrt{\ln(2/\alpha)/(2n)}$ is a confidence band of level $1 - \alpha$. The [Kolmogorov-Smirnov test](/kolmogorov-smirnov-test/) is distribution-free only for a continuous model fixed in advance.
- The [bootstrap](/bootstrap-method/) replaces $F$ by $F_n$. Its guarantees are asymptotic, and it fails for the maximum, for heavy tails and at a boundary, where [subsampling](/subsampling-inference/) with $m \to \infty$, $m/n \to 0$ still works. The [block bootstrap](/block-bootstrap/) handles time series.
- The [percentile interval](/bootstrap-percentile-interval/) is first-order accurate, the [bootstrap-t](/bootstrap-t-interval/) and [BCa](/bca-bootstrap-interval/) intervals second-order for smooth statistics. Small-sample coverage is only measured: for the exponential mean with $n = 10$ (1000 data sets, $b = 1000$, seed 101), nominal 0.95 intervals covered 0.884 (BCa) and 0.943 (bootstrap-t).
- Counting gives exact tests. The [sign test](/sign-test/), the [permutation test](/permutation-test/) and the rank tests have exact level at every $n$ when the data are exchangeable under the null, and so does the Monte Carlo p-value $(1 + c)/(1 + b)$. The chi-square laws of the [Kruskal-Wallis](/kruskal-wallis-test/) and [Friedman](/friedman-test/) statistics are asymptotic. A p-value is not the probability that the null is true.
- Against the t test at the normal, the sign test has asymptotic relative efficiency $2/\pi$ and the [Wilcoxon signed-rank test](/wilcoxon-signed-rank-test/) $3/\pi$, at least $0.864$ for every symmetric law. The [Mann-Whitney test](/mann-whitney-u-test/) tests $P(X > Y) = 1/2$, not equal medians.
- The [breakdown point](/breakdown-point/) counts the replaced points an estimator survives, and the [influence function](/influence-function/) measures one infinitesimal outlier. [Huber's estimator](/huber-m-estimator/) is minimax for the asymptotic variance over the [contamination model](/huber-contamination-model/).
- [Theil-Sen](/theil-sen-estimator/) breaks down at $1 - 1/\sqrt2$ and runs in $O(n \log n)$ expected time by inversion counts. [Least median of squares](/least-median-of-squares/) reaches $\lfloor n/2 \rfloor / n$ at rate $n^{-1/3}$, [least trimmed squares](/least-trimmed-squares/) converges at rate $n^{-1/2}$, and the [MM-estimator](/mm-estimator/) adds 95% efficiency. The [Tukey median](/tukey-median/) in $d$ dimensions has breakdown point at least $1/(d + 1)$; for corrupted $N(\mu, I_d)$ data the [filter](/robust-mean-estimation-filter/) has error $O(\varepsilon\sqrt{\log(1/\varepsilon)})$, free of $d$.
- A [kernel density estimate](/kernel-density-estimation/) has best bandwidth of order $n^{-1/5}$ and AMISE of order $n^{-4/5}$. [Split conformal prediction](/split-conformal-prediction/) uses the $k$-th smallest of $n_2$ calibration scores, $k = \lceil (n_2 + 1)(1 - \alpha) \rceil$, and covers with probability between $1 - \alpha$ and $1 - \alpha + 1/(n_2 + 1)$ for exchangeable data with distinct scores, marginally and not given $x$.

| Estimator | Breakdown point | Efficiency at the normal | Time |
|---|---|---|---|
| Mean | $1/n$ | 1 | $\Theta(n)$ |
| [Median](/median/) | $\lceil n/2 \rceil / n$ | $2/\pi \approx 0.637$ | $\Theta(n)$ expected |
| [Trimmed mean](/trimmed-mean/), $\alpha = 0.2$ | $(g + 1)/n$ | 0.874 | $\Theta(n)$ average |
| Huber, $k = 1.345$, MAD scale | $\lceil n/2 \rceil / n$ | 0.95 | $\Theta(n \log n)$ |
| [Hodges-Lehmann](/hodges-lehmann-estimator/) | $\to 1 - 1/\sqrt2 \approx 0.293$ | $3/\pi \approx 0.955$ | $\Theta(n \log n)$ average |
| [MAD](/median-absolute-deviation/), as a scale | $\lfloor n/2 \rfloor / n$ | 0.3675 | $\Theta(n)$ expected |
| Theil-Sen line | $\to 0.293$ | | $O(n \log n)$ expected |
| [Repeated median](/repeated-median-regression/) line | $\lfloor n/2 \rfloor / n$ | | $O(n \log^2 n)$ expected |
| Least median of squares | $\lfloor n/2 \rfloor / n$ | rate $n^{-1/3}$ | $O(n^3 \log n)$ |
| Least trimmed squares | $(\lfloor (n - p)/2 \rfloor + 1)/n$ | about 0.07 | random starts, C-steps |
| MM-estimator | $1/2$ | 0.95 | random subsets, reweighting |

: Robust estimators of location, scale and a regression line, with $g = \lfloor \alpha n \rfloor$, $p$ coefficients and the LTS coverage $h = \lfloor (n + p + 1)/2 \rfloor$. Efficiencies are asymptotic; the entries give no asymptotic value for the two median-of-slopes lines.

## Choosing a method

For a small sample, use an exact test: the sign test or the signed-rank test (for symmetric differences) on pairs, Mann-Whitney or a permutation test for two groups, Kruskal-Wallis for several and Friedman for blocks. Keep the chi-square approximation for larger samples.

For an interval, start with the bootstrap and the percentile interval, and move to BCa or the bootstrap-t for skewed statistics. For a maximum, a boundary or heavy tails, use subsampling or the m-out-of-n bootstrap.

For location, start from the median and the MAD, then gain efficiency with the Huber estimator or the [biweight](/tukey-biweight/). For a line with at most a quarter of bad points, Theil-Sen is simple; with more, use LTS or an MM-estimator, and the [minimum covariance determinant](/minimum-covariance-determinant/) to flag multivariate outliers. For prediction intervals, put split conformal prediction on top of any fitted model.
