1. ◦ Run the [de Casteljau algorithm](/de-casteljau-algorithm/) on the cubic [Bézier curve](/bezier-curve/) with control points $(0, 0), (0, 4), (4, 4), (4, 0)$ at $t = \tfrac13$. Give every intermediate point, the point $C(\tfrac13)$, the tangent $C'(\tfrac13)$, and the control polygons of the two halves of the split.

2. ◦ A cubic B-spline curve has the [knot vector](/knot-vector/) $(0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 3)$. How many control points does it have, and what is its domain? How smooth is the curve at $u = 1$ and at $u = 2$? Check the number of control points against the dimension that the [Curry-Schoenberg theorem](/curry-schoenberg-theorem/) gives for cubic splines on $[0, 3]$ with these breakpoints.

3. ◦ Take the uniform cubic [B-splines](/b-spline/) $N_0, \dots, N_5$ on the knots $0, 1, \dots, 9$. Compute the nonzero values at $u = 4$ and at $u = \tfrac72$, and check the [partition of unity](/partition-of-unity/). Then do the same at $u = \tfrac52$ and explain why the sum is not 1.

4. ◦ A [rational Bézier curve](/rational-bezier-curve/) of degree 2 has the control points $(1, 0), (1, 1), (0, 1)$ and the weights $1, w, 1$. Find its point at $t = \tfrac12$ as a function of $w$, and the value of $w$ that puts this point on the unit circle. Which conic does the curve trace for that $w$?

5. ◦ Find the Euler characteristic $V - E + F$ and the genus $g$ of three [polygon meshes](/polygon-mesh/): a closed quad mesh with $V = 16$, $E = 32$, $F = 16$; a closed triangle mesh with $V = 10$, $E = 36$, $F = 24$; and a $3 \times 3$ grid of quads with its boundary, $V = 16$, $E = 24$, $F = 9$.

6. ◦ Apply one step of [Catmull-Clark subdivision](/catmull-clark-subdivision/) to a tetrahedron. Give the new numbers of vertices, edges and faces, the type of every new face, and the number of extraordinary vertices. Then give the counts after one step of [Doo-Sabin subdivision](/doo-sabin-subdivision/) on the same tetrahedron, and check $V - E + F$ in both cases.

7. ◦ The [ball pivoting algorithm](/ball-pivoting-algorithm/) places a ball of radius $\rho$ on three points that form an equilateral triangle of side 3 in the plane $z = 0$. Where is the centre of the ball when $\rho = 2$? What happens when $\rho = \tfrac32$?

8. ◦ In [marching squares](/marching-squares/) a cell $[0, 1]^2$ has the corner values $f(0, 0) = 1$, $f(1, 0) = 4$, $f(1, 1) = 0$ and $f(0, 1) = 5$, and a point is inside when $f < c$. For $c = 2$, find the four edge crossings by linear interpolation and use the asymptotic decider to join them into two segments. Which corners does the inside region join when $c = 3$?

9. ◦ Apply [Ramer-Douglas-Peucker](/ramer-douglas-peucker/) to the polyline $(0, 0), (1, 2), (3, 3), (5, 0), (7, 1), (9, 4), (10, 3)$ with $\varepsilon = 1$ and with $\varepsilon = \tfrac32$. List the points that are kept in each case and the distance that decides each split.

10. • Run [Visvalingam-Whyatt](/visvalingam-whyatt/) on the polyline of Exercise 9 until four points remain. Give the triangle area of each removed point at the time of removal, recomputing the neighbours after each step. Compare the result with Ramer-Douglas-Peucker at $\varepsilon = \tfrac32$.

11. • The uniform [Catmull-Rom spline](/catmull-rom-spline/) runs through the corners $(0, 0), (1, 0), (1, 1), (0, 1)$ of a square. Write the middle segment, from $(1, 0)$ to $(1, 1)$, as a cubic Bézier curve, and compute its point at the middle of the segment. Compare the weights on the four points with the [four-point scheme](/four-point-scheme/) at $w = \tfrac1{16}$.

12. • Find the [natural cubic spline](/natural-cubic-spline/) through $(0, 0), (1, 1), (2, 0)$ with the uniform parameters $0, 1, 2$. Give the tangents at the three points, the second derivative at the middle point, and the value of $\int_0^2 C''(x)^2 \, dx$.

13. • A cubic B-spline curve has the knots $(0, 0, 0, 0, 1, 2, 2, 2, 2)$ and the control points $(0, 0), (2, 4), (4, 0), (6, 4), (8, 0)$. Evaluate it at $u = \tfrac32$ by the [de Boor algorithm](/de-boor-algorithm/), showing the three levels.

14. • Insert the knot $u = \tfrac32$ once into the curve of Exercise 13 by [Boehm's formula](/boehm-knot-insertion/). Give the three ratios $\alpha_i$, the new control points, and the new knot vector. Which column of the de Boor scheme of Exercise 13 did you get back?

15. • Apply one step of [Loop subdivision](/loop-subdivision/) to the regular octahedron with the vertices $(\pm 1, 0, 0), (0, \pm 1, 0), (0, 0, \pm 1)$. Compute $\beta_4$, the new position of the vertex $(1, 0, 0)$, and the new point on the edge from $(1, 0, 0)$ to $(0, 1, 0)$.

16. • A cubic polynomial has the Bernstein coefficients $1, -2, 2, -1$ on $[0, 1]$. Write it in the power basis, find its roots in $(0, 1)$, and compare their number with the sign changes of the coefficients, as the [variation diminishing property](/variation-diminishing-property/) allows.

17. • The quadratic with the Bernstein coefficients $-1, 2, 3$ on $[0, 1]$ has one root there. Do one step of [Bézier clipping](/bezier-clipping/): find the interval where the convex hull of the control points $(0, -1), (\tfrac12, 2), (1, 3)$ meets the $t$ axis, and check that the root lies in it.

18. • Take the quadratic B-splines on the knots $(0, 0, 0, 1, 2, 3, 3, 3)$. Use the [Schoenberg-Whitney theorem](/schoenberg-whitney-theorem/) to decide which of these site sequences give a unique interpolant: $(0, 1, 2, \tfrac52, 3)$, $(0, \tfrac14, \tfrac12, \tfrac34, 3)$ and $(0, \tfrac12, \tfrac32, 2, \tfrac52)$.

19. • A [Coons patch](/coons-patch/) has the boundary curves $c_0(u) = (u, 0, 0)$, $c_1(u) = (u, 1, 0)$, $d_0(v) = (0, v, 0)$ and $d_1(v) = (1, v, 4v(1 - v))$. Write the bilinearly blended patch $S(u, v)$, check that it matches $d_1$ at $u = 1$, and find $S(\tfrac12, \tfrac12)$.

20. • Marching squares has $2^4 = 16$ corner configurations. Use Burnside's lemma to count the classes under the rotations of the square, under all eight symmetries, and under the symmetries together with swapping inside and outside. Name the classes in the last case.

21. • A [surface of revolution](/surface-of-revolution/) has a unit-speed profile $(r(s), z(s))$, and its Gaussian curvature is $K = -r''/r$. Compute $K$ for $r(s) = \sin s$ and for $r(s) = e^{-s}$ with $s > 0$. Which surfaces are these?

22. • The ellipse $(2 \cos t, \sin t)$ has the curvature $\kappa(t) = 2 / (4 \sin^2 t + \cos^2 t)^{3/2}$. Find its largest and smallest curvature. For which distances $d$ does the inward [offset curve](/offset-curve/) at distance $d$ have cusps?

23. ★ For a closed mesh with Euler characteristic $\chi$ in which every vertex has valence at least 3, show from $V - E + F = \chi$ that $\sum_v (4 - \operatorname{val} v) = 4\chi$ when every face is a quad and $\sum_v (6 - \operatorname{val} v) = 6\chi$ when every face is a triangle. Deduce that a closed quad mesh of genus 0 has at least 8 vertices of valence 3, and that a closed triangle mesh of genus 0 has at least 4 vertices of valence less than 6. Which meshes reach these bounds? This is why a [subdivision surface](/subdivision-surface/) of a sphere cannot avoid extraordinary vertices.

24. ★ A Catmull-Clark step on a closed mesh with $V$ vertices, $E$ edges and faces with $n_f$ sides gives $V + E + F$ vertices, $2E + \sum_f n_f$ edges and $\sum_f n_f$ faces. Show that on a closed quad mesh with $F$ faces and Euler characteristic $\chi$, after $k$ steps $F_k = 4^k F$, $E_k = 2 \cdot 4^k F$ and $V_k = \chi + 4^k F$. Then show that on any closed mesh the number of extraordinary vertices after the first step equals the number of old extraordinary vertices plus the number of faces that are not quads, and that later steps do not change it.

25. ★ Let $B_n f$ be the Bernstein polynomial of $f$ from the [Bernstein approximation theorem](/bernstein-approximation-theorem/). Show that $B_n(x^3) = x^3 + \tfrac{3 x^2 (1 - x)}{n} + \tfrac{x (1 - x)(1 - 2x)}{n^2}$, and give the order of the error $|B_n(x^3) - x^3|$ as $n \to \infty$.

26. ★ The four-point scheme inserts $\left(-P_{-1} + 9 P_0 + 9 P_1 - P_2\right)/16$ between $P_0$ and $P_1$ when $w = \tfrac1{16}$. Show that this is the value at $\tfrac12$ of the cubic that interpolates the data at $-1, 0, 1, 2$, so that samples of any cubic stay on that cubic. Compute the inserted value for samples of $x^4$ and its error, and compare with the interpolation error formula.

27. ★ In [quadric error metrics](/quadric-error-metrics/) a contracted vertex carries the planes $x = 0$, $y = 0$, $z = 0$ and $x + y + z = 3$, each with weight 1 and unit normal. Find the position that minimizes the sum of squared distances to the four planes, and its cost. What happens to the $3 \times 3$ system when only the planes $x = 0$ and $y = 0$ are present?
