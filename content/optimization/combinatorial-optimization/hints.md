1. The ratios are $5, 3, 5, 2$, so the order is 1, 3, 2, 4. Items 1 and 3 use weight 7, and item 2 is critical: half of it fits, for $20 + 15 + 9 = 44$. The 0-1 optimum is $\{1, 2\}$, with weight 10 and value 38. The repaired greedy compares the prefix $\{1, 3\}$, value 35, with the best single item, value 20, and returns 35.

2. $V[0] = 0, 0, 0, 0, 0, 0, 0$; $V[1] = 0, 0, 0, 4, 4, 4, 4$; $V[2] = 0, 0, 0, 4, 5, 5, 5$; $V[3] = 0, 0, 3, 4, 5, 7, 8$. The optimum is 8, with items 2 and 3.

4. From 0 the tour is $0, -1, 3, 7, -6, 0$, of cost $1 + 4 + 4 + 13 + 6 = 28$. The optimum is $2(7 - (-6)) = 26$. From each of the other four cities the heuristic finds a tour of cost 26. The start at 0 is the only bad one: its tour crosses the gap between $-1$ and $0$ four times instead of twice.

6. $s(1, 2) = s(3, 4) = 6$, $s(2, 4) = 4$, $s(1, 4) = s(2, 3) = 2$, $s(1, 3) = 0$. With $Q = 2$ the routes are $0, 1, 2, 0$ and $0, 3, 4, 0$, of cost 10 each, total 20, which is optimal. With $Q = 4$ the saving $s(2, 4)$ joins them into $0, 1, 2, 4, 3, 0$ of cost 16. This is optimal too: a closed tour through $(0, 0)$, $(4, 1)$ and $(1, 4)$ has Manhattan length at least $2 \cdot 4 + 2 \cdot 4$.

9. The maximum is 2, for example $\{a, d\}$. The graphic matroid has rank 3 and the partition matroid rank 4. The set $U = \{a, b, c\}$ gives $r_1(U) + r_2(\{d, e, f\}) = 1 + 1 = 2$.

11. An item is taken in the relaxed problem exactly when $v_i - \lambda w_i > 0$, and for a feasible $x$ the term $\lambda (W - \sum_i w_i x_i)$ is nonnegative. $L$ is convex and piecewise linear, with slope $W$ minus the weight of the items of ratio above $\lambda$: $-3$ just below $\lambda = 3$ and $+3$ just above. So the minimum is $L(3) = 30 + 8 + 0 + 6 + 0 = 44$. The set $\{0, 1\}^n$ has the integrality property, so by Geoffrion's theorem the Lagrangian dual equals the LP bound.

12. With $C(S, j)$ the cheapest path from city 1 through all of $S$ ending at $j$: $C(\{2\}, 2) = 2$, $C(\{3\}, 3) = 9$, $C(\{4\}, 4) = 10$; $C(\{2, 3\}, 3) = 8$, $C(\{2, 3\}, 2) = 15$, $C(\{2, 4\}, 4) = 6$, $C(\{2, 4\}, 2) = 14$, $C(\{3, 4\}, 4) = 17$, $C(\{3, 4\}, 3) = 18$; $C(\{2, 3, 4\}, 2) = 21$, $C(\{2, 3, 4\}, 3) = 14$, $C(\{2, 3, 4\}, 4) = 16$. Closing the tour gives $\min(23, 23, 26) = 23$, for the tour $1, 2, 4, 3, 1$.

15. The savings are $s(1, 2) = 16$, $s(1, 3) = s(1, 4) = 10$, $s(2, 3) = s(2, 4) = 8$, $s(3, 4) = 0$. The method joins 1 and 2, which fills a truck, and every other positive saving involves 1 or 2, so the cost is $20 + 12 + 12 = 44$. The optimum pairs 1 with 3 and 2 with 4, for $22 + 20 = 42$. With $Q = 2$ the method is a greedy matching on the savings, and it takes the heaviest edge although two lighter edges sum to more.

18. $X_1 = \{r\}$ and $X_2 = \{q\}$. The arcs are $(p, q)$ and $(p, r)$, because $\{q\}$ and $\{r\}$ are independent in $M_1$, and $(q, p)$ and $(r, p)$, because they are independent in $M_2$. The path $r \to p \to q$ gives $\{q, r\}$, a perfect matching; it is the augmenting path $r, p, q$ of bipartite matching.

21. Take $W = 2M$ with $M \ge 2$ and items $(w, v) = (1, 2), (M, M), (M, M)$. The prefix holds items 1 and 2, of value $M + 2$, and the best single item has value $M$. The optimum takes the last two items, for $2M$, and $(M + 2)/(2M) \to 1/2$.

23. Let $S_i$ be the greedy set after $i$ steps. Monotonicity and submodularity give $f(S^*) \le f(S_i \cup S^*) \le f(S_i) + \sum_{e \in S^*} \bigl(f(S_i + e) - f(S_i)\bigr) \le f(S_i) + k \bigl(f(S_{i+1}) - f(S_i)\bigr)$, so the gap $f(S^*) - f(S_i)$ shrinks by the factor $1 - 1/k$ at each step. For the example, give elements 1 to 4 weight 1 and element 5 weight $\varepsilon$, with sets $\{1, 2\}$, $\{3, 4\}$ and $\{1, 3, 5\}$: greedy takes the last set first and ends with $3 + \varepsilon$ against 4.

24. Turn each edge into two opposite arcs of capacity $w_{uv}$, add an arc $v \to t$ of capacity $m_v$ when $m_v > 0$ and an arc $s \to v$ of capacity $-m_v$ when $m_v < 0$. The cut with source side $S + s$ has capacity $f(S) + \sum_{m_v < 0} |m_v|$. In the example the constant is 4, the minimum cut is 1, and the minimum of $f$ is $-3$, at $S = \{1, 2, 3\}$.

25. One choice is $v = (3, 2, 3, 3.5, 3.5)$ for the clients at 1, 2, 5, 9, 11. Then $\sum_j \max(0, v_j - c_{ij})$ is 2 for $A$, 2 for $B$ and 5 for $C$, never more than the opening cost, so $L(v) = \sum_j v_j = 15$.

26. With $|V| - 1$ arcs, at most one into each of the $|V| - 1$ vertices other than $r$ and none into $r$, every vertex other than $r$ has exactly one entering arc. Follow entering arcs backwards from any vertex: a repeated vertex would close a cycle of the forest, so the walk ends at $r$. For the example take $U = \{b \to c, c \to b\}$: $r_1(U) = 1$, and the other two arcs both enter $a$, so $r_2(E \setminus U) = 1$. The maximum is $2 < 3$.

27. Root the tree. Let $D_v[k][s]$ be the fewest cut edges inside the subtree of $v$ when $k$ of its vertices are on side 0 and $v$ is on side $s$, and add the children one at a time, paying 1 for an edge whose ends are on different sides. Merging tables for parts of sizes $a$ and $b$ costs $O(ab)$, and each pair of vertices is counted once, at the merge at their lowest common ancestor, so the total is $O(n^2)$.
