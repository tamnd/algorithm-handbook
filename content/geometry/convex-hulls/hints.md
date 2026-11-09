1. $D(p, q, r) = 3 \cdot 5 - 2 \cdot 1 = 13 > 0$, a left turn, and the triangle has area $13/2$. $D(p, q, r') = 3 \cdot 4 - 2 \cdot 6 = 0$, so $r'$ is on the line through $p$ and $q$; but $r' = p + 2(q - p)$, so it lies beyond $q$, not on the segment.

3. Lower hull $(0,3), (1,1), (4,0), (6,2), (6,5)$; upper hull $(6,5), (3,5), (0,3)$; hull $(0,3), (1,1), (4,0), (6,2), (6,5), (3,5)$. The point $(5,5)$ lies on the edge from $(6,5)$ to $(3,5)$; the test $D = 0$ pops it, so it is not a vertex.

4. The pivot is $(4,0)$. The points $(3,2)$ and $(2,4)$ lie on one ray from the pivot, and $(3,2)$, the nearer, comes first. There are four pops: $(4,3)$ and $(5,5)$ when $(3,5)$ arrives, $(3,2)$ when $(2,4)$ arrives, and $(2,4)$ when $(0,3)$ arrives.

5. $a = (0,3)$, $b = (6,5)$, $R = \{(1,1), (4,0), (6,2), (3,2), (4,3)\}$ and $U = \{(5,5), (2,4), (3,5)\}$. The farthest point is $(4,0)$ in $R$ and $(3,5)$ in $U$. The call on $U$ drops $(5,5)$, which is on the segment from $(6,5)$ to $(3,5)$, and $(2,4)$, which is inside the triangle.

8. $\{(1,1)\}$ against the other three, meeting at $(1,1)$. The two diagonals $\{(0,0), (2,2)\}$ and $\{(2,0), (0,2)\}$, meeting at $(1,1)$. $\{(1,0)\}$ against $\{(0,0), (2,0)\}$, meeting at $(1,0)$; the point $(5,5)$ can go in either part.

10. Three layers: the four corners of the big square; then $(2,1)$, $(5,2)$, $(4,5)$, $(1,4)$, a tilted square around $(3,3)$; then $(3,3)$ alone. Here $k = 3 = \lceil 9/3 \rceil$, so the bound is met.

11. The diagonals from $v_0$ cut the polygon into a fan of triangles. The sign of $D(v_0, v_i, q)$ changes once as $i$ grows, so binary search finds the wedge $v_0 v_i v_{i+1}$ that holds $q$ (or shows that $q$ lies outside all wedges). Then one more test, $D(v_i, v_{i+1}, q)$, decides inside, on the boundary or outside.

13. Pop only on a strict right turn, $D < 0$. Then points in the middle of an edge stay on the stack. When all the points lie on one line, the lower and the upper chain both hold all of them, so the output lists the middle points twice; in that case return the lower chain alone.

15. Rounds $t = 1, 2, 3$ with $m = 4, 16, 256$; the third succeeds. The sum is $n(2 + 4 + 8) = 14n$, against $n \lg 20 \approx 4.3n$. In general, if $t^*$ is the last round, then $2^{t^* - 1} < \lg h$ (unless $t^* = 1$), and $\sum_{t \le t^*} 2^t < 2^{t^* + 1} < 4 \lg h$.

17. The lower bound takes the numbers in any order. The points $(x_i, x_i^2)$ joined in input order form a polyline that crosses itself unless the input is nearly sorted, so Melkman's algorithm does not apply. Its input carries order information that the general problem lacks.

19. The constraints say that the line $y = sx + t$ lies on or above every point. Among such lines, the objective is the height of the line at $x = a$, so the best one touches the upper hull from above at $x = a$, and it contains the hull edge that crosses $x = a$. The Kirkpatrick–Seidel algorithm finds this bridge by prune and search, throwing away a fixed fraction of the candidate points in each round.

21. Put $n - 1$ points on the upper half of a circle; all of them are on the upper hull. Insert one point far enough above the centre that it hides them all, then delete it, and repeat. Each update moves $\Theta(n)$ vertices into or out of the hull, so listing the hull after every update costs $\Theta(n^2)$ in all. Dynamic structures therefore answer queries about the hull instead of listing it.

25. A non-vertical line $y = ax + b$ crosses the $i$-th segment exactly when $l_i \le a x_i + b \le u_i$. In the $(a, b)$-plane this is a strip between two parallel lines, a convex set. Every three strips meet, so by Helly's theorem in dimension 2 all of them do, and a common point $(a, b)$ is the line.

26. For $i < j$ the polynomial $(t - t_i)^2 (t - t_j)^2 = t^4 + c_3 t^3 + c_2 t^2 + c_1 t + c_0$ is nonnegative and vanishes only at $t_i$ and $t_j$. So the hyperplane $c_1 x_1 + c_2 x_2 + c_3 x_3 + x_4 = -c_0$ has every $p_k$ on one side and touches only $p_i$ and $p_j$: it supports the hull along the segment $p_i p_j$. In $\mathbb{R}^3$ there are at most $3n - 6$ edges, far fewer.

27. Four points fail to be in convex position exactly when one of them lies in the triangle of the other three, and at most one can. The probability that a given point does is the expected area, $11/144$, so the probability of failure is $4 \cdot 11/144 = 11/36$. The four points are in convex position with probability $25/36$, and $E[h] = 3 + 25/36 = 133/36 \approx 3.69$.

28. Write $x = \sum \lambda_i s_i$ and draw $k$ points independently, each equal to $s_i$ with probability $\lambda_i$. Their average $y$ has mean $x$, and $E|y - x|^2 = E|s - x|^2 / k \le E|s|^2 / k \le 1/k \le \varepsilon^2$. A random variable is at most its mean for some outcome, so some choice of $k$ points has $|y - x| \le \varepsilon$.

29. If a line separates the sets, each lies in an open half-plane, which is convex, so it contains the hull of the set, and the hulls are disjoint. Conversely, if the hulls are disjoint, take a closest pair of points $p$ and $q$, one in each hull; the perpendicular bisector of $pq$ separates them strictly. Compute both hulls in $O(n \log n)$ time, then test the two convex polygons for [intersection](/convex-polygon-intersection/) in linear time.
