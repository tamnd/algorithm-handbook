1. ◦ In [isogeometric analysis](/isogeometric-analysis/), take cubic splines, $p = 3$, on 10 elements per direction with an open knot vector. How many basis functions does the space of maximal smoothness have in one, two and three dimensions? How many does the $C^0$ space of the same degree on the same elements have?

2. ◦ Following [quadrature for isogeometric analysis](/isogeometric-quadrature/), how many Gauss points per element integrate the 1D mass matrix of quartic B-splines, $p = 4$, exactly (a) when the geometry map is affine and (b) when it is a B-spline map of degree 4? (c) How many points per element does the tensor rule of case (a) use in three dimensions?

3. ◦ Give the Greville abscissae of the cubic B-splines on the knot vector $(0, 0, 0, 0, 1, 2, 3, 3, 3, 3)$, the points at which [isogeometric collocation](/isogeometric-collocation/) imposes the equation. How many are there, and which of them carry boundary conditions?

4. ◦ The half-point rule for even $p$ puts one point at each $2ih$, $i \in \mathbb{Z}$, with weight $2h$. Check that it integrates the uniform quartic B-spline with knots $0, h, 2h, 3h, 4h, 5h$ exactly, and also its translate with knots $h, \ldots, 6h$. The values of the uniform quartic B-spline at its inner knots are $\tfrac1{24}, \tfrac{11}{24}, \tfrac{11}{24}, \tfrac1{24}$.

5. ◦ A bar of length $L = 50$ and section $A$ has a groove of length $\ell = 1$ with section $A' = A/4$. Using the bar model of [defeaturing](/defeaturing/), by what fraction does removing the groove change the end displacement under an end load? By what factor does it change the stress in the grooved part?

6. ◦ A strip of length $40$ and thickness $t = 1.6$ is sampled on both long sides with spacing $s = 0.2$, the top side shifted by $s/2$. Using the results of [mid-surface extraction](/midsurface-extraction/), where does the medial midline start and end, how far is each center from the true midline, and what thickness $2r$ does the method report?

7. ◦ A bicubic NURBS patch with $10 \times 10$ elements of maximal smoothness models a shell. How many unknowns does the [isogeometric Kirchhoff-Love shell](/isogeometric-kirchhoff-love-shell/) have, and how many would a shell model with five unknowns per control point have on the same net? For [subdivision shell elements](/subdivision-shell-elements/), how many vertices does a triangle depend on if it is regular, and if one corner has valence 5 or 7?

8. ◦ A [PHT-spline](/pht-spline/) space on a hierarchical T-mesh has dimension $4(V_b + V_+)$, with $V_b$ boundary vertices and $V_+$ interior crossing vertices. Compute it for a $3 \times 3$ grid of cells, after splitting the center cell into four, and instead after splitting a corner cell into four.

9. • Compute the [Bézier extraction](/bezier-extraction/) operators of the cubic B-splines $N_0, \ldots, N_5$ on the knot vector $(0, 0, 0, 0, 1, 1, 2, 2, 2, 2)$ for both elements. Read off from them the smoothness of the spline space at $u = 1$.

10. • For the quadratic B-splines on $(0, 0, 0, 1, 2, 2, 2)$, the extraction operator of the element $[0, 1]$ has the rows $(1, 0, 0)$, $(0, 1, \tfrac12)$ and $(0, 0, \tfrac12)$. Compute the element mass matrix $M^e = C^e G (C^e)^T$, where $G$ is the Gram matrix of the quadratic [Bernstein polynomials](/bernstein-polynomials/) on $[0, 1]$, and check one entry by direct integration.

11. • Start from a cubic Bézier curve on $[0, 1]$. Count the functions of the spaces that the two orders of refinement give: elevate to degree 4 and then insert the knots $\tfrac14, \tfrac12, \tfrac34$, against inserting those knots first and then elevating. Which order is [k-refinement](/k-refinement/), and what smoothness does each space have at the new knots?

12. • A [T-spline](/t-spline/) splits one cubic blending function at a time. Write the cubic B-spline with local knots $(0, 1, 2, 3, 4)$ as a combination of two cubic B-splines after inserting $u = \tfrac12$, and again after inserting $u = 3$. Check both identities at $x = 2$.

13. • Build a 1D [hierarchical B-spline](/hierarchical-b-spline/) basis: quadratic B-splines on $(0, 0, 0, 1, 2, 3, 4, 4, 4)$ at level 0, their dyadic refinement at level 1, and the refined region $\Omega^1 = [0, 2]$. List the selected functions by their knots, and compute their sum at $x = \tfrac34$ and $x = \tfrac54$. Then truncate the level-0 function with knots $(0, 1, 2, 3)$ as in the [truncated hierarchical B-spline](/truncated-hierarchical-b-spline/), give its value at $x = \tfrac54$, and check that the truncated basis sums to 1 at both points.

14. • Collocate $-u'' = 1$, $u(0) = u(1) = 0$, with quadratic B-splines on $(0, 0, 0, \tfrac13, \tfrac23, 1, 1, 1)$ at the Greville points. Write the row of the middle point and compare it with the three-point difference stencil. Solve the system and explain why the result is the exact solution.

15. • In [trimmed isogeometric analysis](/trimmed-isogeometric-analysis/), the B-spline of degree $p$ that starts at a trimming boundary has, on a cut piece of length $\epsilon h$, the mass diagonal $h\epsilon^{2p+1}/((p!)^2(2p+1))$ and the stiffness diagonal $\epsilon^{2p-1}/(h((p-1)!)^2(2p-1))$. Compute the ratio of the stiffness to the mass diagonal for general $p$ and for $p = 2$, and say what it implies for a generalized eigenvalue problem as $\epsilon \to 0$.

16. • The bound of the [approximation estimates for NURBS spaces](/nurbs-approximation-estimates/) is tight in its power of $h$. On a uniform mesh of $[0, 1]$ with width $h$, compute the $L^2$ error of the piecewise linear interpolant of $x^2$, and compare it with the best piecewise linear approximation in $L^2$, whose error is $h^2/\sqrt{180}$.

17. • In the shrinking-ball method, a sample $p = (0, -t/2)$ on the bottom of a strip of thickness $t$ has the inward normal $(0, 1)$, and the nearest sample on the top is $q = (d, t/2)$. Derive the radius of the disk tangent at $p$ through $q$, the height of its center above the midline and the angle at the center between $p$ and $q$.

18. • In [isogeometric shape optimization](/isogeometric-shape-optimization/), the design model is a quadratic Bézier curve with control points $P_0, P_1, P_2$, and the analysis model inserts the knots $\tfrac13$ and $\tfrac23$. Compute the $5 \times 3$ matrix $T$ with $Q = TP$, and the derivative of the analysis control points with respect to $P_1$.

19. ★ A planar map of degree $(2, 1)$ has $\det J = g(u)$, where $g$ is the quadratic Bézier function with coefficients $(1, a, 1)$. For which $a$ is the map valid? For which $a$ does the test of [volumetric spline parameterization](/volumetric-spline-parameterization/), positive Bernstein coefficients of $\det J$ written in degree 3, prove validity? For which $a$ does it prove validity after one subdivision at $u = \tfrac12$?

20. ★ In the one-cell example of the [finite cell method](/finite-cell-method/), the bar $(0, 1)$ has material with $E = 1$ and load $f = 1$ on $(0, \tfrac12)$, a void with stiffness $\alpha$ and no load on $(\tfrac12, 1)$, $u(0) = 0$ and free ends otherwise. Using the space $\{c_1 x + c_2 x^2\}$, derive the error $u_\alpha(\tfrac12) - u(\tfrac12) = \alpha(1 - \alpha)/(8(1 + 14\alpha + \alpha^2))$.

21. ★ For weighted quadrature with $p = 2$ on a uniform periodic mesh with $h = 1$, the test function $B_i$ has support $(0, 3)$ and the points are $\tfrac12, 1, \tfrac32, 2, \tfrac52$. The exactness conditions ask that the rule reproduce $\int B_i B_j$ for the five B-splines $B_j$ that meet the support of $B_i$, and these integrals are $\tfrac1{120}, \tfrac{13}{60}, \tfrac{11}{20}, \tfrac{13}{60}, \tfrac1{120}$. Derive the five weights and check that they sum to $\int B_i = 1$.

22. ★ Collocate $-u'' = f$ with quadratic B-splines on $(0, 0, 0, 1, 1, 2, 2, 2)$, which have an interior knot of multiplicity $p = 2$, at the Greville points, with Dirichlet rows at both ends. Show that the collocation matrix is singular, whichever one-sided second derivative is used at the knot.
