1. ◦ Which of $f(x) = x_1^2 + 3x_1x_2 + 2x_2^2$ and $h(x) = 2x_1^2 + 2x_1x_2 + x_2^2$ is a [convex function](/convex-function/) on $\mathbb{R}^2$? For the convex one, find the largest $\mu$ for which it is [$\mu$-strongly convex](/strong-convexity/), and its condition number.

2. ◦ Which of these functions on $\mathbb{R}$ are [quasiconvex](/quasiconvex-function/): $x^3$, $-x^2$, $e^{-x^2}$, $\log(1 + |x|)$? Which are convex? For each one that is not quasiconvex, give a sublevel set that is not an interval.

3. ◦ Let $f(x) = |x - 1| + 2|x|$. Find the [subdifferential](/subdifferential/) $\partial f(0)$ and $\partial f(1)$, and use them to find the minimizer of $f$ and the minimum value.

4. ◦ Compute the [convex conjugates](/convex-conjugate/) of $f(x) = 2x^2$ and of $h(x) = 3x - 1$ on $\mathbb{R}$. Check that $f^{**} = f$.

5. ◦ Find a hyperplane that strictly separates the unit disk $\{x : \|x\| \le 1\}$ from the point $p = (3, 4)$, following the proof of the [separating hyperplane theorem](/separating-hyperplane-theorem/): take the nearest point of the disk to $p$, and the hyperplane through the midpoint of the segment between them. Which hyperplanes $3x_1 + 4x_2 = c$ separate strictly?

6. ◦ Use a [Lagrange multiplier](/lagrange-multiplier/) to find the minimum and the maximum of $x_1 + x_2$ on the circle $x_1^2 + x_2^2 = 2$. With $L = x_1 + x_2 + \nu(x_1^2 + x_2^2 - 2)$, give the value of $\nu$ at each point.

7. ◦ Minimize $x_1^2 + x_2^2$ subject to $x_1 + x_2 \ge 4$. Write the [Lagrangian](/lagrangian-function/) with the constraint as $4 - x_1 - x_2 \le 0$, compute the dual function $g(\lambda)$, and find $\lambda^*$ and $d^*$. Is there a duality gap?

8. ◦ The point $a = (3, 3)$ is projected onto the half-plane $x_1 + x_2 \le 2$, that is, $(x_1 - 3)^2 + (x_2 - 3)^2$ is minimized over it. Show that $(1, 1)$ satisfies the [KKT conditions](/kkt-conditions/), and find its multiplier. Show that the feasible point $(0, 2)$, where the constraint is also active, does not.

9. ◦ The largest eigenvalue of a symmetric matrix $C$ is the optimal value of the [semidefinite program](/semidefinite-programming/) $\min t$ subject to $tI - C \succeq 0$. Solve it for $C = \begin{pmatrix} 0 & 2 \\ 2 & 3 \end{pmatrix}$. Then find a matrix $X \succeq 0$ with $\operatorname{tr} X = 1$ and $\operatorname{tr}(CX)$ equal to the optimal value.

10. ◦ Apply the [barrier method](/barrier-method/) to $\min x$ subject to $x \ge 1$, with the barrier $-\log(x - 1)$. Find the minimizer $x^*(t)$ of $tx - \log(x - 1)$, and its gap $x^*(t) - 1$. How large must $t$ be for a gap of at most $10^{-6}$? Starting from $t_0 = 1$, how many times is $t$ multiplied by $\mu = 10$ before that?

11. • Let $f(x) = \max(x_1 + x_2,\; x_1 - x_2,\; -x_1)$ on $\mathbb{R}^2$. Show that $0 \in \partial f(0, 0)$, by writing $0$ as a convex combination of the three slopes, and conclude that $(0, 0)$ minimizes $f$. Is the minimizer unique? Find $\partial f(1, 0)$.

12. • Show that the conjugate of $f(x) = \tfrac12 x^2 + |x|$ is $f^*(y) = \tfrac12\max(|y| - 1, 0)^2$. Find $\nabla f^*$, and check that it is $1$-Lipschitz, as the strong convexity of $f$ predicts.

13. • Find the [convex envelope](/convex-envelope/) of $f(x) = \min(x^2, 1)$ on $[-2, 2]$. The envelope agrees with $x^2$ near $0$, and on each side it is linear from a point of tangency to the end point $(\pm 2, 1)$.

14. • Minimize $x$ subject to $(x - 1)^2 \le 1$ and $(x + 1)^2 \le 1$. Show that the [Slater condition](/slater-condition/) fails. Then find every $\lambda \ge 0$ with $g(\lambda) = p^*$, and show that this set is unbounded.

15. • Minimize $x_1 + x_2$ subject to $x_1^2 + x_2^2 \le 2$. (a) Compute the dual function and find $\lambda^*$. (b) For the [penalty](/penalty-method/) function $x_1 + x_2 + \rho\max(0, x_1^2 + x_2^2 - 2)$, show that the minimizer is the solution $(-1, -1)$ when $\rho \ge \tfrac12$, and find the minimizer and the minimum when $\rho = \tfrac14$.

16. • Solve the [quadratic program](/quadratic-programming/) $\min x_1^2 + x_2^2 + x_3^2$ subject to $x_1 + x_2 + x_3 = 3$ and $x_1 \le \tfrac12$ with the KKT conditions. Give both multipliers, and use the multiplier of the bound to predict how fast the optimal value falls when the bound $\tfrac12$ is raised.

17. • Three assets have mean returns $\mu = (1, 2, 3)$ and covariance $\Sigma = I$. In the Markowitz model of [portfolio optimization](/portfolio-optimization/), with weights that sum to $1$, find the minimum-variance portfolio, and the variance of the best portfolio with return $\rho$ as a function of $\rho$. Find the portfolios for $\rho = \tfrac52$ and $\rho = 3$. Which of them changes when short sales are forbidden, and what is its variance then?

18. • Show that for real $x, y, z$, the conditions $x \ge 0$, $y \ge 0$, $xy \ge z^2$ hold exactly when $\|(2z, x - y)\|_2 \le x + y$. Use this to write $\min 1/x_1 + 1/x_2$ subject to $x_1 + 2x_2 \le 3$, $x > 0$ as a [second-order cone program](/second-order-cone-programming/), and solve it.

19. • Solve the [geometric program](/geometric-programming/) $\min x^2y + 1/x + 4/y$ over $x, y > 0$. Find the weights of the three terms at the optimum, the minimum value and the minimizer.

20. • Run the [cutting-plane method](/cutting-plane-method/) on $f(x) = \max(-x, 2x - 3)$ over $[-2, 4]$, starting at $x_0 = 4$. List the query points, the cuts and the lower bounds until the gap is $0$. Compare the number of oracle calls with the bound for a function with $P$ affine pieces.

21. • Apply the [augmented Lagrangian method](/augmented-lagrangian-method/) with $\rho = 1$ and $y_0 = 0$ to $\min \tfrac12(x_1^2 + x_2^2)$ subject to $x_1 + x_2 = 2$. Find $x_k$ and $y_k$ in closed form. For a general $\rho > 0$, by what factor does $|y_k - y^*|$ shrink at each step?

22. • Apply [ADMM](/admm/) to $\min \tfrac12(x - 4)^2 + |z|$ subject to $x - z = 0$, with $\rho = 1$, $z_0 = u_0 = 0$ and the scaled updates $x \leftarrow \arg\min_x \tfrac12(x - 4)^2 + \tfrac12(x - z + u)^2$, $z \leftarrow \arg\min_z |z| + \tfrac12(x - z + u)^2$, $u \leftarrow u + x - z$. Compute four iterations, find $x_k$ in closed form, and identify the limit of $u_k$.

23. ★ Minimize $-x^2 + 2x$ subject to $x^2 \le 4$, a problem that is not convex. Find $p^*$, compute the dual function, and show that $d^* = p^*$. Show that $x = 2$ is a KKT point with $\lambda = \tfrac12$, and explain why this multiplier gives no lower bound.

24. ★ Use [Fenchel duality](/fenchel-duality/) with $f = \|\cdot\|_1$ and $g$ the indicator of $\{b\}$ to show that the dual of $\min \|x\|_1$ subject to $Ax = b$ is $\max b^\top y$ subject to $\|A^\top y\|_\infty \le 1$. Solve both problems for $A = (1 \;\; 2)$ and $b = 4$, and check the optimality conditions $A^\top y^* \in \partial\|x^*\|_1$.

25. ★ For the linear program $\min x_1 + x_2$ subject to $x_1 + 2x_2 = 2$, $x \ge 0$, find the [central path](/central-path/) $(x(\mu), y(\mu), s(\mu))$ in closed form from $x_is_i = \mu$. Evaluate it at $\mu = 1$, check that the duality gap is $2\mu$, and find the limit as $\mu \to 0$.

26. ★ (a) For which $a > 0$ is $-a\log x$ a [self-concordant function](/self-concordant-function/) on $x > 0$? (b) Show that adding a linear or convex quadratic function keeps self-concordance. (c) The barrier method minimizes $tf_0 + \phi$, not $f_0 + \phi/t$. Show that Newton's method with backtracking takes the same steps on both, and say to which of the two the self-concordant complexity bound applies.

27. ★ For the problem of Exercise 21, compute the dual function $g(y)$. Show that the multiplier update of the augmented Lagrangian method is exactly a [proximal point](/proximal-point-method/) step on $-g$ with parameter $\rho$, that is, $y_{k+1} = \arg\max_y \big(g(y) - (y - y_k)^2/(2\rho)\big)$. Why is the rate linear here, when the general bound is only $O(1/k)$?
