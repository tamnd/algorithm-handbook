1. The frontiers are $\{0\}$, $\{1, 2, 3\}$, $\{4, 5\}$, $\{6, 7\}$ and $\{8\}$, so $D = 5$ and the distances are $(0, 1, 1, 1, 2, 2, 3, 3, 4)$. The rounds read $3, 7, 7, 5, 2$ slots, 24 in all, which is $2m$. Vertex 4 is claimed by 1 and 2, vertex 5 by 2 and 3, vertex 6 by 4 and 5, and vertex 8 by 6 and 7. The dense version reads 24 slots in each of the 5 rounds, 120 in all.

2. The label 0 moves one step per round, so there are 6 rounds. They read $10, 9, 7, 5, 3, 1$ slots, 35 in all, which is $n^2 - 1$, against $6 \cdot 10 = 60$ for the dense form.

7. A height $h$ becomes $\lceil h/2 \rceil$: $20, 10, 5, 3, 2, 1$. Five shortcuts, which is $\lceil \lg 20 \rceil$.

9. Round 1: $m_f = 3$, $m_u = 21$, top-down, 3 edges. Round 2: $m_f = 9 > 12/2$ and the frontier grows, so bottom-up; 4, 5 and 6 find a parent at their first check and 7 checks all 3 neighbours, 6 edges. Round 3: $|F| = 3 < 8/2$, but the frontier does not shrink, so it stays bottom-up, and 7 finds 4 at once, 1 edge. Round 4: $|F| = 1$ and shrinking, so top-down, 3 edges. In total 13 against 24.

10. With $\Delta = 3$ the heavy arcs are $0 \to 2$, $1 \to 3$ and $1 \to 4$. Bucket 0 takes phases for 0 and 1, and its heavy step puts 3 at 6 in bucket 2 and 4 at 9 in bucket 3. Bucket 1 takes phases for 2 and 3, which move 3 to 5 and 4 to 7, and bucket 2 holds 4 and 5. So 3 buckets, 5 phases and 9 requests, one per arc; bucket 3 is never processed. With $\Delta = \infty$ the phases are $\{0\}$, $\{1, 2\}$, $\{2, 3, 4\}$, $\{3, 4, 5\}$, $\{5\}$, with $2 + 5 + 4 + 2 + 0 = 13$ requests. Both give $dist = (0, 2, 4, 5, 7, 7)$.

12. The centre leaves if it flips tails and some leaf flips heads, $(1 - 2^{-7})/2 = 127/256$; a leaf leaves if it flips tails and the centre heads, $1/4$. The expected number is $7/4 + 127/256 = 575/256 \approx 2.25$, a fraction of about $0.28$ of the 8 vertices. No vertex leaves only if all 8 coins agree, with probability $1/128$.

13. The preorder is $0, 1, 2, 3, 4, 5, 6$ with $pre(v) = v + 1$, and $nd = (7, 1, 5, 4, 1, 2, 1)$. The pairs $(low, high)$ are $(1, 7)$, $(2, 3)$, $(2, 7)$, $(4, 7)$, $(5, 6)$, $(5, 7)$, $(7, 7)$ for the vertices 0 to 6. Rule 1 joins 1 with 2 and 4 with 5; rule 2 joins nothing. The blocks are $\{01, 02, 12\}$, $\{23\}$, $\{34, 35, 45\}$ and $\{56\}$, and the bridges are $\{2, 3\}$ and $\{5, 6\}$.

17. With $\{3, 6\}$, $H$ has the arc $3 \to 6$. $R(0)$, $R(1)$ and $R(2)$ hold 3, $R(4)$ and $R(5)$ hold 6, and from 6 on $R(u)$ reaches 9, so the output is exact. Yet the windows $\{0, 1, 2\}$ and $\{7, 8, 9\}$ hold no sampled vertex: the condition of the proof is sufficient, not necessary, because $R(u)$ reaches $t$ arcs and not $t - 1$. With $\{4, 7\}$, $R(0) = \{0, 1, 2, 3\}$ holds no sampled vertex, so the 6 pairs $(0, 4)$ to $(0, 9)$ are missing; every other vertex is exact.

20. The vertex must flip tails and some neighbour heads: $(1 - p)(1 - (1 - p)^d)$, which grows with $d$, so the least value is $p(1 - p)$ at $d = 1$. This gives $q = 1 - p(1 - p)$, which is least, $3/4$, for $p = 1/2$. For $p = 1/3$, $q = 7/9$, and the bound allows $\ln(4/3)/\ln(9/7) \approx 1.14$ times as many rounds.

21. An edge is contracted when its two coins differ, so it takes 2 rounds in expectation. On $a, b, c$: with probability $1/8$ ($b$ heads, $a$ and $c$ tails) both leaves hook and no edge is left; with probability $1/4$ (all heads or all tails) nothing happens; otherwise one vertex leaves and an edge remains. So $E = 1 + E/4 + (5/8) \cdot 2$, and $E = 3$, against a bound of about $8.8$.

22. If the least priority is at 1 or 2, that vertex joins and removes three vertices, and no edge is left. If it is at 0, the edge $\{2, 3\}$ survives only when neither 2 nor 3 joins, which is the order $r(1) < r(2) < r(3)$, with probability $1/6$; the same holds for 3. So $E[m_1] = 2 \cdot \frac14 \cdot \frac16 = 1/12$, against the bound $3/2$.

23. On a path, a decreasing path is a run of consecutive vertices along which $\rho$ is monotone. With 3 vertices there are 3 rounds in the 2 monotone orders and 2 otherwise, so $7/3$. With 4 vertices, 2 orders give 4, the 10 alternating orders give 2 and the other 12 give 3, so $64/24 = 8/3$. For $n = 10^6$ and $\Delta = 3$ the bound is about $1.2 \cdot 10^{-6}$ at $k = 23$ and $1.5 \cdot 10^{-7}$ at $k = 24$, so $k = 24$, while the general formula gives $\max(22.2, 27.6) = 27.6$.

24. With $\lambda(v) = v$, the iteration on $\{0, \ldots, j - 1\}$ colours every vertex $j - 1$ in $j$ rounds and finds only $\{j - 1\}$: $n$ iterations and $n(n + 1)/2$ rounds. With $\lambda(v) = n - 1 - v$, every vertex already holds the largest label that reaches it: 1 iteration, 1 round, all $n$ SCCs. With random labels, $v$ is a root when $\lambda(v)$ is larger than every $\lambda(u)$ with $u > v$, a record of the sequence read from $n - 1$ down, so the expected number is $H_n = 1 + 1/2 + \cdots + 1/n$.
