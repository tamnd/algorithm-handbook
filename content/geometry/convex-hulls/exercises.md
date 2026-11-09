1. ◦ Compute the [orientation test](/orientation-test/) $D(p, q, r)$ for $p = (2, 1)$, $q = (5, 3)$, $r = (3, 6)$. Is $p, q, r$ a left turn or a right turn, and what is the area of the triangle? Then compute $D(p, q, r')$ for $r' = (8, 5)$. Does $r'$ lie on the segment $pq$?

2. ◦ Let $a = (0, 0)$, $b = (4, 0)$ and $c = (0, 4)$. Write $q = (2, 1)$ as a [convex combination](/convex-combination/) of $a$, $b$, $c$. Do the same for $(2, 2)$ and for $(3, 3)$, or show that it cannot be done. Which of the three points lie inside the triangle, which on its boundary and which outside?

3. ◦ Run [Andrew's monotone chain](/andrew-monotone-chain/) on the ten points $(1,1)$, $(4,0)$, $(6,2)$, $(5,5)$, $(2,4)$, $(3,2)$, $(0,3)$, $(4,3)$, $(6,5)$, $(3,5)$. Give the lower hull, the upper hull and the hull. Is $(5, 5)$ a vertex of the hull?

4. ◦ Run the [Graham scan](/graham-scan/) on the ten points of exercise 3. Which point is the pivot? Two points make a tie in the angular sort; which ones, and in what order do they come? How many pops does the scan make in all?

5. ◦ Run [quickhull](/quickhull/) on the ten points of exercise 3. Give the points $a$ and $b$ of line L3, the sets $R$ and $U$ of line L4, and the farthest point chosen in each of the two first calls of FIND-HULL. Which points are dropped by the first call on $U$?

6. ◦ Let $Q$ be the convex quadrilateral with vertices $(0,0)$, $(6,0)$, $(7,3)$, $(2,5)$. Give its [support function](/support-function/) $h_Q(u)$ for $u = (1,0)$, $(-1,0)$, $(0,1)$ and $(0,-1)$, and its widths in the horizontal and the vertical directions. Then find its diameter and its width.

7. ◦ Give the vertices of the polygon $\{(x, y) : x \ge 0,\ y \ge 0,\ x + 2y \le 4,\ 2x + y \le 4\}$. Then describe the triangle with corners $(0,0)$, $(3,0)$, $(1,2)$ by three linear inequalities. Which theorem says that both kinds of description always exist for a bounded polygon?

8. ◦ Find a [Radon](/radon-theorem/) partition, and a point in both hulls, for each set of four points: $\{(0,0), (4,0), (0,4), (1,1)\}$; $\{(0,0), (2,0), (0,2), (2,2)\}$; $\{(0,0), (1,0), (2,0), (5,5)\}$.

9. ◦ Ten points in $\mathbb{R}^3$ are in general position and all of them are vertices of their hull. How many facets and how many edges does the hull have? The cube has 8 vertices but only 6 facets; why does this not contradict the bound $2n - 4$ of [the 3D hull](/convex-hull-3d/), and what do you get if you cut each square face into two triangles?

10. ◦ Find the [convex layers](/convex-layers/) of the nine points $(0,0)$, $(6,0)$, $(6,6)$, $(0,6)$, $(2,1)$, $(5,2)$, $(4,5)$, $(1,4)$, $(3,3)$. How does the number of layers compare with the bound $\lceil n/3 \rceil$?

11. • A convex polygon is given as an array of its $h$ vertices $v_0, \dots, v_{h-1}$ in counterclockwise order. Using only orientation tests, decide in $O(\log h)$ time whether a query point $q$ lies inside, on the boundary or outside.

12. • Prove that the lexicographically smallest point of a finite set $S$ is an [extreme point](/extreme-point/) of $S$. Then prove more generally that if a linear function $\langle u, x \rangle$ has a unique maximizer over $S$, that maximizer is extreme.

13. • Change Andrew's monotone chain so that it outputs every input point on the boundary of the hull, including the points in the middle of edges, each once, in counterclockwise order. Say what happens when all the points lie on one line, and how you handle it.

14. • Two convex polygons are given, with $h_1$ and $h_2$ vertices in counterclockwise order. Compute the hull of their union in $O(h_1 + h_2)$ time.

15. • In [Chan's algorithm](/chan-algorithm/) the round $t$ uses groups of $m = 2^{2^t}$ points, starting at $t = 1$. Suppose $n = 10^6$ and the upper hull has 20 vertices, and a round succeeds exactly when $m$ is at least 20. Which rounds run, and with which $m$? A round costs about $n \lg m$; compare the sum over the rounds with $n \lg 20$, and prove that in general the sum is less than $4 n \lg h$ for $h \ge 3$.

16. • A million points are drawn uniformly from a square. Use the formula of the [convex hull problem](/convex-hull-problem/) for points from a convex $k$-gon to estimate the expected number of hull vertices. The [Jarvis march](/jarvis-march/) makes about $nh$ orientation tests; Andrew's monotone chain makes about $n \lg n$ comparisons to sort and at most about $4n$ orientation tests. Which makes fewer basic steps here?

17. • [Melkman's algorithm](/melkman-algorithm/) finds the hull of a simple polyline in $O(n)$ time. Explain why this does not contradict the $\Omega(n \log n)$ [lower bound](/convex-hull-lower-bound/), which lifts numbers $x_i$ to the points $(x_i, x_i^2)$.

18. • Let $L = \{(0,0), (1,4), (3,2)\}$ and $R = \{(5,1), (6,5), (8,2)\}$. Find the upper and the lower bridge between the hulls of $L$ and $R$, as the merge step of [divide and conquer](/divide-and-conquer-convex-hull/) does, and give the hull of $L \cup R$. Check each bridge by testing all six points against it.

19. • Let $a$ be a number and let the points of $S$ lie on both sides of the line $x = a$. Show that the edge of the upper hull that crosses $x = a$ is given by the optimal solution $(s, t)$ of the linear program: minimize $sa + t$ subject to $y_i \le s x_i + t$ for every point $(x_i, y_i)$ of $S$. Which algorithm of the chapter finds this edge in linear time without solving the program in general?

20. • Points are only inserted, never deleted. Keep the upper hull in a [balanced binary search tree](/balanced-binary-search-tree/) ordered by $x$. Give the insertion step, and show that $n$ insertions take $O(n \log n)$ time in all.

21. • Give a set of $n$ points and a sequence of $n$ updates, alternating one insertion and one deletion, after each of which $\Theta(n)$ vertices join or leave the hull. What does this say about any [dynamic convex hull](/dynamic-convex-hull/) that must list the hull after each update?

22. • Use [Euler's formula](/euler-formula/) to prove that the hull of $n$ points in $\mathbb{R}^3$ has at most $3n - 6$ edges and $2n - 4$ facets, with equality when every facet is a triangle and every point is a vertex.

23. • Tverberg's theorem says that any $7$ points in the plane split into $3$ groups whose hulls share a point. Find such a split for the six vertices of a regular hexagon and its centre. Then find one for the six vertices alone.

24. • Prove that among all triangles with corners in a finite set $S$, some triangle of largest area has all three corners at vertices of the hull of $S$.

25. ★ Several vertical segments in the plane are given, the $i$-th from $(x_i, l_i)$ to $(x_i, u_i)$. Prove that if every three of them are crossed by a common non-vertical line, then one non-vertical line crosses them all. (Use [Helly's theorem](/helly-theorem/) in a plane of parameters.)

26. ★ Take $n \ge 5$ distinct numbers $t_1 < \dots < t_n$ and the points $p_i = (t_i, t_i^2, t_i^3, t_i^4)$ in $\mathbb{R}^4$. Prove that for every $i < j$ the segment $p_i p_j$ is an edge of their hull, so the hull has $n(n-1)/2$ edges. Compare with the bound $3n - 6$ in $\mathbb{R}^3$.

27. ★ Four points are drawn independently and uniformly from the unit square. Given that the expected area of the triangle formed by three such points is $11/144$, find the probability that the four points are in convex position, and the expected number of vertices of their hull.

28. ★ Let $S$ lie in the unit ball of $\mathbb{R}^d$ and let $x \in \operatorname{conv} S$. Prove that for every $\varepsilon > 0$ there are $k = \lceil 1/\varepsilon^2 \rceil$ points of $S$, repeats allowed, whose average lies within distance $\varepsilon$ of $x$. Note that $k$ does not depend on $d$; compare with [Carathéodory's theorem](/caratheodory-theorem/).

29. ★ A set of $n$ red points and a set of $n$ blue points are given in the plane. Prove that a line can strictly separate them if and only if their convex hulls are disjoint, and give an $O(n \log n)$ algorithm that decides which case holds.
