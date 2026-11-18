A simulation of a small protein in a box of water follows about 25,000 atoms. At each time step the program computes the force on every atom from the atoms near it, then moves all of them a little, and the step must be about 2 femtoseconds or the fastest bond vibrations make the motion unstable. One microsecond of the protein's life therefore takes 500 million steps. Whether such a run is worth doing depends on choices that are algorithmic: which pairs of atoms to visit, which integrator to use so that the energy does not drift over those millions of steps, and how to treat the long-range electric forces. This volume collects the methods that turn the laws of physics into programs of that kind, for atoms, stars, fluids, solids, neutrons and weather, and the methods that ask how far the answers can be trusted.

The volume has nine chapters. In this edition two of them are partly written: Chapter 43.2, on molecular simulation, with 1 entry, and Chapter 43.4, on incompressible flow and turbulence, with 2 entries. The other seven chapters are not written yet; each has an opening page that says what it will cover and what to read meanwhile.

## Why scientific computing gets a volume of its own

The numerical methods of Volume 12 solve equations. The methods here solve problems from science, where the equations are only part of the work.

- **The discrete model must keep the physics.** A scheme that conserves mass, momentum or energy exactly, or keeps a symplectic structure, can be run for millions of steps; one that does not may drift far from the truth while every single step looks accurate.
- **Cost is set by interactions.** Forces between all pairs of N particles cost $O(N^2)$ per step. Cutoffs with neighbour lists, trees and multipole expansions bring this down, and each has its own error to control.
- **Scales are far apart.** Bond vibrations take femtoseconds and proteins fold in microseconds or longer; atoms in a crack and the stress in the whole part differ by many orders of magnitude in length. Many methods exist to bridge such gaps.
- **The answer has several errors.** Discretization error, sampling error, model error and uncertain inputs all enter the result, and uncertainty quantification and data assimilation measure and reduce them.

## The chapters

**Chapter 43.1, N-body and particle methods**, is not written yet. It will cover direct summation and the Barnes-Hut tree method, the fast multipole method, particle-mesh and particle-in-cell methods, orbit integrators and particle methods for continua. Meanwhile, read the [octree](/octree/) in Volume 3, the [fast Fourier transform](/fast-fourier-transform/) in Volume 11 and [symplectic integrators](/symplectic-integrators/) in Volume 12.

**Chapter 43.2, Molecular simulation**, is written in part. [Molecular dynamics](/molecular-dynamics/) integrates Newton's equations for atoms under a force field with the velocity Verlet method, one force evaluation per step, and explains the time step limit, cutoffs, neighbour lists and the cost of a run. The planned entries cover potentials, long-range electrostatics, thermostats and barostats, constraints, free energy methods and ab initio dynamics.

**Chapter 43.3, Conservation laws and shock capturing**, is not written yet. It will cover the theory of hyperbolic conservation laws, Riemann solvers and numerical fluxes, high-resolution schemes, discontinuous Galerkin methods and adaptive mesh refinement. Meanwhile, read the [Riemann problem](/riemann-problem/), [Godunov's method](/godunov-method/) and the [WENO scheme](/weno-scheme/) in Volume 12.

**Chapter 43.4, Incompressible flow and turbulence**, is written in part. The [lattice Boltzmann method](/lattice-boltzmann-method/) moves particle populations on a lattice, relaxing them toward a local equilibrium and streaming them to the neighbours, and recovers the Navier-Stokes equations at low Mach number. [Smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/) follows the fluid with particles and computes density and forces from kernel-weighted sums over neighbours. The planned entries cover projection methods, turbulence models and interfaces.

**Chapter 43.5, Finite element practice**, is not written yet. It will cover the weak formulation and the error theory, assembly of elements, mixed and nonstandard methods, adaptivity with error estimators, and time stepping for structures. Meanwhile, read the [finite element method](/finite-element-method/) and the [Galerkin method](/galerkin-method/) in Volume 12 and [Delaunay refinement](/delaunay-refinement/) in Volume 13.

**Chapter 43.6, Particle transport**, is not written yet. It will cover the transport equation, Monte Carlo transport, variance reduction and the deterministic discrete ordinates methods. Meanwhile, read [importance sampling](/importance-sampling/) in Volume 17 and [volumetric path tracing](/volumetric-path-tracing/) in Volume 28.

**Chapter 43.7, Multiscale methods**, is not written yet. It will cover the coupling of atoms with continua, homogenization, coarse-graining, and rare events with accelerated dynamics. Meanwhile, read the [Gillespie algorithm](/gillespie-algorithm/) in Volume 27 and its entry on [minima and barriers of an energy surface](/energy-landscape/).

**Chapter 43.8, Uncertainty quantification**, is not written yet. It will cover forward propagation with multilevel Monte Carlo, polynomial chaos, Sobol sensitivity indices, Bayesian calibration and reduced-order models. Meanwhile, read [quasi-Monte Carlo integration](/quasi-monte-carlo-integration/) in Volume 12 and [Gaussian processes](/gaussian-process/) in Volume 25.

**Chapter 43.9, Data assimilation**, is not written yet. It will cover variational assimilation, ensemble Kalman filters, hybrid methods and particle filters in high dimension. Meanwhile, read the [Kalman filter](/kalman-filter/) in Volume 28, the [particle filter](/particle-filter/) in Volume 25 and [adjoint sensitivity analysis](/adjoint-sensitivity-analysis/) in Volume 32.

## How to read this volume

There is no course through the volume yet. Read Chapter 43.2 in the order its opening page gives, then Chapter 43.4, and do the exercises marked ◦ at the end of each. For each other chapter, its opening page lists written entries elsewhere that cover part of its ground.

Each entry stands on its own; its facts box lists what it needs, by entry number.

## What you need first

From Volume 12 you need [Verlet integration](/verlet-integration/) and [Hamiltonian systems](/hamiltonian-systems/) for Chapter 43.2, and the [Navier-Stokes equations](/navier-stokes-equations/), the [heat equation](/heat-equation/) and the [finite difference method](/finite-difference-method/) for Chapter 43.4. Molecular dynamics takes its forces from the [energy function](/energy-function/) of Volume 27, and both particle methods find their neighbours with [fixed-radius near neighbors](/fixed-radius-near-neighbors/) from Volume 5.

## The exercises

Chapters 43.2 and 43.4 end with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
