## History

Molecular dynamics began at Livermore in 1957, when Berni Alder and Thomas Wainwright followed systems of up to a hundred or so hard spheres on an early computer and found a phase transition between a fluid and a solid. Hard spheres move in straight lines between collisions, so their simulation is a sequence of collision events. Aneesur Rahman simulated liquid argon in 1964 with a continuous Lennard-Jones potential, integrating the equations of motion in fixed time steps, and compared his results with neutron scattering data.

Loup Verlet's paper of 1967 introduced the integrator that carries his name, in its position form, together with a list of the neighbours of each atom that was rebuilt every few steps, the device that made his runs on a Lennard-Jones fluid affordable. William Swope, Hans Andersen, Peter Berens and Kent Wilson wrote the velocity form in 1982. The reasons for its good long-time behaviour, symplecticity and backward error analysis, were understood later, in the numerical analysis of Hamiltonian systems of the 1980s and 1990s.

The first protein was simulated by Andrew McCammon, Bruce Gelin and Martin Karplus in 1977: the bovine pancreatic trypsin inhibitor, for a few picoseconds in vacuum. Yong Duan and Peter Kollman reached one microsecond for the villin headpiece in water in 1998. David Shaw's group built the special-purpose machine Anton and reported millisecond runs in 2010, and in 2011 Kresten Lindorff-Larsen, Stefano Piana, Ron Dror and Shaw folded twelve small proteins in long equilibrium simulations. Karplus, Michael Levitt and Arieh Warshel shared the 2013 Nobel Prize in Chemistry for multiscale models of complex chemical systems.

## Further reading

- Daan Frenkel and Berend Smit, *Understanding Molecular Simulation: From Algorithms to Applications*, second edition, Academic Press, 2002. The standard course on molecular dynamics and Monte Carlo, with ensembles and free energies.
- Michael P. Allen and Dominic J. Tildesley, *Computer Simulation of Liquids*, second edition, Oxford University Press, 2017. The classic text, with periodic boundaries, neighbour lists and long-range forces in detail.
- Benedict Leimkuhler and Charles Matthews, *Molecular Dynamics: With Deterministic and Stochastic Numerical Methods*, Springer, 2015. The integrators from the point of view of numerical analysis, including Langevin dynamics.
- Ernst Hairer, Christian Lubich and Gerhard Wanner, *Geometric Numerical Integration*, second edition, Springer, 2006. The theory behind symplectic methods and backward error analysis.
