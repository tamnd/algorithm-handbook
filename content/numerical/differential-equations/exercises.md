1. ◦ Take one step of length $h = 0.1$ from $y(0) = 1$ on $y' = y$ with [Euler's method](/euler-method/) and with [Heun's method](/heuns-method/). Compare both results with $e^{0.1}$ and say how the two errors fit the orders 1 and 2.

2. ◦ Find a [Lipschitz constant](/lipschitz-condition/) in $y$ for $f(t, y) = t\sin y$ on $0 \le t \le 2$, and for $f(t, y) = y^2$ on $|y| \le 3$. Explain why $f(t, y) = \sqrt{|y|}$ has no Lipschitz constant on any interval around $y = 0$, and give two solutions of $y' = \sqrt{|y|}$, $y(0) = 0$.

3. ◦ [Classify](/pde-classification/) $u_{xx} + 4u_{xy} + 3u_{yy} = 0$, $u_{xx} + 2u_{xy} + u_{yy} = 0$, and $u_{xx} + u_{yy} = 0$ as elliptic, parabolic or hyperbolic.

4. ◦ Euler's method is applied to $y' = -20y$. What is the largest stable step? With $h = 0.15$, by what factor does the numerical solution change at each step?

5. ◦ Write the [Butcher tableau](/butcher-tableau/) of Heun's method and check the conditions $\sum_i b_i = 1$ and $\sum_i b_ic_i = \tfrac12$ for order 2.

6. ◦ A method run with steps $h$, $h/2$ and $h/4$ gives errors $3.2 \times 10^{-3}$, $2.0 \times 10^{-4}$ and $1.25 \times 10^{-5}$ at the final time. Estimate its [order of accuracy](/order-of-accuracy/).

7. ◦ Find the largest stable time step of the [FTCS scheme](/ftcs-method/) for $u_t = u_{xx}$ with $\Delta x = 0.02$, and the largest step allowed by the [CFL condition](/courant-friedrichs-lewy-condition/) for the [upwind scheme](/upwind-scheme/) on $u_t + 2u_x = 0$ with $\Delta x = 0.01$.

8. ◦ By the first Dahlquist barrier, what is the highest order of a zero-stable 3-step method, of an explicit zero-stable 3-step method, and of a zero-stable 4-step method?

9. • Apply [backward Euler](/backward-euler-method/) and the trapezoidal rule with $h = 0.1$ to $y' = -50y$, $y(0) = 1$. Find the factor per step and the value at $t = 1$ for each method, and compare with $e^{-50}$. Which property of the stability function explains the difference?

10. • The $\theta$-method is $y_{n+1} = y_n + h\big((1 - \theta)f(t_n, y_n) + \theta f(t_{n+1}, y_{n+1})\big)$. Find its stability function, and the values of $\theta$ for which it is [A-stable](/a-stability/) and for which it is [L-stable](/l-stability/).

11. • Show that the leapfrog method $y_{n+2} - y_n = 2hf_{n+1}$ is [consistent](/consistency/) and [zero-stable](/zero-stability/), and find its order.

12. • Run Euler's method on $y' = y$, $y(0) = 1$ to $t = 1$ with $h = 0.1$ and $h = 0.05$. Combine the two results by [Richardson extrapolation](/richardson-extrapolation/) and compare all three numbers with $e$.

13. • Solve $y'' = y$, $y(0) = 0$, $y(1) = 1$ by the [shooting method](/shooting-method/): write the solution of the initial value problem with $y'(0) = s$, find $s$, and give $y(0.5)$. Why does one secant step give the exact $s$ here?

14. • Find the amplification factor of the [Lax-Friedrichs scheme](/lax-friedrichs-scheme/) for $u_t + au_x = 0$ and show by [von Neumann analysis](/von-neumann-stability-analysis/) that it is stable exactly when $|\nu| \le 1$, where $\nu = a\Delta t/\Delta x$.

15. • The [Crank-Nicolson](/crank-nicolson-method/) scheme for $u_t = u_{xx}$ has amplification factor $g = (1 - 2rs)/(1 + 2rs)$ with $r = \Delta t/\Delta x^2$ and $s = \sin^2(\theta/2)$. Show that $|g| \le 1$ for all $r$, and compute $g$ for the highest mode $\theta = \pi$ at $r = 10$. What does the result look like on the grid over several steps?

16. • Take one step of velocity [Verlet](/verlet-integration/) with $h = 0.1$ for $q'' = -q$ from $q = 1$, $v = 0$, and compare $q$ and $v$ with $\cos 0.1$ and $-\sin 0.1$.

17. • For $dX = X\,dW$, $X(0) = 1$, the exact solution after a time $h$ is $\exp(\Delta W - h/2)$. With $h = 0.01$ and a Brownian increment $\Delta W = 0.2$, take one step of the [Euler-Maruyama](/euler-maruyama-method/) and the [Milstein](/milstein-method/) methods and compare both with the exact value.

18. • For [Burgers' equation](/burgers-equation/) $u_t + (u^2/2)_x = 0$, find the solution of the [Riemann problem](/riemann-problem/) with $u_L = 2$, $u_R = 0$ and with $u_L = -1$, $u_R = 1$, and the [Godunov](/godunov-method/) flux at the cell face in each case.

19. ★ Show that the stability function of an explicit Runge-Kutta method is a polynomial, and deduce that no explicit method is A-stable. For the 3-stage methods of order 3, $R(z) = 1 + z + z^2/2 + z^3/6$; find the left end of the real stability interval.

20. ★ Let $f$ have Lipschitz constant $L$ and let the solution satisfy $|y''| \le M$. Show that Euler's method has [global error](/global-error/) $|e_n| \le \frac{Mh}{2L}\big(e^{L(t_n - t_0)} - 1\big)$, using a discrete form of [Gronwall's inequality](/gronwall-inequality/). Evaluate the bound for $y' = y$ on $[0, 1]$ with $h = 0.1$ and compare it with the actual error.

21. ★ Show by Taylor expansion that the upwind scheme for $u_t + au_x = 0$ with $a > 0$ solves, to second order, the equation $u_t + au_x = \frac{a\Delta x}{2}(1 - \nu)u_{xx}$. Give the numerical diffusion coefficient for $a = 1$, $\Delta x = 0.01$ and $\nu = 0.5$, and the values of $\nu$ at which it vanishes.

22. ★ In the [parareal algorithm](/parareal-algorithm/) with coarse propagator $G$ and fine propagator $F$, the iteration is $U_{n+1}^{k+1} = G(U_n^{k+1}) + F(U_n^k) - G(U_n^k)$ with $U_0^k = y_0$. Prove that $U_n^k = F^n(y_0)$ for every $n \le k$, so that $N$ iterations on $N$ slices reproduce the fine solution exactly.

23. ★ The 2-stage [Gauss method](/gauss-legendre-runge-kutta/) has $R(z) = (1 + z/2 + z^2/12)/(1 - z/2 + z^2/12)$. Show that $|R(iy)| = 1$ for real $y$ and that both poles lie in the right half-plane, and conclude that the method is A-stable but not L-stable.
