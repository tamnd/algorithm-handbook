1. Page-at-a-time nested loops cost $400 + 400 \cdot 1000 = 400{,}400$ with $S$ outer and $1000 + 1000 \cdot 400 = 401{,}000$ with $R$ outer. Block nested loops cost $400 + \lceil 400/50 \rceil \cdot 1000 = 8400$ with $S$ outer and $1000 + 20 \cdot 400 = 9000$ with $R$ outer. Grace, building on $S$, makes partitions of $400/51 < 8$ pages, which fit in 50, so it costs $3 \cdot 1400 = 4200$. Sort-merge makes $20 + 8 = 28 \le 50$ runs, so its combined plan also costs 4200. An in-memory hash join needs $400 \le B - 2$ and is not possible.

3. The upward pass removes $(4,7)$ from $T$, then $(2,4)$ from $S$, then $(4,9)$ from $R$. The downward pass removes $(9,9)$ from $U$. The output is $(1,1,3,6,8)$, $(2,2,5,6,8)$ and $(3,2,5,6,8)$. The plan builds 5 tuples for $R \bowtie S$ and 5 for the join with $T$, 10 intermediate tuples for 3 output tuples.

4. The lists are $a, b, f, e, d, c$ and $c, d, e, f, a, b$. TA stops at depth 3, when the threshold $0.4 + 0.8 = 1.2$ is below $a$'s 1.7, after 6 sorted and 6 random accesses. FA stops at depth 4, when $e$ and $f$ have been seen in both lists. Both return $a$.

7. The rate is $(1 - e^{-4 \cdot 1000/8000})^4 = (1 - e^{-1/2})^4 \approx 0.024$. About $2000 + 0.024 \cdot 98{,}000 \approx 4349$ tuples are sent, against 100,000 without the filter.

8. The skyline is $\{a, b, d, f, h\}$. The sorted order is $d, f, b, h, a, e, g, c, i$. Pass 1 outputs $d$ and $f$, drops $e$, $g$ and $i$, and writes $b, h, a, c$. Pass 2 outputs $b$ and $h$, drops $c$, and writes $a$. Pass 3 outputs $a$.

10. Grace needs $12{,}000 \le (B - 1)(B - 2)$: $B = 111$ gives 11,990 and $B = 112$ gives 12,210, so $B = 112$. Sort-merge needs $\lceil 10{,}000/B \rceil + \lceil 40{,}000/B \rceil \le B - 2$: $B = 224$ gives $45 + 179 = 224$, too many, and $B = 225$ gives $45 + 178 = 223$, so $B = 225$.

11. With $k = 1$, $c = 396$ and $396 + 398 < 1000$, so $k = 2$, $c = 395$ and $d = \lceil 605/2 \rceil = 303$. Then $\rho = 395/1001$, $W \approx (606/1001) \cdot 4000 \approx 2422$, and the cost is about $4000 + 2 \cdot 2422 \approx 8843$ I/Os, against 12,000 for Grace.

16. (a) $\rho^* = 2$: the cover $AB = CD = 1$ and the packing $1/2$ on every vertex. (b) $5/2$: $1/2$ on every edge and on every vertex. (c) $2$: the cover $AB = CD = 1$ and the packing $y_A = y_B = 1/2$, $y_C = 0$, $y_D = 1$. (d) $5/2$: the cover $AB = 1$ and $1/2$ on $CD, DE, EC$, and the packing $1/2$ on every vertex. The bounds are $N^2$, $N^{5/2}$, $N^2$ and $N^{5/2}$.

21. Each level reads and writes both inputs, $2(M + N)$, and the final join reads them once more. After $L$ levels a part of $R$ has $M/(B - 1)^L$ pages. For the numbers given, $9 \cdot 10^L \ge 100{,}000$ first holds at $L = 5$, so the cost is $11(M + N)$.

22. The work at level $C$ is a sum over the pairs $(a, b)$ of $R$ that survive level $B$ of $\min(|S[b]|, |T[a]|)$. A pair with a light $a$ adds at most $\sqrt{N}$, and there are at most $N$ pairs. There are fewer than $\sqrt{N}$ heavy values, and for each, the pairs $(a, b)$ have distinct $b$, so they add at most $\sum_b |S[b]| \le N$.

23. $R \bowtie S$ and $T \bowtie U$ each have at most $N^2$ tuples, and the final join outputs at most $N^2$, so each hash join runs in $O(N^2)$. For the instance, take $R = \{(i, 0)\}$, $S = \{(0, j)\}$, $T = \{(j, 0)\}$ and $U = \{(1, i)\}$ for $1 \le i, j \le m$. Then $R \bowtie S$ has $m^2$ tuples and $T \bowtie U$ is empty. Generic join that binds $D$ first intersects $\{0\}$ with $\{1\}$ and stops.

24. The top $d$ of the second list is a uniform $d$-subset, independent of the top $d$ of the first. Use $E[D] = \sum_{d \ge 0} \Pr[D > d]$ and $\Pr[D > d] \le (1 - d/N)^d \le e^{-d^2/N}$, with a matching lower bound for $d \le \sqrt{N}$. For $N = 10{,}000$, exact summation gives $E[D] \approx 88.63$, against $\sqrt{\pi N}/2 \approx 88.62$.

25. Put the top object first in the first list with grade 1 and last in the second list with grade 0. Give the other objects grades below 0.2 in the first list and below 0.5 in the second. After depth 2, the top object scores at least 1 and every other object at most $0.2 + 0.5$. Lowering or raising the second grade of the top object, while it stays below every other grade of the second list, changes nothing that is read before depth $N$, so the exact score stays unknown until then.
