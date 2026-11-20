A neutron enters a slab of concrete. It flies a random distance, hits a nucleus, and is absorbed or scattered into a new direction with a new energy; then it flies again. The flight lengths follow an exponential law whose mean is the mean free path, and the outcome of each collision follows the cross sections of the material. Particle transport is the computation of what such random walks do on average: how many neutrons get through a reactor shield, how much dose a photon beam leaves in a tumour, whether a lattice of fuel rods keeps a chain reaction going, how heat moves as radiation through a hot plasma.

There are two ways to compute it. Monte Carlo follows the walks themselves, one history at a time, and counts the events of interest. Its answer carries a statistical error that falls like one over the square root of the number of histories, and when the event is rare, as for a thick shield, most histories are wasted unless the game is biased toward the event and the weights are corrected. Deterministic methods discretize the angular flux, the quantity that the linear Boltzmann equation governs, in position, direction and energy, and solve the resulting large linear systems by sweeps and iterations. Each approach has a known weakness: variance for Monte Carlo, ray effects and slow iterations for discrete ordinates. Much of this chapter is about those weaknesses and their repairs.

## What the chapter covers

1. **The transport equation and its approximations.** The [linear Boltzmann transport equation](/linear-boltzmann-transport-equation/), the [diffusion approximation](/diffusion-approximation-of-transport/) that holds where scattering dominates, the [multigroup approximation](/multigroup-approximation/) in energy, the [k-eigenvalue problem](/k-eigenvalue-problem/) of reactor physics, and the [adjoint flux as importance](/adjoint-importance-function/).
2. **Monte Carlo transport.** [Free-flight sampling](/free-flight-sampling/), the [analog random walk](/analog-monte-carlo-transport/), the [collision](/collision-estimator/) and [track-length](/track-length-estimator/) estimators of the flux, [Kahn's method](/kahn-compton-sampling/) for Compton scattering, and the [condensed history method](/condensed-history-method/) for electrons.
3. **Variance reduction.** [Implicit capture](/implicit-capture/), [splitting and roulette](/particle-splitting/), the [weight window](/weight-window/) that combines them, and the [exponential transform](/exponential-transform/) for deep penetration.
4. **Criticality.** [Monte Carlo criticality calculation](/monte-carlo-criticality/) as power iteration on fission generations, and the [Shannon entropy of the fission source](/fission-source-entropy/) as a check of source convergence.
5. **Deterministic transport.** The [discrete ordinates method](/discrete-ordinates-method/), the [transport sweep](/transport-sweep/), [source iteration](/source-iteration/) and its repair by [diffusion synthetic acceleration](/diffusion-synthetic-acceleration/), the [spherical harmonics method](/spherical-harmonics-method/), and the [method of characteristics](/method-of-characteristics-transport/) for reactor lattices.
6. **Hybrid methods.** [CADIS](/cadis/) builds a biased source and weight windows from a deterministic adjoint for one tally, and [FW-CADIS](/fw-cadis/) does the same for a whole mesh of tallies.
7. **Thermal radiation and rarefied gas.** [Implicit Monte Carlo](/implicit-monte-carlo/) for radiation coupled to a material, and [direct simulation Monte Carlo](/direct-simulation-monte-carlo/) for a dilute gas, a nonlinear problem that shares the free flights and sampled collisions.

## A first reading

Read these in order:

1. [Linear Boltzmann transport equation](/linear-boltzmann-transport-equation/)
2. [Free-flight distance sampling](/free-flight-sampling/)
3. [Analog Monte Carlo particle transport](/analog-monte-carlo-transport/)
4. [Track-length estimator](/track-length-estimator/)
5. [Implicit capture](/implicit-capture/)
6. [Particle splitting](/particle-splitting/)
7. [Diffusion approximation of transport](/diffusion-approximation-of-transport/)
8. [Discrete ordinates method](/discrete-ordinates-method/)
9. [Source iteration](/source-iteration/)
10. [k-eigenvalue problem](/k-eigenvalue-problem/)
11. [Monte Carlo criticality calculation](/monte-carlo-criticality/)

After these, the weight window, the adjoint and CADIS form one thread, and diffusion synthetic acceleration the other. The photon and electron entries (Kahn's method, condensed history), the exponential transform, implicit Monte Carlo and direct simulation Monte Carlo can wait until you need them.

## Before you start

The chapter uses probability and sampling from Volume 17: [inverse transform sampling](/inverse-transform-sampling/), [rejection sampling](/rejection-sampling/) and [importance sampling](/importance-sampling/), and [Monte Carlo integration](/monte-carlo-integration/) from Volume 12. [Russian roulette](/russian-roulette/) and [delta tracking](/delta-tracking/) come from rendering in Volume 28, where [volumetric path tracing](/volumetric-path-tracing/) solves the same equation for light. The deterministic side needs the [advection equation](/advection-equation/), the [heat equation](/heat-equation/), the [upwind scheme](/upwind-scheme/), [Gauss-Legendre quadrature](/gauss-legendre-quadrature/), [fixed-point iteration](/fixed-point-iteration/) and [power iteration](/power-iteration/) from Volume 12, and the [topological sort](/topological-sort/) from Volume 7. The fission source entropy uses [Shannon entropy](/shannon-entropy/) from Volume 24.

No physics beyond the idea of a cross section is assumed: $\Sigma_t$ is the probability of a collision per unit path length, and it splits into the absorption part $\Sigma_a$ and the scattering part $\Sigma_s$. Their ratio $c = \Sigma_s/\Sigma_t$, the scattering ratio, decides the behaviour of almost every method in the chapter.
