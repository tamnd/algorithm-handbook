1. The perpendicular bisector of $ab$ is $x = 4$, and $|o - a| = |o - c|$ gives $o = (4, 2)$ and $R^2 = 20$. The orientation determinant is $D = 48$. Then $I(a, b, c, d) = 336 = 48 \cdot (20 - 13)$, so $d$ is inside, and $I(a, b, c, e) = -288 = 48 \cdot (20 - 26)$, so $e$ is outside.

3. The plane through $(0,0,0)$, $(5,0,25)$ and $(6,4,52)$ is $z = 5x + \tfrac{11}{2} y$. Above $d$ it has height $33/2$, while $d^+ = (0, 3, 9)$ lies lower, so $a^+ b^+ c^+$ is not a lower face and the Delaunay diagonal is $bd$. The in-circle test agrees: $I(a, b, c, d) = 150 > 0$.

4. The parabolas are $y = (x^2 + 64)/16$ and $y = ((x - 7)^2 + 1)/2$. They meet at $(4, 5)$ and $(12, 13)$, and both points are $5$ and $13$ away from $p$, from $q$ and from the sweep line. The arc of $q$ is lower between them, so the arcs are $p$, $q$, $p$.

8. For $k = 1$ the cells are separated at $1/2$, $2$ and $5$. For $k = 2$ the cells are $\{0, 1\}$ for $x < 3/2$, $\{1, 3\}$ for $3/2 < x < 4$ and $\{3, 7\}$ for $x > 4$; each boundary is the midpoint of the site that leaves and the site that enters. For $k = 3$ the cells $\{0, 1, 3\}$ and $\{1, 3, 7\}$ meet at $7/2$, the midpoint of $0$ and $7$, and the farthest site is $7$ to the left of it and $0$ to the right.

10. All eight corners meet at one Voronoi vertex, the center, of degree $8$, so $X = 5$, and with $n = h = 8$ the formulas give $2n - 2 - h - X = 1$ vertex and $3n - 3 - h - X = 8$ edges, all rays. With the center added, the eight corners are still cocircular, but their circle contains the center, so no four sites lie on an empty circle; $n = 9$ and $h = 8$ give $8$ vertices and $16$ edges.

12. The power bisector of $a$ and $m$ is $x = (4 - w)/4$ and that of $m$ and $b$ is $x = (12 + w)/4$. The cell of $m$ is the strip between them, of width $2 + w/2$, which is empty for $w < -4$ and a single line for $w = -4$. A site with an empty cell is redundant and is not a vertex of the regular triangulation.

14. The candidates are the Voronoi vertices inside the square, $(41/8, 3)$, $(3, 1/6)$ and $(3, 35/6)$ (the fourth vertex, $(-5/4, 3)$, lies outside), the points where Voronoi edges cross the sides of the square, and the corners, which are sites. The vertex $(41/8, 3)$ wins with radius $25/8$; the circle passes through $(2,3)$, $(6,0)$ and $(6,6)$. The other two vertices give radius $\sqrt{325}/6 \approx 3.005$, and the best boundary points give $3$.

16. The circle through the three sites has center $(2, 1)$ and radius $5$, so the event fires when the sweep reaches $y = -4$. The site $(2, -2)$ is only $3$ from the center, so the circle is not empty and $(2, 1)$ is not a Voronoi vertex. Its site event comes first, at $y = -2$; the new arc falls on the arc of $(5,5)$ and splits it, so the queued event is deleted as a false alarm.

18. The circle with diameter $pq$ has the midpoint $m$ of $pq$ as center and $|pq|/2$ as radius. It holds no other site inside exactly when no site is nearer to $m$ than $p$ and $q$ are, that is, when $m$ lies on the Voronoi edge of $p$ and $q$. The bisector meets the line $pq$ only at $m$.

21. The two fans share no diagonal, and each flip creates one edge, so the $n - 3$ diagonals of the final fan at $(1, 1)$ need at least $n - 3$ flips. For the upper bound, a Delaunay edge is never flipped away, and by the lifting argument a removed edge never comes back. So every flip removes a different one of the $n(n - 3)/2 - (n - 3)$ diagonals that are not Delaunay.

22. A circle $x^2 + y^2 + Dx + Ey + F = 0$ meets $y = x^2$ where $x^4 + (1 + E) x^2 + Dx + F = 0$, which has no cubic term, so its four roots add up to $0$. The circle through the first three points meets the parabola again at $s = -(x_1 + x_2 + x_3)$, and the parabola is inside the circle between $x_3$ and $s$ when $s > x_3$. So $x_4$ is inside exactly when $x_4 < s$, that is, when the sum is negative. For $-5, -2, 1, 3$ the sum is $-3$ and the diagonal is $x_2 x_4$. With positive numbers the sum is always positive, every triangle is a fan triangle at the smallest number, and the triangles list the numbers in sorted order.

23. The cell boundary is $m = (z_1 + z_2)/2$, and the centroids of $[0, m]$ and $[m, 1]$ under the density $2x$ are $2m/3$ and $\tfrac{2}{3}(1 + m + m^2)/(1 + m)$. Setting $m$ to their average gives $m^2 + m - 1 = 0$, so $m = (\sqrt{5} - 1)/2 \approx 0.618$, and then $z_1 = 2m/3 \approx 0.412$ and $z_2 = 4m/3 \approx 0.824$.

24. A tetrahedron with three vertices on one line is flat, and one that skips a point of a line has that point on an edge, so every tetrahedron is $a_i a_{i+1} b_j b_{j+1}$, of volume $1/6$. The convex hull has volume $(m - 1)^2/6$, so there are $(m - 1)^2$ tetrahedra, one for each pair $(i, j)$, and every pair $a_i b_j$ is an edge.
