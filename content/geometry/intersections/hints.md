1. $4x - 3y - 11 = 0$. The formulas give $A = -4$, $B = 3$, $C = 11$, and the sign rule multiplies all three by $-1$.

3. Here $A^2 + B^2 = 2$ and $e = -1$, so $D = 50 - 1 = 49 > 0$ and there are two points: $(4, 3)$ and $(-3, -4)$.

4. Center $(8,0)$: the circles touch from outside at $(5,0)$ and have three common tangents. Center $(2,0)$: the second circle touches the first from inside at $(5,0)$, with one common tangent. Center $(4,0)$: they meet at $(4, 3)$ and $(4, -3)$ and have two common tangents.

5. (a) They cross at $(2,2)$. (b) They are collinear but disjoint. (c) They are collinear and overlap in the segment $(1,1)$–$(2,2)$.

8. The vertices are $(0,0)$, $(2,0)$, $(3,1)$ and $(0,4)$, and the shoelace formula gives area $7$. The half-plane $y \le 5$ is redundant, since $y \le 4$ on the whole polygon.

10. The centers of similarity divide the segment between the centers in the ratio $2 : 1$, externally and internally, so they are $(12, 0)$ and $(4, 0)$. A line through $(4,0)$ at distance $2$ from the origin makes an angle of $30°$ with the $x$-axis, which gives $x + \sqrt{3}\, y - 4 = 0$ and $x - \sqrt{3}\, y - 4 = 0$.

11. Write down the status after each event. Just right of $x = 2$ the order from the bottom is $s_0, s_2, s_1$, and the new segment $s_2$ is tested against both of its neighbors. Only one of those tests succeeds, and the crossing of $s_0$ and $s_3$ at $(11/3, 0)$ is never looked at.

14. The tangent lines at $x_i$ and $x_j$ meet at $x = (x_i + x_j)/2$, and the boundary takes the lines in the order of their slopes $2 x_i$. So the order is $-1, 2, 3$, and the vertices are $(1/2, -2)$ and $(5/2, 6)$: the boundary sorts the numbers.

16. The slabs are $[0,1]$, $[1,2]$, $[2,3]$, $[3,4]$ and $[4,5]$, with covered lengths $2, 3, 3, 3, 1$. The area is $12$, which inclusion-exclusion confirms: $6 + 6 + 3 - 2 - 1 - 0 = 12$.

21. No. In the plane, Helly's theorem says that if every three sets of a finite family of convex sets have a common point, the whole family has one. A half-plane is convex.

22. There are at most $2n$ end point events and at most $n - 1$ adjacent pairs, so the queue never holds more than $3n - 1$ events. If $s$ and $t$ cross at $p$, they are adjacent in the status at every moment shortly before the sweep reaches $p$, so their crossing event is put back in the queue when they become adjacent again.

23. The slope of the line through $(a, a^3)$ and $(b, b^3)$ is $a^2 + ab + b^2$. Setting it equal to the slope through $(a, a^3)$ and $(c, c^3)$ gives $(b - c)(a + b + c) = 0$.

24. Use a grid of $n/2$ long thin horizontal rectangles and $n/2$ long thin vertical ones, for example $[0, n] \times [2i, 2i + 1]$ and $[2j, 2j + 1] \times [0, n]$ for $0 \le i, j < n/2$. The union has $(n/2 - 1)^2$ square holes, each with four vertices, so the boundary alone has $\Omega(n^2)$ size, while the sweep finds the area in $O(n \log n)$ time.

25. Sweep from left to right with a Fenwick tree indexed by the ranks of the $y$-coordinates. At the left end of a horizontal segment add $1$ at its $y$, and at its right end subtract $1$. At a vertical segment from $y_1$ to $y_2$, add the sum over $[y_1, y_2]$ to the count. Process events with equal $x$ in the order inserts, queries, deletes.
