## What to remember

- A weakly [stationary process](/stationary-process/) has a constant mean and an autocovariance $\gamma(h)$ that depends only on the lag. Sample autocovariances with divisor $n$ give positive semidefinite matrices $[\hat\gamma(i - j)]$; with divisor $n - h$ they may not.
- [AR($p$)](/autoregressive-model/) $\phi(B)X_t = Z_t$ is causal, and [MA($q$)](/moving-average-model/) $X_t = \theta(B)Z_t$ invertible, when the roots of $\phi(z)$, or of $\theta(z)$, lie outside the unit circle. The ACF of an MA($q$) is zero after lag $q$, the [PACF](/partial-autocorrelation-function/) of an AR($p$) is zero after lag $p$, and for an [ARMA](/arma-model/) model both tail off.
- [Yule-Walker](/yule-walker-equations/) costs $\Theta(np)$, always gives a causal fit, and for AR models has the large-sample law of maximum likelihood. The [innovations algorithm](/innovations-algorithm/) gives the exact Gaussian likelihood, and the [Whittle likelihood](/whittle-likelihood/) approximates it after one FFT.
- The [Ljung-Box statistic](/ljung-box-test/) $Q = n(n + 2)\sum_{k=1}^{h}\hat r_k^2/(n - k)$ is compared with $\chi^2_{h - p - q}$ for ARMA($p$, $q$) residuals, as an approximation.
- Unit-root statistics have nonstandard limits: the 5% points of the Dickey-Fuller $\tau$ are about $-1.94$, $-2.86$ and $-3.41$ with no constant, a constant, and a constant and trend, and the [Engle-Granger](/engle-granger-test/) residual test for two series needs about $-3.34$. [KPSS](/kpss-test/) takes stationarity as the null. In a cointegrated VAR, $\Pi = \alpha\beta^\top$ has rank $r$.
- [GARCH(1, 1)](/garch-model/) $\sigma_t^2 = \omega + \alpha\varepsilon_{t-1}^2 + \beta\sigma_{t-1}^2$ is covariance stationary if and only if $\alpha + \beta < 1$, with variance $\omega/(1 - \alpha - \beta)$.
- The [SPRT](/sequential-probability-ratio-test/) with $A = (1 - \beta)/\alpha$ and $B = \beta/(1 - \alpha)$ has error rates at most $\alpha/(1 - \beta)$ and $\beta/(1 - \alpha)$. Five looks at $|Z| \ge 1.96$ give type I error $0.1417$; [O'Brien-Fleming](/obrien-fleming-boundary/) boundaries $c_k = C\sqrt{I_K/I_k}$ bring it back to $\alpha$.
- [Change-point detection](/change-point-detection/) offline minimizes $F(t) = \min_{s < t}[F(s) + \mathcal C(s + 1, t) + \beta]$ exactly with $O(n^2)$ cost evaluations, and [PELT](/pelt-algorithm/) prunes without changing the answer. Online, [CUSUM](/cusum/) $S_t = \max(0, S_{t-1} + Z_t)$ with threshold $h$ has $E_\infty[T] \ge e^h$.
- By [Ville's inequality](/ville-inequality/), a [test martingale](/test-martingale/) ever reaches $1/\alpha$ with probability at most $\alpha$, so the [mixture SPRT](/mixture-sequential-probability-ratio-test/) has level $\alpha$ at every stopping time and [confidence sequences](/confidence-sequence/) cover at all times at once.

| Method | Cost | What holds |
|---|---|---|
| Yule-Walker | $\Theta(np)$ | causal fit; efficient for AR in large samples |
| Innovations algorithm | $\Theta(n^3)$, $\Theta(nq^2)$ for MA($q$) | exact Gaussian likelihood |
| Whittle likelihood | $O(n \log n)$, then $O(N(p + q))$ per evaluation | asymptotic, short memory |
| Ljung-Box test | $\Theta(nh)$ | approximate $\chi^2$ |
| Augmented Dickey-Fuller | $\Theta(nk^2)$ | asymptotic, nonstandard |
| Johansen test | $\Theta(nK^2p^2 + K^3)$ | asymptotic, nonstandard |
| PELT | $\Theta(n^2)$ worst, $O(n)$ expected under conditions | exact minimizer |
| Binary segmentation | $\Theta(n(m + 1))$ | greedy, not optimal |
| CUSUM | $\Theta(1)$ per observation | Lorden optimal |
| Bayesian online detector | $\Theta(t)$ at step $t$ | exact posterior under the model |
| SPRT | $\Theta(1)$ per observation | smallest $E_0[N]$ and $E_1[N]$ at its error rates |
| Mixture SPRT | $\Theta(1)$ per observation | level $\alpha$ at every stopping time |

: The main methods. $n$ observations, orders $p$ and $q$, $N$ frequencies, $h$ lags, $k$ regressors, $K$ series, $m$ change points.

## Choosing a method

For one stationary series, read the ACF and PACF, fit a low-order ARMA model by Gaussian maximum likelihood, and check the residuals with Ljung-Box. Use Yule-Walker for a quick AR fit or a starting value, and Whittle for long or long-memory series. Before differencing a trending series, run ADF and KPSS together. For forecasts with trend and season, Holt-Winters and STL need no model. Add GARCH when the size of the changes varies.

For several series with unit roots, test for cointegration, with Johansen when there are more than two series, and fit an error correction model. For change points in a stored series use PELT; on a stream with known distributions use CUSUM. For a few planned looks use a group sequential design; when the looks are not planned, use the mixture SPRT or a confidence sequence and accept the loss of power.
