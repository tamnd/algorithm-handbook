1. The size is $P(X \ge 10) = (\binom{12}{10} + \binom{12}{11} + \binom{12}{12})/2^{12} = (66 + 12 + 1)/4096 = 79/4096 = 0.0193$. It is at most 0.05, so the test has level 0.05, but its size is well below 0.05 because the count is discrete.

3. $\bar x = 4$, $S^2 = 8/3$, $S = 1.6330$, and the standard error is $S/2 = 0.8165$. The half-width is $3.1824 \cdot 0.8165 = 2.5984$, so the interval is $[1.4016, 6.5984]$.

5. The interval is $[0, 1 - 0.025^{1/20}] = [0, 0.1684]$, since the lower end is 0 when $x = 0$ and the upper end solves $(1 - p)^{20} = 0.025$. The one-sided bound is $1 - 0.05^{1/20} = 0.1391$, a little below $3/20 = 0.15$.

8. Bonferroni compares each p-value with $0.01$ and rejects only the first. Holm compares $0.003 \le 0.01$, $0.012 \le 0.0125$, then $0.018 > 0.0167$ and stops, so it rejects two. The adjusted p-values are $0.015, 0.048, 0.054, 0.08, 0.3$.

12. The formula is $n = ((z_{0.95} + z_{0.9})\sigma/\Delta)^2 = ((1.6449 + 1.2816) \cdot 2.5)^2 = 53.52$, so $n = 54$. The power $\Phi(\Delta\sqrt n/\sigma - z_{0.95})$ is $0.9023$ at $n = 54$ and $0.8975$ at $n = 53$.

13. The BH thresholds are $k/200$. The fifth p-value $0.019$ is below $0.025$, so BH rejects five, although the second, $0.012$, is above its own threshold $0.01$. Holm stops at the second step ($0.012 > 0.05/9$) and rejects one. BY uses the thresholds $k \cdot 0.05/(10 \cdot 2.9290)$, and only the first p-value passes. The BH adjusted p-values are $0.01, 0.038, 0.038, 0.038, 0.038$.

15. The weights for the upper left cell $k = 1, \dots, 5$ are $5, 50, 100, 50, 5$ out of $\binom{10}{6} = 210$. The one-sided p-value is $5/210 = 1/42 = 0.0238$, and the two-sided one adds the table with $k = 1$, giving $1/21 = 0.0476$. Pearson's $X^2 = 20/3 = 6.667$ has asymptotic p-value $0.0098$, but every expected count is 2 or 3, far below the usual rules for the chi-squared approximation.

17. The likelihood ratios are $1/6, 1/3, 3/4, 3, 4$. Reject at $x = 5$ (size 0.1) and at $x = 4$ with probability $\gamma = 0.05/0.1 = 1/2$. The power is $0.4 + 0.3/2 = 0.55$. The non-randomized tests of level 0.15 reject on a set of null probability at most 0.15, and the best is $\{5\}$, with power 0.4.

18. With $T = 30$, $n = 10$ and $\hat\lambda = 3$: $S = (T/\lambda_0 - n)^2/(n/\lambda_0) = 25/5 = 5$, $W = (\hat\lambda - \lambda_0)^2/(\hat\lambda/n) = 10/3$ and $\Lambda = 2(T\ln(\hat\lambda/\lambda_0) - n(\hat\lambda - \lambda_0)) = 4.3279$. The p-values are $0.0253$, $0.0679$ and $0.0375$, so $S > \Lambda > W$, the reverse of the order in the normal mean model.

19. The sum $T$ is Poisson with mean $5\lambda$ and the family has a monotone likelihood ratio in $T$. Under $\lambda = 1$, $P(T \ge 10) = 0.03183$ and $P(T = 9) = 0.03627$, so the test rejects when $T \ge 10$ and with probability $\gamma = (0.05 - 0.03183)/0.03627 = 0.5011$ when $T = 9$. At $\lambda = 2$, the power is $P(T \ge 10) + \gamma P(T = 9) = 0.5421 + 0.5011 \cdot 0.1251 = 0.6048$.

21. $S_1^2/m = 0.8$ and $S_2^2/n = 2.5$, so $\hat\nu = 3.3^2/(0.8^2/4 + 2.5^2/9) = 10.89/0.8544 = 12.745$, which lies between 4 and 13.

23. The procedure rejects something exactly when $p_{(2)} \le q$ or $p_{(1)} \le q/2$. The complement is that both p-values exceed $q/2$ and not both lie in $(q/2, q]$, which has probability $(1 - q/2)^2 - (q/2)^2 = 1 - q$. Under the global null every rejection is false, so the FDR equals the FWER, $q$.

24. With $\ell(\theta) = -5\ln\theta - T/\theta$, $\hat\theta = 2$ and $\Lambda(T) = 2(T - 5 - 5\ln(T/5)) = 3.0685$, with Wilks p-value $0.0798$. $\Lambda$ is large for small and for large $T$; the other root of $\Lambda(t) = 3.0685$ is $t = 2.0319$, and the exact p-value is $P(T \le 2.0319) + P(T \ge 10) = 0.0556 + 0.0293 = 0.0848$. The nominal 5% test rejects outside $[1.7930, 10.7464]$, and its exact size is $0.0538$.

25. Solve $(a - \rho b)^2 \le z^2(1 + 0.25\rho^2)$, a quadratic with leading coefficient $b^2 - 0.25z^2 = 3.0396 > 0$; the set is $[1.7105, 6.1853]$, while the delta method gives $3 \pm 1.96 \cdot 0.9014 = [1.2333, 4.7667]$. For $b = 0.8$ the leading coefficient is negative, since $|b|/0.5 = 1.6 < 1.96$, and the set is $(-\infty, -33.0037] \cup [3.0412, \infty)$.

26. The observed statistics are 5 and 3, and each is the largest of its 20 permutation values, so both marginal p-values are $1/20$. The maximum of the two statistics reaches 3 in two splits (the observed one, and treated units 1, 3, 5, where the first statistic is 3), so the single-step values are $1/20$ and $2/20$. Step-down compares the second variable only with its own law and gives $1/20$ for both, so both are rejected at 0.05; Holm gives $2 \cdot 1/20 = 0.1$ for both and rejects neither.

27. At $p = 0.5$ the interval contains $p$ for $x = 3, \dots, 7$, with coverage $912/1024 = 0.8906$. At $p = 0.2$ it does for $x = 1, \dots, 5$, coverage $0.8863$, and at $p = 0.1$ for $x = 1, \dots, 4$, coverage $0.6497$; at $x = 0$ the interval is the single point 0.
