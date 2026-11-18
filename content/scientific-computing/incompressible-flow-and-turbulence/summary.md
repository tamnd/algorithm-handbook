## What to remember

- **Lattice Boltzmann.** Each node holds populations $f_i$, one per lattice velocity $c_i$. Collision relaxes them toward $f_i^{\mathrm{eq}}(\rho, u)$ with relaxation time $\tau$ (BGK), and streaming moves each one to $x + c_i$. On D2Q9 the weights are $\frac49$, $\frac19$ and $\frac1{36}$, and $c_s^2 = \frac13$ in lattice units.
- At low Mach number the fields obey Navier-Stokes with $p = \rho/3$ and $\nu = (\tau - \frac12)/3$, with errors $O(\Delta x^2)$ under diffusive scaling plus an $O(u^3)$ error in the viscous stress. This limit is cited (Chapman-Enskog), not proved in the entry; the second-order convergence is observed. Proved: collision conserves mass and momentum at every node, and D1Q3 with $\tau = 1$ is FTCS with $\mu = \frac16$, stable and consistent of order 4 for the heat equation.
- BGK needs $\tau > \frac12$ and small lattice speeds ($|u| \lesssim 0.1$); it becomes unstable as $\tau \to \frac12$ unless the speed is reduced, and there is no simple stability bound for nonlinear flows. With halfway bounce-back the effective wall position moves with $\tau$, which shows up as a slip in Poiseuille flow.
- **SPH.** Particles carry mass, velocity and internal energy; $\rho_i = \sum_j m_j W(x_i - x_j, h)$ with the cubic spline kernel, whose second moment is $h^2/3$. The symmetric pressure term $P_i/\rho_i^2 + P_j/\rho_j^2$ makes pair forces equal and opposite, so mass and momentum are conserved exactly by the fully discrete scheme and total energy by the semi-discrete one. The Monaghan viscosity acts only on approaching pairs.
- Not proved: on irregular particles the kernel sums are not exact quadratures, so SPH is not even zeroth-order consistent in general, and convergence to the Euler equations is observed (an $L^1$ order of about 0.6 to 0.7 on Sod).

## Comparing the two methods

| | Lattice Boltzmann | SPH |
|---|---|---|
| Unknowns | $Q$ populations per lattice node | mass, velocity, energy per particle |
| Mesh | fixed regular lattice | none; particles move with the flow |
| Pressure | $p = \rho/3$, no Poisson solve | equation of state, here $P = (\gamma - 1)\rho e$ |
| Proved | mass and momentum conservation, D1Q3 at $\tau = 1$ | mass and momentum conservation, kernel moments |
| Order | second order, observed | low; noisy on disordered particles |
| Cost per step | $\Theta(QM)$ for $M$ nodes | $\Theta(n \log n + nk)$ for $k$ neighbours (1D, by sorting) |
| Time step | $\Delta t \propto \Delta x^2$ in diffusive scaling | $\Delta t \le C h / (c + \lvert v \rvert)$ |
| Suited to | low-Mach flow in complex geometry, porous media, multiphase | free surfaces, splashing, impacts, astrophysical gas |

## Choosing

Use the lattice Boltzmann method for low-Mach flows in complicated geometries, where its locality, simple walls and speed on graphics processors pay off. Use SPH when the fluid breaks up, splashes or has a free surface. Both entries point elsewhere for some problems: the lattice Boltzmann entry to classical Navier-Stokes solvers for high Reynolds numbers with adaptive meshes, compressible flow and strict incompressibility, and the SPH entry to grid methods such as the [finite volume method](/finite-volume-method/) with [WENO](/weno-scheme/) reconstruction for boundary layers and acoustics, where accuracy per degree of freedom matters.
