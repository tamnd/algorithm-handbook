1. ◦ A uniform prior on a success probability $p$ and 2 successes in 8 trials give a Beta$(3, 7)$ posterior. Give the [Bayes estimator](/bayes-estimator/) under squared loss, the posterior mode, and the posterior variance as exact fractions. Which of the three is the maximum likelihood estimate?

2. ◦ Nine measurements from $N(\mu, 9)$ have mean $4.2$. With a flat prior on $\mu$, find the 95% equal-tailed [credible interval](/credible-interval/). The z [confidence interval](/confidence-interval/) has the same ends. Write one sentence for each interval saying what its 95% is a probability of.

3. ◦ A [Bayes factor](/bayes-factor/) is $B_{10} = 4$. Find $P(M_1 \mid y)$ when the prior probability of $M_1$ is $0.2$, and when it is $0.5$.

4. ◦ A uniform prior and 7 successes in 10 trials give a Beta$(8, 4)$ posterior. Find the [posterior predictive distribution](/posterior-predictive-distribution/) of the number of successes in the next 3 trials, as exact fractions. Compare its probabilities of 0 and of 3 with those of the plug-in Binomial$(3, 2/3)$.

5. ◦ Four Poisson counts are all 0. Find the posterior under the [Jeffreys prior](/jeffreys-prior/) $\lambda^{-1/2}$, say whether it is proper, and give its mean. Then do the same for the [improper prior](/improper-prior/) $1/\lambda$.

6. ◦ A posterior is exponential with rate 2. Find the 95% [highest posterior density interval](/highest-posterior-density-interval/) and the 95% equal-tailed interval, and their lengths.

7. ◦ A coin lands heads 5 times in 10 tosses. Compare $M_0: p = 1/2$ with $M_1: p \sim$ Uniform$(0, 1)$ by the [Savage-Dickey density ratio](/savage-dickey-density-ratio/). Give $B_{01}$ as an exact fraction, and check it against $m_0/m_1$.

8. ◦ In the normal [hierarchical model](/hierarchical-bayesian-model/), one group has estimate $y_j = 28$ with standard error $\sigma_j = 10$. Given $\mu = 8$ and $\tau = 5$, find the shrinkage factor, the posterior mean of $\theta_j$ and its posterior standard deviation.

9. ◦ An urn holds one red and one blue ball. Each draw returns the ball together with one more ball of the same colour. Find the probability that the first three draws are red, red, blue, and the probability of blue, red, red. Write $X_i = 1$ for red on draw $i$ and find $\mathrm{Cov}(X_1, X_2)$. Which mixture does [de Finetti's theorem](/de-finetti-theorem/) give for this sequence?

10. ◦ [Nested sampling](/nested-sampling/) runs with $N = 400$ live points on a problem with information $H = 5$ nats. About how many iterations does it take to reach the prior mass where the posterior sits, and what standard error of $\log Z$ does the usual rule give? Say which of the two numbers rests on a heuristic.

11. • A posterior is exponential with rate 2. Underestimating the parameter costs 3 per unit and overestimating it costs 1 per unit. Find the Bayes estimate, and compare it with the posterior mean and median.

12. • Let $X \sim N(\theta, 1)$ with prior $\theta \sim N(0, 4)$. Find the Bayes estimator under squared loss, its Bayes risk, and the Bayes risk of $X$. Then find its frequentist risk at a fixed $\theta$, and the values of $\theta$ at which it is worse than $X$.

13. • Counts $3, 1, 4$ are Poisson$(\lambda)$, and $\lambda$ has a Gamma prior with shape 2 and rate 1. Find the posterior, and the predictive probability that the next count is 0. Compare it with the plug-in $e^{-\hat\lambda}$ at the posterior mean, and give the mean and variance of the predictive law.

14. • Show that the Jeffreys prior for a Bernoulli probability $p$, written in the parameter $\varphi = \arcsin\sqrt p$, is the uniform density $2/\pi$ on $[0, \pi/2]$.

15. • A posterior for $p \in (0, 1)$ has density $2p$. Find its 90% highest density interval. Then write $\psi = p^3$, find the 90% highest density interval of $\psi$, and map it back to $p$. Both sets have posterior probability $0.9$; are they the same set?

16. • Means $\mu_i$ are $+2$ or $-2$ with probability $1/2$ each, and $z_i \sim N(\mu_i, 1)$. Use Tweedie's formula from [empirical Bayes](/empirical-bayes/) to find $\mathbb{E}[\mu \mid z]$, check it by Bayes' theorem directly, and evaluate it at $z = 1$.

17. • One coefficient has $y \sim N(\beta, 1)$ and a [spike-and-slab prior](/spike-and-slab-prior/) with weight $w = 1/2$ on the spike at 0 and a slab $N(0, 3)$. For $y = 2$, find the posterior inclusion probability and the posterior mean of $\beta$.

18. • For the [horseshoe prior](/horseshoe-prior/) with $\lambda \sim C^+(0, 1)$ and $a = \tau^2/\sigma^2$, show that the shrinkage coefficient $\kappa = 1/(1 + a\lambda^2)$ satisfies $P(\kappa \le 1/2) = \frac{2}{\pi}\arctan\sqrt a$. Evaluate it at $a = 1/4$, and check the value by simulation.

19. • Take the posterior Beta$(16, 6)$ of 15 heads in 20 tosses under a uniform prior. Find the [Laplace approximation](/laplace-approximation/) in the scale of $p$: its centre, its standard deviation and its 95% interval. Compare them with the exact mean, standard deviation and equal-tailed interval $[0.528, 0.887]$, and explain the direction of the error.

20. • In [ABC sequential Monte Carlo](/abc-sequential-monte-carlo/), the prior is uniform on $[0, 1]$, the previous population is $0.2$ and $0.4$ with weight $1/2$ each, and the kernel is normal with standard deviation $0.1$. Two new particles at $0.3$ and $0.5$ pass the ABC test. Find their normalized weights, and say why the particle at $0.5$ gets more.

21. • Bernoulli data $(1, 1, 1, 0)$ have a uniform prior. Find each leave-one-out predictive probability $p(y_i \mid y_{-i})$ directly, then check each against the identity $p(y_i \mid y_{-i}) = 1/\mathbb{E}[1/p(y_i \mid \theta) \mid y]$ used by [PSIS-LOO](/pareto-smoothed-importance-sampling-loo/). Give $\mathrm{elpd}_{\mathrm{loo}}$.

22. • Fifty observations from Uniform$(0, \theta)$ have maximum 4. With the prior $1/\theta$, find the posterior and its 95% highest density interval. Explain why this posterior does not approach a normal law as the [Bernstein-von Mises theorem](/bernstein-von-mises-theorem/) would suggest.

23. • In the normal hierarchical model with a flat prior on $\mu$, the likelihood factor of $\tau$ is finite and positive at 0 and decays like $\tau^{1 - J}$. For which numbers of groups $J$ does the prior $p(\tau) \propto \tau^{-1/2}$ give a proper posterior?

24. • A latent $x \sim N(0, 1/\tau)$ and one observation $y \mid x \sim N(x, 1)$. Show that $\pi(x, \tau, y)/\pi(x \mid \tau, y)$ does not depend on $x$ and equals $\pi(\tau)\, N(y; 0, 1 + 1/\tau)$. What does this say about the outer step of [INLA](/integrated-nested-laplace-approximation/) for a Gaussian likelihood?

25. ★ Let $X \sim N(\theta, 1)$ with prior $\theta \sim N(0, 1)$, and let $C(x)$ be the 95% equal-tailed credible interval. Find its frequentist coverage as a function of $\theta$, evaluate it at $\theta = 0$ and $\theta = 3$, and prove that its average over the prior is exactly $0.95$.

26. ★ For $n$ observations from $N(\theta, \sigma^2)$ with $\sigma$ known, $M_0: \theta = 0$ and $M_1: \theta \sim N(0, \tau^2)$, derive $B_{01}$ from the Savage-Dickey density ratio and show that it equals the exact formula of the [Lindley paradox](/lindley-paradox/) entry.

27. ★ With $\tau = \sigma$ and $z = 2$ held fixed, find the smallest $n$ for which $B_{01} \ge 1$. Compare it with the value of $n$ that the expansion $\log B_{01} \approx \frac12\log n - \frac{z^2}{2}$ predicts.

28. ★ For 20 tosses, compare $M_0: p = 1/2$ with $M_1: p \sim$ Uniform$(0, 1)$. Write $B_{10}$ as a function of the number of heads $y$, show directly that $\mathbb{E}_0[B_{10}] = 1$, and find $P_0(B_{10} \ge 10)$ exactly. Compare it with the bound $1/10$ that an [e-variable](/e-variable/) satisfies.

29. ★ In exercise 21, the importance ratio of a point is $r = 1/p(y_i \mid \theta)$ with $\theta$ drawn from the full posterior Beta$(4, 2)$. Show that the ratio of each success has finite variance, and find it. Show that the ratio of the failure has a finite mean but infinite variance, and find the tail index of its distribution.

30. ★ In [simulation-based calibration](/simulation-based-calibration/) the exact posterior is $N(m, s^2)$, but a sampler returns draws from $N(m, c^2 s^2)$. Show that with $L = 1$ draw the rank is uniform for every $c$. With $L = 2$ and $c = 1/2$, find the probability of each rank.
