1. The maximal cliques are $abc, bcd, cde, def, efg, fgh$ and the edge $ah$, which lies in no triangle. So $\omega = 3$. The sets $\{a, d, g\}$ and $\{b, e, h\}$ are independent and no set of 4 is, so $\alpha = 3$. The coloring $a, d, g \mapsto 1$, $b, e, h \mapsto 2$, $c, f \mapsto 3$ is proper, so $\chi = 3$.

2. The first order gives $a1, b2, c3, d1, e2, f3, g1, h2$: three colors. The second gives $a1, b2, c3, d1, f2, e4, g1, h3$: four colors, because $e$ comes after neighbours colored 1, 2 and 3.

3. Vertex $a_i$ and vertex $b_i$ both get color $i$, since each sees colors $1, \ldots, i - 1$ on its earlier neighbours. So greedy uses 4 colors, while the two sides give a 2-coloring.

4. The removal order is $a, b, c, d, e, f, g, h$; every vertex has degree at least 3, and $a$ has degree 3 when it is removed, so the degeneracy is 3 and the bound is 4 colors. Greedy in the order $h, g, \ldots, a$ uses 3: $h1, g2, f3, e1, d2, c3, b1, a2$.

5. $c1, d2, e3, f1, b3, a2, g2, h3$. After $f$, the vertices $b$ and $g$ both see two colors and have degree 3; $b$ comes first alphabetically.

6. The layers are $\{1\}$, $\{2, 3\}$, $\{4, 5\}$, $\{6, 7\}$, $\{8\}$. The edge $45$ joins two vertices of layer 2 and closes the cycle $1, 2, 4, 5, 3, 1$ of length 5. Without it, color the even layers $1, 4, 5, 8$ with one color and $2, 3, 6, 7$ with the other.

7. The roof is a triangle glued to the square along the edge $cd$, so $P = P(C_4, k)\, (k - 2) = ((k - 1)^4 + (k - 1))(k - 2)$. This gives 18 colorings with 3 colors and 168 with 4.

8. The order is $b, f, g, a, c, d, e, h$. In reverse, greedy gives $h1, e2, d3, c1, a2, g1, f4, b4$. The clique $\{a, b, c, d\}$, or $\{d, e, f, h\}$, needs 4 colors.

9. Color the three perfect matchings $\{12, 34\}$, $\{13, 24\}$, $\{14, 23\}$ of $K_4$ with one color each. In $K_5$ a color class is a matching, so it has at most 2 edges, and 10 edges need 5 colors. The chromatic index of $K_n$ is $n - 1$ for even $n$ and $n$ for odd $n$.

11. The order is $c, d, e, f, a, b, g, h$ with degrees $4, 4, 4, 4, 3, 3, 3, 3$, so the guarantee is 4. The run gives $c1, d2, e3, f1, a2, b3, g2, h3$ and uses 3 colors.

14. One coloring is $0 \mapsto 1$, $1 \mapsto 2$, $2 \mapsto 1$, $3 \mapsto 2$, $4 \mapsto 3$, $5 \mapsto 2$, $6 \mapsto 1$, $7 \mapsto 3$, $8 \mapsto 3$, $9 \mapsto 2$. In $K_n$ all $n = \Delta + 1$ vertices are adjacent; an odd cycle has $\Delta = 2$ and is not bipartite.

17. Pick a vertex $v$ of $K_{10}$: it has at least 4 red or at least 6 blue edges, and either case finishes. On $K_9$, the red neighbours of $v$ form a blue clique, so there are at most 3, and the blue neighbours contain no red triangle and no blue triangle, so there are at most 5. Hence every vertex has exactly 3 red edges, and a 3-regular graph on 9 vertices cannot exist.

20. The cliques of $C_7$ are its edges and vertices, so a cover needs at least $\lceil 7/2 \rceil = 4$ of them, and 4 suffice. Since $\alpha(C_7) = 3$, the cover number is larger than the independence number. It equals the chromatic number of the complement of $C_7$.

22. Number the vertices in reverse removal order, so each vertex has at most $d$ neighbours that come earlier. Find each triangle at its last vertex by checking every pair of its earlier neighbours with a hash set of edges. The work is at most $d$ per edge. A subgraph with minimum degree $d$ has at least $d(d + 1)/2$ edges, so $d \le \sqrt{2m}$.

24. The hub takes one color and the cycle must use the other $k - 1$, so $P(W_n, k) = k\, P(C_n, k - 1) = k((k - 2)^n + (-1)^n (k - 2))$. This gives 120 for $W_5$ with 4 colors and 6 for $W_6$ with 3 colors. $\chi(W_n)$ is 3 for even $n$ and 4 for odd $n$.

26. Induct on $n$, removing a vertex $v$. Adding $v$ back raises $\chi(G)$ only if $\deg_G(v) \ge \chi(G - v)$, and raises $\chi(\overline{G})$ only if $\deg_{\overline{G}}(v) \ge \chi(\overline{G} - v)$. The two degrees add up to $n - 1$.
