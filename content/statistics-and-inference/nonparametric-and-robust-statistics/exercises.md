1. ◦ The sample is $1, 1.5, 3, 4, 5$, and the model is the uniform law on $[0, 6]$. Give the [empirical distribution function](/empirical-distribution-function/) at $x = 2$ and $x = 4$, and compute the [Kolmogorov-Smirnov](/kolmogorov-smirnov-test/) statistic $D_5 = \sup_x |F_5(x) - x/6|$. Say where the supremum is reached, and whether the test rejects at 5%, where the critical value for $n = 5$ is $0.5633$.

2. ◦ With the [DKW inequality](/dkw-inequality/) and Massart's constant, give the half-width $\varepsilon$ of the 95% confidence band for $F$ from $n = 200$ independent points. How many points does a 95% band of half-width $0.02$ need?

3. ◦ Compute the median, the [median absolute deviation](/median-absolute-deviation/) and the normal-consistent scale $1.4826\,\mathrm{MAD}$ of $1, 3, 4, 6, 8, 11, 40$. Then change 40 to 4000. Which of the MAD and the sample standard deviation changes, and by how much?

4. ◦ For the ten values $2, 10, 4, 50, 6, 1, 7, 5, 3, 8$, compute the [trimmed mean](/trimmed-mean/) with $\alpha = 0.1$ and with $\alpha = 0.2$, the mean and the median. What is the finite-sample breakdown point of the $0.2$-trimmed mean here?

5. ◦ Thirteen paired differences have 10 positive signs, 2 negative signs and one zero. Give the one-sided and the two-sided p-values of the [sign test](/sign-test/) as exact fractions.

6. ◦ The paired differences are $1.2, -0.4, 2.5, 3.1, -1.8, 0.7, 4.0, 2.2$. Compute the [Wilcoxon signed-rank](/wilcoxon-signed-rank-test/) statistic $W^+$, and its exact one-sided and two-sided p-values.

7. ◦ Two samples are $x = 4.1, 5.6, 7.2$ and $y = 2.3, 3.8, 5.0, 6.1$. Compute the [Mann-Whitney](/mann-whitney-u-test/) statistic $U = \#\{(i, j) : x_i > y_j\}$, its exact one-sided p-value $P(U \ge U_{obs})$ under the null, the two-sided p-value, and the estimate of $P(X > Y)$.

8. ◦ Five pairs have the $x$ ranks $1, 2, 3, 4, 5$ and the $y$ ranks $2, 1, 4, 3, 5$. Compute [Spearman's coefficient](/spearman-rank-correlation/) $r_S = 1 - 6\sum d_i^2/(n(n^2 - 1))$ and the exact one-sided p-value $P(r_S \ge r_{obs})$ under independence, by counting permutations.

9. ◦ List the Walsh averages of $1, 2, 6, 15$ and give the [Hodges-Lehmann estimate](/hodges-lehmann-estimator/). Recompute it when 15 is replaced by 1500, and when 6 and 15 are replaced by 600 and 1500.

10. ◦ In [split conformal prediction](/split-conformal-prediction/), the nine calibration residuals are $0.3, 1.2, 0.8, 2.5, 0.1, 0.9, 1.7, 0.4, 3.6$ and $\alpha = 0.2$. Give $k$, the quantile $q$ and the interval at a new point where the fitted model predicts 10. What is the coverage for exchangeable data with continuous scores? What happens with $n_2 = 50$ calibration points and $\alpha = 0.01$?

11. • The sample is $1, 5, 9$. Find the ideal [bootstrap](/bootstrap-method/) distribution of the median of a resample of size 3, its mean and its variance, by listing the $27$ equally likely ordered resamples.

12. • Group A is $8, 11, 14$ and group B is $5, 7, 9$; the statistic is the mean of A minus the mean of B. Give the exact one-sided and two-sided p-values of the [permutation test](/permutation-test/). What is the smallest two-sided p-value any data could give with groups of 3 and 3? A Monte Carlo run with $b = 999$ random splits finds $c = 95$ at least as large as the observed one: what p-value does it report?

13. • Three groups are $1.2, 3.4, 2.2$; $4.5, 5.1, 3.9$; and $6.0, 7.3, 5.5$. Compute the [Kruskal-Wallis](/kruskal-wallis-test/) statistic $H$, its exact p-value over the $1680$ ways to split nine ranks into three groups of three, and the chi-square approximation with 2 degrees of freedom.

14. • Four blocks rank three treatments as $(1, 2, 3)$, $(1, 3, 2)$, $(1, 2, 3)$ and $(2, 1, 3)$. Compute the rank sums and the [Friedman](/friedman-test/) statistic $Q$. Find its exact p-value over the $6^4$ equally likely rankings, and compare it with the chi-square approximation $e^{-Q/2}$.

15. • Compute the [Huber M-estimate](/huber-m-estimator/) of location of $2, 3, 5, 6, 30$ with $k = 2$ and the scale fixed at $\sigma = 1$, by finding the root of $\sum_i \psi_k(x_i - \theta)$ with $\psi_k(u) = \max(-k, \min(k, u))$. Which points are clipped? Compare it with the mean and the median.

16. • For the points $(1, 1), (2, 3), (3, 4), (4, 7), (5, 25)$, compute the [Theil-Sen](/theil-sen-estimator/) line, the [repeated median](/repeated-median-regression/) line (high median inside, low median outside, intercept the median of $y_i - b x_i$) and the least squares line.

17. • The points $x = 0, 1, 3$ have responses $y = 2, 4, 10$. With the Epanechnikov kernel $K(u) = \frac34(1 - u^2)$ on $[-1, 1]$ and $h = 2$, compute the [kernel density estimate](/kernel-density-estimation/) $\hat f(1)$ and the [Nadaraya-Watson estimate](/nadaraya-watson-estimator/) $\hat m(1)$.

18. • The data lie on the line $y = x$ at $x = 0, 1, 2, 3$. With the same kernel and $h = 2$, compute the Nadaraya-Watson estimate at $x = 0$. Then show that [local linear regression](/local-polynomial-regression/) with any kernel returns $0$ there, and in general reproduces any data that lie on a line.

19. • The five points are the corners of the square $[0, 2]^2$ and its centre $(1, 1)$. Compute the [halfspace depth](/halfspace-depth/) of $(1, 1)$ and of $(1, 1/2)$. Show that every point other than $(1, 1)$ has depth at most 2, so that the [Tukey median](/tukey-median/) is $(1, 1)$. Compare the maximum depth with the bounds $\lceil n/3 \rceil$ and $\lceil n/2 \rceil$.

20. • What is the smallest p-value the exact signed-rank test can give with $n$ nonzero differences? Find the least $n$ for which a one-sided test, and the least $n$ for which a two-sided test, can reject at level $0.05$.

21. • For the two-sided sign test with $n = 10$ at level $0.05$, find the largest symmetric rejection region and its exact size. Why is the size not $0.05$?

22. • Use the formulas of the entries. How many random subsets does the [MM-estimator](/mm-estimator/) need to see a clean one with probability $0.99$ when $p = 5$ and $\varepsilon = 0.2$? What are the coverage $h$ and the breakdown point of [least trimmed squares](/least-trimmed-squares/) with $n = 20$, $p = 2$, and with $h = 15$? What is the least number $m$ of replaced points that can break the Theil-Sen slope with $n = 30$, by the rule $2\binom{n - m}{2} \le \binom n2$?

23. • Compute the [jackknife](/jackknife-resampling/) leave-one-out medians and the jackknife standard error of the median of $3, 5, 6, 8, 9, 12, 14, 15, 19, 22$. On which values of the sample does it depend?

24. ★ Show that for two groups, with no ties, the Kruskal-Wallis statistic equals $z^2$, where $z = (U - mn/2)/\sqrt{mn(N + 1)/12}$ is the standardized Mann-Whitney statistic and $N = m + n$. Check it on the data of exercise 7.

25. ★ The observed statistic and $b$ simulated ones are exchangeable and have no ties, and $c$ is the number of simulated values at least as large as the observed. Prove that the Monte Carlo p-value $(1 + c)/(1 + b)$ satisfies $P(p \le \alpha) \le \alpha$ for every $\alpha$. With $b = 19$ and $\alpha = 0.06$, compute the rejection probability of this p-value and of the naive $c/b$.

26. ★ In split conformal prediction with continuous scores, show that the coverage given the training and calibration data is $F(q)$ and has the Beta law with parameters $k$ and $n_2 + 1 - k$. For $n_2 = 19$ and $\alpha = 0.1$, give $k$, the mean and standard deviation of the conditional coverage, and the probability that it is below $0.8$.

27. ★ Order points by $x$ with distinct $x_i$. Prove that the number of pairs whose slope is less than $t$ is the number of inversions of the sequence $y_i - t x_i$, and that ties in the sequence are pairs with slope exactly $t$. Check it on the points of exercise 16 with $t = 2$. Use it to decide in $O(n \log n)$ time whether the Theil-Sen slope is below $t$.

28. ★ The Pitman asymptotic relative efficiency of the sign test to the t test in the shift model, for a density $f$ with median 0 and variance $\sigma^2$, is $4\sigma^2 f(0)^2$. Derive this from the asymptotic means and variances of the two statistics, and evaluate it for the normal, the Laplace law with density $\frac12 e^{-|x|}$ and the uniform law on $[-1, 1]$.
