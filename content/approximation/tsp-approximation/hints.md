1. The triangle $A, B, C$ fails, since $AC = 5 > AB + BC = 2$. The tours are $A\,B\,C\,D$ with cost 4, and $A\,B\,D\,C$ and $A\,C\,B\,D$ with cost 8 each. The worst triangle needs $5 + M \le 2(1 + M)$, so $M = 3$. The tours then cost 16, 20 and 20, and the worst ratio falls from 2 to $1.25$.

3. OPT is $6 + 4 + 11 + 15 + 9 + 7 = 52$. The minimum spanning tree is unique, with edges $AB, BD, AE, CE, DF$ and cost 37. The 1-tree bounds for the special vertices $A$ to $F$ are 45, 45, 51, 46, 50 and 49. The best is 51, with $C$ special, one below OPT.

4. From $A$ the tour is $A\,B\,D\,E\,C\,F$, cost 60. From $B$ it costs 63. From $C$, $D$, $E$ and $F$ the tour costs 52, which is optimal.

12. Only two moves gain. Removing $DE$ and $FA$ and adding $DF$ and $EA$ gains 8 and gives $A\,B\,D\,F\,C\,E$, the optimal tour. Removing $EC$ and $FA$ and adding $EF$ and $CA$ gains 1 and gives a tour of cost 59.

14. Only the costs at $C$ and $F$ change, and $-2\sum_v \pi_v = 14$. A minimum spanning tree of $B, C, D, E, F$ for the new costs is $BD, CE, DF$ and one edge of cost 8, with total 25, and the two cheapest edges at $A$ cost 13. So $L(\pi) = 52$. Since $L(\pi) \le \text{LP} \le \text{OPT} = 52$, the LP value is 52 and the LP has no gap on this instance.

15. The path is the unique minimum spanning tree, of cost 6. The odd vertices are 0 and 6, at distance $3.3$, so ALG $= 9.3$. The tour $0\,2\,4\,6\,5\,3\,1$ costs $7.5$, which is OPT, and the ratio is $1.24$. In general ALG $= (n - 1) + (n - 1)(1 + \varepsilon)/2$ and OPT $\le (n - 2)(1 + \varepsilon) + 2$, so the ratio tends to $3/2$ as $n \to \infty$ and $\varepsilon \to 0$.

16. The first cycle cover is unique: the cycles $A\,B$ and $C\,D$, cost 14. The representatives $A$ and $C$ form the cycle $A\,C$, cost 11. The arcs cost 25, against the bound $2 \cdot 17 = 34$. The shortcut tour is $A\,B\,C\,D$, cost 19. OPT is the tour $A\,C\,D\,B$, cost 17, and its reverse costs 23.

19. The keys are $P$ 3, $T$ 13, $Q$ 22, $R$ 38, $U$ 52 and $S$ 57. The tour $P\,T\,Q\,R\,U\,S$ costs $3 + 4 + 8 + 5 + 3 + 9 = 32$, and the ratio is $32/22 = 16/11$.

21. A tour must cross each gap between neighbouring points at least twice. If it crosses some gap four times, two of its edges cross that gap in the same direction, say $a \to b$ and $p \to q$; the 2-opt move that replaces them by $\{a, p\}$ and $\{b, q\}$ saves $2(\min(b, q) - \max(a, p)) > 0$. So a 2-optimal tour crosses each gap exactly twice and costs $2(\max - \min)$, which is OPT.

22. If two edges of a tour cross, the 2-opt move that uncrosses them is shorter, because in a convex quadrilateral the two diagonals together are longer than either pair of opposite sides. So a 2-optimal tour has no crossing. If it used a chord $uv$ between two corners that are not adjacent on the polygon, the rest of the tour is a path from $u$ to $v$ through the corners on both sides of the chord, and the edge where it passes from one side to the other crosses $uv$.

23. A tour that uses $k$ edges of cost 2 costs $n + k$, and if $k \ge 1$, its edges of cost 1 form $k$ disjoint paths that cover all vertices. Conversely, $p$ such paths can be joined into a tour with $p$ edges of cost 2. In $K_{2,4}$ each path alternates sides, so it holds at most one more vertex of the larger side than of the smaller; then $4 \le 2 + p$, so $p = 2$ and OPT $= 8$.

24. Sort the points and let $g_1, \ldots, g_{n-1}$ be the gaps. Then $t_1 = \max_i g_i$. A point inside the range is a cut vertex until an edge jumps over it, so $t_2 = \max_i (g_i + g_{i+1})$ for $n \ge 3$. The tour that goes out through every second point and comes back through the others has longest edge $t_2$, and every tour is biconnected, so OPT $= t_2 \le 2 t_1$. The points $0, 1, 2$ have $t_1 = 1$ and OPT $= 2$.

25. Each vertex has three edges at $2/3$, and the Petersen graph is 3-edge-connected, so every cut carries at least $3 \cdot 2/3 = 2$; the value is $15 \cdot 2/3 = 10$. No feasible point costs less than $n = 10$, since every cost is at least 1 and the $x_e$ add up to $n$. With no Hamiltonian cycle a tour needs an edge of cost 2, and a Hamiltonian path closed by such an edge costs 11. So OPT $= 11$ and the ratio is $11/10$.
