The [finite element method](/finite-element-method/) turns a partial differential equation on a complicated domain into a sparse linear system. Its idea fits in one line: write the problem in weak form, pick a space of piecewise polynomials on a mesh, and ask that the equation hold against every function of that space. This chapter is about everything between that line and a working code that gives answers you can trust. It covers the theory that says when the discrete problem has a solution and how close it is, the elements and the assembly loop, the things that go wrong, and the methods that fix them.

Two examples show the range. A car body in a crash is a thin shell of steel that bends, yields and buckles. A simulation needs elements that do not lock in bending, a return mapping for plasticity at every quadrature point, and a time stepper for millions of unknowns. Groundwater flow through layered rock is a Darcy problem whose flux matters more than the pressure. A mixed method with Raviart-Thomas fluxes conserves mass on every cell, and an adaptive mesh puts the unknowns near the wells.

## What the chapter covers

1. **Weak problems and their spaces.** The [weak formulation](/weak-formulation/) poses the problem in a [Sobolev space](/sobolev-space/). The [Lax-Milgram theorem](/lax-milgram-theorem/) gives existence and uniqueness, and [Céa's lemma](/cea-lemma/) bounds the Galerkin error by the best approximation error times $M/\alpha$.
2. **Elements and assembly.** The [Lagrange elements](/lagrange-finite-element/) and the [Ciarlet definition](/ciarlet-finite-element/) of an element in general. Then [assembly](/finite-element-assembly/) of the global matrix, [isoparametric maps](/isoparametric-mapping/) for curved cells, the [patch test](/patch-test/), [static condensation](/static-condensation/), [mass lumping](/mass-lumping/), and the [Bramble-Hilbert lemma](/bramble-hilbert-lemma/) behind the $h^k$ rates.
3. **Locking and mixed methods.** Why low order elements [lock](/finite-element-locking/), the [inf-sup condition](/inf-sup-condition/) for [mixed methods](/mixed-finite-element-method/), and the standard spaces: [Taylor-Hood](/taylor-hood-element/), [Raviart-Thomas](/raviart-thomas-element/) and [Nédélec](/nedelec-element/).
4. **Weak boundary conditions, stabilization and discontinuous methods.** [Nitsche's method](/nitsche-method/), [SUPG](/streamline-upwind-petrov-galerkin/) for convection, the [symmetric interior penalty method](/symmetric-interior-penalty-galerkin/) and the [hybridizable discontinuous Galerkin method](/hybridizable-discontinuous-galerkin/).
5. **Error estimation and adaptivity.** The [residual estimator](/residual-error-estimator/), [Zienkiewicz-Zhu recovery](/zienkiewicz-zhu-estimator/) and the [dual weighted residual method](/dual-weighted-residual-method/). Then [newest vertex bisection](/newest-vertex-bisection/), the [adaptive loop](/adaptive-finite-element-method/), [Dörfler marking](/dorfler-marking/) and the [optimality theorem](/afem-optimality-theorem/).
6. **High order.** The [hp method](/hp-finite-element-method/), with exponential convergence on geometric meshes, and the [spectral element method](/spectral-element-method/).
7. **Dynamics and nonlinear solids.** The [Newmark method](/newmark-beta-method/) and [generalized-$\alpha$](/generalized-alpha-method/) for structural dynamics, the [return mapping algorithm](/return-mapping-algorithm/) for plasticity and the [arc-length method](/arc-length-method/) for paths through limit points.
8. **Beyond the standard mesh.** The [boundary element method](/boundary-element-method/), the meshfree [element-free Galerkin method](/element-free-galerkin-method/), the [extended finite element method](/extended-finite-element-method/) for cracks, and the [virtual element method](/virtual-element-method/) on polygons.

## A first reading

Read these in order:

1. [Weak formulation](/weak-formulation/)
2. [Lax-Milgram theorem](/lax-milgram-theorem/)
3. [Céa's lemma](/cea-lemma/)
4. [Lagrange finite element](/lagrange-finite-element/)
5. [Finite element assembly](/finite-element-assembly/)
6. [Isoparametric mapping](/isoparametric-mapping/)
7. [Patch test](/patch-test/)
8. [Finite element locking](/finite-element-locking/)
9. [Inf-sup condition](/inf-sup-condition/)
10. [Taylor-Hood element](/taylor-hood-element/)
11. [Nitsche's method](/nitsche-method/)
12. [Residual error estimator](/residual-error-estimator/)
13. [Adaptive finite element method](/adaptive-finite-element-method/)
14. [Newmark method](/newmark-beta-method/)

This path goes from the weak problem to a code that assembles, checks itself, avoids locking and adapts its mesh. Sobolev spaces and the Bramble-Hilbert lemma can be read when a proof needs them. The optimality theorem, the hybridizable method and the last group can wait until the rest is familiar.

## Before you start

The chapter assumes the finite element method and the [Galerkin method](/galerkin-method/) at the level of Volume 12, with the [Poisson equation](/poisson-equation/) and its [boundary conditions](/boundary-conditions/) as the model problem. [Lagrange interpolation](/lagrange-interpolation/), [Legendre polynomials](/legendre-polynomials/), [Gauss-Legendre](/gauss-legendre-quadrature/) and [Gauss-Lobatto quadrature](/gauss-lobatto-quadrature/) give the shape functions and the quadrature rules. The linear algebra is that of [sparse matrices](/sparse-matrix/), the [Schur complement](/schur-complement/), the [conjugate gradient method](/conjugate-gradient-method/), [MINRES](/minres/) for saddle point systems and [multigrid](/multigrid-method/). The time steppers build on [initial value problems for ODEs](/ode-initial-value-problem/) and the nonlinear solids on [Newton's method for systems](/newton-method-for-systems/). Meshes come from [mesh generation](/mesh-generation/) in Volume 13, and the [partition of unity](/partition-of-unity/) of Volume 28 is the base of the meshfree and extended methods. The [discontinuous Galerkin method](/discontinuous-galerkin-method/) of the conservation laws chapter is the hyperbolic cousin of group 4. You need real analysis at the level of $L^2$ spaces and integration by parts.
