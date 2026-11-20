1. $V = \{v \in H^1(0, 1) : v(0) = 0\}$. Multiply by $v$, integrate by parts and use $u'(1) = g - 2u(1)$: $a(u, v) = \int_0^1 u'v' + 2u(1)v(1)$ and $\ell(v) = \int_0^1 fv + g\,v(1)$. The Dirichlet condition at 0 is essential and sits in $V$; the Robin condition at 1 is natural and sits in $a$ and $\ell$.

2. $\int_0^1 v'v = \tfrac12[v^2]_0^1 = 0$, so $a(v, v) = \varepsilon|v|_1^2$ and $\alpha = \varepsilon$. By Cauchy-Schwarz and Poincaré, $|a(u, v)| \le (\varepsilon + b/\pi)|u|_1|v|_1$. So $M/\alpha = 1 + b/(\pi\varepsilon) = 1 + 1/(0.02\pi) = 16.92$.

3. The mesh has 25 vertices, 56 edges and 32 triangles. Cubic elements have one unknown per vertex, two per edge and one per triangle: $25 + 112 + 32 = 169$, and condensation removes the 32 interior ones, leaving 137. The boundary carries 16 vertices and 16 edges, so 48 boundary values; with Dirichlet data there are 121 unknowns, and 89 after condensation.

4. With $h = \tfrac12$, the stiffness entry is $2/h = 4$. The consistent mass entry is $2h/3 = \tfrac13$, giving $\lambda = 12$; the lumped one is $h = \tfrac12$, giving $\lambda = 8$. The exact $\pi^2 = 9.87$ lies between: consistent mass overestimates the eigenvalue and lumping underestimates it here.

7. The total is 1. Sorted indicators accumulate to $0.40, 0.60, 0.75, 0.85, 0.93, 0.97, 1.00$, so the minimal sets have 2, 3, 5 and 7 elements.

9. $V = 8$, $E = 19$ (12 cube edges, 6 face diagonals and the main diagonal), $F = 18$ (12 on the boundary and 6 inside), $T = 6$, and $8 - 19 + 18 - 6 = 1$. Linear Lagrange has 8 unknowns, Nédélec 19, Raviart-Thomas 18 and piecewise constants 6.

10. Galerkin with linear elements in 1D is nodally exact here, so $u_h$ is the interpolant of $u = x(1 - x)/2$. On each cell the error of the derivative is a linear function with mean zero and slope $u'' = -1$, so $\int(e')^2 = h^3/12$ per cell. For $N = 3$: $|u - u_h|_1^2 = \tfrac1{108}$ and $|u_h|_1^2 = |u|_1^2 - \tfrac1{108} = \tfrac1{12} - \tfrac1{108} = \tfrac2{27}$, by Galerkin orthogonality.

12. Given $q \in Q_h$, take $v(x) = \int_0^x q$. It is continuous, piecewise quadratic, and $v(1) = 0$ because $q$ has mean zero, so $v \in V_h$, and $b(v, q) = \|q\|^2 = |v|_1\|q\|$. Cauchy-Schwarz gives the reverse bound, so $\beta_h = 1$ for every mesh.

13. $\mathrm{Pe} = 2$, $\tau = 0.005(\coth 2 - 0.5) = 0.0026866$, and $\varepsilon + \tau a^2 = 0.020746 = (ah/2)\coth\mathrm{Pe}$. The plain Galerkin roots are 1 and $(1 + \mathrm{Pe})/(1 - \mathrm{Pe}) = -3$, which alternates in sign. The oscillation goes away when $\mathrm{Pe} \le 1$, that is $h \le 0.01$.

15. $N'(u) = 3u^2 - 6u + 2.5 = 0$ gives $u = 1 \mp 1/\sqrt6$: $(0.591752, 0.636083)$ and $(1.408248, 0.363917)$. Under load control the solution at $\lambda = 0.636083$ jumps to the other root of $N(u) = \lambda$. The three roots sum to 3 and the double root is $1 - 1/\sqrt6$, so it is $u = 1 + 2/\sqrt6 = 1.816497$.

17. Refining one of the first two triangles bisects the diagonal, and its neighbour shares that refinement edge, so both are cut at $(\tfrac12, \tfrac12)$: 4 triangles. The second step cuts the boundary edge from $(0,0)$ to $(1,0)$: 5 triangles. In the third step the refinement edge runs from $(0,0)$ to $(\tfrac12, \tfrac12)$, but the neighbour across it has its refinement edge on the left side of the square. The closure first cuts that side at $(0, \tfrac12)$ and then both triangles at $(\tfrac14, \tfrac14)$: 8 triangles.

21. The error $e = u - I_hu$ vanishes at $0$ and $h$, so $e'$ has mean zero on $[0, h]$. The Poincaré inequality for mean-zero functions on an interval of length $h$ has the sharp constant $h/\pi$, so $\|e'\| \le (h/\pi)\|e''\| = (h/\pi)\|u''\|$. Equality holds for $u = \sin(\pi x/h)$, where $I_hu = 0$ and $e' = (\pi/h)\cos(\pi x/h)$.

22. The Green's function $G_i$ of the node $x_i$ solves $a(G_i, w) = w(x_i)$ for all $w \in H^1_0$. It is linear on $[0, x_i]$ and on $[x_i, 1]$, so it lies in $V_h$. Then $u(x_i) - u_h(x_i) = a(u - u_h, G_i) = 0$ by Galerkin orthogonality.

23. On each triangle $\int_K \nabla\cdot w = \sum_{e \subset \partial K} n_e\cdot\int_e w\,ds$, since the normal is constant on each edge. With $w = v - \Pi_hv$ every edge integral is zero, so $\int_K \nabla\cdot w = 0$, and the integral against a constant $q_h$ on $K$ vanishes. On an edge of length $|e|$, $\int_e 4\lambda_i\lambda_j\,ds = 4|e|\int_0^1 t(1 - t)\,dt = 2|e|/3$.

24. The two edges at vertex $i$ have outward normals at angles $60i^\circ \pm 30^\circ$; half of each edge integral belongs to $\phi_i$, so $\int_{\partial E}\phi_in = \tfrac{\sqrt3}2(\cos 60i^\circ, \sin 60i^\circ)$. With $|E| = 3\sqrt3/2$, $\nabla\Pi^\nabla\phi_i = \tfrac13(\cos 60i^\circ, \sin 60i^\circ)$ and $K^c_{ij} = \tfrac{\sqrt3}6\cos(60^\circ(i - j))$. The matrix has rank 2 and a kernel of dimension 4. The kernel holds the constants and three modes that the projection does not see, so without a stabilization term the stiffness matrix is singular on them.

25. With lumped mass $h$ and stiffness $(2, -1, -1)/h$, central differences with $dt = h$ give $u^{n+1}_j = u^n_{j+1} + u^n_{j-1} - u^{n-1}_j$. Any $f(x - t) + g(x + t)$ satisfies this identity at the nodes, so the scheme is exact. The largest eigenvalue of $M^{-1}K$ is $4/h^2$, so $\omega\,dt = 2$: the exact step is the stability limit itself.
