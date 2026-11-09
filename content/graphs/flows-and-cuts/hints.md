1. Paths $s, a, c, t$ (4), $s, b, c, t$ (2), $s, b, d, t$ (4), $s, b, d, c, t$ (2); the value is 12. At the end, $s$ reaches only $a$ and $b$, and the cut $\{s, a, b\}$ has the arcs $a \to c$, $b \to c$, $b \to d$ with capacity $4 + 2 + 6 = 12$.

2. Phase 1: levels $s$ 0, $a, b$ 1, $c, d$ 2, $t$ 3; the arcs $a \to b$ and $d \to c$ are left out. A blocking flow sends 4 along $s, a, c, t$, 2 along $s, b, c, t$ and 4 along $s, b, d, t$. Phase 2: levels $s$ 0, $a, b$ 1, $d$ 2, $c$ 3, $t$ 4, and 2 units go along $s, b, d, c, t$. Phase 3 finds no path. The total is 12.

3. The value is 9. One decomposition: $s, a, t$ with 4, $s, a, b, c, t$ with 1, $s, b, c, t$ with 4, and the cycle $a, b, c, a$ with 1.

4. Alternate $s, a, b, t$ and $s, b, a, t$, each with bottleneck 1. Edmonds-Karp takes the two paths of length 2 and stops after 2 augmentations.

5. Three, since each corner has degree 3; the three edges at the start corner form a cut.

6. A and B play each other 4 times, and D can win at most 80. Then A can win at most 1 more and B at most 2 more, which is 3 wins for 4 games. So D is eliminated, and $\{A, B\}$ proves it: their average final win total is at least $(79 + 78 + 4)/2 = 80.5$.

7. Phase 1: $a, e, c, d, b$, cut 12; merge $b$ into $d$. Phase 2: $a, e, bd, c$, cut 17. Phase 3: $a, e, bcd$, cut 13. Phase 4: $a, bcde$, cut 11. The minimum cut is $\{a\}$ against the rest, of weight 11.

8. At least $2/(n(n - 1)) = 1/45$. Since $(1 - 1/45)^T \le e^{-T/45}$, about $45 \ln 100 \approx 208$ runs suffice.

9. The path $a$–$d$ (5), $d$–$c$ (4), $c$–$b$ (3). The values: $ab$ 3, $ac$ 4, $ad$ 5, $bc$ 3, $bd$ 3, $cd$ 4.

11. An arc $u \to v$ is in some minimum cut iff it is saturated and the final residual graph has no path from $u$ to $v$. Compute the strong components of the residual graph.

13. Choose everything: $10 + 6 + 3 - 4 - 7 - 2 = 6$. The maximum flow is $19 - 6 = 13$, the sum of the profits minus the best net profit.

17. First $s, a, b, t$ with cost 3 and 1 unit, then $s, b, t$ with cost 4 and 2 units. The total cost is $3 + 8 = 11$.

18. Two cells: the corner has only two neighbours.

21. Each arc is saturated, or found dead, once per phase. After $k$ phases every residual path has more than $k$ arcs, and a residual flow decomposes into arc-disjoint unit paths. The bound is $O(m^{3/2})$.

23. Make the network with a source joined to each edge node, edge nodes joined to their two ends, and each vertex joined to the sink with capacity $g$; a cut of value less than $|E|$ marks a denser set. Binary search on $g$.

24. A minimum $u$–$w$ cut separates $v$ from $u$ or from $w$.

25. Each path between two leaves uses two of the three edges, so the total flow is at most $3/2$, which half a unit on each pair achieves. Every multicut needs two edges.
