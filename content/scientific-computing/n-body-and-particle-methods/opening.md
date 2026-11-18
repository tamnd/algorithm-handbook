A galaxy simulation follows millions or billions of bodies, each pulled by the gravity of every other. Summing all the pairs costs $N(N-1)/2$ force evaluations per step, about $5 \times 10^{11}$ for a million bodies. The methods of this chapter cut that cost by treating distant groups of bodies as one. Barnes and Hut put the bodies in an octree and replace each far-away cell by its centre of mass, for $O(N \log N)$ work per step under the usual assumptions on the distribution. Greengard and Rokhlin's fast multipole method expands far fields in multipoles, translates them into local expansions, and reaches $O(N)$ for a fixed accuracy, with an error bound set by the truncation.

The same ideas serve in electrostatics, in plasma physics, where particles push charges through fields computed on a mesh, and in fluid and solid mechanics, where particles carry vorticity or material. The other half of the subject is time integration. Close encounters and eccentric orbits need small steps for a few bodies and large ones for the rest, and planetary systems over billions of years need symplectic methods that do not let the energy drift.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Direct and tree methods.** The gravitational N-body problem, direct N-body summation, gravitational softening, the Barnes-Hut algorithm, hashed oct-trees and the multipole acceptance criterion.
2. **Fast multipole methods.** Multipole expansions and their truncation error bound, the multipole-to-local translation, the fast multipole method and its adaptive, kernel-independent and black-box forms, and the fast Gauss transform.
3. **Particles and meshes.** The particle-mesh method with cloud-in-cell assignment, the particle-particle particle-mesh and TreePM methods, particle-in-cell plasma simulation, the Vlasov-Poisson system and the Boris pusher.
4. **Integrating orbits.** The fourth-order Hermite integrator, block time steps, the Wisdom-Holman integrator and Kustaanheimo-Stiefel regularization.
5. **Particles for continua and analysis.** The vortex particle method and particle strength exchange, the material point method and its generalized interpolation form, and the friends-of-friends algorithm for finding groups.

## What to read meanwhile

The trees are in Volume 3: the [octree](/octree/), the [quadtree](/quadtree/) and the [k-d tree](/kd-tree/), with [space-filling curves](/space-filling-curve/) such as the [Z-order curve](/z-order-curve/) for hashed trees. Particle-mesh methods solve the [Poisson equation](/poisson-equation/) (Volume 12) with the [fast Fourier transform](/fast-fourier-transform/) (Volume 11). Short-range forces need the pairs within a cutoff, the [fixed-radius near neighbors](/fixed-radius-near-neighbors/) problem of Volume 5.

For the integrators, read [Verlet integration](/verlet-integration/), [symplectic integrators](/symplectic-integrators/) and [Hamiltonian systems](/hamiltonian-systems/) in Volume 12, and [molecular dynamics](/molecular-dynamics/) in Chapter 43.2, which applies them to atoms. [Smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/) in Chapter 43.4 is a particle method for fluids, and friends-of-friends groups are the clusters of [single-linkage clustering](/single-linkage-clustering/) (Volume 25) at a fixed linking length.
