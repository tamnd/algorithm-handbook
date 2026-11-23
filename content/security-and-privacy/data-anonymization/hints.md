1. The table is 3-anonymous, and not more, since every block has three rows. Block A has 2 distinct values, block B has 1 and block C has 3. The woman falls in block B, so the neighbour learns that she has heart disease: this is the homogeneity attack, and k-anonymity does nothing against it.

2. $H = \log_2 6 - (3 \log_2 3 + 2)/6 \approx 1.459$ bits. The integer test compares $6^6 = 46656$ with $l^6 \cdot 3^3 \cdot 2^2$: for $l = 2$ this is $6912$, so the block is entropy 2-diverse; for $l = 3$ it is $78732$, so it is not entropy 3-diverse. Recursive $(c, 2)$ needs $3 < c (2 + 1)$, so $c > 1$; recursive $(c, 3)$ needs $3 < c \cdot 1$, so $c > 3$.

3. Ordered distances: $7/30$, $1/10$ and $1/5$. Equal distances: $1/2$, $1/3$ and $1/3$. The release is $t$-close under the ordered distance exactly when $t \ge 7/30$.

6. The users at $(1, 1)$, $(2, 3)$ and $(3, 0)$ receive $[0, 4)^2$: that quadrant holds three users, but none of its sub-quadrants does. The four others receive the whole area $[0, 8)^2$, because each of their quadrants holds fewer than three users.

8. Every single item has support 4, every pair support 3 and the triple support 2, so $k = 4$, $3$ and $2$ for $m = 1$, $2$ and $3$.

10. The counts are 8 for every vector $(0, j)$, 6 for $(1, 0)$ and $(2, 0)$, 1 for $(1, 1)$, $(1, 2)$, $(1, 3)$, $(2, 1)$ and $(2, 2)$, and 0 only for $(2, 3)$. With MaxSup = 0 the search tries heights 2 and 4, finds nothing and returns the top $(2, 3)$. With MaxSup = 1 it tries height 2, finds $(1, 1)$, then tries height 1, finds nothing and returns $(1, 1)$.

12. MDAV forms $\{25, 26, 29\}$, then $\{6, 7, 8\}$, then $\{9, 14, 24\}$, with loss $382/3 \approx 127.3$. The optimum is $\{6, 7, 8, 9, 14\}, \{24, 25, 26, 29\}$ with loss $264/5 = 52.8$. The total sum of squares is $6392/9 \approx 710.2$, so the losses are about 17.9% and 7.4% of it.

15. Sort the sequence and use the dynamic program over groups of consecutive degrees of sizes $k$ to $2k - 1$, each raised to its largest value. For $k = 3$ the least increase is 6, reached by $(5, 5, 5, 5, 2, 2, 2, 2, 2)$ and by $(5, 5, 5, 3, 3, 3, 2, 2, 2)$. For $k = 2$ it is 2, with $(5, 5, 4, 4, 2, 2, 2, 1, 1)$.

17. The rows of vertices 1 to 6 are $(0, 0, 1, 1)$, $(0, 2, 2, 0)$, $(0, 3, 3, 0)$, $(4, 0, 0, 4)$, $(5, 0, 0, 5)$ and $(6, 6, 0, 0)$, and $c = n(m - 1) = 18$. The matching $\{e_1, e_3\}$ gives the classes $\{1, 2, 3\}$, keeping column 1, and $\{4, 5, 6\}$, keeping column 3, at cost 18. One class of six rows must suppress every entry, since no column is constant, at cost 24.

19. Write $C_i = \sum_{j \le i} (p_j - w_j)$. Since the differences sum to 0, each $|C_i|$ is at most the sum of the positive differences, which is the equal distance. The ordered distance is the mean of $m - 1$ such terms. For $m = 2$ the one term is $|p_1 - w_1|$, which is the equal distance.

20. If all $C_i$ have one sign, $\sum_{i=1}^{m-1} |C_i| = |\sum_{i=1}^{m-1} C_i|$, and summing by parts gives $\sum_{i=1}^{m-1} C_i = \sum_j (m - j)(p_j - w_j) = \sum_j j \, w_j - \sum_j j \, p_j$. For the third block the means are 4.5 and 3.5, giving $1/5$, which is correct. For the first block the partial sums end with a negative term, and the formula gives $1/5$, not $7/30$.

21. Bob's candidate set is $\{a, b\}$ in release 1 and $\{b, c\}$ in release 2, so the attacker learns that his value is $b$. For 2-invariance the person of age 23 must again be in a group with the signature $\{c, d\}$. The groups have distinct values, so the partner must have value $d$, and no one in release 2 has it.

22. Take $m$ copies of the origin of $\mathbb{R}^d$. For each attribute $i$ and each $t = 1, \ldots, k - 1$, add the two points that are $-t$ and $+t$ on attribute $i$ and 0 elsewhere. All of these points are distinct, so the largest number of equal rows is $m$. On attribute $i$, a cut below 0 leaves at most $k - 1$ rows on the left, and a cut at 0 leaves $k - 1$ rows on the right.
