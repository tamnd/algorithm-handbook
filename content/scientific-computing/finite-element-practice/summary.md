## What to remember

- A weak problem $a(u, v) = \ell(v)$ for all $v \in V$ with $a$ bounded by $M$ and coercive with constant $\alpha$ has exactly one solution, with $\|u\|_V \le \|\ell\|_{V'}/\alpha$ ([Lax-Milgram](/lax-milgram-theorem/)). The Galerkin solution in a subspace $V_h$ satisfies $\|u - u_h\|_V \le (M/\alpha)\inf_{v \in V_h}\|u - v\|_V$ ([Céa](/cea-lemma/)).
- The [Bramble-Hilbert lemma](/bramble-hilbert-lemma/) and a scaling argument turn this into rates. For [Lagrange elements](/lagrange-finite-element/) of degree $k$ and $u \in H^{k+1}$, $|u - u_h|_1 \le Ch^k|u|_{k+1}$ and $\|u - u_h\|_0 \le Ch^{k+1}|u|_{k+1}$.
- [Assembly](/finite-element-assembly/) computes each element matrix on a reference cell by quadrature and adds it into the sparse global matrix, in $\Theta(Eqn^2)$ time for $E$ cells, $q$ quadrature points and $n$ local unknowns. The [patch test](/patch-test/) finds consistency errors, but passing it does not prove convergence.
- Low order elements [lock](/finite-element-locking/) under constraints such as incompressibility. A mixed method is stable when the pair of spaces satisfies the [inf-sup condition](/inf-sup-condition/) with a constant $\beta$ that does not depend on $h$; $P_1$-$P_1$ and $Q_1$-$P_0$ fail it, [Taylor-Hood](/taylor-hood-element/), under a mild condition on the mesh, and [Raviart-Thomas](/raviart-thomas-element/) pairs pass it.
- [Nitsche's method](/nitsche-method/), [SUPG](/streamline-upwind-petrov-galerkin/) and the [interior penalty](/symmetric-interior-penalty-galerkin/) methods add terms that the exact solution satisfies, so Galerkin orthogonality still holds. Nitsche and SIPG need a penalty above a bound set by an inverse inequality.
- A posteriori estimators such as the [residual estimator](/residual-error-estimator/) bound the error from computable residuals. [Dörfler marking](/dorfler-marking/) takes a smallest set $\mathcal M$ with $\sum_{\mathcal M}\eta_K^2 \ge \theta\sum\eta_K^2$. For symmetric elliptic problems with exact solves, small $\theta$ and [newest vertex bisection](/newest-vertex-bisection/), the [adaptive loop](/adaptive-finite-element-method/) converges at the best rate of the approximation class.
- On geometric meshes the [hp method](/hp-finite-element-method/) converges like $\exp(-bN^{1/3})$ in 2D for piecewise analytic solutions, where uniform refinement is only algebraic.
- [Newmark](/newmark-beta-method/) with $\beta = \tfrac14$, $\gamma = \tfrac12$ is second order and unconditionally stable for linear problems; the explicit central difference method with [lumped mass](/mass-lumping/) needs $\omega\,dt \le 2$. [Generalized-$\alpha$](/generalized-alpha-method/) keeps second order and sets the damping of the highest frequencies by $\rho_\infty$.

| Method | Global unknowns | Error for smooth $u$ | Main weakness |
|---|---|---|---|
| Lagrange $P_k$ | nodal values | $O(h^k)$ in $H^1$, $O(h^{k+1})$ in $L^2$ | locks at low order under constraints |
| Taylor-Hood $P_{k+1}$-$P_k$ | velocity and pressure nodes | $O(h^{k+1})$ in $H^1 \times L^2$ | indefinite saddle point system |
| Raviart-Thomas $\mathrm{RT}_k$ (mixed Poisson) | face and cell moments | $O(h^{k+1})$ for flux and potential in $L^2$ | indefinite saddle point system |
| SIPG, degree $k$ | all cell coefficients | $O(h^k)$ broken energy, $O(h^{k+1})$ in $L^2$ | many unknowns; penalty must exceed a bound |
| [HDG](/hybridizable-discontinuous-galerkin/), degree $k$ | face traces only | $O(h^{k+1})$ for $u$ and its flux | local solves on every cell |
| hp on geometric meshes | element coefficients | $\exp(-bN^{1/3})$ in 2D, piecewise analytic $u$ | needs the mesh grading and degree choice |
| [Boundary elements](/boundary-element-method/) | boundary values | depends on the element | dense system, needs a fundamental solution |

: Discretizations of the chapter for elliptic problems. The rates are those stated in the entries; constants depend on the shape regularity of the mesh.

## Choosing a method

For a symmetric elliptic problem on a reasonable mesh, start with continuous Lagrange elements of degree 1 or 2 and a conjugate gradient solver with multigrid. Add an adaptive loop with a residual or recovery estimator when the solution has corners or layers. Use the [dual weighted residual method](/dual-weighted-residual-method/) when you care about one output, such as a flux or a stress at a point, more than about the energy norm.

When a constraint appears, such as incompressible flow or nearly incompressible elasticity, do not fight locking with finer meshes. Use a stable mixed pair, Taylor-Hood for Stokes and Raviart-Thomas when the flux must be conserved cell by cell, and check the inf-sup condition of any new pair. For convection-dominated problems, add SUPG or move to a discontinuous method. HDG is the discontinuous method to try when the number of global unknowns matters.

For smooth solutions and high accuracy, raise the degree: [spectral elements](/spectral-element-method/) for wave and flow problems on hexahedral meshes, the hp method when singularities sit at known corners. In structural dynamics, use the average acceleration Newmark method or generalized-$\alpha$ for implicit steps, and central differences with lumped mass for short events such as impact. Boundary elements pay off for linear, constant-coefficient problems on exterior or large domains, with a [fast multipole method](/fast-multipole-method/) for large boundaries. The [meshfree](/element-free-galerkin-method/), [extended](/extended-finite-element-method/) and [virtual element](/virtual-element-method/) methods are for problems where making a good mesh is the hard part.
