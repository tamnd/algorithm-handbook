Molecular simulation computes the properties of matter from the motion of its atoms. [Molecular dynamics](/molecular-dynamics/) integrates Newton's equations for every atom under a model of the potential energy, and averages over the trajectory give pressures, structures, diffusion constants and free energies. The method is simple to state and expensive to run. A bond vibration of hydrogen has a period of about 11 fs. The velocity Verlet method on a harmonic bond with that period shortens the period by 1.4% with a step of 1 fs, by 6% with 2 fs and by 17% with 3 fs, and it becomes unstable above $11/\pi = 3.5$ fs. A microsecond at 2 fs is $5 \times 10^8$ steps, each of which needs the forces on all atoms.

Most of this chapter answers the questions that follow from that cost. Forces must be cheap and accurate, so there are potentials of several kinds and fast methods for the long-range Coulomb sum. The step should be as long as stability allows, so there are constraints and multiple time steps. The run should sample the right ensemble at the right temperature and pressure, so there are thermostats and barostats. Some quantities, free energies above all, are not plain averages, and they need methods of their own.

## What the chapter covers

1. **Molecular dynamics in a box.** The [interatomic potential](/interatomic-potential/) and its standard pair form, the [Lennard-Jones potential](/lennard-jones-potential/). [Periodic boundary conditions](/periodic-boundary-conditions/) make a small box behave as bulk matter, and the [radial distribution function](/radial-distribution-function/) measures its structure. The [linked-cell list](/linked-cell-list/) and the [Verlet neighbour list](/verlet-neighbor-list/) find pairs within the cutoff in linear time. The [microcanonical](/microcanonical-ensemble/) and [canonical](/canonical-ensemble/) ensembles say what a run samples.
2. **Where the forces come from.** The [molecular mechanics force field](/molecular-mechanics-force-field/), the [embedded atom method](/embedded-atom-method/) for metals and the [Behler-Parrinello neural network potential](/behler-parrinello-potential/).
3. **Long-range electrostatics.** [Ewald summation](/ewald-summation/), [particle mesh Ewald](/particle-mesh-ewald/) and [smooth particle mesh Ewald](/smooth-particle-mesh-ewald/).
4. **Long runs, constraints and multiple steps.** The [shadow Hamiltonian theorem](/shadow-hamiltonian/), the constraint methods [SHAKE](/shake-constraint-algorithm/), [RATTLE](/rattle-algorithm/) and [LINCS](/lincs-algorithm/), and the multiple time steps of [RESPA](/respa-multiple-time-step/).
5. **Forces from the electrons.** [Born-Oppenheimer](/born-oppenheimer-molecular-dynamics/) and [Car-Parrinello](/car-parrinello-molecular-dynamics/) molecular dynamics.
6. **Thermostats, barostats and transport.** The [Andersen](/andersen-thermostat/), [Berendsen](/berendsen-thermostat/) and [stochastic velocity rescaling](/stochastic-velocity-rescaling/) thermostats, [Langevin dynamics](/langevin-dynamics/) with the [BAOAB integrator](/baoab-langevin-integrator/), [Brownian dynamics](/brownian-dynamics/), the [Nose-Hoover thermostat](/nose-hoover-thermostat/) and its [chains](/nose-hoover-chains/), the [Parrinello-Rahman barostat](/parrinello-rahman-barostat/) and the [Green-Kubo relations](/green-kubo-relations/).
7. **Free energy.** [Free energy perturbation](/free-energy-perturbation/), the [Bennett acceptance ratio](/bennett-acceptance-ratio/), [thermodynamic integration](/thermodynamic-integration/) and the [Jarzynski equality](/jarzynski-equality/). Along a [collective variable](/collective-variable/): [umbrella sampling](/umbrella-sampling/), the [weighted histogram analysis method](/weighted-histogram-analysis-method/) and [metadynamics](/metadynamics/).

## A first reading

Read these twelve entries in order:

1. [Molecular dynamics simulation](/molecular-dynamics/)
2. [Lennard-Jones potential](/lennard-jones-potential/)
3. [Periodic boundary conditions](/periodic-boundary-conditions/)
4. [Linked-cell list](/linked-cell-list/)
5. [Canonical ensemble](/canonical-ensemble/)
6. [Radial distribution function](/radial-distribution-function/)
7. [Molecular mechanics force field](/molecular-mechanics-force-field/)
8. [Ewald summation](/ewald-summation/)
9. [SHAKE constraint algorithm](/shake-constraint-algorithm/)
10. [Langevin dynamics](/langevin-dynamics/)
11. [Nose-Hoover thermostat](/nose-hoover-thermostat/)
12. [Free energy perturbation](/free-energy-perturbation/)

Together they give a working simulation of a liquid, with a thermostat and one free energy method.

Leave for later the electronic structure methods, the Behler-Parrinello potential, the shadow Hamiltonian theorem, BAOAB and the Nose-Hoover chains. Of the free energy methods, read thermodynamic integration and umbrella sampling next. Treat the Berendsen thermostat as a warning: it is widely used for equilibration, but it does not sample the canonical ensemble.

## Before you start

The chapter assumes the [Verlet method](/verlet-integration/), [Hamiltonian systems](/hamiltonian-systems/) and [symplectic integrators](/symplectic-integrators/) (Volume 12), and for the stochastic thermostats, [stochastic differential equations](/stochastic-differential-equation/) and the [Euler-Maruyama method](/euler-maruyama-method/) (Volume 12). The mesh Ewald methods use the [fast Fourier transform](/fast-fourier-transform/) (Volume 11) and [B-splines](/b-spline/) (Volume 28). The free energy methods draw on the [partition function](/partition-function/) (Volume 25), [importance sampling](/importance-sampling/) and [Markov chains](/markov-chain/) (Volume 17).

The [P3M method](/p3m-method/) of Chapter 43.1 treats gravity with the same splitting of short and long range as Ewald summation. Coarse-grained models, QM/MM and reaction paths are in Chapter 43.7, starting from [dissipative particle dynamics](/dissipative-particle-dynamics/), the [QM/MM method](/qm-mm-method/) and the [nudged elastic band](/nudged-elastic-band/).
