1. ◦ For the triangle $(0,0), (4,0), (0,3)$, compute the circumradius $R$, the shortest edge, the [radius-edge ratio](/radius-edge-ratio/) $\rho$ and the smallest angle. Check that $\rho = 1/(2\sin\theta_{\min})$. Then compute the mean ratio $4\sqrt3 A/\sum \ell_i^2$ and the radius ratio $2r/R$ from the [mesh quality measures](/mesh-quality-measures/).

2. ◦ Compute the [scaled Jacobian](/scaled-jacobian/) of the quadrilateral $(0,0), (3,0), (2,2), (0,1)$, taken in that order: at each corner, the cross product of the two edge vectors divided by the product of their lengths, and then the minimum. At which corners is the minimum reached, and is the bilinear map of this quad one to one?

3. ◦ A circle of radius $2$ is to be split into equal chords whose distance from the arc is at most $\delta = 0.01$. What angle may each chord span, how long is each chord, and how many edges are needed? Use the chord deviation rule of the [mesh sizing function](/mesh-sizing-function/).

4. ◦ A [boundary layer mesh](/boundary-layer-mesh-generation/) starts with a first layer of height $h_1 = 0.001$ and grows each layer by the ratio $r = 1.25$. How many layers are needed before the total height reaches $0.05$? Give the total heights after the last two layers.

5. ◦ Take the boundary of a cube and split one face into two quadrilaterals, so that the sphere is covered by 7 quads. Show that no [hexahedral mesh](/hexahedral-mesh-generation/) of the ball has this boundary. What is the smallest change to the boundary mesh that removes the obstruction, and which theorem then gives a hex mesh?

6. ◦ For the structured $2 \times 4 \times 5$ grid of hexahedra, count the sheets and chords of the [spatial twist continuum](/spatial-twist-continuum/), the hexes $H$, the boundary quads $B$ and the interior quads $I$. Check $6H = 2I + B$.

7. ◦ In [topological improvement](/topological-tetrahedral-mesh-improvement/), an interior edge lies in 6 tetrahedra. Edge removal deletes the edge and retriangulates the ring of its neighbours. How many tetrahedra replace the 6, and among how many triangulations of the ring does the dynamic program choose?

8. ◦ On the segment $[0, 10]$, the size must be $0.1$ at $x = 0$, may never exceed $2$, and must be $\tfrac12$-Lipschitz. Write the largest such size function, find where it reaches $2$, and estimate the number of edges as $\int_0^{10} dx/h(x)$. Compare with a uniform mesh of size $0.1$.

9. ◦ A source face with 40 quads and 52 nodes, 22 of them on its boundary, is swept through 12 layers by [hexahedral sweeping](/hexahedral-sweeping/). How many hexes and nodes does the mesh have? How many quads lie on the source, target and linking sides together, and how many inside? Check the counts of the source face with Euler's formula $V - E + F = 1$ for a disk.

10. • The quadratic $f = 4x^2 + y^2$ is interpolated on the unit square with error at most $\varepsilon = 1/50$. Build the metric $M = |H|/(8\varepsilon)$ of [anisotropic mesh adaptation](/anisotropic-mesh-adaptation/), give the edge lengths in the two axis directions, and estimate the number of unit triangles in the metric. Compare with an isotropic mesh that meets the same error.

11. • For the quadrilateral $(0,0), (3,0), (3,1), (0,2)$, compute the error $\int (f_I - f)$ of the linear interpolant of $f = x^2 + y^2$ for both diagonals, using the formula $\frac{|\tau|}{12}\sum \ell_i^2$ for one triangle from the [optimal Delaunay triangulation](/optimal-delaunay-triangulation/). Which diagonal is Delaunay, and which has the larger smallest angle?

12. • Two tetrahedra share the triangle $a = (0,0,0)$, $b = (1,0,0)$, $c = (0,1,0)$ and have apexes $d = (\tfrac13, \tfrac13, 1)$ and $e = (\tfrac13, \tfrac13, -1)$. Compute the volumes of $abde$, $bcde$ and $cade$ after a 2-3 flip and check that they add up to the old volume. Repeat with $e = (2, 2, -1)$ and explain why the flip is now invalid.

13. • A tetrahedron of the body-centred cubic lattice used by [isosurface stuffing](/isosurface-stuffing/) has the vertices $(0,0,\tfrac12)$, $(0,0,-\tfrac12)$, $(\tfrac12,\tfrac12,0)$, $(\tfrac12,-\tfrac12,0)$, two cube centres and two corners of a unit cube. Compute its edge lengths, circumradius, radius-edge ratio, volume and dihedral angles. How many such tetrahedra are there per cube?

14. • A polygon with $B$ boundary edges is meshed with quadrilaterals, with $V_i$ interior vertices and no extra boundary vertices. Use Euler's formula and $4Q = 2E_{\mathrm{int}} + B$ to show $Q = V_i + B/2 - 1$. Check it on a $4 \times 4$ grid of a square.

15. • Show that a triangulation of a polygon with $B$ boundary edges and $V_i$ interior vertices has $T = B + 2V_i - 2$ triangles. What does this say about a perfect matching of the dual graph in [Blossom-Quad](/blossom-quad/)? Apply it to a regular pentagon split into five triangles around its centre.

16. • A channel of width $0.1$ has walls on both sides, and each wall grows boundary layers with $h_1 = 0.001$ and $r = 1.2$. After how many layers do the two stacks meet? How many full layers fit on each side?

17. • The triangle $(-1,0), (1,0), (0,\varepsilon)$ has a largest angle near $180°$. Compute the linear interpolant $p$ of $u = x^2$ on it, and the error $|\nabla(u - p)|$. Do the same for the right triangle $(0,0), (1,0), (0,\varepsilon)$, which has a small angle but no large one. Relate the result to the [maximum angle condition](/maximum-angle-condition/).

18. • A mesh conforms to an $L$-Lipschitz sizing function with constants $c_1 = \tfrac12$, $c_2 = 1$ and $L = \tfrac12$. Bound the ratio of the lengths of two edges joined by a path of 3 edges, and by a path of 10 edges.

19. • Evaluate Shewchuk's constants $D_T$, $D_F$ and $D_S$ of [tetrahedral Delaunay refinement](/tetrahedral-delaunay-refinement/) at $B = 2.5$, $3$ and $4$. What lower bound on edge length near a vertex $v$ does each give, and what happens as $B$ approaches $2$?

20. • Pillowing adds one layer of hexes between a hex mesh and its boundary, one new hex for each boundary quad. Pillow the $2 \times 2 \times 2$ grid. Count the hexes, the boundary quads and the interior quads before and after, and check $6H = 2I + B$ both times.

21. ★ Around a point where the size is $h_0$, a sizing function grows as $h(r) = h_0 + Lr$ out to radius 1. The number of triangles is about $\int dA/h^2$ times $4/\sqrt3$. Compute it in closed form for $L = \tfrac12$, show that it grows like $\log(1/h_0)$, and give values for $h_0 = 10^{-2}, 10^{-3}, 10^{-4}$. Compare with a uniform mesh of size $h_0$. What is the growth in three dimensions?

22. ★ In three dimensions the number of unit tetrahedra in a metric $M$ is proportional to $\int \sqrt{\det M}$. For a quadratic whose Hessian has eigenvalues $\lambda_1 \le \lambda_2 \le \lambda_3$, find the ratio of the anisotropic count to the isotropic count at the same error, and evaluate it for $\lambda = 1, 100, 10^4$.

23. ★ For the quadrilateral of Exercise 11, show that the difference of the two interpolation errors equals the volume of the tetrahedron spanned by the four points lifted to the paraboloid $z = x^2 + y^2$. Compute that volume, and explain with the [lifting map](/paraboloid-lifting-map/) why the Delaunay diagonal always gives the smaller error.

24. ★ Let $T(t)$ have the vertices $(0,0,0)$, $(1,0,0)$, $(1,1,0)$, $(0,1,t)$. Compute its circumradius, radius-edge ratio and volume as functions of $t$, and the dihedral angle at the edge from $(0,0,0)$ to $(1,0,0)$. Show that every bound $B \ge 2$ of Delaunay refinement accepts $T(t)$ for small $t$, while its smallest dihedral angle tends to $0$. Give the numbers for $t = 0.1$.

25. ★ A free vertex $p$ is joined to the five vertices of the pentagon $(-2,-2), (2,-2), (2,2), (0,0), (-2,2)$, which has a reflex corner at the origin. Find the kernel, the set of positions where all five triangles have positive area. Find the position that maximizes the smallest triangle area, the problem solved by the linear program of [mesh untangling](/mesh-untangling/), and its value. Where does Laplacian smoothing put $p$, and what goes wrong there?
