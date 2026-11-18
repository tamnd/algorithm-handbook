## What to remember

- Animation asks for plausible, controllable motion at large time steps, not for accuracy. Most methods here give up accuracy, energy or exact incompressibility to get it.
- On the MAC grid, divergence and gradient are compact central differences, and the pressure matrix has no checkerboard null space. The projection is orthogonal, so it never increases the kinetic energy.
- Stable fluids is stable for any $\Delta t$, because each semi-Lagrangian value is an interpolation of old values. It is first order and dissipative, with an effective viscosity of order $u\,\Delta x$, and it does not conserve the advected quantity.
- BFECC and the MacCormack variant make advection second order for smooth fields. Their linear amplification factors are $A(3 - |A|^2)/2$ and $A + \tfrac12(1 - |A|^2)$, both at most 1 in modulus when $|A| \le 1$. A limiter keeps values in the range of the stencil.
- The PIC transfer averages, so it never adds energy and loses a lot of it. FLIP adds only the change of the grid velocity: much less dissipation, but no energy bound and visible noise. APIC carries an affine velocity matrix and keeps angular momentum under the hypotheses of its paper.
- Weakly compressible SPH compresses by about $(v/c)^2$, about 1% with $c = 10\,v_{\max}$, and its step obeys $\Delta t \le 0.4\,h/(c + v_{\max})$. PCISPH, IISPH and DFSPH iterate on the pressure to a density error $\eta$ and take larger steps, but none of their loops has a general proof of convergence. Like position based fluids, all of them enforce incompressibility only approximately.
- Boussinesq buoyancy and vorticity confinement are forces added to a constant density flow. The first is linear in temperature and smoke density; the second adds energy and is tuned by eye.
- Gerstner waves, FFT synthesis and height field water animate a surface with no volume solver. FFT synthesis costs $O(N^2 \log N)$ per frame on an $N \times N$ patch and repeats with the patch.

## The main solvers compared

| Method | Velocity on | Incompressibility | Character |
|---|---|---|---|
| [Foster-Metaxas](/foster-metaxas-fluids/) | MAC grid | SOR sweeps to a tolerance | explicit; CFL and viscous step limits |
| [Stable fluids](/stable-fluids/) | grid | Poisson solve and projection | any step; first order, dissipative |
| [BFECC](/bfecc/) | grid | as stable fluids | second order; three plain steps |
| [MacCormack](/unconditionally-stable-maccormack/) | grid | as stable fluids | second order; two plain steps |
| [PIC](/particle-in-cell/) | particles and grid | grid projection | very dissipative |
| [FLIP](/fluid-implicit-particle/) | particles and grid | grid projection | little dissipation, noisy |
| [APIC](/affine-particle-in-cell/) | particles and grid | grid projection | little dissipation, less noise |
| [WCSPH](/weakly-compressible-sph/) | particles | about 1% compression | no solve; $\Delta t \le 0.4h/(c + v_{\max})$ |
| [PCISPH](/pcisph/) | particles | iterate to $\eta$, at least 3 passes | no convergence proof |
| [IISPH](/implicit-incompressible-sph/) | particles | relaxed Jacobi, $\omega = 1/2$ | clamped; no convergence proof |
| [DFSPH](/divergence-free-sph/) | particles | density and divergence solvers | no convergence proof |
| [PBF](/position-based-fluids/) | particles | fixed number of Jacobi passes | keeps linear, not angular momentum |

: Fluid solvers of the chapter. Grid costs are $\Theta(g)$ per pass and $O(gk)$ per pressure solve; particle costs are $O(n + q)$ per pass, with $q$ neighbor pairs.

In the swirl test of the APIC entry, after 40 steps PIC keeps 1.5% of the kinetic energy, the 0.95 blend 75%, FLIP 95% and APIC 98%, with noise of 0.0005, 0.069, 0.159 and 0.028 m/s.

## Choosing a method

For smoke and fire in a box, use stable fluids on a MAC grid with Boussinesq buoyancy. Add a sharper advection step or vorticity confinement when the smoke looks too smooth. For splashing liquids on a grid, FLIP with a small PIC share, about 0.95 to 0.99, is the common choice, and APIC when the noise of FLIP shows. Track the surface with a particle level set or rebuild it from the particles.

For particle liquids with many free droplets, choose an SPH solver. WCSPH is the simplest, but its steps are bound to the numerical speed of sound. IISPH or DFSPH allow much larger steps for the same density error. Position based fluids fit real time budgets where a fixed cost per frame matters more than the density error. For an open ocean seen from a distance, FFT synthesis is cheap and rich; for a pool that reacts to objects, use height field water; for a few stylized waves, Gerstner waves are enough.
