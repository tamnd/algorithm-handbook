2. The roots are $p = 3 \pm 5$, so the stabilizing root is $p = 8$. The gain is $K = 8$, the closed-loop pole is $3 - 8 = -5$, and the cost is $8x_0^2$. The Hamiltonian matrix has the characteristic polynomial $s^2 - 25$, so its eigenvalues are $\pm 5$. For $-5$ the first row gives $8v_1 - v_2 = 0$, so the eigenvector is $(1, 8)$ and $p = v_2/v_1 = 8$.

3. With no terminal cost the gain uses $P_{N-1}$ of the Riccati recursion from $P_0 = 0$: $P_1 = 1$, $P_2 = 3/2$. So $K_1 = 0$, $K_2 = 1/2$, $K_3 = 3/5$, and the closed-loop factors are $1$, $1/2$ and $2/5$. The horizon $N = 1$ gives $u = 0$ and $x_{k+1} = x_k$, which is stable but not asymptotically stable.

4. A box $|x_i| \le c_i$ is invariant when, for each row, the sum of $|a_{ij}| c_j$ is at most $c_i$. For the first matrix the row sums are $0.9$ and $0.9$, so the unit box is invariant. For the second the first row sum is $1.1$, and $(1, 1)$ maps to $(1.1, 0.1)$. The scaled box needs $0.6c + 0.5 \le c$ and $0.2c + 0.3 \le 1$, so $1.25 \le c \le 3.5$.

6. The cost of $u = -Kx$ is $p = (1 + K^2)/(2(K - 1))$. So $P_0 = 5/2$, $K_1 = 5/2$, $P_1 = 29/12$, $K_2 = 29/12$ and $P_2 = 985/408$. The errors are about $0.0858$, $0.00245$ and $2.1 \times 10^{-6}$: each is close to a constant times the square of the one before.

8. With $M = 1$ the move is $\Delta u = \sum s_i / \sum s_i^2$ over the horizon: $1.3/0.89 \approx 1.461$ for $P = 2$ and $2.25/1.7925 \approx 1.255$ for $P = 3$. With $M = P = 2$ the matrix $\begin{bmatrix} 0.5 & 0 \\ 0.8 & 0.5 \end{bmatrix}$ is square, the fit is exact, and $\Delta u = (2, -1.2)$.

10. From $x_N = 2^N x + \sum_{i=0}^{N-1} 2^{N-1-i} u_i = 0$ with $|u_i| \le 1$, the reachable sum is at most $2^N - 1$ in absolute value. So $\mathcal{X}_N = [-(1 - 2^{-N}), 1 - 2^{-N}]$: $[-1/2, 1/2]$, $[-3/4, 3/4]$, $[-7/8, 7/8]$. The limit is the open interval $(-1, 1)$.

12. The cost is $x^2 + u_0^2 + (x + u_0)^2 + u_1^2 + (x + u_0 + u_1)^2$, so $H = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$, $F = (2, 1)$ and $c = 3$. The minimizer is $U = -(3/5, 1/5)x$ with value $\frac85 x^2$, and the recursion gives $P_2 = 8/5$. At $x = 2$ the unconstrained $u_0 = -6/5$ breaks the bound; fixing $u_0 = -1$ and minimizing over $u_1$ gives $u_1 = -1/2$ and the cost $13/2$. The derivative of the cost in $u_0$ there is $1$, which is the multiplier of $u_0 \ge -1$.

13. $V_1(x) = x^2$. Then $V_2 = (6, 2, 0, 2, 6)$ and $V_3 = (7, 2, 0, 2, 7)$ on $x = -2, \dots, 2$. From $x = 2$ the move $u = -1$ costs $4 + 1 + V_2(1) = 7$ and $u = 0$ costs $4 + V_2(2) = 10$. The Riccati value is $P_3 x^2 = \frac85 \cdot 4 = 6.4$, lower because it may use any real input.

14. The start lies above the switching curve $x_1 = -x_2|x_2|/2$, so $u = -1$ first. Along $u = -1$, $x_1 + x_2^2/2 = 2$; it meets the branch $x_1 = x_2^2/2$ of the curve at $(1, -\sqrt 2)$, at time $2 + \sqrt 2$. Then $u = +1$ for $\sqrt 2$ more. The total $2 + 2\sqrt 2 \approx 4.828$ agrees with $T^*$.

17. The unconstrained input is $u = -\varphi x/(1 + \varphi) = -x/\varphi$, which meets the bound at $|x| = \varphi$. There are three regions: $|x| \le \varphi$ with $u = -x/\varphi$ and $V = \varphi x^2$, and $x \ge \varphi$ (or $x \le -\varphi$) with $u = -1$ (or $+1$) and $V = x^2 + 1 + \varphi(|x| - 1)^2$. At $x = \varphi$ both pieces have value $2\varphi + 1$ and slope $2\varphi^2$.

22. Both Riccati equations are $1 - p^2 = 0$, so $K = L = 1$. The controller is $\dot{\hat x} = -2\hat x + y$, $u = -\hat x$, so $C(s) = 1/(s + 2)$, the loop gain is $1/(s(s + 2))$, and the closed loop is $(s + 1)^2$. Since $s^2 + 2s + k$ is Hurwitz for every $k > 0$, the gain margin is infinite. Crossover is at $\omega^2 = \sqrt 5 - 2$, $\omega \approx 0.486$, and the phase margin is about $76.3$ degrees. This loop has good margins, but LQG gives no guarantee of them.

24. With $s = \sqrt{x_1 + x_2^2/2}$, $\partial_{x_1} T = 1/s$ and $\partial_{x_2} T = 1 + x_2/s$. The equation reduces to $1 + x_2/s = |1 + x_2/s|$, which holds when $s \ge -x_2$. That is clear for $x_2 \ge 0$; for $x_2 < 0$, being above the curve means $x_1 > x_2^2/2$, so $s^2 > x_2^2$. The minimizing input is $-\mathrm{sign}(\partial_{x_2} T) = -1$.

25. Inside $|x| \le \varphi$ the LQR plan $u_0 = -x/\varphi$, $u_1 = -x/\varphi^3$ is feasible. For $\varphi \le x \le \varphi^2$ the plan is $u_0 = -1$ and $u_1 = -(x - 1)/\varphi$, and for $x \ge \varphi^2$ both inputs are $-1$; the negative side is symmetric. So there are five regions, with breakpoints $\pm\varphi$ and $\pm\varphi^2 = \pm(1 + \varphi)$. In every region $|u_1|$ is at most $|u_0|$, so $u_1$ cannot saturate alone.

26. Without constraints the MPC law is $u = -K_N x$ with the gain computed from $P_{N-1}$ of the Riccati recursion from 0. That recursion converges to the stabilizing solution, so $K_N$ tends to the LQR gain $K$ and $A - BK_N$ tends to $A - BK$, which is Schur. The eigenvalues depend continuously on the matrix, so $A - BK_N$ is Schur for all large $N$.

27. A gain $k$ is the LQR law when $p = k$ solves $2p - p^2 + q = 0$ and $1 - k < 0$. So $q = k^2 - 2k$, and $q \ge 0$ with $k > 1$ gives $k \ge 2$. So every LQR gain of this plant is at least $2$, while the loop is stable exactly for $k > 1$. Any LQR gain can be multiplied by a factor above $1/2$ and stay stable, and for $q = 0$ no smaller factor works: this is the lower gain margin.

28. $g'(p) = a^2 r^2/(r + b^2 p)^2 > 0$ and $g''(p) < 0$, and $g(p) < q + a^2 r/b^2$. Since $p_1 = q > p_0$ and $g$ is increasing, induction gives $p_{k+1} \ge p_k$. A bounded increasing sequence converges, and its limit is a fixed point. A concave $g$ with $g(0) = q > 0$ crosses the diagonal once on $p > 0$, so the fixed point is unique there.
