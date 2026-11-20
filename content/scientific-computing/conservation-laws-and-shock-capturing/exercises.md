1. ◦ Burgers' equation $u_t + (u^2/2)_x = 0$ starts from $u_0(x) = 1/(1 + x^2)$. At what time does the first shock form, from which starting point $x_0$ does the steepest characteristic leave, and where does the shock appear?

2. ◦ Burgers' equation starts from $u = 2$ for $x < 0$, $u = 1$ for $0 < x < 1$ and $u = 0$ for $x > 1$. Use the [Rankine-Hugoniot conditions](/rankine-hugoniot-conditions/) to find the speeds of the two shocks, the time and place where they meet, and the speed of the single shock after that.

3. ◦ Traffic on a road obeys $\rho_t + f(\rho)_x = 0$ with the flux $f(\rho) = \rho(1 - \rho)$, where $\rho$ is the density as a fraction of the jam density. Cars at density $0.2$ run into cars at density $0.8$. Find the speed of the jump between them and check the [Lax entropy condition](/lax-entropy-condition/). Note that this flux is concave, not convex: which sign of $\rho_R - \rho_L$ is admissible?

4. ◦ A normal shock in air ($\gamma = 1.4$) moves into gas at rest with Mach number 3 relative to that gas. From the jump conditions of the [Euler equations](/euler-equations-of-gas-dynamics/), the density ratio is $(\gamma + 1)M^2/((\gamma - 1)M^2 + 2)$ and the pressure ratio is $1 + 2\gamma(M^2 - 1)/(\gamma + 1)$. Compute both, the Mach number of the gas behind the shock relative to the shock, $M_2^2 = (1 + \frac{\gamma-1}{2}M^2)/(\gamma M^2 - \frac{\gamma-1}{2})$, and the limit of the density ratio as $M \to \infty$.

5. ◦ Water 0.5 m deep flows at 5 m/s into a stationary hydraulic jump ($g = 9.81$ m/s²). With the [shallow water equations](/shallow-water-equations/), find the Froude number upstream, the depth and speed downstream, the Froude number downstream, and the head lost in the jump, $(h_2 - h_1)^3/(4h_1h_2)$.

6. ◦ Cell averages are $(1, 1, 2, 4, 4)$ on a unit grid. For the middle cell, compute the slope and the two face values of the [MUSCL scheme](/muscl-scheme/) with the minmod, van Leer and MC limiters. Which gives the steepest reconstruction? What do all three give in the fourth cell?

7. ◦ A one-dimensional Euler code has a state with $\rho = 1$, $p = 1$, $u = 0.5$ and $\gamma = 1.4$ as its fastest cell. With $\Delta x = 0.01$ and Courant number 0.9, what is the time step?

8. ◦ The [Yee scheme](/yee-fdtd-scheme/) runs in three dimensions on a cubic grid with $\Delta x = 1$ mm in vacuum. What is the largest stable time step? How many steps does it take a wave to cross a box of 30 cm?

9. ◦ A [perfectly matched layer](/perfectly-matched-layer/) is 10 cells deep, with the profile $\sigma = \sigma_{\max}(d/D)^3$ and the design reflection $R = 10^{-8}$ at normal incidence ($c = 1$, lengths in cells). Find $\sigma_{\max}$ from $\sigma_{\max} = -(m+1)c\ln R/(2D)$, and the reflection of the continuous layer at incidence angles of $45°$ and $60°$.

10. • The [Lax-Friedrichs scheme](/lax-friedrichs-scheme/) for $u_t + u_x = 0$ is $u_j^{n+1} = \frac12(1 + \nu)u_{j-1} + \frac12(1 - \nu)u_{j+1}$. Show that it is monotone for $|\nu| \le 1$, and compute $\sum_k (k + \nu)^2 c_k$. Explain with [Godunov's order barrier](/godunov-order-barrier/) why this number shows the scheme is only first order, and for which $\nu$ it vanishes.

11. • The Beam-Warming scheme for $u_t + u_x = 0$ is $u_j^{n+1} = u_j - \frac\nu2(3u_j - 4u_{j-1} + u_{j-2}) + \frac{\nu^2}2(u_j - 2u_{j-1} + u_{j-2})$. Write it as $\sum_k c_k u_{j+k}$ at $\nu = \frac12$, apply one step to $(0, 0, 0, 1, 1, 1, 1)$, and say where the new extremum appears and why the barrier predicts one.

12. • Forward Euler in time with central differences in space, $u_j^{n+1} = u_j - \frac\nu2(u_{j+1} - u_{j-1})$, uses a stencil that contains the domain of dependence of $u_t + u_x = 0$ whenever $|\nu| \le 1$. Show that its amplification factor satisfies $|g|^2 = 1 + \nu^2\sin^2\theta$, so it is unstable for every $\nu > 0$. What does this say about the [CFL condition](/courant-friedrichs-lewy-condition/)?

13. • For Burgers' equation with the entropy pair $\eta = u^2/2$, $\psi = u^3/3$, show that a jump from $u_L$ to $u_R$ moving at the Rankine-Hugoniot speed produces entropy at the rate $s(\eta_R - \eta_L) - (\psi_R - \psi_L) = (u_L - u_R)^3/12$. Deduce that the entropy inequality admits the jump exactly when the Lax condition does.

14. • A traffic light turns green: the traffic flux is $f(\rho) = \rho(1 - \rho)$, with $\rho = 1$ (a jam) for $x < 0$ and $\rho = 0$ for $x > 0$. Find the solution, the density and the flux at the light $x = 0$, and the speed of the shock when later cars at density $\frac12$ meet a queue at density 1.

15. • For Burgers' equation with $u_L = -1$ and $u_R = 2$, compute the [Rusanov flux](/rusanov-flux/), the Roe flux $\frac12(f_L + f_R) - \frac12|\hat a|(u_R - u_L)$ with $\hat a = (u_L + u_R)/2$, the [HLL flux](/hll-riemann-solver/) with $S_L = -1$, $S_R = 2$, and the exact Godunov flux. Which of them lie on the dissipative side of the Godunov flux, as an E-flux must?

16. • The shallow water equations with $g = 1$ have $h_L = 2$, $h_R = 1$ and water at rest on both sides. Compute the [Roe](/roe-solver/) flux at the dam with the averages $\bar h = (h_L + h_R)/2$ and $\bar u = (\sqrt{h_L}u_L + \sqrt{h_R}u_R)/(\sqrt{h_L} + \sqrt{h_R})$, and compare it with the exact flux $(h^*u^*, h^*u^{*2} + \frac12h^{*2})$ for $h^* = 1.45384$, $u^* = 0.41692$, and with the Rusanov mass flux.

17. • Show that the [Kurganov-Tadmor scheme](/kurganov-tadmor-scheme/) with all slopes set to zero is the finite volume scheme with the Rusanov flux, and that the [Nessyahu-Tadmor scheme](/nessyahu-tadmor-scheme/) with zero slopes is the staggered Lax-Friedrichs scheme.

18. • The unlimited face value of the [piecewise parabolic method](/piecewise-parabolic-method/) is $a_{j+1/2} = \frac7{12}(a_j + a_{j+1}) - \frac1{12}(a_{j-1} + a_{j+2})$. On a unit grid with the face at $x = \frac12$, show that it is exact for the cell averages of $1$, $x$, $x^2$ and $x^3$, and find its error for $x^4$.

19. • In one dimension the Yee scheme has the dispersion relation $\sin(\omega\Delta t/2) = S\sin(k\Delta x/2)$ with $S = c\Delta t/\Delta x$. For a wave with 10 cells per wavelength, compute the phase speed as a fraction of $c$ for $S = 0.5$, $0.99$ and $1$. Repeat for 20 cells per wavelength at $S = 0.5$, and give the factor by which the error falls.

20. • Take the (2,1) [summation-by-parts operator](/summation-by-parts-operators/) with $h = \frac14$ on $[0, 1]$ and $u = x^2$ at the five nodes. Compute $Du$ and its error at each node. Then check the two identities $\mathbf 1^T H Du = u_n - u_0$ and $u^T H D u = \frac12(u_n^2 - u_0^2)$ with $H = h\,\mathrm{diag}(\frac12, 1, 1, 1, \frac12)$.

21. • Show that the [discontinuous Galerkin method](/discontinuous-galerkin-method/) with $k = 0$ and forward Euler in time is the first-order finite volume scheme with the same numerical flux. With the upwind flux for $u_t + au_x = 0$, which scheme is it, and what does the energy identity of the method give for it?

22. ★ For a scalar law with a $C^1$ flux, take a jump $u_L > u_R$ that satisfies the Rankine-Hugoniot condition. Show that it satisfies all of Kruzkov's entropy inequalities, with $\eta = |u - k|$ and $\psi = \operatorname{sgn}(u - k)(f(u) - f(k))$, if and only if the graph of $f$ lies on or below the chord from $(u_R, f(u_R))$ to $(u_L, f(u_L))$. Deduce that for a convex flux this is the Lax condition.

23. ★ For a convex flux, prove that the Godunov flux is $\min_{u_L \le u \le u_R} f(u)$ when $u_L \le u_R$ and $\max_{u_R \le u \le u_L} f(u)$ when $u_L > u_R$. Check the formula against the Godunov flux of Exercise 15.

24. ★ For a scalar law with the entropy $U = u^2/2$, show that $F^* = \int_0^1 f(u_L + \theta(u_R - u_L))\,d\theta$ satisfies the condition $(u_R - u_L)F^* = \psi_R - \psi_L$, $\psi = uf(u) - q(u)$, of an [entropy stable scheme](/entropy-stable-scheme/) with no dissipation. Compute $F^*$ in closed form for $f(u) = u^3/3$ and check that it is consistent.

25. ★ For the shallow water equations in the variables $(h, hu)$, show that the Jacobian evaluated at $\bar h = (h_L + h_R)/2$ and the $\sqrt h$-weighted average $\bar u$ satisfies $F(U_R) - F(U_L) = \hat A(U_R - U_L)$ for all positive $h_L, h_R$.

26. ★ An explicit two-stage Runge-Kutta method is written as $u^{(1)} = u + \beta_{10}\Delta t L(u)$, $u^{n+1} = \alpha_{20}u + \alpha_{21}u^{(1)} + \Delta t(\beta_{20}L(u) + \beta_{21}L(u^{(1)}))$ with all $\alpha, \beta \ge 0$ and $\alpha_{20} + \alpha_{21} = 1$. Its SSP coefficient is the smallest ratio $\alpha_{ik}/\beta_{ik}$ over the nonzero $\beta_{ik}$ (with $\alpha_{10} = 1$). Show that a method of second order has SSP coefficient at most 1, so the [SSP Runge-Kutta](/strong-stability-preserving-runge-kutta/) method of Heun type is optimal among two-stage methods.
