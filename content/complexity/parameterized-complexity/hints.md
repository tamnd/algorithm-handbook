1. The vertex $a$ has degree $5 > 3$, so it is taken and $k$ drops to 2. The leaves become isolated and are deleted. The kernel is the triangle and the edge $uv$: 5 vertices and 4 edges, which passes the test of at most $k^2 = 4$ edges. The triangle needs 2 vertices and the edge needs 1 more, so the answer is no. The whole graph has vertex cover number 4.

4. For $(1, 3)$, $\lambda$ is the root of $x^3 = x^2 + 1$, about $1.4656$, and $\lambda^{20} \approx 2090$. For $(2, 2)$, $\lambda = \sqrt{2} \approx 1.4142$ and $\lambda^{20} = 1024$. The vector $(2, 2)$ is better.

5. The probability is $4!/4^4 = 3/32 = 0.09375$. After $t$ colorings the path is missed with probability $(29/32)^t$, which is about $0.0108$ for $t = 46$ and $0.0098$ for $t = 47$. So 47 colorings are needed.

6. Both answers are 3. For $C_5$ with edges $12, 23, 34, 45, 51$, delete $23$, $45$ and $51$, which leaves the clusters $\{1,2\}$, $\{3,4\}$ and $\{5\}$. For $C_6$, delete every second edge to leave three disjoint edges. A script checked by brute force over all sets of edits that 2 edits do not suffice for either cycle.

7. (a) True, since clique is $\mathsf{W}[1]$-complete. (b) False: trying all $k$-sets is an XP algorithm, and $\mathsf{W}[2] \subseteq \mathsf{XP}$. (c) True. (d) False: it is FPT, by a search tree with $6^k$ leaves or by the kernel of exercise 10.

10. If $n \ge 4k$, some color class of a proper 4-coloring has at least $n/4 \ge k$ vertices, so the answer is yes and the kernel outputs a fixed yes-instance. The coloring is only used in the proof; it need not be computed. Otherwise the graph itself has fewer than $4k$ vertices.

12. The LP has a unique optimum of value $5/2$: $x_c = 1$, the leaves get 0, and $x$, $y$, $z$ get $1/2$. So $V_1 = \{c\}$, $V_0$ is the set of leaves and $V_{1/2} = \{x, y, z\}$. Take $c$; the kernel is the triangle with $k = 2$, at most $2k = 4$ vertices. The answer is yes, for example $\{c, x, y\}$.

14. With $k = \log_2 n$, $(2e)^k = n^{\log_2(2e)}$ and $\log_2(2e) \approx 2.443$. The time is $O(n^{2.443}(n + m))$.

15. (a) $\sqrt{k} = o(k)$, so this is an $f(k) \cdot n^{o(k)}$ algorithm, which ETH excludes for clique. (b) $k / \log_2 k = o(k)$, so this is a $2^{o(k)} n^{O(1)}$ algorithm, which ETH excludes for vertex cover (exercise 20).

20. Sparsify the 3-SAT instance so that $m = O(n)$. The standard graph has a triangle per clause and an edge between complementary literals; it has $3m$ vertices and an independent set of size $m$ exactly when the formula is satisfiable. So it has a vertex cover of size $k = 2m = O(n)$, and a $2^{o(k)}$ algorithm would decide 3-SAT in time $2^{o(n)}$.

21. Make a terminal for each element and one more terminal $r$, and a non-terminal for each set. Join $r$ to every set and each set to its elements. A tree that connects all terminals through $k$ set vertices is the same as a cover by $k$ sets, and the parameter does not change.

22. Outside a vertex cover the graph has no edges, so a clique has at most one vertex outside it. Find a cover $C$ of size $\tau$ by branching, then try every subset of $C$ and every way to add one vertex outside. The time is $2^{\tau} n^{O(1)}$. A script compared this method with brute force on 200 random graphs (seed 7) and found no difference.

24. For each edge $uv$, add a new vertex adjacent to $u$ and $v$. A vertex cover leaves an independent set plus new vertices with at most one neighbor each, which is bipartite. An odd cycle transversal hits every new triangle, and swapping each new vertex in it for an end of its edge gives a vertex cover that is no larger. A script checked the equality on 200 random graphs (seed 2024).
