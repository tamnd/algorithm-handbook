1. ◦ A laminate in one dimension has $a(y) = 1$ on a third of each period and $a(y) = 9$ on the other two thirds. Following [periodic homogenization](/periodic-homogenization/), compute the effective coefficient $a^*$ and the arithmetic mean $\langle a \rangle$. Compute the derivative $\chi'$ of the corrector in each phase, check that its mean is zero, and check that the flux $a(1 + \chi')$ is the same in both phases.

2. ◦ An atomic chain has nearest-neighbour springs $V_1(r) = \frac12 k_1 (r - 1)^2$ and second-neighbour springs $V_2(r) = \frac12 k_2 (r - 1.8)^2$, with $k_1 = 1$ and $k_2 = 0.25$. Use the [Cauchy-Born rule](/cauchy-born-rule/) to find the equilibrium spacing $a$, and the modulus $W''(1)$ of $W(F) = \frac1a \bigl(V_1(Fa) + V_2(2Fa)\bigr)$.

3. ◦ A state of a [kinetic Monte Carlo](/kinetic-monte-carlo/) run has three events with rates 2, 5 and 3 per second. The random numbers are $u_1 = 0.65$ and $u_2 = 0.5$. Which event is chosen, and how long is the time step?

4. ◦ Use [harmonic transition state theory](/harmonic-transition-state-theory/) with unit masses. (a) For $V(x) = 2(x^2 - 1)^2$, give the rate of escape from the well at $x = -1$ as a function of $\beta$. (b) In two dimensions, the Hessian at the minimum has eigenvalues 4 and 9, and at the saddle $-2$ and 1. Compute the prefactor. (c) An event has the prefactor $10^{13}$ per second and the barrier 0.8 eV. Compute its rate at 500 K, with $k_B = 8.617 \times 10^{-5}$ eV/K.

5. ◦ For $V(x, y) = (x^2 - 1)^2 + 2y^2$, an image of the [nudged elastic band](/nudged-elastic-band/) sits at $(0.1, 0.2)$ with the tangent $\tau = (1, 0)$. Compute the gradient, the force on the image if it is the climbing image, and the perpendicular part of the true force that a plain image feels.

6. ◦ For $V(x) = \frac12 x^T H x$ with $H = \operatorname{diag}(2, -1)$, the [dimer method](/dimer-method/) has its axis $N = (\cos\theta, \sin\theta)$. Give the curvature $C(\theta) = N^T H N$ at $\theta = 45°$ and at $\theta = 90°$. At $x = (0.2, 0.3)$ with $N = (0, 1)$, compute the force $F$ and the translation force $F^\dagger$, and say in which direction the dimer moves.

7. ◦ [Coarse projective integration](/coarse-projective-integration/) takes $k$ inner steps and then a projective step of $M = 50$ inner steps, so a fast mode with factor $\zeta$ per inner step is multiplied by $\sigma(\zeta) = ((M+1)\zeta - M)\zeta^k$. The fast factors lie in $[0, 0.4]$. Find the smallest $k$ with $|\sigma(\zeta)| \le 1$ on that interval, the smallest $k$ that the entry's sufficient condition $\rho^k \le 1/(2M+1)$ allows, and the saving factor $(M + k + 1)/(k + 1)$ for the smaller $k$.

8. ◦ A random bar is made of cells of length 1 whose coefficients are 1 or 9, each with probability $\frac12$, independently. Give the effective coefficient of a long bar. A [representative volume element](/representative-volume-element/) of two cells gives the apparent coefficient of the two cells in series: list its values with their probabilities, and compute its mean.

9. ◦ A [phase-field model](/phase-field-model/) has $W(u) = \frac14(u^2 - 1)^2$ and $\varepsilon = 0.01$. (a) Give the surface tension. (b) For Allen-Cahn with $M = 1/\varepsilon^2$, when do a disk and a ball of radius 0.5 disappear in the sharp interface limit? (c) For Cahn-Hilliard, which of the uniform states $u_0 = 0.5$ and $u_0 = 0.6$ is linearly unstable? For the unstable one, give the fastest-growing $|k|^2$ and its growth rate in terms of $M$.

10. ◦ The [string method](/string-method/) reparametrizes the polygon $(0,0)$, $(3,0)$, $(3,4)$ into $N = 4$ segments of equal arc length. Give the three interior points.

11. ◦ A [hyperdynamics](/hyperdynamics/) run takes five steps of $h = 1$ fs with the bias $\Delta V = 0.1$, 0.15, 0.2, 0.05 and 0 eV at $k_BT = 0.05$ eV. Compute the hyper time and the boost of the five steps.

12. • For $-(a(x/\varepsilon) u_\varepsilon')' = 1$ on $(0, 1)$ with $u_\varepsilon(0) = u_\varepsilon(1) = 0$, $a$ 1-periodic and $1/\varepsilon$ an integer, prove that $u_\varepsilon(j\varepsilon) = u_0(j\varepsilon)$ at every cell boundary. For the laminate of Exercise 1 with $\varepsilon = \frac14$, compute $u_\varepsilon(\frac12)$ exactly, and compare with the value that the arithmetic mean $\langle a \rangle$ would give.

13. • A kinetic Monte Carlo model has three states in a cycle, $A \to B$ at rate 1, $B \to C$ at rate 2 and $C \to A$ at rate 4. Give the fraction of time spent in each state and the fraction of steps that end in each state. Then describe a sum tree over $M$ rates that selects an event and updates one rate in $O(\log M)$ time each.

14. • In [temperature-accelerated dynamics](/temperature-accelerated-dynamics/), an event with barrier 0.6 eV is seen after 1 ns at 600 K. Extrapolate its time to 300 K. With $\nu_{\min} = 10^{12}$ per second, $\delta = 10^{-3}$ and this event as the shortest so far, compute the stop time $t_{\text{stop}}$ of the high temperature run and the boost $t_{\text{low}}/t_{\text{stop}}$.

15. • In [parallel replica dynamics](/parallel-replica-dynamics/), take the elapsed time per transition as $c + s/m$ steps, with $c = 10$ and a mean escape time $s = 100$. Compute the speedup over a serial run for $m = 4$, 16 and 64, its limit as $m \to \infty$, and the largest $m$ for which the efficiency (speedup over $m$) is at least $\frac12$.

16. • Fit the pair force $F(r) = c_1(2 - r) + c_2(r - 1)$ on $[1, 2]$ by least squares to the samples $(r, f) = (1.2, 1.5)$, $(1.6, 0.4)$ and $(1.8, 0.1)$, as in [force matching](/force-matching-coarse-graining/). Give the normal equations and $c$ exactly.

17. • In [iterative Boltzmann inversion](/iterative-boltzmann-inversion/) with $\alpha = 1$ and $k_BT = 2.5$, a bin has $g = 1.2$ and $g^* = 1$. Compute the change of the potential in that bin and say why its sign is right. Then show that in the dilute limit, where $g = e^{-\beta V}$, the method reaches the target after one update from any start.

18. • A [multiscale finite element method](/multiscale-finite-element-method/) element $[0, H]$ has $a = 1$ on its first half and $a = 3$ on its second. Compute the basis function $\varphi$ with $(a\varphi')' = 0$, $\varphi(0) = 0$, $\varphi(H) = 1$, its value at $H/2$, and the element stiffness $\int_0^H a \varphi'^2$.

19. • For $-\kappa u'' + a u' = 0$ with $a = 1$, $\kappa = 0.05$ and $h = 0.2$, compute the element Péclet number, the stabilization parameter $\tau$ of the [variational multiscale method](/variational-multiscale-method/), and the ratio of successive nodal differences of the Galerkin solution. What ratio do the exact solution and the stabilized scheme give?

20. • An [FE² method](/fe2-method/) cell is two bars of equal length in series, with $\sigma = c e + e^3$ and $c = 1$ and $c = 2$. For the mean strain $E = 0.5$, solve for the two strains, and compute the macro stress $\Sigma$ and the tangent $d\Sigma/dE$.

21. • In the [heterogeneous multiscale method](/heterogeneous-multiscale-method/) in one dimension, $A_K$ is the harmonic mean of $a(x/\varepsilon)$ over an interval of length $\delta$ centred at $x_K$. For $a(y) = 2 + \sin 2\pi y$ and $\delta = 1.5\varepsilon$, compute $A_K$ exactly when $x_K/\varepsilon$ is an integer, an integer plus $\frac14$, and an integer plus $\frac34$. Compare with $a^* = \sqrt3$.

22. • The scalar process $dv = -(\gamma/m) v\, dt + (\sigma/m)\, dW$ is the velocity part of [dissipative particle dynamics](/dissipative-particle-dynamics/) for one pair with fixed weights. Find its stationary variance and show that it equals $k_BT/m$ exactly when $\sigma^2 = 2\gamma k_BT$.

23. • For the one-dimensional [peridynamics](/peridynamics/) model with $C = 3E/\delta^3$, the dispersion relation is $\rho\omega^2 = 2C(\delta - \sin(k\delta)/k)$. Give the ratio of the wave speed to the local value $\sqrt{E/\rho}$ at $k\delta = 0.5$, the value of $k\delta$ where it falls to 0.9, and the largest frequency for $E = 200$ GPa, $\rho = 7800$ kg/m³ and $\delta = 1$ mm.

24. ★ For $V(x) = x^2/2 - x^3/3$ with unit mass, the well at $x = 0$ has the barrier $\frac16$ at $x = 1$. Show that $k_{\mathrm{TST}}/k_{\mathrm{HTST}} = 1 - \frac{5}{6\beta} + O(\beta^{-2})$.

25. ★ Derive the harmonic transition state rate in two dimensions from the TST formula: expand $V$ to second order at the minimum and at the saddle, do the Gaussian integrals, and show that the result is $\frac{\nu_1\nu_2}{\nu_1^S} e^{-\beta\Delta E}$, with $\nu = \sqrt{\lambda}/2\pi$ for each positive eigenvalue $\lambda$.

26. ★ Cells of a random bar have independent coefficients with the same law, and the apparent coefficient of a window of $m$ cells is their harmonic mean. Prove that its expectation is at least $a^* = \langle a^{-1} \rangle^{-1}$ and does not increase with $m$.

27. ★ In the setting of Exercise 12, prove that $\max_x |u_\varepsilon(x) - u_0(x)| \le C\varepsilon$, and give a constant $C$ in terms of the bounds $0 < \alpha \le a \le \Lambda$.

28. ★ For $\dot x = ax + by$, $\dot y = cx + dy$ with $d < 0$, the [Mori-Zwanzig formalism](/mori-zwanzig-formalism/) gives $\dot x = ax + bc\int_0^t e^{ds}x(t-s)\,ds + b e^{dt}y_0$. Take $a = -1$, $b = c = 1$, $d = -3$: compare the Markov approximation $\dot x = (a - bc/d)x$ with the slow eigenvalue of the full system. Then show that for fixed $a$, $b$, $c$ the two differ by $-abc/d^2 + O(d^{-3})$ as $d \to -\infty$.
