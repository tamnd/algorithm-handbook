## What to remember

- A test has level $\alpha$ when $\sup_{\theta \in \Theta_0} P_\theta(\text{reject}) \le \alpha$. A [p-value](/p-value/) is valid when $P(p \le u) \le u$ under the null, and then "reject when $p \le \alpha$" has level $\alpha$. It is not $P(H_0 \mid \text{data})$. Discrete tests attain only some sizes: for $\text{Binomial}(20, 1/2)$, "reject when $X \ge 15$" has size $5425/262144 = 0.0207$.
- The values $\theta_0$ that a family of tests does not reject form a confidence set with coefficient $1$ minus the largest size ([test-interval duality](/test-interval-duality/)). A [pivot](/pivotal-quantity/) gives exact intervals: under normal iid data, $\bar x \pm t_{n-1, 1-\alpha/2}\,S/\sqrt n$ covers $\mu$ with probability exactly $1 - \alpha$. Coverage describes the procedure over repeated samples, not a posterior probability.
- The [binomial test](/binomial-test/), [Fisher's exact test](/fisher-exact-test/) and the [Clopper-Pearson interval](/clopper-pearson-interval/) hold their level for every $n$. The [chi-squared tests](/chi-squared-goodness-of-fit-test/) and the [likelihood ratio](/likelihood-ratio-test/), [Wald](/wald-test/) and [score](/score-test/) tests rely on limits: by [Wilks' theorem](/wilks-theorem/), $2(\ell(\hat\theta) - \ell(\hat\theta_0)) \to \chi^2_r$ under regularity and an interior null.
- [Neyman-Pearson](/neyman-pearson-lemma/): rejecting when $f_1(x)/f_0(x) > k$, randomized at the boundary, has the largest power among tests of its size. With a monotone likelihood ratio in $T$, "reject when $T$ is large" is [uniformly most powerful](/uniformly-most-powerful-test/) one-sided ([Karlin-Rubin](/karlin-rubin-theorem/)); two-sided problems have no UMP test in general.
- For a two-sided z-test, the [sample size](/sample-size-determination/) for power $1 - \beta$ at effect $\Delta$ is $\lceil ((z_{1-\alpha/2} + z_{1-\beta})\sigma/\Delta)^2 \rceil$, so it grows like $1/d^2$.
- [Bonferroni](/bonferroni-correction/) ($p_i \le \alpha/m$) and [Holm](/holm-bonferroni-method/) ($p_{(k)} \le \alpha/(m - k + 1)$ until the first failure) control the family-wise error rate strongly under any dependence. [Hochberg's](/hochberg-procedure/) step-up form needs the Simes inequality.
- The [false discovery rate](/false-discovery-rate/) $E[V/\max(R, 1)]$ is at most the FWER. [Benjamini-Hochberg](/benjamini-hochberg-procedure/) rejects the $k$ smallest p-values for the largest $k$ with $p_{(k)} \le kq/m$; its FDR is at most $(m_0/m)q$ under independence or positive regression dependence. Under arbitrary dependence, [Benjamini-Yekutieli](/benjamini-yekutieli-procedure/) runs BH at $q/\sum_{i=1}^m 1/i$.
- An [e-variable](/e-variable/) has $E_P[E] \le 1$ for every null $P$. By Markov's inequality, rejecting when $E \ge 1/\alpha$ has level $\alpha$, and products of e-variables built in sequence stay e-variables.

| Method | Guarantee | Holds under | Time |
|---|---|---|---|
| Binomial test | size $\le \alpha$, exact | independent trials | $\Theta(n)$ |
| t-test, t interval | size $\alpha$, coverage $1 - \alpha$, exact | normal iid data | $\Theta(n)$ |
| Welch's t-test | size near $\alpha$, approximate | two normal samples | $\Theta(m + n)$ |
| Clopper-Pearson interval | coverage $\ge 1 - \alpha$, exact | binomial count | $\Theta(nb)$ |
| Wilson interval | coverage near $1 - \alpha$ on average, dips below | binomial count | $\Theta(1)$ |
| Fisher's exact test | size $\le \alpha$ given the margins | $2 \times 2$ table | $\Theta(n)$ |
| Chi-squared tests | size $\to \alpha$ | large expected counts | $\Theta(k)$, $\Theta(rc)$ |
| Likelihood ratio test | size $\to \alpha$ | regular model, interior null | $\Theta(n + m)$ |
| Fisher's method | size $\alpha$, exact | independent uniform p-values | $\Theta(k)$ |
| Bonferroni | FWER $\le \alpha$ | any dependence | $\Theta(m)$ |
| Holm | FWER $\le \alpha$ | any dependence | $\Theta(m \log m)$ |
| Benjamini-Hochberg | FDR $\le (m_0/m)q$ | independence or PRDS | $\Theta(m \log m)$ |
| Benjamini-Yekutieli | FDR $\le (m_0/m)q$ | any dependence | $\Theta(m \log m)$ |

: The main methods. $n$ observations or trials, $m$ hypotheses or a second sample size, $b$ bisection steps, $k$ cells or p-values.

## Choosing a method

For roughly normal data use the [t-test](/student-t-test/) and the [t interval](/t-confidence-interval/), and [Welch's test](/welch-t-test/) for two means. For a proportion, use the binomial test and the Wilson interval, or Clopper-Pearson when coverage must never fall below $1 - \alpha$. For small $2 \times 2$ tables use Fisher's exact test. In parametric models, prefer the likelihood ratio test when both fits are cheap and the score test when only the null fit is.

For many tests, choose the error rate first. Use Holm for a few hypotheses that each matter, and [Westfall-Young](/westfall-young-procedure/) when the tests are correlated and a permutation group fits the null. Use Benjamini-Hochberg for screens of independent or positively dependent tests, and Benjamini-Yekutieli when the dependence is unknown.
