Start Burgers' equation $u_t + u u_x = 0$ with a smooth hump. Each point of the profile moves at its own height, so the top overtakes the foot ahead of it, the front steepens, and after a finite time the slope is infinite: a shock has formed, and the smooth solution has ended. The same happens in gas dynamics, in shallow water and in traffic. After that time only weak solutions exist, discontinuous functions that satisfy the conservation law in an integral sense, and they are not unique; an entropy condition picks the physical one, and the Rankine-Hugoniot conditions fix the speed of the jump.

Numerical methods must capture such jumps without smearing them over many cells or ringing around them. Two theorems frame the field. The Lax-Wendroff theorem says that a conservative, consistent scheme that converges converges to a weak solution, so conservation form matters. Godunov's order barrier says that a linear scheme that never creates new oscillations is at most first order, so accurate shock-capturing schemes must be nonlinear, adapting their stencils or limiting their slopes near discontinuities.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Theory.** Hyperbolic conservation laws, weak solutions, the Rankine-Hugoniot conditions, the Lax entropy condition, the Lax-Wendroff theorem and Godunov's order barrier theorem.
2. **Riemann solvers and fluxes.** The Euler equations of gas dynamics and their exact Riemann solver, the Roe solver with the Harten-Hyman entropy fix, the HLL and HLLC solvers, the Rusanov flux, flux vector splitting and the AUSM scheme.
3. **High-resolution schemes.** MUSCL, ENO and the piecewise parabolic method, the MacCormack method, the central schemes of Nessyahu-Tadmor and Kurganov-Tadmor, strong stability preserving Runge-Kutta methods, positivity-preserving limiters, entropy stable schemes and summation-by-parts operators.
4. **Discontinuous Galerkin and adaptivity.** The discontinuous Galerkin and Runge-Kutta discontinuous Galerkin methods, adaptive mesh refinement and the Berger-Colella method.
5. **Other systems and boundaries.** The shallow water equations with well-balanced schemes, the ghost fluid method, the Yee FDTD scheme for electromagnetics and the perfectly matched layer.

## What to read meanwhile

Volume 12 has the core of the subject already written. Start with the [advection equation](/advection-equation/), [Burgers' equation](/burgers-equation/) and the [Riemann problem](/riemann-problem/), then read the [finite volume method](/finite-volume-method/), the [upwind scheme](/upwind-scheme/), the [Lax-Friedrichs scheme](/lax-friedrichs-scheme/), the [Lax-Wendroff method](/lax-wendroff-method/) and [Godunov's method](/godunov-method/). The high-resolution ideas are there too: [total variation diminishing](/total-variation-diminishing/) schemes, [flux limiters](/flux-limiter-methods/) and the [WENO scheme](/weno-scheme/), with the [CFL condition](/courant-friedrichs-lewy-condition/) and [von Neumann stability analysis](/von-neumann-stability-analysis/) for the time step.

[Smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/) in Chapter 43.4 solves the Sod shock tube without a mesh and compares it with the exact Riemann solution.
