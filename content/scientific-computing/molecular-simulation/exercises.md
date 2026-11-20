1. ◦ In reduced units with $\epsilon = \sigma = 1$, evaluate the [Lennard-Jones potential](/lennard-jones-potential/) and the pair force $-\phi'(r)$ at $r = 1.5$. Is the force attractive or repulsive? Where is the minimum of $\phi$?

2. ◦ A liquid of $N = 500$ atoms at density $\rho = 0.8$ has, summed over one configuration, 1200 unordered pairs at distances in $[1, 1.1)$. Compute the ideal-gas count per atom for that shell and the estimate of the [radial distribution function](/radial-distribution-function/) there.

3. ◦ In the [canonical ensemble](/canonical-ensemble/), the kinetic energy of $N_f$ quadratic degrees of freedom is a gamma variable with mean $N_f k_B T/2$ and variance $N_f (k_B T)^2/2$. For 100 atoms in 3D with the total momentum fixed, find $N_f$, the mean and the standard deviation of $K$ in units of $k_B T$, and the relative fluctuation.

4. ◦ The [Andersen thermostat](/andersen-thermostat/) gives each particle a new velocity with probability $1 - e^{-\nu h}$ per step. For $\nu = 0.5$ and $h = 0.005$, find this probability and the mean number of steps between two collisions of one particle.

5. ◦ The [Berendsen thermostat](/berendsen-thermostat/) scales the velocities by $\lambda$ with $\lambda^2 = 1 + \frac{h}{\tau}\left(\frac{K_0}{K} - 1\right)$. For $K = 150$, $K_0 = 100$ and $h/\tau = 0.1$, find $\lambda$ and the new kinetic energy. For a system with no forces, after how many steps is $K - K_0$ below 1?

6. ◦ In [Ewald summation](/ewald-summation/), the real-space terms beyond $r_c$ are of order $e^{-\alpha^2 r_c^2}$. Find $\alpha r_c$ for a relative error of $10^{-6}$, and $\alpha$ for $r_c = 9$ Å.

7. ◦ Three samples from state 0 give the energy differences $\beta \Delta U = 0.5$, $1.5$ and $-0.2$. Compute the estimate of $\beta \Delta A$ by [free energy perturbation](/free-energy-perturbation/), and compare it with the mean of $\beta \Delta U$.

8. ◦ A particle on a line has $U_\lambda(x) = \frac12 (1 + 3\lambda) x^2$ with $k_B T = 1$. Show that $\langle \partial U/\partial\lambda \rangle_\lambda = \frac{3}{2(1 + 3\lambda)}$. Estimate $\Delta A$ by [thermodynamic integration](/thermodynamic-integration/) with the trapezoidal rule on 2 and on 4 intervals and with Simpson's rule on 2, and compare with the exact $\frac12 \ln 4$.

9. • Run one step of velocity Verlet with $h = 0.2$ on $\ddot x = -x$ from $x = 1$, $v = 0$. Show that $\tilde E = \frac12 v^2 + \frac12 (1 - h^2/4) x^2$ is conserved exactly, and use it to bound $|H - \frac12|$ along the whole run. What is the largest $h$ for which the bound is at most 0.005? Relate $\tilde E$ to the [shadow Hamiltonian](/shadow-hamiltonian/).

10. • A periodic cube of side $L = 10$ holds $N = 800$ atoms, with cutoff $r_c = 2.5$, so the [linked-cell list](/linked-cell-list/) has $4^3 = 64$ cells. With uniform positions and each pair of neighbouring cells visited once, find the expected number of distance tests and compare it with all $N(N-1)/2$ pairs. What fraction of the tests find a pair within $r_c$?

11. • A [Verlet neighbour list](/verlet-neighbor-list/) at density $0.8$ uses $r_c = 2.5$ and a skin of $0.5$. Find the mean number of listed neighbours per atom and the fraction that lie within $r_c$. After what largest displacement of any atom must the list be rebuilt?

12. • [Brownian dynamics](/brownian-dynamics/) in the potential $\frac12 k x^2$ takes the step $x_{n+1} = (1 - c) x_n + \sqrt{2 D h}\, \xi_n$, with $c = h D k/(k_B T)$. For $D = 1$, $k = 100$ and $k_B T = 1$, find the stationary variance for $h = 0.005$ and compare it with $k_B T/k$. For which $h$ is the scheme unstable?

13. • One step of [stochastic velocity rescaling](/stochastic-velocity-rescaling/) has $K' = c K + (1 - c)\frac{K_0}{N_f}\left(R_1^2 + \sum_{i=2}^{N_f} S_i^2\right) + 2 R_1 \sqrt{c(1 - c) K K_0/N_f}$, with standard normal $R_1$ and $S_i$ and $c = e^{-h/\tau}$. For $K = 2$, $K_0 = 3$, $N_f = 6$ and $h/\tau = 0.2$, find the mean and the variance of $K'$.

14. • [Smooth particle mesh Ewald](/smooth-particle-mesh-ewald/) spreads a charge with the cardinal B-spline of order 4. For a charge a quarter of a grid spacing past a node, find the four weights as fractions and check that they sum to 1.

15. • An [umbrella sampling](/umbrella-sampling/) window has the bias $w(s) = \frac12 \kappa s^2$ with $\kappa = 50$ and $k_B T = 1$. Its histogram has 4000, 3000 and 1000 counts in bins of equal width at $s = 0$, $0.1$ and $0.2$. Find $F(0.1) - F(0)$ and $F(0.2) - F(0)$.

16. • The work of a pulling experiment is Gaussian with mean 3 and standard deviation 1.5, with $k_B T = 1$. Use the [Jarzynski equality](/jarzynski-equality/) to find $\Delta F$ and the mean dissipated work. Bound the probability of a work value below $\Delta F - 2$.

17. • [Metadynamics](/metadynamics/) in its well-tempered form converges to the bias $V = -\frac{\Delta T}{T + \Delta T} F$. For $k_B T = 1$ and $k_B \Delta T = 7$, a barrier of height 8 in $F$ becomes a barrier of what height in $F + V$? What does the standard form, without tempering, aim at?

18. • In the [embedded atom method](/embedded-atom-method/), take the embedding function $F(\bar\rho) = -\sqrt{\bar\rho}$, no pair term, and a density of 1 from each nearest neighbour. For a lattice with $z$ nearest neighbours, find the cohesive energy $E_c$ and the unrelaxed vacancy energy $E_v$. Evaluate $E_v/E_c$ for $z = 8$ and $z = 12$, find its limit, and compare with a pair potential.

19. • A particle in 3D has an Ornstein-Uhlenbeck velocity with friction $\gamma = 2$ and $k_B T/m = 1$, so its velocity autocorrelation is $3 e^{-\gamma t}$. Use the [Green-Kubo relations](/green-kubo-relations/) to find $D$, and find the mean squared displacement at $t = 1$.

20. ★ Take $\ddot x = -\Omega^2 x - \kappa x$ with $\Omega = 10$ and $\kappa = 1$. [RESPA](/respa-multiple-time-step/) gives half kicks of the slow force $-\kappa x$ at both ends of an outer step $h$ and solves the fast motion exactly in between. Show that the one-step map has the trace $2\cos\Omega h - \frac{\kappa h}{\Omega}\sin\Omega h$, and find the interval of $h$ just below $\pi/\Omega$ where it is unstable.

21. ★ Two forward work values $w_F = 1$ and $2$ come from state 0, and two reverse work values $w_R = -0.5$ and $0$ from state 1, all in units of $k_B T$. With equal sample sizes, the [Bennett acceptance ratio](/bennett-acceptance-ratio/) solves $\sum_F f(w_F - C) = \sum_R f(w_R + C)$ for $C = \beta\Delta A$, with $f(x) = 1/(1 + e^x)$. Find $C$ by bisection, and compare it with the forward and reverse perturbation estimates.

22. ★ A spring is switched from $k = 1$ to $k = 4$ with $k_B T = 1$. For samples from $k = 1$, find $\langle e^{-W} \rangle$ and its variance, and the number of samples for a standard error of 0.01 in $\Delta A$. Show that in the reverse direction the estimator has infinite variance.

23. ★ Velocity Verlet on a harmonic bond of angular frequency $\omega$ rotates by $\tilde\omega h$ per step, with $\cos\tilde\omega h = 1 - (\omega h)^2/2$. For a bond with period 11 fs, find the numerical period for steps of 1, 2 and 3 fs, and the step at which the method becomes unstable.

24. ★ Under Andersen collisions at rate $\nu$, a free particle in 3D keeps its velocity until its next collision. Show that its velocity autocorrelation is $3 \frac{k_B T}{m} e^{-\nu t}$, and use Green-Kubo to show that $D = k_B T/(m\nu)$. For $\nu = 0.5$ and $k_B T/m = 1$, find $D$ and the mean squared displacement at $t = 10$.
