1. (a) 10 triangles and 9 diagonals. (b) $n + 2h - 2 = 22$ triangles and $n + 3h - 3 = 23$ diagonals. (c) The point $(2,0)$ lies on a hull edge, so $h = 5$ and the counts are $2n - h - 2 = 3$ triangles and $3n - h - 3 = 7$ edges, not the 4 triangles that $h = 4$ would give.

3. The vertex $v_3$ is reflex, and it lies inside the triangles $v_4 v_0 v_1$ and $v_0 v_1 v_2$, so $v_0$ and $v_1$ are not ears. The ears are $v_2$ and $v_4$. The segments $v_1 v_4$ and $v_0 v_2$ cross the edges at $v_3$ and $v_2 v_4$ runs outside, so the only diagonals are $v_0 v_3$ and $v_1 v_3$, and the polygon has exactly one triangulation.

4. $F_0$ and $F_3$ share the diagonal $v_0 v_3$, and the distance is 2: flip $v_0 v_2$ to $v_1 v_3$ and $v_0 v_4$ to $v_3 v_5$. $F_0$ and $F_1$ share no diagonal, and the distance is 3: flip $v_0 v_2$ to $v_1 v_3$, then $v_0 v_3$ to $v_1 v_4$, then $v_0 v_4$ to $v_1 v_5$.

8. Count edges of the tree in two ways: $t_1 + 2t_2 + 3t_3 = 2(t_1 + t_2 + t_3 - 1)$, which gives $t_1 = t_3 + 2$. For the 10-gon there are 8 triangles, $t_1 = 3$ and $t_3 = 1$, so 4 triangles have exactly one polygon edge and 1 has none.

11. $F$ and $D$ are start vertices, $A$ and $C$ end vertices, $B$ a split vertex and $E$ a merge vertex. The merge vertex $E$ becomes the helper of the edge $FA$, and the split vertex $B$ below it is joined to that helper, so the only diagonal is $BE$. The two pieces $ABEF$ and $BCDE$ are convex quadrilaterals, and the polygon is cut into 4 triangles.

13. The bridge is walked twice, so its two endpoints appear twice in the list, which has $7 + 2 = 9$ vertices. Ear clipping gives $9 - 2 = 7$ triangles and $9 - 3 = 6$ diagonals, and with the bridge there are 7, as $n + 3h - 3$ predicts.

15. Cut off the four corner tetrahedra at alternate corners, such as the one at $(0,0,0)$ with its three neighbors; each has volume $1/6$, and what remains is a regular tetrahedron of volume $1/3$. Six tetrahedra of volume $1/6$ each come from cutting around a main diagonal. Both cuts use the same 8 vertices, so the number of tetrahedra is not determined by the vertices.

17. A triangle has dual degree $3$ minus the number of its polygon edges, so no internal triangle means no degree 3 node, which is a path. Build such a triangulation from one end: choose the tip of the first ear ($n$ ways), then add each of the next $n - 4$ triangles on the left or the right end of the covered chain; the last triangle is forced. Each path is built twice, once from each end, which gives $n \cdot 2^{n-4}/2$. For $n = 8$ the count is 64.

18. The two triangulations share no diagonal, so at least 3 flips are needed, and 3 would suffice only if every flip created a diagonal of $T_2$. But every flip in $T_1$ creates a long diagonal $v_1 v_4$, $v_2 v_5$ or $v_3 v_0$, which is not in $T_2$. Four flips suffice: go through the fan $F_1$.

19. If $v_0$ is not joined to every vertex, some triangle $v_0 v_i v_j$ has a neighbor across $v_i v_j$ with a third vertex $v_k$ not adjacent to $v_0$; flipping $v_i v_j$ to $v_0 v_k$ is allowed because the polygon is convex, and it raises the degree of $v_0$ by one. The degree goes from at least 2 to $n - 1$, so at most $n - 3$ flips are needed, and two triangulations are joined through $F_0$ by at most $2n - 6$ flips.

20. By the inscribed angle theorem, $d$ lies inside the circle through $a$, $b$ and $c$ exactly when $\angle abc + \angle cda > \pi$. When $d$ is outside that circle, $a$ is inside the circle through $b$, $c$ and $d$. Compare angles that look at the same chord from points inside and on a circle: each of the six angles of the triangulation with $ac$ is larger than some angle of the one with $bd$, so its smallest angle is larger. In exercise 9 the angles at $b$ and $d$ are both about $112.6°$, so $bd$ is the better diagonal.
