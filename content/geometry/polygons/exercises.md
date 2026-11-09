1. ◦ Let $u = (2, 5)$ and $v = (-3, 4)$. Compute the [cross product](/cross-product/) $u \times v$ and the [dot product](/dot-product/) $u \cdot v$. Is the turn from $u$ to $v$ clockwise or counterclockwise, and is the angle between them acute or obtuse?

2. ◦ Let $p = (1, 1)$, $q = (4, 2)$ and $r = (x, 5)$. Write the [orientation test](/orientation-test/) of $p, q, r$ as a function of $x$. For which $x$ are the points collinear, and for which does $p \to q \to r$ turn left?

3. ◦ For the triangle $a = (1, 1)$, $b = (4, 2)$, $c = (2, 6)$, compute twice its [signed area](/oriented-triangle-area/) and say whether it is listed counterclockwise. Then find the barycentric coordinates of $p = (2, 3)$ as ratios of signed areas, and decide whether $p$ lies inside.

4. ◦ The pentagon $v_0 = (1,0)$, $v_1 = (5,1)$, $v_2 = (4,4)$, $v_3 = (2,3)$, $v_4 = (0,5)$ is simple. (a) Find its area with the [shoelace formula](/shoelace-formula/). (b) Decide its [orientation](/polygon-orientation/) from the orientation test at the lowest vertex alone. (c) Which vertex is reflex? (d) Count its boundary lattice points $B$ and use [Pick's theorem](/picks-theorem/) to get the number $I$ of interior lattice points.

5. ◦ Run the [crossing number algorithm](/crossing-number-algorithm/) with a ray to the right and the half-open rule on the pentagon of Exercise 4, for the query points $(2,2)$ and $(3,4)$. How many edges does each ray cross, and what is the answer? Which vertex does the second ray pass through, and why does the half-open rule give the right count there?

6. ◦ (a) How many guards does the [art gallery theorem](/art-gallery-theorem/) promise for a simple polygon with 12 vertices, and with 14? (b) How many reflex vertices has a [rectilinear polygon](/rectilinear-polygon/) with 12 vertices, and what is $\lfloor n/4 \rfloor$ for it? (c) A polygon has 3 reflex vertices. What is the most pieces [Hertel-Mehlhorn](/hertel-mehlhorn/) can return, and what lower bound holds for the fewest convex pieces?

7. ◦ Compute the [Minkowski sum](/minkowski-sum-convex-polygons/) of the unit square $[0,1]^2$ and the triangle $(0,0), (2,0), (0,2)$ by merging edge directions. List its vertices counterclockwise and give its area.

8. • Let $a = (1, 1)$, $b = (7, 4)$ and $p = (4, 7)$. Using only dot and cross products, find the [projection](/point-projection-and-reflection/) of $p$ onto the line $ab$, the distance from $p$ to the line, and the reflection of $p$ in the line.

9. • (a) The square $(0,0), (2,0), (2,2), (0,2)$ is listed twice in a row as one closed polygon with 8 vertices. What does the [winding number](/winding-number-algorithm/) give at $(1,1)$, what does the crossing number give, and what does the shoelace sum $\sum v_i \times v_{i+1}$ return? (b) At the center of the regular star heptagons $\{7/2\}$ and $\{7/3\}$, what are the winding numbers, and what do the even-odd and nonzero rules say?

10. • Clip the triangle $(0,0), (6,0), (0,6)$ to the window $[1,4]^2$ with [Sutherland-Hodgman](/sutherland-hodgman/), in the order left, right, bottom, top. Give the vertex list after all four passes and the area of the result.

11. • The L-shaped hexagon $v_0 = (0,0)$, $v_1 = (4,0)$, $v_2 = (4,2)$, $v_3 = (2,2)$, $v_4 = (2,4)$, $v_5 = (0,4)$ is triangulated by the fan of diagonals from $v_3$. Run [Hertel-Mehlhorn](/hertel-mehlhorn/), trying the diagonals in the order $v_3 v_5$, $v_3 v_0$, $v_3 v_1$. Which diagonals are removed, and what pieces remain? Is the result optimal?

12. • Find the [kernel](/polygon-kernel/) of the L-shaped hexagon $(0,0), (6,0), (6,3), (3,3), (3,6), (0,6)$ and its area. Which edges cut it down?

13. • In the hexagon of Exercise 12, find the [shortest path inside the polygon](/euclidean-shortest-path-in-polygon/) from $(5,2)$ to $(2,5)$ and its length.

14. • Describe the [straight skeleton](/straight-skeleton/) of the rectangle $[0,6] \times [0,2]$: its inner nodes, its arcs and their total length. Check the counts of $n - 2$ inner nodes and $2n - 3$ arcs.

15. • Let $P = [0,2]^2$ and $Q$ the triangle $(3,0), (5,0), (3,2)$. Compute $P \oplus (-Q)$. Use it to decide whether $P$ and $Q$ intersect, and find the distance between them.

16. • Prove that a rectilinear polygon with $n$ vertices has exactly $(n - 4)/2$ reflex vertices, and conclude that $n$ is even.

17. • Let $f(n, m, a, b) = \sum_{i=0}^{n-1} \lfloor (a i + b)/m \rfloor$. Compute $f(5, 3, 2, 1)$ directly. Then apply one step of the reduction used for [lattice points in a non-lattice polygon](/lattice-points-in-non-lattice-polygon/), $f(n, m, a, b) = f(\lfloor y/m \rfloor, a, m, y \bmod m)$ with $y = an + b$, and check that the new sum has the same value.

18. ★ A lattice polygon $P$ is cut by a diagonal $d$ into lattice polygons $P_1$ and $P_2$, and $d$ has $c$ lattice points strictly between its endpoints. Express $I$ and $B$ for $P$ in terms of $I_1, B_1, I_2, B_2$ and $c$, and show that if Pick's theorem holds for $P_1$ and $P_2$ then it holds for $P$.

19. ★ Compute $P \oplus (-P)$ for the triangle $P = (0,0), (2,0), (0,1)$, and compare its area with the area of $P$. Then prove that for every convex polygon $P$ with $n$ vertices, $P \oplus (-P)$ is centrally symmetric and has at most $2n$ vertices, with exactly $2n$ when no two edges of $P$ are parallel.

20. ★ Derive the centroid of a simple polygon from the triangle fan at the origin: show that $C_x = \frac{1}{6A} \sum_i (x_i + x_{i+1})(x_i y_{i+1} - x_{i+1} y_i)$, with the matching formula for $C_y$, where $A$ is the signed area. Apply it to the L-shaped hexagon of Exercise 11.

21. ★ Count the lattice points in the closed triangle with vertices $(0,0)$, $(100/3, 0)$ and $(0, 25)$, that is, the integer solutions of $x, y \ge 0$, $3x + 4y \le 100$. Write the count as a floor sum and evaluate it with the reduction of Exercise 17, then check it by another method.
