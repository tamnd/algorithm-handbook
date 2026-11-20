1. ◦ Let $Q = e^{\xi}$ with $\xi \sim N(0, 0.25)$, so the standard deviation of $\xi$ is 0.5. Compute $\mathbb{E}[Q]$, $\mathrm{Var}(Q)$ and $P(Q > 2)$, as in [forward uncertainty propagation](/forward-uncertainty-propagation/). How many Monte Carlo samples give a standard error of 0.01 for the mean, and how many a relative error of 10 % for $P(Q > 2)$?

2. ◦ For [multilevel Monte Carlo](/multilevel-monte-carlo/), give the cost for root mean square error $\varepsilon$ from the [complexity theorem](/mlmc-complexity-theorem/) when $(\alpha, \beta, \gamma)$ is $(1, 2, 1)$, $(1, 1, 1)$ and $(1, 1, 2)$. For each, give the cost $\varepsilon^{-2-\gamma/\alpha}$ of plain Monte Carlo on the finest level, and check the condition $\alpha \ge \frac12\min(\beta, \gamma)$.

3. ◦ A resistance $R \sim N(10, 1)$ and a load $S \sim N(6, 1.5^2)$ are independent, and failure is $G = R - S \le 0$. Write $G$ in standard normal variables, and use the [first-order reliability method](/first-order-reliability-method/) to find $\beta$, the design point $u^*$ and the values of $R$ and $S$ there. Give $P_f$, and say why FORM is exact here.

4. ◦ Let $f(x_1, x_2) = 2x_1 + x_2 + 4x_1x_2$ with $x_1$, $x_2$ independent and uniform on $[0, 1]$. Write the [Hoeffding-Sobol decomposition](/hoeffding-sobol-decomposition/) $f = f_0 + f_1 + f_2 + f_{12}$, the variance of each term, and the first order and total [Sobol indices](/sobol-indices/).

5. ◦ Apply the [Morris method](/morris-method/) with $p = 4$ levels to $f(x_1, x_2) = 2x_1 + x_2^2$ on $[0, 1]^2$. Give $\Delta$, the base values that $x_2$ can take, every possible elementary effect of each input, and $\mu^*$ and $\sigma$ of $x_1$. What does a nonzero $\sigma$ of $x_2$ tell you?

6. ◦ The 3-point Gauss-Hermite rule for $\xi \sim N(0, 1)$ has the nodes $0$, $\pm\sqrt3$ and the weights $\frac23$, $\frac16$, $\frac16$. In the basis $He_0 = 1$, $He_2 = \xi^2 - 1$, $He_4 = \xi^4 - 6\xi^2 + 3$, with $\mathbb{E}[He_k^2] = k!$, expand $f(\xi) = \xi^4$ exactly. Then compute $c_0$ and $c_2$ by [non-intrusive spectral projection](/non-intrusive-spectral-projection/) with this rule, and explain which one is wrong and why.

7. ◦ Solve $(3 + \xi)u = 1$, with $\xi$ uniform on $[-1, 1]$, by the [stochastic Galerkin method](/stochastic-galerkin-method/) with the basis $1$, $\xi$. Give $u_0$ and $u_1$, and compare $u_0$ with the exact mean.

8. ◦ Run [DEIM](/discrete-empirical-interpolation-method/) on $u_1 = (1, -2, 0, 1)$ and $u_2 = (0, 1, 3, 1)$. Give the two indices, and the approximation $\hat f$ of $f = (1, 1, 1, 1)$.

9. ◦ Three snapshots are $(1, 1, 0, 0)$, $(1, 0, 1, 0)$ and $(0, 1, 1, 0)$. For a [POD-Galerkin model](/pod-galerkin-reduced-model/), compute the eigenvalues of the $3 \times 3$ correlation matrix $S^TS$, the first POD mode, and the snapshot error $\sum_i \|s_i - \Pi s_i\|^2$ with one mode. Check it against $\sum_{i>1}\lambda_i$.

10. ◦ Count runs. (a) The [Saltelli scheme](/saltelli-sampling-scheme/) with $d = 8$ and $N = 1000$, with and without second order indices. (b) The number of chaos terms of total degree 3 in 8 inputs, and the usual range of runs for [regression](/regression-polynomial-chaos/). (c) The smallest number of points per curve for the [Fourier amplitude sensitivity test](/fourier-amplitude-sensitivity-test/) with $M = 4$ and $\omega_{\max} = 29$. (d) The number of levels and of evaluations of [subset simulation](/subset-simulation/) with $p_0 = 0.1$ and $N = 2000$ for $P_f \approx 2 \times 10^{-9}$, assuming each level's fraction comes out at its expected value.

11. • The Brownian bridge on $[0, 1]$ has the covariance $\min(s, t) - st$, with eigenvalues $\lambda_k = 1/(k^2\pi^2)$ and eigenfunctions $\sqrt2\sin(k\pi t)$. As a [random field](/random-field/), what fraction of the total variance $\int_0^1 t(1-t)\,dt$ do the first one, two and three terms of its Karhunen-Loève expansion keep? Write a short program to find the smallest number of terms that keeps 95 %.

12. • The points $x_i = (2i - 1)/(2N)$, $i = 1, \ldots, N$, have the star discrepancy $D_N^* = 1/(2N)$. For $f(x) = x^2$ on $[0, 1]$, give the [Koksma-Hlawka](/koksma-hlawka-inequality/) bound on the error of the equal-weight rule, the actual error, and the standard error of plain Monte Carlo with $N$ points.

13. • A multilevel Monte Carlo estimator has $V_0 = 1$, $V_l = 4^{-l}$ for $l \ge 1$, $C_l = 2^l$ and levels $0$ to $5$. For $\varepsilon = 0.01$, compute $N_l = \lceil 2\varepsilon^{-2}\sqrt{V_l/C_l}\sum_k\sqrt{V_kC_k}\rceil$ and the total cost. Compare with plain Monte Carlo on level 5 for the same variance $\varepsilon^2/2$, taking the variance of the finest level output as 1.

14. • [Multifidelity Monte Carlo](/multifidelity-monte-carlo/) has a high fidelity model with $\sigma_1 = 1$ and cost $w_1 = 1$, and a low fidelity model with $\sigma_2 = 1.2$, correlation $\rho_2 = 0.95$ and cost $w_2 = 0.01$. For the budget $p = 100$, compute $r_2$, $m_1$ and $m_2$ (rounded down), the weight $\alpha_2$, and the ratio of the variance to that of plain Monte Carlo at the same budget.

15. • For $(c + \xi)u = 1$ with $\xi$ uniform on $[-1, 1]$ and $c > 1$, show that the stochastic Galerkin mean with the basis $1$, $\xi$ is $3c/(3c^2 - 1)$, and that its error against the exact mean $\frac12\ln\frac{c+1}{c-1}$ is $\frac{4}{45c^5} + O(c^{-7})$.

16. • Fit $y \approx c_0 + c_1\xi$ by least squares to the runs $(\xi, y) = (-1, 1)$, $(0, 2)$, $(1, 4)$. Give $c$, the diagonal of the hat matrix, and the leave-one-out residuals and mean square error used by regression polynomial chaos. Check one residual by refitting without that run.

17. • A [sparse polynomial chaos](/sparse-polynomial-chaos/) problem minimizes $\frac12\|y - \Psi c\|^2 + \lambda\|c\|_1$ with orthonormal columns, $\Psi^T\Psi = I$. Show that the solution is the soft thresholding of $\Psi^Ty$, and give it for $\Psi^Ty = (3, -0.5, 1.2, 0.8)$ and $\lambda = 1$. How many [ISTA](/iterative-shrinkage-thresholding/) steps of length 1 from $c = 0$ does it take?

18. • Write a program that counts the distinct nodes of the Smolyak grid of [stochastic collocation](/stochastic-collocation-method/) with nested Clenshaw-Curtis rules, $m(0) = 1$ and $m(l) = 2^l + 1$, for $d = 4$ and levels $L = 0$ to 4. Compare level 2 and level 4 with the full tensor grids built from the same one-dimensional rules.

19. • Run the [empirical interpolation method](/empirical-interpolation-method/) on $g(x; \mu) = x + \mu x^2$ on the grid $\{0, \frac12, 1\}$ with the training set $\{1, 2\}$. Give $\mu_1$, $x_1$, $q_1$, then $\mu_2$, $x_2$, $q_2$. For $\mu = 3$, give the error of $I_1 g$ and of $I_2 g$ on the grid.

20. • In $\mathbb{R}^2$ with the Euclidean norm, compute the [Kolmogorov width](/kolmogorov-width/) $d_1$ of $K = \{e_1, e_2\}$ and the error of the strong greedy algorithm after one step. Do the same for $\{e_1, e_2, e_3\}$ in $\mathbb{R}^3$. What does this say about the [weak greedy](/weak-greedy-reduced-basis/) bounds for small $n$?

21. • A reduced state of dimension 1 is observed as $a = 1$, 0.8, 0.66, 0.55. Fit the discrete model $a_{k+1} = c_1a_k + c_2a_k^2$ by least squares, as [operator inference](/operator-inference/) does, and give the residuals of the fit.

22. • A rank-one step of the [proper generalized decomposition](/proper-generalized-decomposition/) for a matrix $F$ alternates $x \leftarrow Fy/\|y\|^2$ and $y \leftarrow F^Tx/\|x\|^2$. For $F = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $y = (1, 0)$, do two steps, show that the iteration is the power method for $FF^T$, and give the limit of $xy^T$ and the Frobenius error that remains.

23. ★ Derive the sample sizes of multilevel Monte Carlo: minimize $\sum_l N_lC_l$ subject to $\sum_l V_l/N_l = \varepsilon^2/2$, treating $N_l$ as real. Show that the minimal cost is $2\varepsilon^{-2}\bigl(\sum_l\sqrt{V_lC_l}\bigr)^2$, and deduce the $O(\varepsilon^{-2})$ case of the complexity theorem when $\beta > \gamma$.

24. ★ From the Hoeffding-Sobol decomposition of a function of independent inputs, prove $0 \le S_i \le S_{Ti} \le 1$ and $\sum_iS_i \le 1 \le \sum_iS_{Ti}$. When do the two sums equal 1?

25. ★ In the Saltelli scheme, prove that $\mathbb{E}\bigl[\frac12(f(A) - f(AB_i))^2\bigr] = \mathbb{E}[\mathrm{Var}(Q \mid \xi_{\sim i})]$, so the numerator of Jansen's estimator of $S_{Ti}$ is unbiased. Is the ratio $\hat S_{Ti}$ unbiased?

26. ★ For $G(u) = \beta - u_1$ in standard normal space and failure $G \le 0$, sample from $N(u^*, I)$ at the design point $u^* = (\beta, 0, \ldots, 0)$ and weight by the density ratio, as in [importance sampling](/importance-sampling/). Show that the second moment of one weighted indicator is $e^{\beta^2}\Phi(-2\beta)$. For $\beta = 3$, give the relative variance per sample and the number of samples for a 10 % relative error, against plain Monte Carlo.

27. ★ A scalar parameter has the prior $N(0, 1)$ and the datum $y = u + \eta$ with $\eta \sim N(0, \gamma^2)$. Find the posterior, and show that the Hellinger distance $d_H^2 = \frac12\int(\sqrt p - \sqrt q)^2$ between the posteriors for $y$ and $y'$ satisfies $d_H \le L|y - y'|$ with $L = 1/(2\sqrt2\,\gamma\sqrt{1 + \gamma^2})$, as the [well-posedness theorem](/bayesian-inverse-problem-well-posedness/) predicts. Evaluate both sides for $\gamma = 1$ and $|y - y'| = 0.2$.
