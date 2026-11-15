1. ◦ A coin is tossed $n = 10$ times and shows $X$ heads. Compare $\hat p = X/n$ with the add-one estimator $\tilde p = (X + 1)/(n + 2)$. Compute the [bias](/estimator-bias/) of $\tilde p$ and the [mean squared error](/mean-squared-error/) of both estimators at $p = 0.1$ and at $p = 1/2$, as exact fractions. Which estimator is better at each point?

2. ◦ A population has the three values $\{1, 3, 8\}$, and a sample of two is drawn without replacement. List the three possible sample means and write down the [sampling distribution](/sampling-distribution/) of $\bar y$. Find its mean and variance exactly, and check the variance against $(1 - n/N)\,S^2/n$, where $S^2$ is the population variance with divisor $N - 1$.

3. ◦ Let $X_1, \ldots, X_{50}$ be iid uniform on $(0, \theta)$ with $\theta = 1$. Compute $P(|\max_i X_i - 1| > 0.05)$. Then compute $P(|2X_1 - 1| > 0.05)$ and explain why it does not depend on $n$. Which of the two estimators is [consistent](/consistent-estimator/), and which is unbiased?

4. ◦ One worker has seen the data $(2, 4)$ and another $(4, 5, 10)$. Each keeps the triple $(n, \bar x, M)$, where $M$ is the sum of squared deviations from its own mean. Write down both triples, merge them with the [Chan-Golub-LeVeque formula](/chan-parallel-variance/), and check the merged mean and sample variance against the five values directly. How much is lost if the two values of $M$ are simply added?

5. ◦ Two samples from an exponential law with rate $\lambda$ are $(1, 2, 6)$ and $(3, 3, 3)$. Write down the [likelihood](/likelihood-function/) of each, and show that they are the same function of $\lambda$. Compute $L(2)/L(1)$ and the maximum likelihood estimate. Use the [factorization theorem](/fisher-neyman-factorization-theorem/) to show that $(x_{(1)}, \sum x_i)$ is sufficient, and say why it is not minimal.

6. ◦ Compute the [Kullback-Leibler divergence](/kullback-leibler-divergence/) $D(\mathrm{Pois}(2) \,\|\, \mathrm{Pois}(3))$ and $D(\mathrm{Pois}(3) \,\|\, \mathrm{Pois}(2))$ to five decimals, starting from the general formula for two Poisson laws.

7. ◦ Ten Bernoulli trials give 7 successes. Starting from $p_0 = 1/2$, compute the [score](/score-function/) $U(p_0)$, the Fisher information $I_n(p_0)$, and one step of [Fisher scoring](/fisher-scoring/). Show that for this model one step reaches $T/n$ from any start $p_0 \in (0, 1)$. Give the standard error $\sqrt{\hat p(1 - \hat p)/n}$ at the estimate.

8. ◦ A binary covariate $z$ is always observed. For the four units with $z = 0$, the values of $y$ are $2, 4, 6$ and one missing value. For the four units with $z = 1$, they are $10$ and three missing values. Compute the complete-case mean of $y$, and the mean after each missing value is replaced by the mean of the observed values with the same $z$. Under which [missing-data mechanism](/missing-data-mechanism/) is the second estimate justified? Classify each of these: (a) a lab drops samples at random; (b) older patients skip a test, and age is recorded; (c) people with high incomes refuse to report their income.

9. ◦ A population has three units with $y = (1, 4, 10)$. One unit is drawn, unit $i$ with probability $\pi_i = (0.2, 0.3, 0.5)$. List the three possible [Horvitz-Thompson](/horvitz-thompson-estimator/) estimates of the total, and check that their mean is the total $15$. Compute the variance of the estimator, and compare it with the variance when each unit has probability $1/3$.

10. • Continue Exercise 1 with $n = 10$. Using [statistical decision theory](/statistical-decision-theory/), find the values of $p$ at which the risk of $\tilde p$ is smaller than the risk of $\hat p$. Compare the maximum risks of the two estimators. Then compute the risk of $(X + \sqrt n/2)/(n + \sqrt n)$ and show that it is constant in $p$. Does either of the first two estimators have a smaller maximum risk?

11. • Let $X_1, \ldots, X_5$ be iid exponential with rate $\lambda$, and let $T = \sum X_i$. Compute the [Cramér-Rao bound](/cramer-rao-bound/) for unbiased estimators of $\lambda$. Show that $4/T$ is unbiased, and compute its variance. Is the bound reached? Then compute the mean squared error of the MLE $5/T$ and find the constant $c$ that minimizes the mean squared error of $c/T$.

12. • For the same exponential model with $n$ observations, start from the unbiased estimator $\mathbf 1\{X_1 > 1\}$ of $e^{-\lambda} = P(X > 1)$ and condition on $T = \sum X_i$ ([Rao-Blackwell](/rao-blackwell-theorem/)). Use the fact that $X_1/T$ has the Beta$(1, n - 1)$ law and is independent of $T$. Evaluate the result for the data $(0.5, 1.5, 2.0, 0.8, 1.2)$ and compare it with the plug-in estimate $e^{-\hat\lambda}$.

13. • Let $X_1, \ldots, X_n$ be iid uniform on $(0, \theta)$ with $T = \max_i X_i$. Find the [UMVUE](/minimum-variance-unbiased-estimator/) of $\theta^2$. Show that the square of the UMVUE of $\theta$, $((n + 1)T/n)^2$, is biased upward, and find its mean.

14. • Forty waiting times from an exponential law with mean $\theta$ have $\bar x = 2.5$. Give three 95% intervals for $\theta$: the Wald interval $\bar x \pm 1.96\,\bar x/\sqrt n$; the interval from the [delta method](/delta-method/) on the log scale, transformed back; and the exact interval from $2n\bar X/\theta \sim \chi^2_{2n}$, with $\chi^2_{80}$ quantiles $57.153$ and $106.629$. Which of the two approximate intervals is closer to the exact one?

15. • The counts $(0, 0, 1, 1, 2, 3, 3, 5, 7, 8)$ are fitted by a Poisson model. Treat the MLE as an [M-estimator](/m-estimator/) with $\psi(x, \lambda) = x/\lambda - 1$. Compute $\hat A$, $\hat B$, and the sandwich standard error, and compare it with the model-based standard error $\sqrt{\hat\lambda/n}$. Show that for this $\psi$ the sandwich variance is the sample variance, with divisor $n$, over $n$.

16. • Compute [Huber's estimate](/huber-m-estimator/) of location with $k = 2$ and unit scale for the data $(2, 3, 5, 6, 30)$, and compare it with the mean and the median. Check that $\sum \psi_k(x_i - \hat\theta) = 0$, and compute the sandwich variance estimate $\hat B/(n\hat A^2)$.

17. • [Welford's algorithm](/welford-algorithm/) adds a value to $(n, m, M)$. Derive the reverse step, which removes a value $x$. Apply it to remove $14$ from the triple $(5, 8, 64)$ of the data $(3, 7, 7, 9, 14)$, and check the result directly.

18. • A circus owner has 50 elephants and wants their total weight from a single weighing. He plans to weigh Sambo, the typical elephant, with probability $99/100$, and each of the other 49 with equal probability. Suppose every elephant weighs 4 tons. Compute the two possible [Horvitz-Thompson](/horvitz-thompson-estimator/) estimates of the total, check that the estimator is unbiased, and compute its standard deviation.

19. • Lindley's variant of the [James-Stein estimator](/james-stein-estimator/) shrinks toward the grand mean: $\hat\theta_i = \bar x + (1 - (p - 3)/S)(x_i - \bar x)$ with $S = \sum (x_i - \bar x)^2$. Apply it to $x = (2.0, 0.5, -1.0, 3.5, 0.0)$ with $\sigma^2 = 1$. What is its risk when all $\theta_i$ are equal, compared with the risk $5$ of $X$?

20. • Five observations from a Cauchy location model are $(-1.0, 0.2, 0.9, 1.6, 12.0)$. The Fisher information per observation is $1/2$. Run [Fisher scoring](/fisher-scoring/) from the median, and Newton's method from $5$ and from $8$. Where does each converge, and what kind of critical point of the log-likelihood is each limit? Compare the expected and observed standard errors at the maximum.

21. • Let $\hat p = X/n$ with $X \sim \mathrm{Bin}(n, 1/2)$, and $g(p) = p(1 - p)$. Show that the first-order [delta method](/delta-method/) gives a degenerate limit. Find the limit law of $n(g(\hat p) - 1/4)$. At $n = 100$, compare the exact probability that $n(1/4 - g(\hat p))$ exceeds the 95% point of the limit with $0.05$.

22. ★ Let $X_1, \ldots, X_n$ be iid normal with unknown mean $\mu$ and known $\sigma$. Find the UMVUE of $P(X \le c) = \Phi((c - \mu)/\sigma)$ by [Rao-Blackwell](/rao-blackwell-theorem/) and [Lehmann-Scheffé](/lehmann-scheffe-theorem/), starting from $\mathbf 1\{X_1 \le c\}$. Evaluate it for $n = 4$, $\sigma = 1$, $\bar x = 0.5$, $c = 1$, and compare with the plug-in $\Phi((c - \bar x)/\sigma)$.

23. ★ Use the two moment conditions $E[X - \mu] = 0$ and $E[\operatorname{sign}(X - \mu)] = 0$ for a symmetric law in [GMM](/generalized-method-of-moments/). Compute $S$ and $G$ and the efficient asymptotic variance $(G^\top S^{-1} G)^{-1}/n$ when the law is normal with variance $\sigma^2$, and when it is Laplace with scale $b$. In each case, show that one of the two conditions adds nothing.

24. ★ In the Neyman-Scott problem, $X_{i1}, X_{i2}$ are iid $N(\mu_i, \sigma^2)$ for $i = 1, \ldots, n$, with a separate mean for each pair. Find the MLE of $\sigma^2$ and its limit as $n \to \infty$. Give a consistent estimator based on $D_i = X_{i1} - X_{i2}$ and its asymptotic variance. Which condition of the [asymptotic normality of the MLE](/asymptotic-normality-of-mle/) fails?

25. ★ Extend the [Chan-Golub-LeVeque merge](/chan-parallel-variance/) to the third central sum $M_3 = \sum (x_i - \bar x)^3$. Express $M_3$ of the union in terms of $n_a$, $n_b$, $\delta = \bar x_b - \bar x_a$, and the second and third sums of the parts. Check it on $(3, 7)$ and $(7, 9, 14)$.

26. ★ For $X \sim N_p(\theta, I)$ and a constant $c > 0$, compute the risk of $(1 - c/\|X\|^2)X$ under squared error with Stein's lemma, in terms of $E[1/\|X\|^2]$. For which $c$ does it dominate $X$, and which $c$ is best? Compute the risk at $p = 5$, $c = 1$, $\theta = 0$, and compare it with the [James-Stein](/james-stein-estimator/) risk at $\theta = 0$.
