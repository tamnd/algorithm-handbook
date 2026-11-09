1. Euler gives $1.1$ and Heun gives $1.105$, against $e^{0.1} = 1.1051709$. The errors are $5.2 \times 10^{-3}$ and $1.7 \times 10^{-4}$, close to $h^2/2$ and $h^3/6$, the local errors of methods of order 1 and 2.

4. The step must satisfy $|1 - 20h| \le 1$, so $h \le 0.1$. With $h = 0.15$ the factor is $1 - 3 = -2$: the solution doubles in size and changes sign at each step.

6. Each halving divides the error by $16$, so $p = \log_2 16 = 4$.

7. FTCS needs $\Delta t \le \Delta x^2/2 = 2 \times 10^{-4}$. Upwind needs $2\Delta t/0.01 \le 1$, that is $\Delta t \le 0.005$.

9. Backward Euler multiplies by $1/(1 + 5) = 1/6$ per step and gives $1.65 \times 10^{-8}$ at $t = 1$. The trapezoidal rule multiplies by $(1 - 2.5)/(1 + 2.5) = -3/7$ and gives $2.1 \times 10^{-4}$. Look at $R(z)$ as $z \to -\infty$.

11. Here $\rho(\zeta) = \zeta^2 - 1$ and $\sigma(\zeta) = 2\zeta$. Check $\sum j^q\alpha_j = q\sum j^{q-1}\beta_j$ for $q = 0, 1, 2, 3$; the first failure gives the order.

13. The solution is $y = s\sinh t$, so $s = 1/\sinh 1 = 0.8509$ and $y(0.5) = \sinh 0.5/\sinh 1 = 0.4434$. The far value $y(1; s)$ is linear in $s$.

19. Each stage is a polynomial in $z$ of degree at most its index, so $R$ is a polynomial and $|R(z)| \to \infty$ along the negative real axis. Solve $R(z) = -1$ numerically: $z \approx -2.5127$.

20. Write $e_{n+1} = e_n + h\big(f(t_n, y(t_n)) - f(t_n, y_n)\big) + \delta_{n+1}$, so $|e_{n+1}| \le (1 + hL)|e_n| + Mh^2/2$, and sum the geometric series with $1 + hL \le e^{hL}$. For $y' = y$, $M = e$ and $L = 1$, the bound is $0.234$; the actual error is $e - 1.1^{10} = 0.125$.

21. Expand $u(x - \Delta x, t)$ and $u(x, t + \Delta t)$, and use $u_{tt} = a^2u_{xx}$, which holds to the order needed. The coefficient is $0.0025$, and it vanishes at $\nu = 0$ and $\nu = 1$.

22. Use induction on $k$. If $U_n^k = F^n(y_0)$ for $n \le k$, then for $n \le k$ the two $G$ terms in the update of $U_{n+1}^{k+1}$ have the same argument and cancel.

23. On the imaginary axis the numerator and denominator are complex conjugates. The poles solve $z^2 - 6z + 12 = 0$, so $z = 3 \pm i\sqrt3$. As $z \to \infty$, $R(z) \to 1$.
