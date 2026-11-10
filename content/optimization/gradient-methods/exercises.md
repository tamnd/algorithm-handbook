1. ◦ Run [gradient descent](/gradient-descent/) on $f(x) = 2x^2$ from $x_0 = 1$ with the fixed steps $\alpha = 0.1$, $0.25$, $0.5$ and $0.6$. Give $x_3$ in each case, and the set of steps for which the iterates converge to $0$.

2. ◦ Let $f(x) = \frac12x^\top Ax$ with $A = \begin{pmatrix} 5 & 3 \\ 3 & 5\end{pmatrix}$. Find the [smoothness](/smoothness/) constant $L_f$, the strong convexity constant $\mu$ and the [condition number](/condition-number-of-an-optimization-problem/) $\kappa$. For gradient descent with step $1/L_f$, give the factor per step on $f(x_k) - f^*$ that the [linear convergence theorem](/linear-convergence-strongly-convex/) guarantees, and the worst factor on this particular $f$. Give the factor by which the step $2/(\mu + L_f)$ reduces $\|x_k - x^*\|$. Then give the tuned [heavy ball](/momentum-method/) parameters $\alpha$, $\beta$ and the rate $\rho$. Ignoring the polynomial factor of the heavy ball bound, how many steps does each of the last two methods need to reduce the distance to $x^*$ by $10^{-6}$?

3. ◦ Classify each error sequence as sublinear, linear, superlinear but not quadratic, or quadratic, and give the first $k$ with $e_k \le 10^{-6}$: $e_k = 2^{-k}$, $e_k = 1/k^2$, $e_k = 2^{-2^k}$, $e_k = 1/k!$. Use the definitions of the entry on [convergence rates](/convergence-rate/).

4. ◦ Let $f(x) = x_1^2 + 4x_2^2$, $x = (1, 1)$ and $d = -\nabla f(x)$. Write $\varphi(\alpha) = f(x + \alpha d)$ as a polynomial. Find the steps that satisfy the [Armijo condition](/armijo-condition/) with $c = 10^{-4}$ and with $c = \frac12$. Run [backtracking](/backtracking-line-search/) from $\alpha_0 = 1$ with $\rho = \frac12$ for each $c$, and give the accepted step, the number of trials and the new value of $f$. Compare with the [exact step](/exact-line-search/).

5. ◦ Let $x = (1.2, -0.3, -2, 0.5)$. Compute $\operatorname{prox}_{th}(x)$ for $h = \lambda\|\cdot\|_1$ with $t\lambda = 0.5$, for $h = \frac\lambda2\|\cdot\|^2$ with $t\lambda = 1$, for $h = \lambda\|\cdot\|_0$ with $t\lambda = 0.5$, and for the indicator of the box $[0, 1]^4$. Use the formulas of the entry on the [proximal operator](/proximal-operator/).

6. ◦ Project $v = (0.8, 0.6, -0.2)$ onto the box $[0, 1]^3$, onto the closed unit ball and onto the probability simplex $\{x \ge 0 : x_1 + x_2 + x_3 = 1\}$.

7. ◦ Compute $t_2, \dots, t_5$ for the sequence $t_1 = 1$, $t_{k+1} = (1 + \sqrt{1 + 4t_k^2})/2$ of [Nesterov's method](/nesterov-accelerated-gradient/), to four decimals, and the momentum weights $\beta_k = (t_k - 1)/t_{k+1}$ for $k = 1, \dots, 4$. Compare them with the weights $(k - 1)/(k + 2)$ of the simpler choice $t_k = (k + 1)/2$.

8. ◦ The first gradient is $g_1 = (0.02, -5)$. Give the first step of [Adam](/adam/) with $\alpha = 10^{-3}$, $\beta_1 = 0.9$, $\beta_2 = 0.999$ and $\epsilon$ taken as $0$. Give the step without the bias correction, and the step of plain gradient descent with step $10^{-3}$.

9. ◦ Take one step of [mirror descent](/mirror-descent/) with the entropy on the simplex in $\mathbb{R}^3$ from $x = (\frac13, \frac13, \frac13)$, with gradient $g = (1, 0, -1)$ and $\eta = \ln 2$. Give the new point and the change of the linear function $g^\top x$.

10. ◦ A [finite sum](/finite-sum-minimization/) has $N = 10^4$ terms and condition number $\kappa = 10^6$. Ignoring constants and the factor $\log(1/\varepsilon)$, compare the number of component gradients for gradient descent, accelerated gradient descent, [SVRG](/svrg/) and Katyusha. For $\kappa = 10^6$, from which $N$ on does SVRG need fewer component gradients than accelerated gradient descent?

11. • For the function $\varphi(\alpha)$ of Exercise 4, find the set of steps that satisfy the [Wolfe conditions](/wolfe-conditions/) with $c_1 = 10^{-4}$ and $c_2 = 0.9$, and the set that satisfies the strong Wolfe conditions with $c_2 = 0.1$.

12. • Show that the [Polyak step](/polyak-step-size/) on $f(x) = |x|^p$ with $p \ge 1$ gives $x_{k+1} = (1 - 1/p)x_k$. How many steps does it take from $x_0 = 1$ to reach $|x| \le 10^{-6}$ when $p = 4$? Explain why the linear rate is remarkable here, given that $x^4$ satisfies neither strong convexity nor the [Polyak-Lojasiewicz condition](/polyak-lojasiewicz-condition/).

13. • Consider [logistic regression](/logistic-regression/) $f(w) = \frac12\sum_{i=1}^2\log(1 + e^{-y_ia_i^\top w})$ with $a_1 = (1, 2)$, $a_2 = (2, 1)$ and labels $y_i \in \{-1, 1\}$. Using $\ell'' \le \frac14$ for $\ell(z) = \log(1 + e^{-z})$, give an upper bound on $L_f$ that does not depend on the labels, and the step $1/L_f$. Add the ridge term $\frac{0.1}{2}\|w\|^2$ and bound $L_f$, $\mu$ and $\kappa$.

14. • Run two cyclic sweeps of [coordinate descent](/coordinate-descent/) with steps $1/L_i$ on $f(x) = \frac12x^\top Ax - b^\top x$, $A = \begin{pmatrix} 4 & 2 \\ 2 & 3\end{pmatrix}$, $b = (1, 2)$, from $x_0 = (0, 0)$. Show that each sweep multiplies the error $x - x^*$ by $\frac13$, and that for every $2 \times 2$ positive definite matrix the factor is $a_{12}^2/(a_{11}a_{22})$.

15. • Run the heavy ball method $x_{k+1} = x_k - \alpha f'(x_k) + \beta(x_k - x_{k-1})$ on $f(x) = \frac12x^2$ with $\alpha = 1$, $\beta = \frac12$ and $x_{-1} = x_0 = 1$, up to $x_5$. Find a step at which $f$ increases. Find the roots of the characteristic polynomial of the recurrence and their modulus.

16. • Let $C$ be a closed convex set and $\Pi_C$ the Euclidean projection onto it. Prove that $(x - \Pi_C(x))^\top(z - \Pi_C(x)) \le 0$ for every $z \in C$, and deduce that $\|\Pi_C(x) - \Pi_C(y)\| \le \|x - y\|$.

17. • Run the [proximal gradient method](/proximal-gradient-method/) on the lasso $\frac12\|Ax - b\|^2 + \|x\|_1$ with $A = \operatorname{diag}(1, 2)$ and $b = (3, 1)$, with step $t = 1/L_f$, from $x_0 = (0, 0)$. Find $x^*$ and $F^*$, the iterates $x_1$ to $x_3$, a closed form for $x_k$, and the first $k$ with $\|x_k - x^*\| \le 10^{-6}$.

18. • Run Fletcher-Reeves [nonlinear conjugate gradient](/nonlinear-conjugate-gradient/) with exact line search on $f(x) = x_1^2 + 4x_2^2$ from $(1, 1)$. Give $\alpha_0$, $x_1$, $\beta_1$, $d_1$, $\alpha_1$ and $x_2$ as exact fractions.

19. • Let $f_1(x) = (x - 1)^2$, $f_2(x) = (x + 1)^2$ and $F = \frac12(f_1 + f_2)$. At $x = 0.2$, with snapshot $\tilde x = 0.5$, compute the two possible stochastic gradients of SGD and the two possible estimates of [SVRG](/svrg/), with their means and variances. Explain why the SVRG estimate has variance $0$ here at every $x$, and give a pair $f_1$, $f_2$ for which it does not.

20. • A coordinate receives the same gradient $g \ne 0$ at every step. With $\epsilon = 0$ and zero initial accumulators, give the length of step $t$ for [AdaGrad](/adagrad/) with step $\eta$, for [RMSProp](/rmsprop/) with step $\eta$ and decay $\beta$, and for Adam with step $\alpha$. Give the total distance AdaGrad covers in the first 100 steps, to two decimals.

21. • Compute the [Bregman divergence](/bregman-divergence/) $D_\psi(x, y)$ of $\psi(x) = x^4$ for $(x, y) = (0, 1)$, $(1, 0)$, $(2, 1)$ and $(1, 2)$, and of $\psi(x) = e^x$ for $(0, 1)$ and $(1, 0)$. Use the first function to show that $D_\psi(0, 2) > D_\psi(0, 1) + D_\psi(1, 2)$.

22. • Let $f$ be convex and $L_f$-smooth and $x_{k+1} = x_k - \nabla f(x_k)/L_f$. Using co-coercivity, prove that $\|\nabla f(x_{k+1})\| \le \|\nabla f(x_k)\|$ and $\|x_{k+1} - x^*\| \le \|x_k - x^*\|$ for every minimizer $x^*$.

23. ★ Let $f(x) = \frac12(\mu x_1^2 + Lx_2^2)$ with $0 < \mu < L$. Show that steepest descent with [exact line search](/exact-line-search/) from $x_0 = (L, \mu)$ produces $x_k = \left(\frac{\kappa - 1}{\kappa + 1}\right)^k(L, (-1)^k\mu)$, so that the Kantorovich factor $\left(\frac{\kappa - 1}{\kappa + 1}\right)^2$ on $f$ is attained at every step, for every $\kappa$.

24. ★ For the heavy ball method on $f(x) = \frac\lambda2x^2$ with $\lambda > 0$ and $0 \le \beta < 1$, prove that the iterates converge to $0$ from every start if and only if $0 < \alpha\lambda < 2(1 + \beta)$. Check that the parameters $\mu = 1$, $L = 25$, $\alpha = 1/9$, $\beta = 4/9$ of Lessard, Recht and Packard satisfy this for every $\lambda \in [1, 25]$, and conclude what the function in their counterexample cannot be.

25. ★ Let $g : \mathbb{R}^m \to \mathbb{R}$ be $\mu$-strongly convex and differentiable, let $A$ be an $m \times n$ matrix with smallest nonzero singular value $\sigma_+$, and let $f(x) = g(Ax)$. Prove that $f$ satisfies the [Polyak-Lojasiewicz condition](/polyak-lojasiewicz-condition/) with constant $\mu\sigma_+^2$.

26. ★ The [Robbins-Monro algorithm](/robbins-monro-algorithm/) estimates the mean $\theta$ of independent observations $\xi_n$ with variance $\sigma^2$ by $x_{n+1} = x_n - \frac an(x_n - \xi_n)$. Let $V_n = \mathbb{E}(x_n - \theta)^2$. Derive the recurrence for $V_n$, show that $nV_n \to a^2\sigma^2/(2a - 1)$ for $a > \frac12$, find the best $a$, and show that $V_n$ decreases only like $n^{-2a}$ for $0 < a < \frac12$.

27. ★ Prove that the Euclidean projection of $v \in \mathbb{R}^n$ onto the probability simplex is $x_i = \max(v_i - \theta, 0)$ for a unique $\theta$, and give an $O(n\log n)$ algorithm that finds $\theta$. Apply it to $v = (1.2, 0.7, 0.4, -1)$.
