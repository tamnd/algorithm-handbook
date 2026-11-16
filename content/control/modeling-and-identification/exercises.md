1. ◦ Use the [Laplace transform](/laplace-transform/) to solve $\dot y + 2y = 1$ for $t \ge 0$ with $y(0^-) = 1$. Give $Y(s)$, its partial fractions, $y(t)$ and the limit of $y(t)$ as $t \to \infty$.

2. ◦ Let $G(s) = (s - 2)/((s + 1)(s + 3))$. Give its [poles and zeros](/poles-and-zeros/) and its static gain $G(0)$. Find the unit step response $y(t)$, its slope at $t = 0^+$ and its final value. In which direction does the response start, and in which direction does it end?

3. ◦ Find the equilibria of $\dot x = x - x^3$ and [linearize](/jacobian-linearization/) at each. Which are locally asymptotically stable? Then linearize $\dot x = -x^3$ and $\dot x = x^3$ at $0$. What does the linearization tell you there, and what is the true behaviour of each system?

4. ◦ Compute the [matrix exponential](/matrix-exponential/) $e^{At}$ for $A = \begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix}$. Give the solution of $\dot x = Ax$ from $x(0) = (0, 1)$, and the time and value of the maximum of its first component.

5. ◦ Let $A = \operatorname{diag}(0.5, 0.2)$, $B = (1, 1)^T$, $C = (1, 0)$ and $D = 0$. Compute the [Markov parameters](/markov-parameters/) $h_1, \ldots, h_4$ and the rank of the Hankel matrix $\begin{pmatrix} h_1 & h_2 \\ h_2 & h_3 \end{pmatrix}$. Which mode is missing from the impulse response, and why? Give a minimal realization.

6. ◦ Discretize $\dot x = -x + 2u$ by a [zero-order hold](/zero-order-hold-discretization/) with $h = \ln 2$. Give $A_d$ and $B_d$, and check that the discrete step response from $x_0 = 0$ equals the continuous step response at $t = kh$. What first step does forward Euler with the same $h$ give instead?

7. ◦ For the input $u(k) = (-1)^k$, compute $r_u(0)$ and $r_u(1)$ and the covariance matrix of two lags. Of what order is this input [persistently exciting](/persistent-excitation/)? If it drives $y(k) = b_1 u(k-1) + b_2 u(k-2)$, which combination of $b_1$ and $b_2$ can the data determine?

8. ◦ A step of height $2$ is applied at $t = 0$ to a process at rest. The output rises from $10$ to a final value of $16$. It reaches $28.3$ percent of its change at $t = 3$ and $63.2$ percent at $t = 5$. Fit a first-order plus dead time model by the two-point form of the [process reaction curve](/process-reaction-curve/) method: give $K$, $T$, $L$ and the transfer function.

9. • A [signal-flow graph](/signal-flow-graph/) has the source $u$, the nodes $x_1, \ldots, x_4$ and the output $y = x_4$. Its edges are $u \to x_1$ with gain $1$, $x_1 \to x_2$ with gain $a$, $x_2 \to x_1$ with gain $-p$, $x_2 \to x_3$ with gain $b$, $x_3 \to x_4$ with gain $c$, $x_4 \to x_3$ with gain $-r$, and $u \to x_3$ with gain $d$. List the loops, the forward paths and their cofactors, and find the gain from $u$ to $y$ by [Mason's gain formula](/masons-gain-formula/).

10. • Find the [state-transition matrix](/state-transition-matrix/) $\Phi(t, t_0)$ of the [linear time-varying system](/linear-time-varying-system/) $\dot x = A(t)x$ with $A(t) = \begin{pmatrix} -1 & t \\ 0 & -1 \end{pmatrix}$. Why may you use the exponential of the integral of $A$ here? Do all solutions tend to $0$?

11. • The loop gain is $L(s) = 2e^{-s\tau}/(s + 1)$ with unity negative feedback. Find the gain crossover frequency, the phase margin for $\tau = 0$, and the delay margin, the smallest $\tau$ at which the loop loses stability. See [time-delay systems](/time-delay-system/).

12. • Sample $G(s) = 1/(s(s+1))$, with $A = \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix}$, $B = (0, 1)^T$ and $C = (1, 0)$, by a zero-order hold with $h = \ln 2$. Give $A_d$, $B_d$ and the pulse transfer function $H(z)$. Where are its poles and its zero? Check the first two samples of the step response against the continuous step response $t - 1 + e^{-t}$.

13. • Find the [Smith-McMillan form](/smith-mcmillan-form/) of $G(s) = \begin{pmatrix} 1/(s+1) & 1/(s+1) \\ 1/(s+1) & 1/(s+2) \end{pmatrix}$. What is its McMillan degree, and does it have transmission zeros? Every entry has degree 1; how many states does a minimal realization need?

14. • Let $G(s) = \begin{pmatrix} 1/(s+1) & 1/(s+2) \\ 2/(s+1) & 1/(s+1) \end{pmatrix}$. Find its pole polynomial and its [transmission zeros](/transmission-zero/), and give an input direction $u_0$ that the zero blocks. What does the zero mean for the steady-state outputs under constant inputs?

15. • The Markov parameters of an unknown single-input single-output system are $h_1 = 1$, $h_2 = 1$, $h_3 = 2$ and $h_4 = 3$. Run the [Ho-Kalman algorithm](/ho-kalman-algorithm/) with $2 \times 2$ Hankel matrices. Give the order, a realization, its poles and the predicted $h_5$, $h_6$ and $h_7$.

16. • Fit $y(k) + a\, y(k-1) = b\, u(k-1) + e(k)$ by [least squares](/least-squares-arx-identification/) to the data $u = (1, 1, -1, -1, 1)$ and $y = (0, 1, 1.5, -0.25, -1)$. Give the normal matrix $R$, the vector $f$, the exact estimate and the residual sum of squares.

17. • The system $G(q) = q^{-1}/(1 - 0.5q^{-1})$ is driven by the periodic input $u = 1, -1, 1, -1, \ldots$ and has reached periodic steady state. Find the output over one period. Compute the [empirical transfer function estimate](/empirical-transfer-function-estimate/) from one period ($N = 2$) and compare it with $G(e^{i\omega})$ at $\omega = \pi$. Why is there no estimate at $\omega = 0$?

18. • Run [SINDy](/sindy/) with the library $\{1, x\}$ and threshold $\lambda = 0.2$ on the data $x = (0, 1, 2, 3)$ and $\dot x = (0.1, -1, -2.1, -2.9)$. Give the first least squares fit, the term that is removed, and the final model in exact form.

19. • In [kernel-based identification](/kernel-based-identification/) the estimate is $\hat g = (R + \sigma^2 K^{-1})^{-1} r$ with $R = \Phi^T\Phi$ and $r = \Phi^T y$. Assume $R = NI$ and the diagonal kernel $K = \operatorname{diag}(c\lambda, c\lambda^2, \ldots, c\lambda^d)$, which is the DC kernel with $\rho = 0$. Express $\hat g_k$ through the least squares estimate $r_k / N$. For $N = 100$, $\sigma^2 = 1$, $c = 1$ and $\lambda = 0.5$, give the shrinkage factors at $k = 1$, $5$ and $10$.

20. ★ The data come from $y(k) - 0.5\, y(k-1) = u(k-1) + e(k) + 0.5\, e(k-1)$ in open loop, with $u$ a white $\pm 1$ sequence and $e$ white with unit variance, independent of $u$. Find the limit as $N \to \infty$ of the [least-squares ARX](/least-squares-arx-identification/) estimate of $(a, b)$ in $y(k) + a\, y(k-1) = b\, u(k-1)$. Then find the limit of the [instrumental variable](/instrumental-variable-identification/) estimate with the instruments $\zeta(k) = (u(k-1), u(k-2))$.

21. ★ The plant $y(k) + a\, y(k-1) = b\, u(k-1) + e(k)$, with $a = -0.8$, $b = 1$ and white $e$, runs under the feedback $u(k) = -c_1 y(k) - c_2 y(k-1)$ with no external signal. For which $c_2$ do the data determine $(a, b)$ in the ARX model of the same orders? For $c_1 = 0.5$ and $c_2 = 0.2$, give the closed-loop AR model of $y$ and recover $a$ and $b$ from it. See [closed-loop identification](/closed-loop-identification/).

22. ★ A scalar signal is $x_k = 2(0.8)^k + (0.5)^k$, so $x_0, \ldots, x_3 = 3, 2.1, 1.53, 1.149$. Apply [dynamic mode decomposition](/dynamic-mode-decomposition/) to the scalar snapshots $x_0, \ldots, x_3$ and give its eigenvalue. Then stack delayed snapshots $z_k = (x_k, x_{k+1})$, $k = 0, 1, 2$, fit the $2 \times 2$ map with $z_{k+1} = A z_k$ from the two pairs, and give its eigenvalues.

23. ★ A [Hammerstein model](/hammerstein-wiener-model/) has $f(u) = u + \beta u^2$ and $G(q) = 0.5q^{-1}/(1 - 0.5q^{-1})$, and it starts at rest. Show that under any input with values in $\{-1, 1\}$ its output equals the output of the linear system $G$ plus $\beta$ times the unit step response of $G$. What can such data reveal about $\beta$, and how many input levels are needed to see the curvature of $f$?
