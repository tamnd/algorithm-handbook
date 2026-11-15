## What to remember

- The [survival function](/survival-function/) and the [hazard](/hazard-function/) describe the same law. In continuous time $h = f/S$ and $S(t) = \exp(-H(t))$ with $H(t) = \int_0^t h$. In discrete time $S(t) = \prod_{t_j \le t}(1 - h_j)$, which is at most $\exp(-\sum_{t_j \le t} h_j)$.
- Every method of the chapter assumes independent [censoring](/censoring/), and data $(Y, \delta)$ cannot test it (Tsiatis).
- The [Kaplan-Meier estimator](/kaplan-meier-estimator/) is $\hat S(t) = \prod_{t_j \le t}(1 - d_j/n_j)$, with $d_j$ events among $n_j$ at risk. It is the nonparametric MLE. The [Nelson-Aalen estimator](/nelson-aalen-estimator/) $\hat H(t) = \sum_{t_j \le t} d_j/n_j$ always gives $\exp(-\hat H) \ge \hat S$.
- [Greenwood's formula](/greenwood-formula/) $\hat S(t)^2\sum_{t_j \le t} d_j/(n_j(n_j - d_j))$ estimates the variance of $\hat S(t)$. Its intervals are pointwise and asymptotic; the log-log interval $\bigl(\hat S^{\exp(z\hat\tau)}, \hat S^{\exp(-z\hat\tau)}\bigr)$ stays inside $(0, 1)$.
- The [log-rank test](/log-rank-test/) sums observed minus expected events, $U = \sum_j (d_{1j} - d_j n_{1j}/n_j)$, with hypergeometric variance $V = \sum_j d_j(n_j - d_j)n_{1j}n_{0j}/(n_j^2(n_j - 1))$. Under equal hazards $U^2/V$ is asymptotically $\chi^2_1$. It is the score test of the Cox model.
- The [Cox model](/cox-proportional-hazards-model/) $h(t \mid x) = h_0(t)e^{\beta^{\mathsf T}x}$ is fitted by the [partial likelihood](/cox-partial-likelihood/) $\prod_j e^{\beta^{\mathsf T}x_{(j)}}/\sum_{i \in R(t_j)} e^{\beta^{\mathsf T}x_i}$, which does not contain $h_0$ and has a concave logarithm. The [Breslow estimator](/breslow-estimator/) recovers $H_0$, and the [Schoenfeld residuals](/schoenfeld-residuals/) check proportionality.
- In the [accelerated failure time model](/accelerated-failure-time-model/) $\log T = \mu + \gamma^{\mathsf T}x + \sigma W$, $e^{\gamma_k}$ multiplies every quantile. The Weibull model is both AFT and proportional hazards, with hazard ratio $e^{-\gamma^{\mathsf T}x/\sigma}$. In a gamma [frailty model](/frailty-model/) the marginal hazard ratio $r(1 + \theta H_0)/(1 + \theta r H_0)$ drifts from $r$ towards $1$.
- With [competing risks](/competing-risks/) the cumulative incidence $F_k(t) = \int_0^t S(u-)\,dH_k(u)$ is the probability of a cause-$k$ event by $t$, and $\sum_k F_k + S = 1$. One minus Kaplan-Meier with the other causes censored overstates it. The [Aalen-Johansen estimator](/aalen-johansen-estimator/) estimates $F_k$, and the [Fine-Gray model](/fine-gray-model/) puts covariates on it.
- [Harrell's C](/harrell-c-index/) is the fraction of comparable pairs ordered correctly by the risk score. Its value depends on the censoring.

| method | estimates or tests | data | time | what is guaranteed |
|---|---|---|---|---|
| Kaplan-Meier | $S(t)$ | right-censored | $\Theta(n \log n)$ | nonparametric MLE; Greenwood intervals asymptotic |
| Nelson-Aalen | $H(t)$ | right-censored | $\Theta(n \log n)$ | asymptotically normal |
| Turnbull | $S(t)$ | interval-censored | $\Theta(n \log n + k\,nm)$ for $k$ iterations | NPMLE as the limit of EM |
| log-rank | $h_1 = h_0$ | right-censored groups | $\Theta(n \log n)$ | asymptotic $\chi^2_1$; permutation version exact only with equal censoring |
| Cox partial likelihood | $\beta$ | right-censored, covariates | $O(n \log n)$ once, $O(np^2 + p^3)$ per Newton step | asymptotically normal under proportional hazards |
| Breslow | $H_0(t)$ | after a Cox fit | $\Theta(n \log n + np)$ | consistent under the Cox model |
| Aalen-Johansen | $F_k(t)$, transition matrices | competing risks, multistate | $\Theta(n \log n + mK)$ | asymptotic, under independent censoring |
| Fine-Gray | subdistribution $\beta$ | competing risks, covariates | $O(np^2 + p^3)$ per Newton step after a sort | asymptotic, sandwich variance |
| Harrell's C | ranking quality | right-censored, scores | $O(n \log n)$ with a Fenwick tree | descriptive; depends on the censoring |

: The main methods of the chapter. $n$ subjects, $p$ covariates, $m$ distinct event times (innermost intervals for Turnbull), $K$ causes.

## Choosing a method

To describe one sample, plot the Kaplan-Meier curve with log-log Greenwood intervals. Use Nelson-Aalen for the cumulative hazard itself. If the event is only known to lie between two examinations, use the Turnbull estimator rather than imputing the midpoint.

To compare groups, the log-rank test is the default and is most sensitive under proportional hazards. When the curves are expected to differ early or late, choose a weighted test in advance; choosing the weight after seeing the curves invalidates the level. To adjust for covariates, fit a Cox model, get predicted curves from the Breslow estimate, and plot the scaled Schoenfeld residuals against time before reading the hazard ratios. If proportional hazards fails and a parametric law fits, an AFT model gives time ratios. For clustered subjects, a frailty model or a sandwich variance accounts for the dependence.

When other events can prevent the one of interest, report the Aalen-Johansen cumulative incidence, not one minus Kaplan-Meier. For effects on the rate among those still event-free, fit cause-specific Cox models; for effects on the risk itself, fit a Fine-Gray model, one cause at a time. To judge a risk score, report Harrell's C with the amount of censoring, or Uno's weighted version.
