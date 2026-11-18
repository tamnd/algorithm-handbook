A neutron enters a slab of concrete. It flies a random distance, with an exponential distribution whose mean is the mean free path, hits a nucleus, and is absorbed or scattered in a new direction with a new energy; then it flies again. A Monte Carlo code follows millions of such histories and counts how many get through. When the answer is one in a billion, as for a thick reactor shield, almost every history is wasted, and the method lives on variance reduction: splitting particles that move toward the region of interest, killing most of those that move away while raising the weight of the survivors, with rules taken from the solution of an adjoint problem.

The quantity behind all this is the angular flux, which obeys the linear Boltzmann transport equation in position, direction and energy, six or seven dimensions in all. Deterministic methods discretize those variables instead of sampling them: discrete ordinates in angle, multigroup in energy, and sweeps through the mesh along each direction. Their basic iteration converges slowly when scattering dominates, and diffusion synthetic acceleration repairs that. Reactor physics adds an eigenvalue problem, whose eigenvalue $k$ says whether a chain reaction grows or dies out. The same equations describe photons in medical physics, radiation in stars, and light in a rendered scene.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The equation.** The linear Boltzmann transport equation, the k-eigenvalue problem, the multigroup energy approximation and the diffusion approximation of transport.
2. **Monte Carlo transport.** Analog Monte Carlo particle transport, free-flight distance sampling, Kahn's method for Compton scattering, collision and track-length estimators, the condensed history method, Monte Carlo criticality calculations with the Shannon entropy of the fission source, implicit Monte Carlo and direct simulation Monte Carlo.
3. **Variance reduction.** Implicit capture, particle splitting, weight windows, the exponential transform, the adjoint flux as an importance function, and the CADIS and forward-weighted CADIS methods.
4. **Deterministic methods.** The discrete ordinates method, transport sweeps, source iteration and diffusion synthetic acceleration, the spherical harmonics method and the method of characteristics.

## What to read meanwhile

The sampling tools are written in Volume 17: [inverse transform sampling](/inverse-transform-sampling/) for free-flight distances, [rejection sampling](/rejection-sampling/), the [alias method](/alias-method/) and [importance sampling](/importance-sampling/), with [Monte Carlo integration](/monte-carlo-integration/) in Volume 12 for the error estimates. Light transport in Volume 28 is the same problem for photons: read [path tracing](/path-tracing/), [volumetric path tracing](/volumetric-path-tracing/), [Russian roulette](/russian-roulette/) and [multiple importance sampling](/multiple-importance-sampling/).

The k-eigenvalue is computed by [power iteration](/power-iteration/) (Volume 12), and source iteration is a stationary iteration of the same family as the [Jacobi method](/jacobi-method/) and the [Gauss-Seidel method](/gauss-seidel-method/). The angular quadratures of discrete ordinates build on [Gaussian quadrature](/gaussian-quadrature/).
