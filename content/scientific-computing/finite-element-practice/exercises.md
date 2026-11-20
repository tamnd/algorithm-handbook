1. ◦ Write the [weak formulation](/weak-formulation/) of $-u'' = f$ on $(0, 1)$ with $u(0) = 0$ and the Robin condition $u'(1) + 2u(1) = g$. Give the space $V$, the bilinear form $a$ and the linear form $\ell$, and say which boundary condition is essential and which is natural.

2. ◦ Take $a(u, v) = \varepsilon\int_0^1 u'v' + b\int_0^1 u'v$ on $H^1_0(0, 1)$ with the norm $|v|_1 = \|v'\|_{L^2}$ and the Poincaré inequality $\|v\|_{L^2} \le |v|_1/\pi$. Find a coercivity constant $\alpha$ and a continuity constant $M$, and evaluate the factor $M/\alpha$ of [Céa's lemma](/cea-lemma/) for $\varepsilon = 0.02$ and $b = 1$.

3. ◦ The unit square is cut into $4 \times 4$ squares, each split into two triangles by a diagonal. How many global degrees of freedom does the cubic [Lagrange element](/lagrange-finite-element/) have on this mesh? How many remain after [static condensation](/static-condensation/) of the cell interiors? Answer both questions again with zero Dirichlet values on the whole boundary.

4. ◦ Solve $-u'' = \lambda u$ on $(0, 1)$ with $u(0) = u(1) = 0$ by linear elements on two cells, so with one interior node. Find the discrete eigenvalue with the consistent mass matrix and with the [lumped mass](/mass-lumping/) matrix, and compare both with the exact value $\pi^2$.

5. ◦ The [Newmark method](/newmark-beta-method/) with $\gamma = \tfrac12$ and $\beta < \tfrac14$ is stable for $\omega\,dt \le (\gamma/2 - \beta)^{-1/2}$. Find the limit for the central difference method ($\beta = 0$) and for Fox-Goodwin ($\beta = \tfrac1{12}$). For a spring with $\omega = 20$, what is the largest stable time step of each?

6. ◦ Compute $\alpha_m$, $\alpha_f$, $\gamma$ and $\beta$ of the [generalized-$\alpha$ method](/generalized-alpha-method/) with the Chung-Hulbert choice $\alpha_m = (2\rho_\infty - 1)/(\rho_\infty + 1)$, $\alpha_f = \rho_\infty/(\rho_\infty + 1)$, $\gamma = \tfrac12 - \alpha_m + \alpha_f$, $\beta = \tfrac14(1 - \alpha_m + \alpha_f)^2$, for $\rho_\infty = 0.8$ and for $\rho_\infty = 0$. Give exact fractions.

7. ◦ Seven elements have squared error indicators $0.40, 0.20, 0.15, 0.10, 0.08, 0.04, 0.03$. How many elements does [Dörfler marking](/dorfler-marking/) with a set of minimal size mark for $\theta = 0.5$, $0.75$, $0.9$ and $1$?

8. ◦ A [boundary element](/boundary-element-method/) model has $m = 20000$ boundary elements. How much memory does the dense matrix need in double precision, and about how many floating point operations does a dense LU factorization take?

9. ◦ The unit cube is cut into the six tetrahedra that share the main diagonal from $(0,0,0)$ to $(1,1,1)$. Count the vertices, edges, faces and tetrahedra, and check Euler's relation $V - E + F - T = 1$. Which counts are the numbers of global degrees of freedom of linear Lagrange, lowest order [Nédélec](/nedelec-element/), lowest order [Raviart-Thomas](/raviart-thomas-element/) and piecewise constant elements?

10. • Solve $-u'' = 1$ on $(0, 1)$ with $u(0) = u(1) = 0$ by linear elements on a uniform mesh of $N$ cells. Show that $|u - u_h|_1^2 = h^2/12$ with $h = 1/N$. For $N = 3$, give $|u - u_h|_1^2$ and $|u_h|_1^2$ as fractions.

11. • Compute the element stiffness matrix of linear elements for $-\Delta u$ on an equilateral triangle. Then assemble the row of an interior vertex of the regular mesh where six equilateral triangles meet at each vertex. What finite difference stencil do you get?

12. • In 1D, let $V_h$ be continuous piecewise quadratics on a uniform mesh of $(0, 1)$ with $v(0) = v(1) = 0$, normed by $|v|_1$, and $Q_h$ continuous piecewise linears with mean zero, normed in $L^2$. For $b(v, q) = \int_0^1 v'q$, find the [inf-sup constant](/inf-sup-condition/) $\beta_h$ exactly.

13. • For $-\varepsilon u'' + au' = f$ with $a = 2$, $\varepsilon = 0.01$ and linear elements with $h = 0.02$, compute the element Péclet number $\mathrm{Pe} = ah/(2\varepsilon)$, the [SUPG](/streamline-upwind-petrov-galerkin/) parameter $\tau = \frac{h}{2|a|}(\coth\mathrm{Pe} - 1/\mathrm{Pe})$ and the total diffusion $\varepsilon + \tau a^2$. Find the ratio of the two roots of the plain Galerkin difference equation with $f = 0$, and the largest $h$ for which plain Galerkin does not oscillate.

14. • A 1D bar has $E = 200$, initial yield stress $\sigma_y = 1$ and linear isotropic hardening modulus $K = 20$. Starting from rest, apply the [return mapping algorithm](/return-mapping-algorithm/) to the strains $0.01$, then $0.005$, then $-0.01$. Give the stress after each step, the consistent tangent after the first, and the yield stress and plastic strain at the end, as fractions.

15. • A one-degree-of-freedom model has the internal force $N(u) = u^3 - 3u^2 + 2.5u$ and the load $\lambda$. Find the two limit points $(u, \lambda)$ that the [arc-length method](/arc-length-method/) passes. Under load control, past the first limit point, to which $u$ does the solution jump?

16. • The unit square is cut into $10 \times 10$ squares, each split into two triangles, with zero Dirichlet data on the boundary. Count the global unknowns of continuous Lagrange elements, of the [symmetric interior penalty method](/symmetric-interior-penalty-galerkin/) and of the [hybridizable discontinuous Galerkin method](/hybridizable-discontinuous-galerkin/) with traces of degree $k$, for $k = 1$ and $k = 3$.

17. • Split the unit square by the diagonal from $(0,0)$ to $(1,1)$ into two triangles whose refinement edge is that diagonal. Apply [newest vertex bisection](/newest-vertex-bisection/), where each bisection makes the midpoint the newest vertex of both children. Refine one of the two triangles, then the triangle with vertices $(0,0)$, $(1,0)$, $(\tfrac12, \tfrac12)$, then the triangle with vertices $(0,0)$, $(\tfrac12, 0)$, $(\tfrac12, \tfrac12)$. How many triangles are there after each step, and which vertices does the closure add in the last step?

18. • Nodes sit at $0$, $1$ and $2$ with the weight $w(r) = (1 - r/1.5)_+$. At $x = 0.8$, compute the Shepard functions (moving least squares with a constant basis) and the [element-free Galerkin](/element-free-galerkin-method/) shape functions with a linear basis. Which of them reproduce the function $x$?

19. • Let $a(u, v) = \int_0^1 u'v' + b\int_0^1 u'v + c\int_0^1 uv$ on $H^1_0(0, 1)$ with constants $b$ and $c$. For which $c$ is $a$ coercive, so that the [Lax-Milgram theorem](/lax-milgram-theorem/) applies? Does the answer depend on $b$?

20. • The Gauss-Lobatto rule with three points on $[-1, 1]$ has weights $\tfrac13, \tfrac43, \tfrac13$. Check that it integrates $x^2$ and $x^3$ exactly, and find its value for $x^4$. For the [spectral element method](/spectral-element-method/) in 3D with degree $N$, compare the cost of applying the stiffness matrix of one element by a dense element matrix and by sum factorization.

21. ★ Prove that linear interpolation on $[0, h]$ satisfies $|u - I_hu|_1 \le (h/\pi)|u|_2$, and that the constant $1/\pi$ cannot be improved. This is the sharp 1D case of the [Bramble-Hilbert lemma](/bramble-hilbert-lemma/) bound.

22. ★ Prove that for $-u'' = f$ on $(0, 1)$ with $u(0) = u(1) = 0$ and linear elements on any mesh, the Galerkin solution equals $u$ at every node. Use the Green's function of a node.

23. ★ For the $P_2$-$P_0$ Stokes pair in 2D, let $\Pi_h$ map $v \in H^1_0(\Omega)^2$ to $V_h$ with $\int_e \Pi_hv\,ds = \int_e v\,ds$ on every edge $e$. Show that $b(v - \Pi_hv, q_h) = \int_\Omega \nabla\cdot(v - \Pi_hv)\,q_h = 0$ for every piecewise constant $q_h$, which is the property in the Fortin criterion. Compute $\int_e 4\lambda_i\lambda_j\,ds$ for the edge bubble of the edge $e$ between vertices $i$ and $j$, which is used to correct the edge means.

24. ★ For the lowest order [virtual element method](/virtual-element-method/) on a regular hexagon of side 1, compute the gradient of the projection $\Pi^\nabla\phi_i$ of each vertex basis function, using $\nabla\Pi^\nabla v = |E|^{-1}\int_{\partial E}v\,n\,ds$ with $v$ linear on each edge. Give the consistency matrix $K^c_{ij} = |E|\,\nabla\Pi^\nabla\phi_i\cdot\nabla\Pi^\nabla\phi_j$, its rank, and the dimension of its kernel. Why does the method need a stabilization term?

25. ★ The wave equation $u_{tt} = u_{xx}$ is discretized by linear elements with lumped mass on a uniform periodic mesh of size $h$ and stepped with the central difference method. Show that for $dt = h$ the nodal values are exact for any initial data that are themselves exact at the nodes and at $t = -dt$. How does this relate to the stability limit $\omega\,dt \le 2$?
