In these exercises $A$ has the singular system $(\sigma_k; v_k, u_k)$ of the [singular value expansion](/singular-value-expansion/), the data are $y^\delta$ with $\|y^\delta - Ax^\dagger\| \le \delta$, and $b_k = \langle u_k, y^\delta\rangle$. A linear method with [spectral filter factors](/spectral-filter-factors/) $f_k$ gives $x = \sum_k f_k\,(b_k/\sigma_k)\,v_k$. When $A$ is a diagonal matrix, $u_k$ and $v_k$ are the unit vectors and $b_k$ is the $k$th entry of $y^\delta$.

1. ◦ The integration operator $(Ax)(s) = \int_0^s x(t)\,dt$ on $L^2(0, 1)$ has $\sigma_k = 2/((2k-1)\pi)$. Compute $\sigma_1$, $\sigma_5$ and $\sigma_{10}$, and the ratio $\sigma_1/\sigma_{10}$. What is its [degree of ill-posedness](/degree-of-ill-posedness/)?

2. ◦ In Hadamard's example on the page [well-posed problem](/well-posed-problem/), the Cauchy data $\partial_y u(x, 0) = \sin(nx)/n$ give the solution $u(x, y) = \sin(nx)\sinh(ny)/n^2$. For $n = 5$ and $n = 30$, give the size of the data and the amplitude of the solution at $y = 1$. Which of Hadamard's three conditions fails?

3. ◦ Let $A$ have the singular values $1$, $0.3$ and $0.03$. Compute the filter factors of Tikhonov regularization with $\alpha = 0.01$, of [truncated SVD](/truncated-svd/) with $k = 2$, and of [Landweber iteration](/landweber-iteration/) with $\omega = 1$ after $k = 100$ steps. For which $\omega$ does Landweber iteration converge here?

4. ◦ For the integration operator of Exercise 1, let the data have the coefficients $b_k = k^{-p}$. Use the [Picard condition](/picard-condition/) to find the values of $p$ for which $Ax = y$ has a solution in $L^2(0, 1)$. Decide the cases $p = 2$, $p = 1.5$ and $p = 1.4$.

5. ◦ Classify the decay $\sigma_k = k^{-1/2}$, $\sigma_k = k^{-3}$, $\sigma_k = e^{-k}$ and $\sigma_k = e^{-k^2\pi^2 T}$ (the backward heat equation) as mildly, moderately or severely ill posed.

6. ◦ A $6 \times 6$ problem has $|b_k| = 1, 0.3, 0.05, 0.02, 0.012, 0.011$ for $k = 1, \ldots, 6$, the noise level is $\delta = 0.02$, and $\tau = 1.1$. The residual of truncated SVD with $k$ terms is $(\sum_{i > k} b_i^2)^{1/2}$. Which $k$ does the [discrepancy principle](/morozov-discrepancy-principle/) choose?

7. ◦ In the scalar [linear Gaussian inverse problem](/linear-gaussian-inverse-problem/) $y = 2x + e$ with prior $x \sim N(0, 1)$ and noise $e \sim N(0, 1)$, the datum is $y = 3$. Compute the posterior mean and variance. Check that the mean is the Tikhonov solution with $\alpha = \sigma^2/\gamma^2$.

8. ◦ Let $A = \mathrm{diag}(1, 1, 0.1)$ and let every entry of $y$ be nonzero. After how many steps does [CGLS](/cgls/), started at 0, reach the least squares solution in exact arithmetic? Does Landweber iteration ever reach it?

9. • Show that $\max_{\sigma > 0} \sigma/(\sigma^2 + \alpha) = 1/(2\sqrt\alpha)$, and conclude that the noise part of a Tikhonov solution has norm at most $\delta/(2\sqrt\alpha)$. Evaluate the bound for $\alpha = 10^{-4}$ and $\delta = 10^{-3}$, and compare it with truncated SVD that keeps the components with $\sigma_k \ge \sqrt\alpha$.

10. • Tikhonov regularization gives the filter factor $1/2$ at $\sigma^2 = \alpha$. Find the number of Landweber steps $k$ for which the Landweber filter factor at $\sigma^2 = \alpha$ is also $1/2$, for $\alpha = 0.01$ and $\alpha = 0.001$ with $\omega = 1$. Compare with the rule $\alpha \approx 1/(\omega k)$.

11. • Check the identity $\sum_k \sigma_k^2 = \int_0^1\!\int_0^1 K(s, t)^2\,dt\,ds$ for the integration operator, whose kernel is $K(s, t) = 1$ for $t < s$ and 0 otherwise. Use $\sum_{k \ge 1} (2k-1)^{-2} = \pi^2/8$.

12. • For a linear filter method the [resolution matrix](/resolution-matrix/) is $R = V\,\mathrm{diag}(f_k)\,V^{\mathsf T}$. Compute its trace for Tikhonov regularization with $\alpha = 0.01$ when the singular values are $1$, $0.5$, $0.1$ and $0.01$, and for truncated SVD with $k = 2$. Why is the trace called the effective number of parameters?

13. • Let $A = \mathrm{diag}(1, 0.1)$, $y^\delta = (1, 0.05)$ and $\tau\delta = 0.05$. Show that the Tikhonov residual $\|Ax_\alpha - y^\delta\|$ increases with $\alpha$, and find the $\alpha$ of the discrepancy principle and the solution $x_\alpha$ to three digits.

14. • Let $A = \mathrm{diag}(1, 0.01)$, $x^\dagger = (1, 1)$ and $e = (0.01, 0.01)$, and run Landweber iteration with $\omega = 1$ from 0. (a) Write the error $\|x_k - x^\dagger\|$ as a function of $k$. (b) Find the step with the smallest error, and that error. (c) What does the error tend to as $k \to \infty$? (d) Which step does the discrepancy principle with $\tau = 1.1$ choose, and what is the error there? Relate the answers to [semi-convergence](/semi-convergence/).

15. • Let $\sigma_k = 1/k$, let $x^\dagger = (A^*A)^\nu w$ with $\|w\| \le 1$, and let $\delta = 10^{-6}$. Bound the bias of truncated SVD with $k$ terms by $\sigma_{k+1}^{2\nu}$ and its noise part by $\delta/\sigma_k$. Balance the two to find $k$ and the order of the error for $\nu = 1/2$, $1$ and $2$.

16. • The [Tikhonov convergence rates](/tikhonov-convergence-rates/) give the bound $\tfrac32\rho^{1/(2\nu+1)}\delta^{2\nu/(2\nu+1)}$ for $\alpha = (\delta/\rho)^{2/(2\nu+1)}$ and $0 < \nu \le 1$. Take $\rho = 1$. Compute $\alpha$ and the bound for $\nu = 1/2$ with $\delta = 10^{-4}$ and $10^{-6}$, and for $\nu = 1$ with $\delta = 10^{-3}$ and $10^{-6}$. What happens to the bound when the [source condition](/source-condition/) holds with $\nu = 2$?

17. • For soft thresholding at $\lambda$ with noise variance $\sigma^2 = 1$, [Stein's unbiased risk estimate](/stein-unbiased-risk-estimate/) is $\sum_k \min(y_k^2, \lambda^2) + 2\,\#\{k : |y_k| > \lambda\} - m$. For $y = (3, 0.5, -2, 0.2, 1.2)$ compute it at $\lambda = 0$, $0.4$, $1$ and $1.5$, and find the $\lambda \ge 0$ that minimizes it.

18. • Show that for a linear forward operator $F(x) = Ax$ the step of the [iteratively regularized Gauss-Newton method](/iteratively-regularized-gauss-newton/) gives $x_{k+1} = x_0 + (A^*A + \alpha_k I)^{-1}A^*(y - Ax_0)$, whatever $x_k$ is. With $\alpha_0 = 1$ and $q = 0.5$, how many steps are needed before $\alpha_k \le 10^{-6}$?

19. • Show that the proposal of [preconditioned Crank-Nicolson MCMC](/preconditioned-crank-nicolson-mcmc/) maps a draw $u \sim N(m_0, C)$ to a draw $v \sim N(m_0, C)$. Conclude that with a zero misfit $\Phi$ every proposal is accepted. In one dimension with $m_0 = 1$, $C = 4$ and $\beta = 0.6$, give the law of $v$ given $u = 3$.

20. ★ Prove the [Bakushinskii veto](/bakushinskii-veto/) for linear methods: if a rule $\alpha = \alpha(y^\delta)$ that does not use $\delta$ makes $R_{\alpha(y^\delta)}y^\delta \to A^\dagger y$ for every $y$ in the domain of $A^\dagger$ and every $y^\delta$ with $\|y^\delta - y\| \le \delta \to 0$, then $A^\dagger$ is continuous on its domain.

21. ★ Show that for $0 < \nu < 1$ and $\alpha > 0$,

$$\sup_{t > 0} \frac{t^\nu\,\alpha}{t + \alpha} = \nu^\nu (1 - \nu)^{1 - \nu}\,\alpha^\nu .$$

Explain why this gives the Tikhonov bias bound under a source condition, and why for $\nu > 1$ the bias is still of order $\alpha$ when the spectrum of $A^*A$ is $(0, \|A\|^2]$. This is the [qualification](/qualification-of-regularization/) 1 of Tikhonov regularization.

22. ★ Let $y = Ax + e$ with $e \sim N(0, \sigma^2 I_m)$ and let $H$ be the symmetric influence matrix of Tikhonov regularization, so that $Ax_\alpha = Hy$. Show that the [unbiased predictive risk estimator](/unbiased-predictive-risk-estimator/) $U(\alpha) = \frac1m\|(I - H)y\|^2 + \frac{2\sigma^2}{m}\mathrm{tr}\,H - \sigma^2$ has expected value $\frac1m\,\mathbb{E}\|Hy - Ax\|^2$.

23. ★ The [approximate inverse](/approximate-inverse/) entry solves the integration problem with the hat mollifier of width $\gamma$, whose kernel has norm $\sqrt2\,\gamma^{-3/2}$, and finds the rate $\delta^{4/7}$ for a smooth solution. Take instead $x(t) = |t - \tfrac12|$ and $p = \tfrac12$. Show that the smoothing error is exactly $\gamma/3$, find the $\gamma$ that minimizes $\gamma/3 + \sqrt2\,\delta\gamma^{-3/2}$, and give the rate. Evaluate $\gamma$ and the bound for $\delta = 10^{-3}$.

24. ★ In [randomize-then-optimize](/randomize-then-optimize/) let $F(x) = Gx$ with $G$ of size $M \times n$ and full column rank, so the posterior is $\pi(x) \propto \exp(-\frac12\|Gx - \bar y\|^2)$. Let $G = QR$ be a thin [QR decomposition](/qr-decomposition/). Show that the solution of $Q^{\mathsf T}Gx = Q^{\mathsf T}(\bar y + \varepsilon)$ with $\varepsilon \sim N(0, I_M)$ is an exact draw from $\pi$.
