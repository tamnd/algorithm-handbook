1. (a) FPTAS. (b) EPTAS. (c) PTAS. (d) EPTAS. (e) FPTAS. (f) PTAS only: the exponent of $n$ grows with $1/\varepsilon$. (g) No scheme: the time is exponential in $n$.

3. $\mathrm{OPT} = 65$, from items 4 and 5. For $\varepsilon = 1/2$: $K = 6$, scaled profits $10, 8, 6, 5, 5$, and $q^* = 10$. Both $\{1\}$ and $\{4, 5\}$ have scaled profit 10, and the table keeps the lighter one, $\{1\}$ of weight 9, so the result is 60, above the bound $32.5$. For $\varepsilon = 1/4$: $K = 3$, scaled profits $20, 16, 12, 11, 10$, $q^* = 21$, and the result is $\{4, 5\}$ with profit 65, the optimum.

5. Step 1 keeps $0, 14$; step 2 keeps $0, 14, 18, 32$. Step 3 merges $0, 14, 18, 32, 46, 60, 64, 78$; TRIM removes 64 ($\le 66$) and line L6 removes 78, leaving $0, 14, 18, 32, 46, 60$. Step 4 merges $0, 14, 18, 32, 46, 58, 60, 72, 76, 90, 104, 118$; TRIM removes 60 ($\le 63.8$) and 76 ($\le 79.2$), and line L6 removes 90, 104 and 118. The result is 72, while $\mathrm{OPT} = 76 = 18 + 58$ and $\mathrm{OPT}/1.8 \approx 42.2$.

6. With $B = 1000$ and $\varepsilon = 1/1001$: $64{,}000 \cdot 1001 = 64{,}064{,}000$ steps. With $\varepsilon = 1/25$: $1{,}600{,}000$ steps. The exact table needs about $40 \cdot 1000 = 40{,}000$.

10. EPTAS: $2^j \le 100$, so $\varepsilon = 1/6$. PTAS: $10^{4j} \le 10^{10}$, so $\varepsilon = 1/2$. $n^2/\varepsilon^3$: $j^3 \le 100$, so $\varepsilon = 1/4$. $n/\varepsilon^2$: $j^2 \le 10^6$, so $\varepsilon = 1/1000$.

12. $LB = 14$, and the tests are 28, 20, 16 and 14, all accepted. At $T = 14$ the large jobs are the two 9s, both rounded to 7, and one configuration holds both, so one machine gets 18; the result has makespan $18 \le 21$. But $\mathrm{OPT} = 15$, and the test at $T = 20$, with no large jobs, already found a schedule of makespan 15. Keep the best schedule of all accepted tests; the guarantee stays $(1 + 1/k)\,\mathrm{OPT}$.

13. The page's proof gives $\mathrm{ALG} \ge \mathrm{OPT} - p_{\min}$, and $G$ alone is a candidate, so $\mathrm{ALG} \ge p(G) \ge k\,p_{\min}$. If $p_{\min} \le \mathrm{OPT}/(k+1)$ the first bound gives the claim, and otherwise the second does. So $k = \lceil 1/\varepsilon \rceil - 1$ suffices.

15. (a) Multiply every length by $c + 1$: all makespans become multiples of $c + 1$, so a result within $c$ of the optimum is optimal. (b) $I^{(k)}$ multiplies every length by $k$. Copies of the jobs on the same $m$ machines do not multiply the optimum, and copies with $km$ machines leave it unchanged.

19. For $x \ge 0$, $\sqrt x \le \varepsilon x + \frac{1}{4\varepsilon}$, because the difference is $\varepsilon\bigl(\sqrt x - \frac{1}{2\varepsilon}\bigr)^2 \ge 0$. So $c(\varepsilon) = 1/(4\varepsilon)$, and the asymptotic ratio is 1.

22. Each bin holds at most two items, so the number of bins is $n$ minus the number of pairs. Sort the items; put the largest with the smallest if they fit, and alone otherwise, and repeat. An exchange argument shows that some optimal packing makes the same choice for the largest item.

23. Given $G$ with $n \ge 5$ vertices, add a disjoint complete graph $K_n$. The result has $2n$ vertices and at least $n(n-1)/2 \ge (2n)^2/10$ edges, and its maximum cut is that of $G$ plus $\lfloor n^2/4 \rfloor$. A cut size is an integer at most $N^2$ on $N$ vertices, so an FPTAS with $\varepsilon < 1/N^2$ would be exact.

24. Give item $i$ the weights $(a_i, M - a_i)$ with $M = 2A$, the capacities $A$ and $(n/2)M - A$, and profit 1. A set of $s$ items fits only if $s \le n/2$, and $s = n/2$ forces its sum to be exactly $A$. So $\mathrm{OPT} = n/2$ exactly when the answer is yes, and an FPTAS with $\varepsilon = 1/(n + 1)$ decides it.

25. Let $B$ be the least edge cost such that the edges of cost at most $B$ hold an $s$-$t$ path of delay at most $D$; binary search over the sorted costs, with one shortest-delay computation on the DAG per test. An optimal path has an edge of cost at least $B$, and the path found has at most $n - 1$ edges of cost at most $B$. Drop the edges of cost above $(n - 1)B$, round the costs down by $K = \varepsilon B / n$, and fill a table of least delay over vertex and scaled cost, with at most $n(n - 1)/\varepsilon$ costs. The error is below $(n - 1)K < \varepsilon B \le \varepsilon\,\mathrm{OPT}$, and the time is $O(mn^2/\varepsilon + m \log m)$.

26. Drop the jobs with $p_j > d_j$. A set of jobs can all finish on time exactly when they do so in order of due date. Sort by due date, and let $A[j][q]$ be the least total length of an on-time subset of the first $j$ jobs with weight $q$; job $j$ may be added when $A[j-1][q - w_j] + p_j \le d_j$. Scale the weights by $K = \varepsilon w_{\max}/n$, which works because $w_{\max} \le \mathrm{OPT}$.

27. If the job that ends last is one of the $k$ longest, the makespan is the optimum for those $k$ jobs, at most $\mathrm{OPT}$. Otherwise its length is at most $p_{k+1}$, and the bound for list scheduling gives at most $\sum_j p_j/m + (1 - 1/m)\,p_{k+1}$. Some machine gets $1 + \lfloor k/m \rfloor$ of the $k + 1$ longest jobs, so $\mathrm{OPT} \ge (1 + \lfloor k/m \rfloor)\,p_{k+1}$. With $k = m \lceil 1/\varepsilon \rceil$ the ratio is below $1 + \varepsilon$, but $m^k$ is not polynomial when $m$ grows.
