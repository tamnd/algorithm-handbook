1. Five matches give 10. With $d = 2$ the three gap symbols cost 6, so the score is 4. With the affine penalty there are two gaps, of lengths 2 and 1, costing $4 + 3 = 7$, so the score is 3.

3. It fills $1001 \cdot 501 = 501{,}501$ cells. For the score alone it keeps two rows of the shorter sequence, 1002 entries. Hirschberg's algorithm computes about twice as many cells as the full table, about $10^6$, and keeps only a few rows.

6. $E = \frac{1}{3} \cdot 10^9 \cdot 3^{-20} = 10^9 / 3^{21} \approx 0.0956$, and $P = 1 - e^{-E} \approx 0.0912$.

9. The entropy is $\frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 2 + 2 \cdot \frac{1}{8} \cdot 3 = 1.75$ bits, so the stack is $2 - 1.75 = 0.25$ bits high. The letters take their frequencies of it: A 0.125, C 0.0625, G and T 0.03125 each.

10. Put $u = e^\lambda$. For $\pm 1$ the equation is $u/4 + 3/(4u) = 1$, so $u^2 - 4u + 3 = 0$ and $u = 3$. For $+1/-2$ it is $u/4 + 3/(4u^2) = 1$, so $u^3 - 4u^2 + 3 = (u - 1)(u^2 - 3u - 3) = 0$ and $u = (3 + \sqrt{21})/2$, $\lambda \approx 1.3327$. The identities are $u/4$: 75% and about 95%.

13. The forward row is $-4, 0, 1, -1, -3, -2$ for $j = 0, \ldots, 5$, and the backward row is $2, 4, 0, -1, -2, -6$. Their sums peak at 4, the optimal score, only at $j = 1$: AC is aligned with A, and GTC with GTAC.

14. With $d = 2$ the best score is 4, reached by `AGGTCA` over `AG--CA` and over `A-G-CA`. With the affine penalty the best is 3, reached only by `AG--CA`, where the two gap symbols form one gap.

16. Count the strings of 0s and 1s with no hit by a dynamic program over the last few columns. With 10 columns, 111 hits in 520 of 1024 cases and 1101 in 535, so $0.508$ against $0.522$. With 8 columns both hit in 107 of 256. The spaced seed's hits overlap less, so they are spread over more regions.

19. The distance sums are 3, 4, 4 and 5, so GATTACA is the center, with $S = 3$. The bound gives a cost of at most $(k - 1)S = 9$. The six pairwise distances are 1, 1, 1, 1, 2 and 2, so every alignment costs at least 8. The exact program gives 9, so here the star alignment is optimal.

21. The function $f(\lambda) = \sum p_a p_b e^{\lambda s(a, b)}$ is a sum of exponentials, so it is convex. It has $f(0) = 1$ and $f'(0) = \sum p_a p_b s(a, b) < 0$, and it tends to infinity because one term has a positive exponent. A convex function that starts at 1, goes down and then goes to infinity crosses 1 exactly once on $\lambda > 0$.

22. A forward pass with two rows finds the score and an end cell $(i^*, j^*)$ of an optimal alignment. A second pass on the reversed prefixes $x_1 \cdots x_{i^*}$ and $y_1 \cdots y_{j^*}$ finds a start cell where the score reaches the optimum. Between the two cells the alignment is global, so Hirschberg's algorithm finds it in linear space.

23. Each pair has a unique optimal alignment: A over C, A over the A of AC, and C over the C of AC. The first needs A and C in one column, and the other two would then put both letters of AC in that column, which is impossible. So one pair costs at least 1 more than its distance, and the alignment with columns (A, C, A) and ($-$, $-$, C) costs 4.

24. Align only the letters A: the score is at least the smaller number of As in the two sequences, which is $n/4 - O(\sqrt{n})$ in expectation. The Karlin-Altschul law needs a negative expected score, and with free gaps an alignment can avoid every mismatch, so the score has a positive drift and grows linearly.
