Molecular dynamics resolves the vibration of atoms with steps of a femtosecond, but a metal part fails over hours and a protein binds a drug over milliseconds. A finite element model of the part treats the metal as a continuum, which is accurate far from a crack and wrong at its tip, where individual bonds break. One model is too expensive, the other too crude. Multiscale methods couple them, using the fine model only where or when it is needed and passing information between the scales.

There are two broad strategies. Concurrent methods run both models at once on different parts of the domain: atoms near the crack tip, a continuum elsewhere, or a quantum model for a reactive site inside a classical one. Sequential methods compute effective parameters from the fine model and hand them to the coarse one: homogenized material constants from a periodic microstructure, or a coarse-grained force field fitted to atomistic data. A third family attacks time scales. Rare events, such as a vacancy hopping in a crystal, happen once in billions of vibrations, and methods built on transition state theory find the saddle points and the rates, then jump from event to event by kinetic Monte Carlo.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Coupling atoms and continua.** Multiscale modeling in general, the Cauchy-Born rule, the quasicontinuum method, QM/MM methods and peridynamics.
2. **Homogenization and upscaling.** Periodic homogenization and two-scale convergence, representative volume elements and the FE2 method, multiscale finite elements, localized orthogonal decomposition, the variational multiscale method, the heterogeneous multiscale method and coarse projective integration.
3. **Coarse-graining.** The Mori-Zwanzig formalism, coarse-graining by force matching, iterative Boltzmann inversion, dissipative particle dynamics and phase-field models.
4. **Rare events and long times.** Harmonic transition state theory, kinetic Monte Carlo, the nudged elastic band, string and dimer methods, transition path sampling, forward flux sampling, and the accelerated dynamics methods: hyperdynamics, parallel replica dynamics and temperature accelerated dynamics.

## What to read meanwhile

The two ends of the scale are written. [Molecular dynamics](/molecular-dynamics/) in Chapter 43.2 is the fine model, and the [finite element method](/finite-element-method/) of Volume 12 is the coarse one; read [Hamiltonian systems](/hamiltonian-systems/) and [stochastic differential equations](/stochastic-differential-equation/) with the [Euler-Maruyama method](/euler-maruyama-method/) in Volume 12 for the dynamics in between.

For rare events and stochastic jumps, the [Gillespie algorithm](/gillespie-algorithm/) of Volume 27 is kinetic Monte Carlo for chemical reactions, and the [chemical Langevin equation](/chemical-langevin-equation/) is its continuous approximation. The Volume 27 entry on [energy minima and barriers](/energy-landscape/) shows what transition state theory works with, and [parallel tempering](/parallel-tempering/) in Volume 17 is one way to cross barriers when only equilibrium sampling is needed.
