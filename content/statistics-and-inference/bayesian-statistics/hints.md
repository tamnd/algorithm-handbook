1. The posterior mean is $3/10$, the mode is $(3 - 1)/(3 + 7 - 2) = 1/4$, and the variance is $3 \cdot 7/(10^2 \cdot 11) = 21/1100$. The mode is the maximum likelihood estimate $2/8$, because the uniform prior is flat.

4. The beta-binomial law gives $P(0, 1, 2, 3) = 5/91, 20/91, 36/91, 30/91$. The plug-in law gives $1/27, 2/9, 4/9, 8/27$. The predictive puts more mass on both ends: $5/91 \approx 0.055$ against $0.037$ for 0, and $30/91 \approx 0.330$ against $0.296$ for 3, because it also carries the uncertainty about $p$.

6. The density is decreasing, so the highest density interval starts at 0: it is $[0, \ln 20/2] = [0, 1.4979]$. The equal-tailed interval is $[-\ln 0.975/2, -\ln 0.025/2] = [0.0127, 1.8444]$, of length $1.8318$.

7. The posterior is Beta$(6, 6)$, whose density at $1/2$ is $\frac{11!}{5!\,5!}\,2^{-10} = 2772/1024 = 693/256 \approx 2.707$. The prior density is 1, so $B_{01} = 693/256$. Directly, $m_0 = \binom{10}{5}2^{-10} = 252/1024$ and $m_1 = 1/11$, and their ratio is $693/256$. The data favour the fair coin.

9. Both orders have probability $\frac{1 \cdot 2 \cdot 1}{2 \cdot 3 \cdot 4} = 1/12$, which is $\int_0^1 \theta^2(1 - \theta)\, d\theta$. $P(X_1 = X_2 = 1) = 1/3$ and $P(X_1 = 1) = 1/2$, so the covariance is $1/3 - 1/4 = 1/12$, the variance of a uniform $\Theta$. The mixing law is Beta$(1, 1)$, the uniform law.

12. The posterior is $N(0.8x, 0.8)$, so the estimator is $0.8X$ and its Bayes risk is $0.8$; the Bayes risk of $X$ is 1. At a fixed $\theta$, the risk of $0.8X$ is the variance $0.64$ plus the squared bias $0.04\theta^2$. It exceeds 1 when $|\theta| > 3$, where the prior has little mass.

13. The posterior is Gamma with shape 10 and rate 4, and the predictive is negative binomial: $P(0) = (4/5)^{10} = 0.1074$, against $e^{-2.5} = 0.0821$ for the plug-in. The predictive mean is $2.5$ and its variance is $2.5 + 2.5/4 = 3.125$, more than the Poisson variance $2.5$.

15. The highest density set of $p$ is $[c, 1]$ with $1 - c^2 = 0.9$, that is $[0.3162, 1]$. The density of $\psi$ is $\frac23\psi^{-1/3}$, which decreases, so its set is $[0, d]$ with $d^{2/3} = 0.9$, $d = 0.8538$. Mapped back it is $p \in [0, 0.9487]$. The two sets differ: a highest density region is not kept under a non-affine change of variable.

16. The marginal is $m(z) = \frac12\varphi(z - 2) + \frac12\varphi(z + 2)$, and $z + (\log m)'(z)$ simplifies to $2\tanh(2z)$. Bayes' theorem gives the same, since $P(\mu = 2 \mid z) = e^{2z}/(e^{2z} + e^{-2z})$. At $z = 1$ the value is $2\tanh 2 = 1.928$: the estimate moves almost all the way to the nearer point.

19. The log density is $15\log p + 5\log(1 - p)$, with mode $0.75$ and curvature $15/0.75^2 + 5/0.25^2 = 106.67$, so the standard deviation is $0.0968$ and the interval is $[0.560, 0.940]$. The exact mean is $16/22 = 0.727$ and the exact standard deviation $0.0929$. The posterior is skewed to the left, and the normal law centred at the mode misses it on the right.

22. The posterior is $50 \cdot 4^{50}\theta^{-51}$ on $\theta > 4$, so $P(\theta > t \mid x) = (4/t)^{50}$ and the interval is $[4, 4 \cdot 20^{1/50}] = [4, 4.247]$. The model is not regular: its support depends on $\theta$. The posterior has width of order $1/n$, not $1/\sqrt n$, and its rescaled limit is exponential, not normal.

25. The posterior is $N(x/2, 1/2)$, so $C(x) = x/2 \pm 1.386$. Since $X/2 - \theta \sim N(-\theta/2, 1/4)$, the coverage is $\Phi(2.772 + \theta) - \Phi(\theta - 2.772)$: $0.9944$ at $\theta = 0$ and $0.4097$ at $\theta = 3$. For the average, write the joint law of $(\theta, X)$ in both orders and use Fubini's theorem: the average coverage equals the average over $X$ of the posterior probability of $C(X)$, which is $0.95$ for every $X$.

27. The exact formula is $B_{01} = \sqrt{1 + n}\, \exp(-2n/(1 + n))$. It is $0.996$ at $n = 49$ and $1.005$ at $n = 50$, so the answer is $n = 50$. The expansion gives $\frac12 \log n = 2$, so $n = e^4 \approx 54.6$; its remainder term is still visible at this $n$.

28. $B_{10}(y) = 2^{20}/\big(21\binom{20}{y}\big)$, so $\mathbb{E}_0[B_{10}] = \sum_y \binom{20}{y}2^{-20} \cdot 2^{20}/\big(21\binom{20}{y}\big) = 21/21 = 1$. $B_{10} \ge 10$ when $\binom{20}{y} \le 2^{20}/210$, that is for $y \le 4$ or $y \ge 16$. Then $P_0(B_{10} \ge 10) = 2(1 + 20 + 190 + 1140 + 4845)/2^{20} = 1549/131072 \approx 0.0118$, well below $1/10$.

29. For a success, $r = 1/\theta$, and $\mathbb{E}[\theta^{-2}] = B(2, 2)/B(4, 2) = 10/3$, so the variance is $10/3 - 25/9 = 5/9$. For the failure, $r = 1/(1 - \theta)$ has mean $B(4, 1)/B(4, 2) = 5$, but $\mathbb{E}[(1 - \theta)^{-2}] = 20\int_0^1 \theta^3(1 - \theta)^{-1}\, d\theta$ diverges. Near $\theta = 1$ the density is about $20(1 - \theta)$, so $P(r > t) \approx 10/t^2$: tail index 2, a generalized Pareto shape of $1/2$.

30. With $L = 1$ the rank is 0 when the draw exceeds the truth. The difference of the two is symmetric about 0, so this has probability $1/2$ whatever $c$ is. With $L = 2$, rank 0 means that both draws exceed the truth. The two differences are normal with correlation $1/(1 + c^2) = 0.8$, and the orthant formula gives $\frac14 + \frac{1}{2\pi}\arcsin 0.8 = 0.3976$. By symmetry rank 2 has the same probability, and rank 1 has $0.2048$, against $1/3$ each for a correct sampler. A simulation with `random.Random(29)` and 100000 replications gives $0.3972$, $0.2046$ and $0.3982$ for ranks 0, 1 and 2.
