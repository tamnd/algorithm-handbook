1. ◦ In the [vorticity-streamfunction formulation](/vorticity-streamfunction-formulation/) with $u = \psi_y$ and $v = -\psi_x$, take $\psi = \sin\pi x\sin\pi y$ on the unit square. Compute $u$, $v$ and the vorticity $\omega = v_x - u_y$, and show that $\omega = 2\pi^2\psi$. Which of the two wall conditions, no penetration and no slip, does this velocity satisfy on the four sides?

2. ◦ A flow has $Re = UL/\nu = 10^6$. Using the scalings of [Kolmogorov's 1941 theory](/kolmogorov-1941-theory/) with all constants set to one, find $L/\eta$, the ratio of the large-eddy time to the Kolmogorov time, and the number of grid points $(L/\eta)^3$ that a [direct numerical simulation](/direct-numerical-simulation/) of a cube of side $L$ would need.

3. ◦ In the log layer, $dU/dy = u_\tau/(\kappa y)$. Take water ($\nu = 10^{-6}$ m²/s), $u_\tau = 0.04$ m/s, $y = 2$ cm and $\kappa = 0.41$. Find the mixing length, the eddy viscosity of the [mixing length model](/mixing-length-model/) and its ratio to the molecular viscosity.

4. ◦ A [k-epsilon](/k-epsilon-model/) solution has $k = 0.5$ m²/s² and $\varepsilon = 2$ m²/s³ at a point. Find $\nu_t$ with $C_\mu = 0.09$. Convert to the variable of the [k-omega model](/k-omega-model/) with $\omega = \varepsilon/(\beta^* k)$ and $\beta^* = 0.09$, and compute $k/\omega$.

5. ◦ The resolved strain rate at a point is $\bar S = \operatorname{diag}(a, -\tfrac a2, -\tfrac a2)$, an axisymmetric stretching. Show that $|\bar S| = \sqrt{2\bar S_{ij}\bar S_{ij}} = \sqrt3\,a$. With $a = 10$ 1/s, $C_s = 0.17$ and $\Delta = 1$ cm, find the eddy viscosity of the [Smagorinsky model](/smagorinsky-model/).

6. ◦ In lattice units, what kinematic viscosity does the [lattice Boltzmann method](/lattice-boltzmann-method/) give at $\tau = 0.8$, and what $\tau$ gives $\nu = 0.05$? What is the Mach number of a lattice speed $|u| = 0.1$? A simulation of water ($\nu = 10^{-6}$ m²/s) uses $\Delta x = 1$ mm and $\tau = 0.8$: how long is one time step in seconds?

7. ◦ In the unit cell, the [piecewise linear interface](/piecewise-linear-interface-calculation/) with normal $n = (1, 3)$ is the line $x + 3y = \beta$, and the liquid fills $x + 3y \le \beta$. Find $\beta$ for the volume fractions $f = 0.1$ and $f = 0.4$, and give the heights at which the second line meets the two vertical sides.

8. ◦ The [immersed boundary method](/immersed-boundary-method/) spreads a force from a point at $X = 0.3h$ to the grid nodes $-h$, $0$, $h$ and $2h$ with Peskin's four-point kernel. Compute the four weights, and check that they sum to 1, that their first moment about $X$ is zero and that their squares sum to $3/8$. What are the weights when the point sits on a node?

9. ◦ Particles of unit mass sit at $x = 0, 1, 2, \ldots$ (a half-infinite row with a free end at $x = 0$), with the 1D cubic spline of the [SPH smoothing kernel](/sph-smoothing-kernel/) entry and $h = 1$. Compute the density of the end particle and of the particle at $x = 1$, and the standard SPH estimate $\sum_j (m_j/\rho_j)A_j\,\partial_xW(x_i - x_j)$ of the derivative of $A(x) = x$ at the end particle, taking $\rho_j = 1$.

10. • Apply one projection of the [marker-and-cell method](/marker-and-cell-method/) on a closed $2 \times 2$ box of cells $(i, j)$, $i, j \in \{0, 1\}$, with $\Delta x = \Delta t = 1$. The interior faces carry $u_{10}$ (between cells $(0,0)$ and $(1,0)$), $u_{11}$ (between $(0,1)$ and $(1,1)$), $v_{01}$ (between $(0,0)$ and $(0,1)$) and $v_{11}$ (between $(1,0)$ and $(1,1)$); the wall faces carry zero. Start from $u^* = (u_{10}, u_{11}, v_{01}, v_{11}) = (1, 0, 0, 0)$, solve the pressure equation with $p_{00} = 0$, and give $p$, the projected velocity, its divergence and its kinetic energy $\sum$ (face value)$^2$.

11. • On the MAC grid of exercise 10, the discrete divergence $D$ and gradient $G$ satisfy $D = -G^{\mathsf T}$. Prove that the projected velocity $u = u^* - Gp$, with $DGp = Du^*$, is the discrete divergence-free field closest to $u^*$ in the Euclidean norm, and that $\|u^*\|^2 = \|u\|^2 + \|Gp\|^2$. Check the identity on the numbers of exercise 10. This is the discrete form of the projection in [Chorin's method](/chorin-projection-method/).

12. • Find the [Helmholtz-Hodge decomposition](/helmholtz-hodge-decomposition/) of $u = (\sin x\cos y,\ 0)$ on the periodic square $[0, 2\pi]^2$: a gradient $\nabla q$ plus a divergence-free field $w$. Check that the two parts are orthogonal by computing $\|u\|^2$, $\|\nabla q\|^2$ and $\|w\|^2$ in $L^2$.

13. • For the [artificial compressibility method](/artificial-compressibility-method/) on a periodic grid with $\Delta x = \Delta y = 0.1$, $\nu = 0.01$ and $c = 1$, find $\mu_{\max}$ and the largest pseudo-time step allowed by the entry's sharp condition for the linear Stokes problem. Compare it with the acoustic limit alone ($\nu = 0$) and the viscous limit alone ($c = 0$).

14. • Split the unit square into $n \times n$ squares and each square into two triangles by a diagonal. Count the unknowns of the P1–P0 pair (continuous piecewise linear velocity, zero on the boundary; piecewise constant pressure with zero mean). Show that for every $n \ge 2$ the pressure space is larger than the velocity space, give a lower bound on the number of spurious pressure modes, and say what this means for the [inf-sup condition](/inf-sup-condition/).

15. • Suppose that the K41 spectrum $E(k) = C\varepsilon^{2/3}k^{-5/3}$ holds up to a sharp cutoff $k_d$ and is zero beyond, and that the dissipation $2\nu\int_0^{k_d}k^2E(k)\,dk$ equals $\varepsilon$. Find $k_d\eta$ with $\eta = (\nu^3/\varepsilon)^{1/4}$, and evaluate it for $C = 1.5$.

16. • Show that the energy transfer from resolved to subgrid scales in the Smagorinsky model, $-\tau_{ij}\bar S_{ij}$ with $\tau_{ij} - \tfrac13\tau_{kk}\delta_{ij} = -2\nu_r\bar S_{ij}$, equals $\nu_r|\bar S|^2$, so the model never returns energy to the resolved scales. Evaluate it for the data of exercise 5.

17. • In homogeneous simple shear $dU/dy = S$, the [Boussinesq closure](/boussinesq-eddy-viscosity/) gives $-\langle u'v' \rangle = \nu_tS$ and the production $P = \nu_tS^2$. Assume local equilibrium $P = \varepsilon$ and the k-epsilon eddy viscosity $\nu_t = C_\mu k^2/\varepsilon$. Show that $-\langle u'v' \rangle/k = \sqrt{C_\mu}$, and explain how the measured ratio of about 0.3 fixes $C_\mu$.

18. • Water ($\nu = 10^{-6}$ m²/s, $\rho = 1000$ kg/m³) flows past a wall, and the first cell center is at $y = 5$ mm with $U = 2$ m/s. Solve the log law $U/u_\tau = \ln(yu_\tau/\nu)/\kappa + B$ with $\kappa = 0.41$ and $B = 5.2$ for $u_\tau$ by fixed-point or Newton iteration. Give $u_\tau$, $y^+$ and the wall shear stress, and say whether the point lies in the range where [wall functions](/wall-functions/) are meant to be used.

19. • Run D1Q3 with $\tau = \frac34$ from a unit mass at one node, starting at equilibrium. Show that after two steps the density two nodes away is $-\frac1{54}$. Why does this not contradict the requirement $\tau > \frac12$?

20. • The Taylor-Green vortex decays like $e^{-2\nu k^2 t}$. On a $32 \times 32$ lattice with $\tau = 0.8$, after how many steps has the velocity amplitude halved, and after how many the kinetic energy? Show that over the entry's $S = N^2/8$ steps the amplitude falls by the same factor $e^{-\pi^2/10} \approx 0.373$ for every $N$.

21. • The D2Q9 equilibrium is a second-order expansion in $u$ and turns negative at large speeds. With $\rho = 1$, find the largest $|u|$ for which all nine populations are nonnegative when $u$ points along the $x$ axis, and when it points along the diagonal $(1, 1)$. Which populations reach zero first in each case?

22. ★ On the mesh of $n \times n$ squares of side $h$, take the Q1–P0 pair: continuous bilinear velocity, zero on the boundary, and one pressure per square. Prove that the checkerboard pressure $p_{ij} = (-1)^{i+j}$ satisfies $\int p\,\nabla\cdot u\,dx = 0$ for every discrete velocity $u$. Conclude that the pair is not inf-sup stable.

23. ★ Assume that near a wall the mean velocity has the inner form $U = u_\tau f(y^+)$ with $y^+ = yu_\tau/\nu$, that farther out it has the defect form $U_0 - U = u_\tau g(y/\delta)$, and that both hold in an overlap region for every large $Re_\tau = \delta u_\tau/\nu$. Show that $y\,dU/dy$ is constant in the overlap, and derive the log law $U^+ = \frac1\kappa\ln y^+ + B$. Which parts of the result does the argument not determine?

24. ★ For the D2Q9 velocity set, let the rest velocity have weight $w_0$, the four axis velocities $w_1$ and the four diagonals $w_2$. Find all $w_0$, $w_1$, $w_2$ and $c_s^2$ for which $\sum_iw_i = 1$, $\sum_iw_ic_{i\alpha}c_{i\beta} = c_s^2\delta_{\alpha\beta}$ and $\sum_iw_ic_{i\alpha}c_{i\beta}c_{i\gamma}c_{i\delta} = c_s^4(\delta_{\alpha\beta}\delta_{\gamma\delta} + \delta_{\alpha\gamma}\delta_{\beta\delta} + \delta_{\alpha\delta}\delta_{\beta\gamma})$. Why does the [Chapman-Enskog expansion](/chapman-enskog-expansion/) need the fourth-moment condition?

25. ★ The D1Q2 lattice has velocities $c = \pm1$, weights $\frac12$ and equilibrium $f_\pm^{\mathrm{eq}} = \rho/2$, with the [BGK collision](/bgk-collision-operator/) at relaxation time $\tau$. Show that it is consistent with $\rho_t = D\rho_{xx}$ with $D = \tau - \frac12$ in lattice units. Check the claim at $\tau = 1$ by showing that the variance of a unit mass grows by exactly 1 per step.

26. ★ In [smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/), take the symmetric pressure force $\dot v_i = -\sum_jm_j\bigl(p_i/\rho_i^2 + p_j/\rho_j^2\bigr)\nabla_iW_{ij}$ with a radial kernel, so that $\nabla_iW_{ij} = F(|x_i - x_j|)(x_i - x_j)$. Prove that the total linear momentum $\sum_im_iv_i$ and, in two or three dimensions, the total angular momentum $\sum_im_ix_i \times v_i$ are constant in time.
