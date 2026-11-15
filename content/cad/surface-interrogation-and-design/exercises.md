1. ◦ Project $p = (2, 0)$ onto the unit circle $r(t) = (\cos t, \sin t)$. Show that $(r - p) \cdot r' = 2 \sin t$, so that a [Newton](/newton-point-inversion/) step on this equation is $t \mapsto t - \tan t$. Run three steps from $t_0 = 1$ and three from $t_0 = 2$. Which point of the circle does each run approach, and which of them is the foot point?

2. ◦ Join the half line $y = 0$, $x \le 0$, at the origin to the arc $y = x^2$, $x \ge 0$, and in a second drawing to $y = x^3$, $x \ge 0$. Draw the [curvature comb](/curvature-comb/) of each join with scale $s$. In which drawing does the tip curve jump, and by how much? Which join is $G^2$?

3. ◦ On the cylinder $x^2 + z^2 = 1$ with the light direction $l = (0, 0, 1)$, find the [isophote](/isophote/) of level $c$ for $c = 0.9$, $0.8$ and $0.7$. Then show that for every light direction the isophotes of the cylinder are unions of rulings, and explain why the same holds on every [developable surface](/developable-surface/).

4. ◦ Let $a(u, v) = (u, v, 0)$. Test the two patches $b(u, v) = (1 + u,\ v - u,\ u v)$ and $b(u, v) = (1 + 3u,\ v + 2u,\ u^2)$ against $a$ with the condition of [tangent plane continuity](/tangent-plane-continuity/) along the common edge $(1, v, 0)$. For the patch that passes, give $\alpha$ and $\beta$ and a reparametrization that makes the join $C^1$. For the other, find where along the edge the tangent planes agree.

5. ◦ [Implicitize](/implicitization/) the curve $(t^2 - 1,\ t^3 - t)$ by eliminating $t$ from $x - t^2 + 1 = 0$ and $y - t^3 + t = 0$. Which parameter values map to the origin, and what are the two tangent lines there?

6. ◦ A cone has base radius $3$ and height $4$. Unroll it: give the radius and the angle of the sector. Cut the cone at half its height and give the annular sector of the lower part, with the lengths of its two arcs.

7. ◦ Check that the cubic [Bézier curve](/bezier-curve/) with control points $(0, 0)$, $(1, 0)$, $(2, 1)$, $(2, 3)$ is a [Pythagorean hodograph curve](/pythagorean-hodograph-curve/), and compute its arc length. Compare it with the length of the control polygon and with the chord.

8. ◦ A patch of the unit sphere is the cap of angular radius $30°$ about $(0, 0, 1)$. A plane patch has a unit normal at the angle $40°$ from $(0, 0, 1)$. Does the [Sederberg-Meyers test](/sederberg-meyers-loop-detection/) exclude a closed loop of their intersection? Now tilt the plane to $20°$. Show that the test fails, and find a plane with that normal that cuts the sphere patch in a closed loop.

9. ◦ A setback [vertex blend](/vertex-blend/) at the corner of a cube leaves a hole with six sides. Count the control points of a [generalized Bézier patch](/generalized-bezier-patch/) of degree $3$ over it, and of an S-patch of degree $3$ with six sides. Which is cheaper?

10. • Let $z(u, v) = u v (a u + b v) / (u + v)$ on $u, v \ge 0$, not both zero, with $z(0, 0) = 0$. Show that $z_v(u, 0) = a u$ and $z_u(0, v) = b v$, that the twist $z_{uv}$ is $a$ on the edge $v = 0$ and $b$ on the edge $u = 0$, and that it equals $(a + b)/2$ on the whole diagonal $u = v$. What does this say about [twist compatibility](/twist-compatibility/), and what is $z$ when $a = b$?

11. • Apply [Levin's method](/levin-quadric-intersection/) to the two cylinders $x^2 + y^2 = 1$ and $x^2 + z^2 = 1$. Find the roots of $\det(\alpha S_u + \beta T_u)$, decide which member of the pencil the method accepts, and parametrize the intersection. Where do the branches cross, and how do the two cylinders meet there?

12. • On the bump $z = 27 u (1 - u) v (1 - v)$ over $[0, 1]^2$, the plane $z = 1.68$ cuts a small loop with $u$ and $v$ in $[\tfrac12 - \tfrac1{30}, \tfrac12 + \tfrac1{30}]$. For which $N$ from $1$ to $20$ does [lattice evaluation](/lattice-evaluation-intersection/) with the lines $u = k/N$ and $v = k/N$ find the loop, if each line is searched for sign changes? Treat $N = 15$ with care.

13. • For the paraboloid of revolution $z = (x^2 + y^2)/2$, show that the [principal curvatures](/surface-curvature/) at distance $\rho$ from the axis are $1/(1 + \rho^2)^{3/2}$ along the meridian and $1/(1 + \rho^2)^{1/2}$ along the parallel. Find all [umbilic points](/umbilic-point/) and describe the [lines of curvature](/lines-of-curvature/).

14. • On the cone of exercise 6, find the shortest path on the surface between two points of the base circle that lie on opposite sides of the axis. Compare its length with half the base circle and with the path through the apex, and find how close to the apex it comes.

15. • On the paraboloid $r(u, v) = (u \cos v, u \sin v, u^2/2)$, a [geodesic](/geodesics-on-parametric-surfaces/) from $r(1, 0)$ to $r(1, \pi/2)$ found by shooting starts with $(u', v') = (-0.582864, 1.236313)$. Show that its speed is $1.485911$, and use Clairaut's relation, that $u^2 v' / |r'|$ is constant along a geodesic of a surface of revolution, to predict the smallest value of $u$ on it without integrating.

16. • Run the [interval projected polyhedron](/interval-projected-polyhedron/) method by hand on $f(t) = t^2 - \tfrac12$ over $[0, 1]$. Write $f$ in the [Bernstein basis](/bernstein-polynomials/), cut the convex hull of the control points with the axis, restrict $f$ to the new interval and repeat once. Give the two intervals and their widths, and say what the widths show about the rate of convergence.

17. • Offset the parabola $y = x^2$ by $d = 1$ toward its concave side. Find the parameters and the points where the offset has cusps, and the point where it crosses itself. Which piece does [offset trimming](/offset-trimming/) remove?

18. • A globe of radius $100$ mm is to be covered by gores that are pieces of cylinders, as in [developable surface approximation](/developable-surface-approximation/). How many strips are needed for an error of at most $0.5$ mm with tangent cylinders, and with secant cylinders that halve the error? Compare with the estimate $\pi \sqrt{R / 2\varepsilon}$.

19. • In exercise 1, let $t^* \approx 1.1656$ be the root of $\tan t = 2t$ in $(0, \pi/2)$. Show that Newton converges to $t = 0$ from every start with $|t_0| < t^*$, and find the limit of the run from $t_0 = 1.17$.

20. • Show that the tangent surface $r(t, v) = c(t) + v\, c'(t)$ of the twisted cubic $c(t) = (t, t^2, t^3)$ has the same normal along each ruling, so it is [developable](/developable-surface/). Give that normal, and find where the surface is not regular.

21. ★ Show that every [PH cubic](/pythagorean-hodograph-curve/) that is not a straight line is similar to a piece of the curve $(s^3/3 - s,\ s^2)$, the Tschirnhausen cubic.

22. ★ A cone unrolls to a sector of angle $\Theta = \pi/2$. Two points lie on one ruling at distances $1$ and $2$ from the apex. Find all geodesics between them and their lengths. In general, show that the geodesics between two points at the developed angle $\theta$ correspond to the integers $k$ with $|\theta + k \Theta| < \pi$.

23. ★ Let $c$ be a closed convex $C^2$ curve with curvature $\kappa > 0$, and let $d < 1/\max \kappa$. Prove that the inner offset at distance $d$ is a simple closed convex curve, so that [offset trimming](/offset-trimming/) has nothing to remove. For the ellipse $x^2/4 + y^2 = 1$, find the largest such $d$ and the points where the first cusps appear.

24. ★ Let $r(u_0, v_0)$ be a foot point of $p = r(u_0, v_0) + h N$ with unit normal $N$. Show that the Hessian of $\tfrac12 |r - p|^2$ there is the first [fundamental form](/fundamental-forms/) minus $h$ times the second, and conclude that the foot point is a strict local minimum of the distance when $1 - h \kappa_1 > 0$ and $1 - h \kappa_2 > 0$. Apply this to the saddle $r(u, v) = (u, v, u v)$ and $p = (0, 0, h)$.

25. ★ In lattice evaluation, let a closed loop of $g = 0$ in the parameter square be a regular level curve with $\nabla g \ne 0$. Prove that if its extent in $u$ is longer than $1/N$, some line $u = k/N$ shows a sign change of $g$, so the loop is found. Use the [Jordan curve theorem](/jordan-curve-theorem/).
