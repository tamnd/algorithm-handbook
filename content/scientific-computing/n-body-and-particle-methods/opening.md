Put $N = 300$ bodies at random in a cube and compute the gravity on each one. The direct way visits all $N(N-1)/2 = 44850$ pairs, and its forces are exact up to rounding. The Barnes-Hut tree replaces each distant group of bodies by its centre of mass. On these bodies, with the opening angle $\theta = 0.5$, it computes 34319 body-cell interactions in place of the $N(N-1) = 89700$ body-body ones, with a median relative force error of $5.7 \times 10^{-3}$; with $\theta = 1$ it needs only 10417, and the error grows to $4 \times 10^{-2}$. At $N = 300$ the saving is small. At $N = 10^6$ the direct sum has $5 \times 10^{11}$ pairs per step, while the tree needs $O(N \log N)$ work for typical distributions. Every fast method of this chapter makes that same trade: a controlled error for a lower cost.

The chapter is about systems of many particles that act on each other through a long-range field, gravity or the Coulomb force, and about the particle methods that grew from them. Its methods fall into three families. Trees and multipole expansions approximate the far field of groups of particles. Meshes solve for the field with the fast Fourier transform. Special time integrators follow orbits for a long time. The same ideas then serve plasmas, vortex flows and deforming solids.

## What the chapter covers

1. **The problem and the exact sum.** The [gravitational N-body problem](/gravitational-n-body-problem/) is a system of $6N$ ordinary differential equations that conserves energy, momentum and angular momentum. [Direct summation](/direct-n-body-summation/) computes the forces in $\Theta(N^2)$ time, and [gravitational softening](/gravitational-softening/) bounds the force at short range.
2. **Trees and multipole expansions.** The [multipole expansion](/multipole-expansion/) and its [truncation error bound](/multipole-truncation-error-bound/) say how far a group must be. The [multipole acceptance criterion](/multipole-acceptance-criterion/) decides it in a tree, the [Barnes-Hut algorithm](/barnes-hut-algorithm/) uses it, and the [hashed oct-tree](/hashed-oct-tree/) stores the tree without pointers.
3. **The fast multipole method.** The [multipole-to-local translation](/multipole-to-local-translation/) is the core of the [fast multipole method](/fast-multipole-method/), which runs in $O(N)$ time for a fixed accuracy. The [adaptive FMM](/adaptive-fast-multipole-method/) handles clustered bodies, the [kernel-independent FMM](/kernel-independent-fast-multipole-method/) and the [black-box FMM](/black-box-fast-multipole-method/) avoid analytic expansions, and the [fast Gauss transform](/fast-gauss-transform/) applies the idea to the Gaussian kernel.
4. **Fields on a mesh.** [Cloud-in-cell assignment](/cloud-in-cell-assignment/) spreads mass to a grid for the [particle-mesh method](/particle-mesh-method/). The [P3M method](/p3m-method/) and the [TreePM method](/treepm-method/) add short-range sums, and the [friends-of-friends algorithm](/friends-of-friends-algorithm/) finds halos in the results.
5. **Plasmas.** The [Vlasov-Poisson system](/vlasov-poisson-system/) is the model, the [Boris pusher](/boris-pusher/) moves the charges, and [particle-in-cell](/plasma-particle-in-cell/) codes sample the model with it.
6. **Time steps for gravitating bodies.** The [Hermite integrator](/hermite-n-body-integrator/) with [block time steps](/block-time-steps/) serves star clusters, the [Wisdom-Holman integrator](/wisdom-holman-integrator/) serves planetary systems, and [Kustaanheimo-Stiefel regularization](/kustaanheimo-stiefel-regularization/) treats close binaries.
7. **Particles in continua.** The [vortex particle method](/vortex-particle-method/) with [particle strength exchange](/particle-strength-exchange/) simulates incompressible flow, and the [material point method](/material-point-method/) with [GIMP](/generalized-interpolation-material-point/) simulates large deformations of solids.

## A first reading

Read these fourteen entries in order:

1. [Gravitational N-body problem](/gravitational-n-body-problem/)
2. [Direct N-body summation](/direct-n-body-summation/)
3. [Gravitational softening](/gravitational-softening/)
4. [Multipole expansion](/multipole-expansion/)
5. [Multipole acceptance criterion](/multipole-acceptance-criterion/)
6. [Barnes-Hut algorithm](/barnes-hut-algorithm/)
7. [Fast multipole method](/fast-multipole-method/)
8. [Cloud-in-cell assignment](/cloud-in-cell-assignment/)
9. [Particle-mesh method](/particle-mesh-method/)
10. [P3M method](/p3m-method/)
11. [Boris pusher](/boris-pusher/)
12. [Plasma particle-in-cell](/plasma-particle-in-cell/)
13. [Hermite N-body integrator](/hermite-n-body-integrator/)
14. [Wisdom-Holman integrator](/wisdom-holman-integrator/)

The truncation bound and the multipole-to-local translation can wait until the fast multipole method is clear. Skip at first the hashed oct-tree, the kernel-independent and black-box variants and the fast Gauss transform. Block time steps and Kustaanheimo-Stiefel regularization matter only for collisional systems such as star clusters. The last group stands apart and can be read on its own after the mesh group.

## Before you start

The chapter integrates [initial value problems](/ode-initial-value-problem/) for [Hamiltonian systems](/hamiltonian-systems/), and it relies on [symplectic integrators](/symplectic-integrators/) such as [Verlet integration](/verlet-integration/), all in Volume 12. The mesh methods solve the [Poisson equation](/poisson-equation/) (Volume 12) with the [fast Fourier transform](/fast-fourier-transform/) (Volume 11). The expansions use [Legendre polynomials](/legendre-polynomials/), [Lagrange interpolation](/lagrange-interpolation/) and [Chebyshev interpolation](/chebyshev-interpolation/) from Volume 12. The trees are the [octree](/octree/) and the [quadtree](/quadtree/) of Volume 3, with the [Z-order curve](/z-order-curve/) and a [hash table](/hash-table/); friends-of-friends uses the [disjoint-set](/disjoint-set/) structure of Volume 3 to find [connected components](/connected-components/) (Volume 7). The P3M method splits the force as in [Ewald summation](/ewald-summation/) from Chapter 43.2. The vortex group assumes the [Navier-Stokes equations](/navier-stokes-equations/) and the material point method the [finite element method](/finite-element-method/), both in Volume 12; [smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/), a related particle method for fluids, is in Chapter 43.4.
