1. ◦ A [binomial test](/binomial-test/) of $H_0: p = 1/2$ against $p > 1/2$ uses $n = 12$ trials and rejects when $X \ge 10$. Compute its size as an exact fraction and as a decimal. Is it a level-0.05 test?

2. ◦ A [z-test](/z-test/) has $n = 36$ observations from a normal law with known $\sigma = 3$, the null $\mu = 10$ and the sample mean $\bar x = 10.9$. Compute $z$, the one-sided [p-value](/p-value/) for the alternative $\mu > 10$ and the two-sided p-value. Which of the two tests rejects at level 0.05?

3. ◦ The sample is $2, 4, 4, 6$. Compute $\bar x$, the [sample variance](/sample-variance/) $S^2$ and the 95% [t interval](/t-confidence-interval/) for the mean, using $t_{3, 0.975} = 3.1824$.

4. ◦ A spinner with four equal sectors is spun 100 times and lands on the sectors 18, 22, 35 and 25 times. Compute the [chi-squared goodness-of-fit](/chi-squared-goodness-of-fit-test/) statistic, its degrees of freedom and its asymptotic p-value. Is fairness rejected at level 0.05?

5. ◦ In $n = 20$ trials there are no successes. Give the two-sided 95% [Clopper-Pearson interval](/clopper-pearson-interval/) for $p$. Compare the one-sided 95% upper bound $1 - 0.05^{1/20}$ with the rule of three, $3/n$.

6. ◦ In a paired study, 8 subjects change from "no" to "yes" and 1 changes from "yes" to "no". Compute the exact two-sided p-value of [McNemar's test](/mcnemar-test/) and the uncorrected chi-squared statistic with its asymptotic p-value.

7. ◦ Eight independent tests of true nulls are each run at level 0.01. Compute the exact [family-wise error rate](/family-wise-error-rate/) and compare it with the bound that the [union bound](/union-bound/) gives.

8. ◦ The p-values are $0.003, 0.012, 0.018, 0.04, 0.3$ and $\alpha = 0.05$. How many hypotheses does the [Bonferroni correction](/bonferroni-correction/) reject, and how many does [Holm's method](/holm-bonferroni-method/) reject? Give Holm's adjusted p-values.

9. ◦ Two independent studies report $p_1 = 0.04$ and $p_2 = 0.10$. Compute the statistic of [Fisher's method](/fisher-combined-probability-test/), its degrees of freedom and the combined p-value, using $P = q(1 - \ln q)$ with $q = p_1p_2$.

10. • Compute the [power](/statistical-power/) of the test of exercise 1 at $p = 0.8$, as an exact fraction and as a decimal.

11. • A two-sided z-test at $\alpha = 0.05$ has $n = 25$, $\sigma = 10$ and the null $\mu = 50$. Compute its power at $\mu = 54$, and say how much of it comes from the tail on the wrong side.

12. • A one-sided z-test at $\alpha = 0.05$ must reach power 0.9 at an effect of 4 when $\sigma = 10$. Use the formula of [sample size determination](/sample-size-determination/) to find the smallest $n$, and check the power at $n$ and at $n - 1$.

13. • Ten p-values are $0.001, 0.012, 0.014, 0.016, 0.019, 0.3, 0.4, 0.5, 0.7, 0.9$. At level 0.05, how many hypotheses do the [Benjamini-Hochberg procedure](/benjamini-hochberg-procedure/), Holm's method and the [Benjamini-Yekutieli procedure](/benjamini-yekutieli-procedure/) reject? Give the first five BH adjusted p-values.

14. • The p-values are $0.02, 0.03, 0.045$ and $\alpha = 0.05$. How many hypotheses do Holm's method and the [Hochberg procedure](/hochberg-procedure/) reject? What must hold for Hochberg's answer to be backed by a guarantee?

15. • A $2 \times 2$ table has rows $(5, 0)$ and $(1, 4)$. With the margins fixed, list the hypergeometric weights of the upper left cell, and compute the one-sided and the two-sided p-values of [Fisher's exact test](/fisher-exact-test/), the two-sided one by the rule that sums the tables no more likely than the observed one. Compute also Pearson's $X^2$ and its asymptotic p-value, and say why it should not be trusted here.

16. • For $x = 0$ successes in $n = 20$ trials, show that the 95% [Wilson interval](/wilson-score-interval/) is $[0, z^2/(n + z^2)]$ with $z = 1.96$, compute its upper end and compare it with exercise 5.

17. • $X$ takes the values $1, \dots, 5$ with probabilities $f_0 = (0.3, 0.3, 0.2, 0.1, 0.1)$ under the null and $f_1 = (0.05, 0.1, 0.15, 0.3, 0.4)$ under the alternative. Use the [Neyman-Pearson lemma](/neyman-pearson-lemma/) to find the test of size exactly 0.15 with the largest power, and that power. What is the best power of a non-randomized test of level 0.15?

18. • Ten counts from a Poisson law sum to 30. For $H_0: \lambda = 2$, compute the [score](/score-test/), [Wald](/wald-test/) and [likelihood ratio](/likelihood-ratio-test/) statistics and their asymptotic $\chi^2_1$ p-values. In which order are they here?

19. • Five counts come from a Poisson law with mean $\lambda$. Find the [uniformly most powerful](/uniformly-most-powerful-test/) test of $\lambda \le 1$ against $\lambda > 1$ of size exactly 0.05: the cut point, the randomization probability, and the power at $\lambda = 2$.

20. • For the sample of exercise 3, compute the 95% [prediction interval](/prediction-interval/) for one more observation from the same normal law. Separately, for 19 iid observations from any continuous law, what is the probability that a new observation falls between the smallest and the largest?

21. • Two normal samples have $m = 5$, $S_1^2 = 4$ and $n = 10$, $S_2^2 = 25$. Compute the Welch-Satterthwaite degrees of freedom of [Welch's t-test](/welch-t-test/) and check them against the bounds $\min(m, n) - 1$ and $m + n - 2$.

22. • Five [e-values](/e-variable/) are $40, 25, 12, 3, 0.5$. The e-BH rule rejects the $k$ largest for the largest $k$ with $e_{(k)} \ge m/(kq)$. How many does it reject at $q = 0.1$? Then turn the p-value $0.004$ into an e-value with the calibrator $\kappa p^{\kappa - 1}$, $\kappa = 1/2$, and say whether it rejects at $\alpha = 0.05$.

23. ★ Two true nulls have independent uniform p-values. Show that the Benjamini-Hochberg procedure at level $q$ rejects at least one of them with probability exactly $q$, so that its FDR and its FWER are both $q$ here.

24. ★ Five waiting times are exponential with mean $\theta$ and sum $T = 10$. For $H_0: \theta = 1$, compute the likelihood ratio statistic and its p-value from [Wilks' theorem](/wilks-theorem/). Then use the exact law of $T$ under the null, Gamma with shape 5 and scale 1, to compute the exact p-value of the same statistic, and the exact size of the nominal 5% test.

25. ★ Two independent estimates are $a \sim N(\mu_1, 1)$ and $b \sim N(\mu_2, 0.25)$, with known variances, and $a = 6$, $b = 2$. Find the exact 95% confidence set for $\rho = \mu_1/\mu_2$ by the method of [Fieller's theorem](/fieller-theorem/), with $z = 1.96$ in place of the t quantile, and compare it with the delta-method interval. Then find the set for $b = 0.8$.

26. ★ Six units, the first three treated, have two variables: $9, 8, 10 \mid 4, 5, 3$ and $7, 9, 8 \mid 6, 4, 5$. The statistic of each variable is the treated mean minus the control mean. Over all 20 ways to choose three treated units, compute the marginal [permutation](/permutation-test/) p-values, the single-step maxT adjusted p-values and the step-down adjusted p-values of the [Westfall-Young procedure](/westfall-young-procedure/). Which hypotheses does it reject at $\alpha = 0.05$, and which does Holm's method reject on the marginal p-values?

27. ★ Compute the exact coverage of the nominal 95% Wald interval $\hat p \pm 1.96\sqrt{\hat p(1 - \hat p)/n}$ for $n = 10$ at $p = 0.5$, $0.2$ and $0.1$, by listing the counts $x$ whose interval contains $p$.
