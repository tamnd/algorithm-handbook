2. $Y_N = \{(1, 9), (2, 7), (4, 4), (6, 3), (9, 2), (10, 1)\}$. The ideal point is $(1, 1)$ and the nadir point is $(10, 9)$. The point $(2, 7)$ dominates $(3, 8)$, and $(4, 4)$ dominates both $(5, 5)$ and $(7, 6)$.

4. The fronts are $\{P, Q, S, U, W\}$ and $\{R, T, V\}$. The Fonseca and Fleming ranks are $1$ on the first front, $2$ for $R$ (dominated by $Q$), and $3$ for $T$ (by $Q$ and $S$) and for $V$ (by $S$ and $U$). So $T$ and $V$ are on front $2$ but have rank $3$.

6. Sorted by the first objective, the strips are $5 \cdot 1$, $4 \cdot 2$, $2 \cdot 1$ and $1 \cdot 1$, so the hypervolume is $16$. The exclusive contributions are $1$, $4$, $1$ and $1$ in the same order.

8. The nearest points are $(1, 5)$ for $(0, 6)$, either point at distance $\sqrt 8$ for $(3, 3)$, and $(5, 1)$ for $(6, 0)$, so $\mathrm{IGD} = (\sqrt 2 + 2\sqrt 2 + \sqrt 2)/3 = 4\sqrt 2/3 \approx 1.886$. For IGD+ only the excess over the reference point counts: $1$, $2$ and $1$, so $\mathrm{IGD}^+ = 4/3$.

10. With $\lambda = (t, 1 - t)$, the point $(9, 2)$ beats $(6, 3)$ only if $t < 1/4$ and beats $(10, 1)$ only if $t > 1/2$. For the Tchebycheff function take $w_i = 1/y_i$, that is, $w = (1/9, 1/2)$: the value at $(9, 2)$ is $1$, and every other point of $Y$ has a value above $1$, the closest being $10/9$ at $(10, 1)$.

11. $\binom{N-1}{t} / \binom{N}{t} = (N - t)/N$. For $N = 10$ the least $t$ is $5$.

15. A point $(2^j, 2^{6-j})$ covers $(2^k, 2^{6-k})$ exactly when $\lvert j - k \rvert \le 1$, so each point covers at most three of the seven, and at least three points are needed. The set $\{(2, 32), (16, 4), (64, 1)\}$, with $j = 1, 4, 6$, covers all seven.

19. Round 1 checks the ideal point $(0, 0)$: $z = 2$, and the cut is $y_1 + y_2 \ge 4$. Round 2 has the vertices $(0, 4)$, with $z = 0$, and $(4, 0)$, with $z = 1/2$ and the cut $y_1 + 3 y_2 \ge 6$. Round 3 has the vertices $(0, 4)$, $(3, 1)$ and $(6, 0)$, all with $z = 0$, so the algorithm stops.

21. Sort the points by the first coordinate. The point in place $k$ is nondominated exactly when its second coordinate is the smallest among the first $k$ points, and by symmetry this has probability $1/k$. Sum over $k$ by linearity of expectation.

22. Membership in NP is clear. Given $a_1, \ldots, a_n$ with sum $2S$, build a chain of $n$ diamonds; diamond $i$ offers one side of total cost $(a_i, 0)$ and one of cost $(0, a_i)$, and set $B_1 = B_2 = S$. Every path costs $(\sigma, 2S - \sigma)$, and it meets both bounds exactly when $\sigma = S$.

23. The program is feasible at $(x^*, 0)$, and its optimum is $0$ because any $s \ne 0$ would give a solution that dominates $x^*$. Its dual asks for $\lambda$ and $\mu \ge 0$ with $C^T \lambda = A^T \mu$ and $\lambda \ge \mathbf{1}$, and strong duality gives $\lambda^T C x^* = \mu^T b$. Then $\lambda^T C x = \mu^T A x \ge \mu^T b$ for every $x \in X$.

24. Sort by $y_1$, so that $y_2$ falls. A chosen subset $i_1 < \cdots < i_k$ has the hypervolume $\sum_t (r_1 - y_{1, i_t})(y_{2, i_{t-1}} - y_{2, i_t})$, with $y_{2, i_0} = r_2$, so each term depends only on two consecutive chosen points. Let $D[t][j]$ be the best value of $t$ chosen points that end at $j$, and take the maximum over $i < j$ of $D[t-1][i]$ plus the term for the pair $(i, j)$.

25. Remove the dominated points of $A$ and sort the rest by $a_1$, so that $a_2$ falls; a dominated point never gives a smaller value. For a fixed $b$, the term $a_1 - b_1$ rises along the list and $a_2 - b_2$ falls, so the best $a$ is next to the place where they cross, which a binary search finds.
