1. The queue order is $0, 1, 3, 2, 4, 6, 5, 7, 8$. Distances of $0, \ldots, 8$: $0, 1, 2, 1, 2, 3, 2, 3, 4$. Parents: $1, 3 \leftarrow 0$; $2, 4 \leftarrow 1$; $6 \leftarrow 3$; $5 \leftarrow 2$; $7 \leftarrow 4$; $8 \leftarrow 5$. Layers: $\{0\}$, $\{1, 3\}$, $\{2, 4, 6\}$, $\{5, 7\}$, $\{8\}$.

2. $d/f$: $0: 1/12$, $1: 2/7$, $3: 3/6$, $5: 4/5$, $2: 8/11$, $4: 9/10$, $6: 13/14$. Tree edges $01, 13, 35, 02, 24$; back edge $30$; forward edge $03$; cross edges $21, 45, 64, 65$.

3. (a) $b, c, a, d, f, e, g, h$. (b) The finish order is $h, e, a, g, d, b, f, c$, so the ordering is $c, f, b, d, g, a, e, h$.

4. $G$ is bipartite with sides $\{0, 2, 4, 6\}$ and $\{1, 3, 5, 7\}$. With $37$ added it is not: $1, 2, 3, 7, 6, 1$ is a cycle of length 5.

5. (a) Valid: $u$ is the root, with children $v$ and $x$, and $w$ is a child of $v$. (b) Invalid: $[1, 6]$ and $[2, 7]$ overlap without nesting. (c) Valid: two trees, $u$ over $v$ and $w$ over $x$.

6. Six regions with 4-neighbour moves, two with 8-neighbour moves.

7. Each of the 12 edges is walked exactly twice, so 24.

8. The order is $0, 1, 3, 2$: after 1 is visited, the label $\{0\}$ of 3 beats the label $\{1\}$ of 2. In the reverse order $2, 3, 1, 0$, the later neighbours of 2 are 3 and 1, which are not adjacent.

9. Set $c[s] = 1$, and when $u$ is scanned add $c[u]$ to $c[v]$ for each neighbour $v$ with $\mathrm{dist}[v] = \mathrm{dist}[u] + 1$; every shortest path to $v$ ends with such an edge. The answers are 6 and 20.

10. Six moves. The square h8 is the only one at distance 6; every other square is within 5 moves.

11. A vertex lies on an $s$–$t$ walk exactly when it is reachable from $s$ and $t$ is reachable from it. Search from $s$ in $G$ and from $t$ in the transpose, and intersect. With edges $sa, av, va, at$, the vertex $v$ is on the walk $s, a, v, a, t$ but on no simple path.

13. There are 42.

18. Take a leaf $v$ of a depth-first tree. All its neighbours are ancestors, so the farthest of them is at least $k$ levels up.

22. Number the vertices by their position in the given order, sort each adjacency list by that number with one counting sort, run BFS with the sorted lists and compare. If any BFS produces the order, this one does.

24. Run a complete DFS and take the vertex $r$ that finishes last. If some root exists, $r$ is one, by the white-path theorem; check with one search from $r$.

26. With the single edge $(3, 1)$ and the vertex 2, the lexicographically smallest ordering is $2, 3, 1$, but $3, 1, 2$ puts 1 earlier. Run Kahn's algorithm on the transpose, always taking the largest source, and reverse the result.
