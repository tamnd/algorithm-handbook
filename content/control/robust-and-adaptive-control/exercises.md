1. ◦ Let $G(s) = 1/(s^2 + s + 1)$. Use $|G(j\omega)|^2 = 1/((1 - \omega^2)^2 + \omega^2)$ to find the [H-infinity norm](/h-infinity-norm/) and the frequency of the peak. Then compute the [H2 norm](/h2-norm/), either from a Gramian or from the integral of $|G(j\omega)|^2$. Which of the two norms is larger here?

2. ◦ Take $G(s) = 1/(s + 2)$ with the realization $A = -2$, $B = C = 1$, $D = 0$, and the Hamiltonian $H_\gamma = \begin{pmatrix} A & \gamma^{-2} B B^T \\ -C^T C & -A^T \end{pmatrix}$ of [H-infinity norm computation](/h-infinity-norm-computation/). Find the eigenvalues of $H_\gamma$ for $\gamma = 0.4$ and $\gamma = 0.6$. For $\gamma = 0.4$, check that $|G(j\omega)| = \gamma$ at the frequency given by the imaginary eigenvalue. What do the two tests say about $\|G\|_\infty$, and what is its exact value?

3. ◦ Let $M = \begin{pmatrix} 0 & 2 \\ 0.5 & 0 \end{pmatrix}$ and the structure $\boldsymbol\Delta = \{\mathrm{diag}(\delta_1, \delta_2) : \delta_i \in \mathbb{C}\}$. Compute $\rho(M)$, $\bar\sigma(M)$ and the [structured singular value](/structured-singular-value/) $\mu(M)$ from $\det(I - M\Delta)$. Then find $D = \mathrm{diag}(d, 1)$ with $\bar\sigma(D M D^{-1}) = \mu(M)$.

4. ◦ Close the loop around $P(s) = 1/(s + 1)$ with the gain $K = 4$. Find the complementary sensitivity $T$ and $\|T\|_\infty$. For the multiplicative [uncertainty model](/model-uncertainty/) $P(1 + w\Delta)$ with a constant weight $w$ and $\|\Delta\|_\infty \le 1$, find the largest $w$ that the [small-gain theorem](/small-gain-theorem/) certifies. Then find the exact set of real $\delta$ for which the loop with the plant $P(1 + \delta)$ is stable, and explain why it is much larger.

5. ◦ The family $s^3 + q_2 s^2 + q_1 s + q_0$ has $q_2 \in [3, 4]$, $q_1 \in [2, 5]$ and $q_0 \in [1, 7]$. Write the four polynomials of [Kharitonov's theorem](/kharitonov-theorem/) and test each with the cubic condition $a_2 a_1 > a_0$ (all coefficients positive). Is the whole family Hurwitz?

6. ◦ The plant $\dot y = 2y + u$ is controlled by $u = k y + l r$, and the reference model is $\dot y_m = -3 y_m + 3 r$. Find the gains $k^*$ and $l^*$ that make the closed loop equal the model, as in [model reference adaptive control](/model-reference-adaptive-control/). With the constant command $r = 1$, the adaptive gains may settle at other values while the error goes to zero. Which relation do all such resting values satisfy, and why does a constant command fail to be [persistently exciting](/persistent-excitation/) for two parameters?

7. ◦ For $y(t + 1) = 1.2\, y(t) + 2 u(t) + e(t + 1) - 0.3\, e(t)$ with white noise $e$ of variance $\sigma^2$, find the minimum variance control law $u = -f y$ that a [self-tuning regulator](/self-tuning-regulator/) aims at, and the variance of $y$ in closed loop. Is the open loop stable?

8. ◦ The statement "$F_0(x) = x + 2 \ge 0$ whenever $F_1(x) = 1 - x^2 \ge 0$" holds. Find every $\tau \ge 0$ with $F_0(x) - \tau F_1(x) \ge 0$ for all real $x$, the certificate of the [S-procedure](/s-procedure/).

9. • Let $p(s) = s^3 + s^2 + s + 0.9$ and $q(s) = s^3 + 3 s^2 + 3 s + 8.9$. Show that both are Hurwitz. Find the set of $\lambda \in [0, 1]$ for which $(1 - \lambda) p + \lambda q$ is not Hurwitz. What does this say about testing corners, and why does the [edge theorem](/edge-theorem/) still give the right answer?

10. • Take $P(s) = 1/(s - 2)$ with the [coprime factors](/coprime-factorization/) $N = 1/(s + 1)$ and $M = (s - 2)/(s + 1)$. Find constants $X$ and $Y$ with $MX + NY = 1$, and write every stabilizing controller by the [Youla parametrization](/youla-parametrization/). Which value $Q(0)$ gives integral action? Take the constant $Q$ with that value, and give the controller and the closed-loop characteristic polynomial.

11. • Replace the factor of the [Rohrs counterexample](/rohrs-counterexample/) by $100/(s + 10)^2$, so the plant is $2/(s + 1) \cdot 100/(s + 10)^2$, and freeze the feedback gain $k_y$ in $u = k_y y + k_r r$. Find the interval of $k_y$ for which the loop is stable, and the phase crossover frequency of the plant. Then run the adaptive law of the original example, from the same starting gains, with the command $0.3 + 1.85 \sin \omega t$ for several $\omega$ between 3 and 16 rad/s, and record when $k_y$ passes the lower limit.

12. • In [H-infinity loop shaping](/h-infinity-loop-shaping/), $\gamma_{\min} = \sqrt{1 + \rho(XZ)}$ where $X$ and $Z$ solve the control and filter Riccati equations of the normalized coprime factor problem. Compute $X$, $Z$, $\gamma_{\min}$ and the margin $\varepsilon_{\max} = 1/\gamma_{\min}$ for $P(s) = 1/(s - 1)$. Then show that $P(s) = k/s$ gives the same $\gamma_{\min}$ for every $k > 0$.

13. • The plant $y(k + 1) = 0.8\, y(k) + 2 u(k)$, $y(0) = 0$, repeats a task of $N$ steps. [Iterative learning control](/iterative-learning-control/) updates $u_{j+1}(k) = u_j(k) + \gamma e_j(k + 1)$. Find the values of $\gamma$ for which the error converges as $j \to \infty$ for every $N$. Then find the values for which $|1 - \gamma e^{j\theta} P(e^{j\theta})| < 1$ for all $\theta$, with $P(z) = 2/(z - 0.8)$, a sufficient condition for monotone decrease of $\|e_j\|_2$. What happens at $\gamma = 0.5$?

14. • The gradient estimator $\dot{\hat\theta} = \phi(t)\,(y - \phi^T \hat\theta)$ sees $y = \phi^T \theta^*$ with $\theta^* = (1, 1)$ and starts at $\hat\theta(0) = 0$. Compare $\phi(t) = (\sin t, \sin 2t)$ and $\phi(t) = (1, 2)\sin t$. Show that the second regressor keeps $\hat\theta$ on a line, find its limit, and simulate both with a fixed step to confirm.

15. • The output $y = x + b u$ has an unknown gain $b$ with estimate $\hat b = 2$ and variance $p = 1$. The [certainty equivalence](/certainty-equivalence/) law treats $b = \hat b$. Compare its expected cost $E[y^2]$ with the law that minimizes $E[y^2] = (x + \hat b u)^2 + p u^2$. Give both costs for general $\hat b$ and $p$.

16. • Write $1/(s + 1 + \delta)$ as an upper [linear fractional transformation](/linear-fractional-transformation/) of a $2 \times 2$ transfer matrix $M$ and the scalar $\delta$. Which radius $r$ does small gain give for complex $|\delta| < r$? Compare it with the exact set of real $\delta$, and with the exact set of complex $\delta$ for which the system is stable.

17. • Let $G = H = a/(s + a)$ with $a > 0$. Compute $\|G\|_2$, $\|GH\|_2$, $\|G\|_\infty$ and $\|GH\|_\infty$. Show that the H2 norm is not submultiplicative for $a < 1$, while the H-infinity norm is submultiplicative for every system.

18. • For [L1 adaptive control](/l1-adaptive-control/) with $H(s) = 1/(s + 1)$ and the filter $C(s) = \omega_c/(s + \omega_c)$, the condition is $\|G\|_{L_1} L < 1$ with $G = H(1 - C)$. Compute $\|G\|_{L_1}$ in closed form for $\omega_c = 3$, and decide the condition for $L = 2$ and $L = 3$.

19. • Compute the Hankel singular values of $G(s) = 1/(s + 1)^2$ from the controllability and observability Gramians of any minimal realization. The bounds $\sigma_1 \le \|G\|_\infty \le 2(\sigma_1 + \sigma_2)$ start the bisection. Give the starting interval and the exact norm.

20. ★ Let $A_1 = \begin{pmatrix} -1 & a \\ 0 & -1 \end{pmatrix}$ and $A_2 = A_1^T$. Find all $a$ for which the polytope $\mathrm{conv}\{A_1, A_2\}$ is [quadratically stable](/quadratic-stability/), and all $a$ for which every member is Hurwitz. Explain why a common Lyapunov matrix is needed for an [LPV system](/lpv-system/) that may switch fast between the two.

21. ★ Let $M = u v^T$ with $u = (1, 2, -1)$, $v = (3, -1, 2)$, and the structure of three complex scalars on the diagonal. Show that $\mu(M) = \sum_i |u_i v_i|$ for every rank-one $M$ and give its value here, with $\rho(M)$ and $\bar\sigma(M)$. Then find a diagonal $D$ for which $\bar\sigma(D M D^{-1})$ reaches $\mu$, so the upper bound of [mu analysis](/mu-analysis/) is exact for rank one.

22. ★ For the scalar plant $\dot x = a x + w_1 + u$ with errors $z = (x, u)$ and measurement $y = x + w_2$, where $a \ge 0$, use the conditions of [DGKF synthesis](/dgkf-h-infinity-synthesis/) to find $\gamma_{\mathrm{opt}}$ as a function of $a$. Check the formula by bisection on the Riccati conditions for $a = 0$ and $a = 2$, and explain why no $\gamma \le 1$ is achievable.

23. ★ Compute the [nu-gap metric](/nu-gap-metric/) between $P_1 = 1/(s + 1)$ and $P_2 = 2/(s + 1)$: find the chordal distance $\kappa(\omega)$, its maximum and the frequency of the maximum, and check the winding number condition. Which controllers are guaranteed to stabilize both plants?

24. ★ For the stable plant $P(s) = (2 - s)/(s + 1)$ and the weight $W(s) = (s + 3)/(s + 1)$, show that every stabilizing controller has $\|WS\|_\infty \ge 5/3$. Use the Youla parameter of a stable plant to find a controller that reaches the bound, and give its closed-loop pole. Relate the result to [mixed-sensitivity design](/mixed-sensitivity-design/).
