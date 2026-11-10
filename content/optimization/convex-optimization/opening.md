Find the point of the line $x_1 + 2x_2 = 5$ that is nearest to the origin. The answer is $(1, 2)$, at squared distance $5$, and there is a short proof that nothing better exists. For any number $\nu$, the minimum of $x_1^2 + x_2^2 + \nu(x_1 + 2x_2 - 5)$ over the whole plane is at most $5$, because on the line the added term is zero. At $\nu = -2$ that minimum is exactly $5$. A lower bound that meets the value of a feasible point proves that the point is optimal. The number $\nu$ is a [Lagrange multiplier](/lagrange-multiplier/), and the bound is a value of the dual function.

For convex problems such a certificate almost always exists, and the algorithms of this chapter produce it along with the answer. The chapter covers the theory of convex functions and sets that makes this work, the standard classes of convex problems, and the main methods that solve them: interior-point methods, multiplier methods, and methods for functions with kinks.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Convex functions.** The [convex function](/convex-function/) and its tests, the [epigraph](/epigraph/), [strong convexity](/strong-convexity/) and [quasiconvex functions](/quasiconvex-function/).
2. **Constrained problems and multipliers.** The [constrained problem](/constrained-optimization/), the [Lagrangian](/lagrangian-function/), and the [convex optimization problem](/convex-optimization-problem/), in which every local minimum is global. The [convex feasibility problem](/convex-feasibility-problem/) asks only for a point in an intersection of convex sets.
3. **Separation and subgradients.** The [separating](/separating-hyperplane-theorem/) and [supporting hyperplane theorems](/supporting-hyperplane-theorem/), and the [subgradient](/subgradient/) and [subdifferential](/subdifferential/) that replace the gradient at a kink.
4. **Duality and optimality conditions.** [Lagrangian duality](/lagrangian-duality/), the [Slater condition](/slater-condition/) that makes the dual bound exact, and the [KKT conditions](/kkt-conditions/).
5. **Conjugates and envelopes.** The [convex conjugate](/convex-conjugate/), [Fenchel duality](/fenchel-duality/) and the [convex envelope](/convex-envelope/).
6. **Problem classes.** [Quadratic programming](/quadratic-programming/), [portfolio optimization](/portfolio-optimization/), [second-order cone programming](/second-order-cone-programming/), [semidefinite programming](/semidefinite-programming/), [geometric programming](/geometric-programming/) and [convex relaxation](/convex-relaxation/).
7. **Interior-point methods.** The [barrier method](/barrier-method/), the [central path](/central-path/), [self-concordant functions](/self-concordant-function/) and the primal-dual [interior-point method](/interior-point-method/) for linear programs.
8. **Penalty and multiplier methods.** The [penalty method](/penalty-method/), [dual ascent](/dual-ascent/), [dual decomposition](/dual-decomposition/), the [augmented Lagrangian method](/augmented-lagrangian-method/) and [ADMM](/admm/).
9. **Methods for nonsmooth functions.** The [cutting-plane method](/cutting-plane-method/), the [proximal point method](/proximal-point-method/) and the [bundle method](/bundle-method/).

## A first reading

The chapter has 37 entries. A first pass can take these twelve, in order:

1. [Convex function](/convex-function/)
2. [Convex optimization problem](/convex-optimization-problem/)
3. [Lagrange multiplier](/lagrange-multiplier/)
4. [Lagrangian function](/lagrangian-function/)
5. [Subgradient](/subgradient/)
6. [Lagrangian duality](/lagrangian-duality/)
7. [Slater condition](/slater-condition/)
8. [KKT conditions](/kkt-conditions/)
9. [Quadratic programming](/quadratic-programming/)
10. [Barrier method](/barrier-method/)
11. [Augmented Lagrangian method](/augmented-lagrangian-method/)
12. [ADMM](/admm/)

These give the optimality conditions, the duality bound, one problem class, and one method of each main kind. The conjugate, Fenchel duality, self-concordance and the bundle method are advanced or research-level and can wait. So can the cone programs, unless your problems have norms or matrix constraints in them.

## Before you start

The chapter assumes [convex sets](/convex-set/) and the [convex hull](/convex-hull/) from Chapter 13.1, and the [gradient](/gradient/) from Chapter 15.4. Two methods here, the penalty method and dual ascent, run [gradient descent](/gradient-descent/) inside, and ADMM and the proximal point method use the [proximal operator](/proximal-operator/); both are in Chapter 15.4, which you can read alongside this one. From linear algebra you need [positive definite matrices](/positive-definite-matrix/), and the interior-point methods take steps of [Newton's method for systems](/newton-method-for-systems/). Several entries extend linear programming, so the [linear programming problem](/linear-programming-problem/), [LP duality](/lp-duality/) and the [separation oracle](/separation-oracle/) of Chapter 15.1 help, as does the [LP relaxation](/lp-relaxation/) of Chapter 15.2 for convex relaxation. Portfolio optimization uses the [covariance matrix](/covariance-matrix/).

The roadmap below lists every entry in the order of the groups.
