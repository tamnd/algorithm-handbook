## What to remember

- The pressure has no equation of its own: it enforces $\nabla\cdot\mathbf u = 0$. By the [Helmholtz-Hodge decomposition](/helmholtz-hodge-decomposition/) $\mathbf u^* = \mathbf w + \nabla q$, removing $\nabla q$ is an orthogonal projection; on the staggered grid $G^{\mathsf T} = -D$ keeps the discrete projection orthogonal.
- [Chorin's projection method](/chorin-projection-method/) is first order in time. At walls the splitting imposes the artificial condition $\partial p/\partial n = 0$ and a numerical boundary layer; in the basic scheme the velocity is first order in $L^2$ but the pressure only of order $\Delta t^{1/2}$; the incremental form recovers first order.
- Velocity and pressure must be discretized compatibly. The staggered [MAC](/marker-and-cell-method/) grid has no spurious pressure modes. Collocated finite volumes need [Rhie-Chow interpolation](/rhie-chow-interpolation/) against the checkerboard. Mixed finite elements need a pair that satisfies the [inf-sup condition](/inf-sup-condition/), such as the [Taylor-Hood element](/taylor-hood-element/); equal-order and P1–P0 pairs fail it.
- A converged [SIMPLE](/simple-algorithm/) iteration solves the discrete steady equations whatever the under-relaxation; its convergence is observed, not proved. [PISO](/piso-algorithm/) uses a fixed number of pressure correctors per time step, each gaining one power of $\Delta t$ in the splitting error.
- The [volume of fluid method](/volume-of-fluid-method/) conserves volume exactly, and its accuracy depends on the interface reconstruction. The [continuum surface force](/continuum-surface-force/) model spreads $\sigma\kappa$ over a few cells; curvature errors drive spurious currents, which a balanced-force discretization reduces.
- [Kolmogorov's 1941 theory](/kolmogorov-1941-theory/) gives $L/\eta \sim Re^{3/4}$, so [direct numerical simulation](/direct-numerical-simulation/) needs about $Re^{9/4}$ grid points and $Re^3$ work. The $k^{-5/3}$ spectrum is a scaling law with experimental support, not a theorem, and global regularity of the 3D Navier-Stokes equations is an open problem.
- [RANS](/reynolds-averaged-navier-stokes/) closures and [LES](/large-eddy-simulation/) subgrid models are models, not consequences of the equations: their constants are fitted to measured flows, they are judged against experiments and DNS, and none is right for all flows.
- The [lattice Boltzmann method](/lattice-boltzmann-method/) gives the Navier-Stokes equations at low Mach number with $\nu = (\tau - \tfrac12)/3$ in lattice units, with errors $O(\Delta x^2)$ and $O(\mathrm{Ma}^2)$. [Smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/) conserves mass and momentum exactly through symmetric pair forces, but particle disorder adds an error that does not shrink with the kernel width.

| Model | Unknowns added | Near a wall | Constants |
|---|---|---|---|
| [Mixing length](/mixing-length-model/) | none | $\ell_m = \kappa y$ with van Driest damping, $A^+ = 26$ | $\kappa = 0.41$ measured; $\ell_m$ prescribed per flow |
| [k-epsilon](/k-epsilon-model/) | $k$, $\varepsilon$ | not valid in the sublayer; [wall functions](/wall-functions/) or damping terms | $C_\mu = 0.09$, $C_1 = 1.44$, $C_2 = 1.92$, $\sigma_k = 1.0$, $\sigma_\varepsilon = 1.3$, fitted |
| [Wilcox k-omega](/k-omega-model/) | $k$, $\omega$ | integrated to the wall, no damping functions | $\alpha = 5/9$, $\beta = 3/40$, $\beta^* = 9/100$, $\sigma = \sigma^* = 1/2$, fitted |
| [k-omega SST](/k-omega-sst-model/) | $k$, $\omega$ | integrated to the wall | two blended sets; shear stress limiter $a_1 = 0.31$, fitted |
| [Spalart-Allmaras](/spalart-allmaras-model/) | $\tilde\nu$ | integrated to the wall, $\tilde\nu = 0$ | $c_{b1} = 0.1355$ fitted; $c_{w1} = 3.239$ derived from the log layer |
| [Smagorinsky](/smagorinsky-model/) (LES) | none | too large at walls; van Driest factor | $C_s \approx 0.17$ from Lilly's estimate, about 0.1 fitted in channel flow |
| [Dynamic](/dynamic-subgrid-model/) (LES) | none; a test filter | coefficient computed | none fitted; averaging and clipping are choices |

: Turbulence closures of the chapter. "Fitted" means calibrated against measured or simulated flows; derived constants hold only under the assumptions of their derivation.

## Choosing a method

For unsteady flow on a structured grid, the MAC grid with a projection step is the simplest correct choice; use the incremental form when the pressure at walls matters. Steady flow on unstructured finite volume meshes is the home of SIMPLE with Rhie-Chow interpolation, and PISO serves unsteady runs. For finite elements, pick an inf-sup stable pair first.

For interfaces where mass must not drift, use VOF with [PLIC](/piecewise-linear-interface-calculation/) and a balanced-force CSF; [front tracking](/front-tracking-method/) gives better curvature when topology changes are rare. Elastic bodies on a Cartesian grid call for the [immersed boundary method](/immersed-boundary-method/).

DNS is possible only at modest Reynolds numbers and serves as the reference for models. For engineering flows with walls, RANS is the usual choice: SST or Spalart-Allmaras integrated to the wall for aerodynamics, k-epsilon with wall functions on coarse grids with the first point at $30 \lesssim y^+ \lesssim 300$. LES costs much more but resolves the large eddies, which matters for mixing, noise and separation. Validate any turbulence model against measurements of a similar flow.

Lattice Boltzmann fits low-Mach flow in complex geometry such as porous media. SPH suits violent free surfaces and fragmentation; use [incompressible SPH](/incompressible-sph/) when the pressure matters.
