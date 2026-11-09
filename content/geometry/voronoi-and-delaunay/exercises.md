1. ◦ Let $a = (0,0)$, $b = (8,0)$ and $c = (2,6)$. Find the [circumcenter](/circumcenter/) $o$ and the radius $R$ of the [circumcircle](/circumcircle/) of $abc$. Then evaluate the [in-circle](/in-circle-test/) determinant $I(a, b, c, d)$ for $d = (7,4)$ and for $e = (9,1)$, and check both values against $I = D(a, b, c)(R^2 - |d - o|^2)$, where $D(a, b, c)$ is the orientation determinant.

2. ◦ Ten sites in general position have $6$ sites on the boundary of their convex hull. How many vertices, edges and unbounded edges has their [Voronoi diagram](/voronoi-diagram/), and how many of its cells are bounded? How many triangles and edges has their [Delaunay triangulation](/delaunay-triangulation/)? What is the average number of edges of a [Voronoi cell](/voronoi-cell/)?

3. ◦ The quadrilateral $a = (0,0)$, $b = (5,0)$, $c = (6,4)$, $d = (0,3)$ is convex. Use the [lifting map](/paraboloid-lifting-map/) to decide which diagonal, $ac$ or $bd$, gives the Delaunay triangulation: find the plane through the lifted points $a^+, b^+, c^+$ and compare its height above $d$ with the height of $d^+$.

4. ◦ The sweep line is $y = 0$ and the sites $p = (0,8)$ and $q = (7,1)$ lie above it. Write the parabolas of the two sites, find the two breakpoints of the [beach line](/beach-line/), and give the order of its arcs from left to right.

5. ◦ In a [power diagram](/power-diagram/), the site $p = (0,0)$ has weight $4$ and the site $q = (6,0)$ has weight $0$. Find the line that separates their cells, and compare it with the ordinary bisector.

6. ◦ Three sites $1/10$, $2/10$ and $9/10$ lie on the interval $[0, 1]$ with uniform density. Carry out one step of [Lloyd's algorithm](/lloyds-algorithm/) and compute the energy $\int_0^1 \min_i (x - z_i)^2 \, dx$ before and after the step. Which [centroidal tessellation](/centroidal-voronoi-tessellation/) does the iteration approach, and what is its energy?

7. ◦ A set has $8$ sites in general position, $5$ of them corners of the convex hull and $3$ inside it. How many cells, vertices and edges has its [farthest-point Voronoi diagram](/farthest-point-voronoi-diagram/)? How many of the edges are rays?

8. ◦ The four sites $0$, $1$, $3$ and $7$ lie on the $x$-axis. Give the cells of the [order-$k$ Voronoi diagram](/order-k-voronoi-diagram/) for $k = 1, 2, 3$, with the $x$-coordinates of the lines that separate them. Check that the order-3 diagram is the farthest-point diagram.

9. ◦ Describe the [medial axis](/medial-axis/) of the rectangle $[0, 6] \times [0, 2]$ and compute its total length. Give the length for $[0, a] \times [0, b]$ with $a \ge b$.

10. • The eight corners of a regular octagon lie on one circle. Use the size formula with the excess $X = \sum (k_x - 3)$ over Voronoi vertices of degree $k_x$ to count the vertices and edges of their Voronoi diagram. Then add the center of the octagon as a ninth site and count again.

11. • How many Delaunay triangulations has the set of corners of a regular octagon? How many triangles has each, and what does the [uniqueness theorem](/delaunay-triangulation-uniqueness/) say about this set?

12. • In a power diagram, the sites $a = (0,0)$ and $b = (4,0)$ have weight $0$ and the site $m = (2,0)$ has weight $w$. Find the cell of $m$ on the $x$-axis as a function of $w$. For which $w$ is the cell of $m$ empty, and what happens to $m$ in the [regular triangulation](/regular-triangulation/)?

13. • In the multiplicatively [weighted Voronoi diagram](/weighted-voronoi-diagram/) with distance $|x - p|/w_p$, the site $p = (0,0)$ has weight $2$ and $q = (6,0)$ has weight $1$. Find the curve that separates their cells. Which cell is bounded, even though both sites are on the hull?

14. • Find the [largest empty circle](/largest-empty-circle/) of the sites $(0,0)$, $(6,0)$, $(6,6)$, $(0,6)$, $(2,3)$, with center in the square $[0, 6]^2$. Give its center, its radius and the sites on it.

15. • The Delaunay triangulation of $(0,0)$, $(6,0)$, $(6,6)$, $(0,6)$, $(2,3)$ has four triangles. List them. Then insert $(3,1)$ with the [Bowyer-Watson algorithm](/bowyer-watson-algorithm/): which triangles form the cavity, how many triangles replace them, and how many triangles does the new triangulation have?

16. • The sites $(-2,4)$, $(5,5)$ and $(7,1)$ have consecutive arcs, in this order from left to right, on the beach line of [Fortune's algorithm](/fortunes-algorithm/), and a circle event is queued for them. At which position of the sweep line does it fire, and which Voronoi vertex would it create? The input also contains the site $(2,-2)$. What happens to the event?

17. • Show that if $q$ is a nearest neighbour of the site $p$, then $pq$ is an edge of the Delaunay triangulation. Name an empty circle through $p$ and $q$.

18. • A Delaunay edge $pq$ is a Gabriel edge when the circle with diameter $pq$ holds no other site inside. Show that $pq$ is a [Gabriel edge](/gabriel-graph/) if and only if its dual Voronoi edge meets the segment $pq$, and that it then meets it at the midpoint.

19. • For $a = (0,0)$, $b = (5,1)$, $c = (10,0)$, $d = (5,-12)$, which diagonal of the convex quadrilateral $abcd$ is Delaunay? Compare the lengths of the two diagonals and the smallest angles of the two triangulations. What does this say about the triangulation of least total edge length?

20. • Show that computing the [Euclidean minimum spanning tree](/euclidean-minimum-spanning-tree/) of $n$ points takes $\Omega(n \log n)$ time in the [algebraic decision tree](/algebraic-decision-tree/) model, by a reduction from sorting.

21. ★ Let $P$ be the points $(i, i^2)$ for $i = 1, \ldots, n$, and start [Lawson's algorithm](/lawson-flip-algorithm/) from the fan triangulation whose diagonals all end at $(n, n^2)$. Show that every run, whatever the order of the flips, makes at least $n - 3$ and at most $(n - 2)(n - 3)/2$ flips. For $n = 6$ these bounds are 3 and 6, and runs with each count exist.

22. ★ Four points $(x_i, x_i^2)$ lie on the parabola, with $x_1 < x_2 < x_3 < x_4$. Show that they are cocircular if and only if $x_1 + x_2 + x_3 + x_4 = 0$, and that the Delaunay diagonal is $x_1 x_3$ when the sum is positive and $x_2 x_4$ when it is negative. Which diagonal do the numbers $-5, -2, 1, 3$ give, and why does the [lower bound](/voronoi-construction-lower-bound/) use positive numbers?

23. ★ Two sites $z_1 < z_2$ lie in $[0, 1]$ with density $\rho(x) = 2x$. Find the centroidal Voronoi tessellation: the sites and the boundary $m$ between the two cells.

24. ★ Put $m$ points $(i, 0, 0)$ and $m$ points $(0, j, 1)$, for $i, j = 1, \ldots, m$, on two skew lines in space. Show that every tetrahedralization of these $n = 2m$ points, the [Delaunay tetrahedralization](/higher-dimensional-delaunay/) among them, has $(m - 1)^2$ tetrahedra and $m^2 + 2(m - 1)$ edges, so the size is $\Theta(n^2)$.
