1. The Hessian of $f$ is $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$, with determinant $-1$, so it has a negative eigenvalue, $3 - \sqrt{10}$, and $f$ is not convex. The Hessian of $h$ is $\begin{pmatrix} 4 & 2 \\ 2 & 2 \end{pmatrix}$, with eigenvalues $3 \pm \sqrt5$. So $h$ is strongly convex with $\mu = 3 - \sqrt5 \approx 0.764$, and its condition number is $(3 + \sqrt5)/(3 - \sqrt5) = (7 + 3\sqrt5)/2 \approx 6.85$.

3. Both terms are finite everywhere, so the sum rule holds. At $0$, $\partial|x - 1| = \{-1\}$ and $\partial(2|x|) = [-2, 2]$, so $\partial f(0) = [-3, 1]$. At $1$, $\partial f(1) = [-1, 1] + 2 = [1, 3]$. Since $0 \in \partial f(0)$, the minimizer is $x^* = 0$, with $f(0) = 1$.

6. Stationarity gives $1 + 2\nu x_1 = 0$ and $1 + 2\nu x_2 = 0$, so $x_1 = x_2 = -1/(2\nu)$, and the constraint gives $\nu = \pm\tfrac12$. The minimum is $-2$ at $(-1, -1)$, with $\nu = \tfrac12$. The maximum is $2$ at $(1, 1)$, with $\nu = -\tfrac12$.

10. The derivative is $t - 1/(x - 1)$, so $x^*(t) = 1 + 1/t$ and the gap is $1/t$, which is $m/t$ for $m = 1$ constraint. A gap of $10^{-6}$ needs $t \ge 10^6$, so $t$ is multiplied by $10$ six times. The dual point $\lambda = 1/(t(x^*(t) - 1))$ is $1$ for every $t$, which is $\lambda^*$.

12. For $|y| \le 1$ the supremum of $xy - \tfrac12x^2 - |x|$ is at $x = 0$, because then $y \in \partial|x|$ at $0$, so $f^*(y) = 0$. For $y > 1$ the maximizer is $x = y - 1$, which gives $\tfrac12(y - 1)^2$. The gradient $\nabla f^*(y) = \operatorname{sign}(y)\max(|y| - 1, 0)$ is soft thresholding, and $f$ is $1$-strongly convex.

13. A tangent line at $a > 0$ is $y = 2ax - a^2$. It passes through $(2, 1)$ when $a^2 - 4a + 1 = 0$, so $a = 2 - \sqrt3 \approx 0.268$. The envelope is $x^2$ for $|x| \le 2 - \sqrt3$, and $(4 - 2\sqrt3)|x| - (7 - 4\sqrt3)$ for $2 - \sqrt3 \le |x| \le 2$.

14. The two disks meet only at $0$, so the feasible set is $\{0\}$ and $p^* = 0$. The Lagrangian is $(\lambda_1 + \lambda_2)x^2 + (1 - 2\lambda_1 + 2\lambda_2)x$. Its infimum is $0$ when the linear coefficient is $0$ and the quadratic one is positive, and negative or $-\infty$ otherwise. So the optimal multipliers are $(s + \tfrac12, s)$ for every $s \ge 0$. Slater is sufficient for strong duality, not necessary, and without it the multipliers need not be bounded.

16. With $L = \|x\|^2 + \nu(x_1 + x_2 + x_3 - 3) + \lambda(x_1 - \tfrac12)$, try the bound active. Then $x_2 = x_3 = \tfrac54$, $\nu = -\tfrac52$ and $\lambda = \tfrac32 \ge 0$, so $x^* = (\tfrac12, \tfrac54, \tfrac54)$ with value $\tfrac{27}{8}$. Raising the bound by $\delta$ lowers the value by about $\tfrac32\delta$.

19. There are three terms and two variables, so the degree of difficulty is $0$ and the dual weights are fixed by the exponents: $2\delta_1 - \delta_2 = 0$, $\delta_1 - \delta_3 = 0$, $\delta_1 + \delta_2 + \delta_3 = 1$. So $\delta = (\tfrac14, \tfrac12, \tfrac14)$, and the minimum is $4^{1/4}\,2^{1/2}\,16^{1/4} = 4$. At the optimum the terms are $\delta_i \cdot 4 = 1, 2, 1$, so $x = \tfrac12$ and $y = 4$.

22. The updates are $x = (4 + z - u)/2$, $z = \operatorname{sign}(x + u)\max(|x + u| - 1, 0)$ and $u \leftarrow u + x - z$. The iterates $(x, z, u)$ are $(2, 1, 1)$, $(2, 2, 1)$, $(\tfrac52, \tfrac52, 1)$, $(\tfrac{11}4, \tfrac{11}4, 1)$. From $k = 2$ on, $u_k = 1$ and $x_{k+1} = (3 + x_k)/2$, so $x_k = 3 - 2^{2-k}$. The limit is $x^* = 3$, and $y^* = \rho u = 1$ is the slope of $|z|$ at $3$.

23. On $[-2, 2]$ the minimum is $p^* = -8$ at $x = -2$. The Lagrangian $(\lambda - 1)x^2 + 2x - 4\lambda$ is bounded below only for $\lambda > 1$, where $g(\lambda) = -4\lambda - 1/(\lambda - 1)$. This is largest at $\lambda = \tfrac32$, with $g = -8$. At $x = 2$ with $\lambda = \tfrac12$, the Lagrangian is $-\tfrac12x^2 + 2x - 2$, which is unbounded below: KKT points of a nonconvex problem need not be minima of the Lagrangian.

24. The conjugate of $\|\cdot\|_1$ is the indicator of $\{\|v\|_\infty \le 1\}$, and $g^*(-y) = -b^\top y$. For the numbers, the primal optimum is $x^* = (0, 2)$ with value $2$, and the dual is $\max 4y$ subject to $|y| \le 1$ and $|2y| \le 1$, so $y^* = \tfrac12$ with value $2$. Then $A^\top y^* = (\tfrac12, 1)$, whose first entry is in $[-1, 1]$ and whose second is $\operatorname{sign}(x_2^*) = 1$.

25. With $s = (1 - y, 1 - 2y)$, the conditions are $x_1 = \mu/(1 - y)$, $x_2 = \mu/(1 - 2y)$ and $x_1 + 2x_2 = 2$. They give $4y^2 + (4\mu - 6)y + 2 - 3\mu = 0$, and the root with $s > 0$ is $y(\mu) = (3 - 2\mu - \sqrt{4\mu^2 + 1})/4$. At $\mu = 1$, $y = (1 - \sqrt5)/4$, $s = (\varphi^2/2, \varphi)$ and $x = (2/\varphi^2, 1/\varphi) \approx (0.764, 0.618)$, where $\varphi$ is the golden ratio. As $\mu \to 0$ the path tends to $x = (0, 1)$, $y = \tfrac12$, $s = (\tfrac12, 0)$.

26. (a) $f'' = a/x^2$ and $|f'''| = 2a/x^3$, so the condition $|f'''| \le 2(f'')^{3/2}$ holds exactly when $a \ge 1$. (b) A linear term changes neither $f''$ nor $f'''$, and a convex quadratic adds a constant $c \ge 0$ to $f''$ only. (c) Scaling a function by $1/t$ scales the gradient and the Hessian by the same factor, so the Newton step and the backtracking test do not change. The squared Newton decrement, used in the stopping test, does change, by the factor $1/t$, and the bound needs a self-concordant function, which is $tf_0 + \phi$.

27. The minimizer of the Lagrangian is $x = -y(1, 1)$, so $g(y) = -y^2 - 2y$, with maximum $1$ at $y^* = -1$. The proximal step gives $y_{k+1} = (y_k - 2\rho)/(1 + 2\rho)$, the same as the augmented Lagrangian update. Here $g$ is strongly concave, because $f$ is a strongly convex quadratic, and so the proximal point step contracts the distance to $y^*$ by $1/(1 + 2\rho)$.
