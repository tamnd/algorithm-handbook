## What to remember

- Molecular dynamics integrates Newton's equations with velocity Verlet, one force evaluation per step. The fastest motion sets the step, about 1 fs for bonds to hydrogen and 2 fs once they are constrained.
- The method is symplectic, so it follows a shadow Hamiltonian that differs from the true one by $O(h^2)$, and the energy error stays bounded over very long runs instead of drifting.
- Periodic boundary conditions with the minimum image stand in for bulk matter. Cell lists and Verlet lists find the pairs within a cutoff in $O(N)$ time.
- The Coulomb sum of a periodic system needs Ewald summation or a mesh variant. Particle mesh Ewald and its smooth form cost $O(N \log N)$ per step.
- Plain dynamics samples the microcanonical ensemble at best. A thermostat is canonical only if its theory says so: Andersen, Langevin, stochastic velocity rescaling and Nose-Hoover (when the dynamics is ergodic) are, and Berendsen is not.
- Constraints remove the fastest vibrations. SHAKE and RATTLE iterate one bond at a time, and LINCS solves a matrix series that suits parallel machines.
- Free energy differences are logarithms of ratios of partition functions. They need overlap between the states compared, or a path of intermediate states, or a bias along a collective variable.
- The choice of potential decides what can be simulated. Pair potentials miss the many-body physics of metals, fixed force fields cannot break bonds, and electronic structure costs orders of magnitude more per step.

| Thermostat | Canonical | Ergodicity | Effect on dynamics |
|---|---|---|---|
| Andersen | yes | from the collisions | destroys velocity memory; $D = k_B T/(m\nu)$ for a free particle |
| Berendsen | no | not relevant | smooth; kinetic energy fluctuations too small |
| Stochastic velocity rescaling | yes | needs the dynamics to mix velocity directions | small for usual $\tau$ |
| Langevin, BAOAB | yes, up to the step error | proved for $\gamma > 0$ | friction slows diffusion as $\gamma$ grows |
| Nose-Hoover | yes, if ergodic | fails for one oscillator | deterministic, time-reversible |
| Nose-Hoover chains | yes, if ergodic | measured, not proved | deterministic, time-reversible |

: Thermostats of the chapter. "Canonical" means that the exact dynamics samples the canonical ensemble; the entries give the conditions.

## Choosing a method

For a first simulation of a liquid, use velocity Verlet with a cutoff, a cell or Verlet list, and periodic boundaries. Add smooth particle mesh Ewald as soon as there are charges, since a plain cutoff on Coulomb forces gives wrong structure and wrong energies. Constrain the bonds to hydrogen with SHAKE, RATTLE or LINCS and use a 2 fs step. RESPA can lengthen the step for the slow forces further, but resonance limits the outer step to about a third of the fastest period.

Equilibrate with Berendsen if you like, then switch. For production, stochastic velocity rescaling and Nose-Hoover chains change the dynamics little, which matters for diffusion and other transport coefficients computed by Green-Kubo integrals. Langevin dynamics, best with the BAOAB splitting, is the most robust sampler, and it is the right model when a solvent is left out; at high friction it becomes Brownian dynamics. Andersen collisions suit small systems but ruin the dynamics. Run at constant pressure with Parrinello-Rahman and a thermostat when the box shape can change.

For free energies between two states, use the Bennett acceptance ratio when samples of both states exist, and thermodynamic integration or a chain of perturbation windows when the states are far apart. Free energy perturbation in one direction is reliable only when the distributions overlap well. For a profile along one or two collective variables, use umbrella sampling with WHAM, or well-tempered metadynamics when the windows cannot be placed in advance. Nonequilibrium work and the Jarzynski equality suit pulling experiments, but the exponential average converges slowly when the dissipated work is large. When bonds break, the forces must come from Born-Oppenheimer or Car-Parrinello dynamics, or from a neural network potential trained on such calculations.
