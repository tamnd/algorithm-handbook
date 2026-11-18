Cover a domain with triangles and look for the solution of the Poisson equation among functions that are linear on each triangle and continuous across edges. The weak form of the equation turns into a sparse linear system with one unknown per vertex, assembled triangle by triangle from small element matrices. Céa's lemma then says that the computed solution is, up to a constant, the best approximation from the chosen space in the $H^1$ norm, so for a smooth solution the error falls in proportion to the mesh size. The finite element method is this idea carried to elasticity, heat flow, electromagnetics and fluids, on meshes that follow any geometry.

Practice is where the method gets hard. Some pairs of spaces fail: for incompressible flow and nearly incompressible solids, a careless choice of elements locks or produces spurious pressures, and the inf-sup condition says which pairs work. Singularities at corners and cracks spoil the convergence rate unless the mesh is refined where the error is large, which needs error estimators computed from the solution itself. And dynamics, plasticity and buckling bring their own time integrators and nonlinear solvers.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Foundations.** The weak formulation, Sobolev spaces, the Lax-Milgram theorem, Céa's lemma, the Bramble-Hilbert lemma and the Ciarlet definition of a finite element.
2. **Building and assembling elements.** Lagrange elements and isoparametric mappings, finite element assembly, static condensation, mass lumping, the patch test and locking.
3. **Mixed and nonstandard methods.** Mixed finite elements and the Babuška-Brezzi inf-sup condition, the Taylor-Hood, Raviart-Thomas and Nédélec elements, Nitsche's method, the symmetric interior penalty and hybridizable discontinuous Galerkin methods, streamline upwind Petrov-Galerkin and the virtual element method.
4. **Adaptivity.** Residual-based and Zienkiewicz-Zhu error estimators, the dual weighted residual method, Dörfler marking, newest vertex bisection, the optimality of adaptive finite element methods, hp finite elements and spectral elements.
5. **Dynamics, nonlinearity and other discretizations.** The Newmark-beta and generalized-alpha methods, the return mapping algorithm for plasticity, the arc-length method, and the boundary element, element-free Galerkin and extended finite element methods.

## What to read meanwhile

The method itself is written in Volume 12: read the [finite element method](/finite-element-method/) and the [Galerkin method](/galerkin-method/), with the [Poisson equation](/poisson-equation/) as the model problem and [spectral methods](/spectral-methods/) for the high-order end. The linear systems are solved by the [conjugate gradient method](/conjugate-gradient-method/), [GMRES](/gmres/) and the [multigrid method](/multigrid-method/), also in Volume 12.

Meshes come from Volume 13: [mesh generation](/mesh-generation/), the [Delaunay triangulation](/delaunay-triangulation/) and [Delaunay refinement](/delaunay-refinement/), which gives triangles with a lower bound on their angles, the shape regularity that the error estimates need.
