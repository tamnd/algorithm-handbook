1. Page-at-a-time nested loops cost $400 + 400 \cdot 1000 = 400{,}400$ with $S$ outer and $1000 + 1000 \cdot 400 = 401{,}000$ with $R$ outer. Block nested loops cost $400 + \lceil 400/50 \rceil \cdot 1000 = 8400$ with $S$ outer and $1000 + 20 \cdot 400 = 9000$ with $R$ outer. Grace, building on $S$, makes partitions of $400/51 < 8$ pages, which fit in 50, so it costs $3 \cdot 1400 = 4200$. Sort-merge makes $20 + 8 = 28 \le 50$ runs, so its combined plan also costs 4200. An in-memory hash join needs $400 \le B - 2$ and is not possible.

2. The rate is $(1 - e^{-4 \cdot 1000/8000})^4 = (1 - e^{-1/2})^4 \approx 0.024$. About $2000 + 0.024 \cdot 98{,}000 \approx 4349$ tuples are sent, against 100,000 without the filter.

4. The bounds are $5 \cdot 4 \cdot 3 = 60$ and $1 + 7 \cdot 5 = 36$. The eight group-bys have $5, 5, 4, 4, 4, 3, 2, 1$ cells for $ABC$, $AB$, $AC$, $BC$, $A$, $B$, $C$ and ALL, so CUBE has 28 cells. ROLLUP keeps only $ABC$, $AB$, $A$ and ALL, with $5 + 5 + 4 + 1 = 15$ cells. COUNT and MAX are distributive, AVG and the variance are algebraic, and MEDIAN and COUNT DISTINCT are holistic.

5. The pipelines are: scan $S$ into the hash table, ended by the build side of the join; scan $R$, select, probe and update the aggregation table, ended by the hash aggregation; read the aggregation table into the sort, ended by the sort; read the sorted output to the root. Writing and reading back both intermediate results costs $2(300 + 500) = 1600$ extra I/Os.

7. The upward pass removes $(4,7)$ from $T$, then $(2,4)$ from $S$, then $(4,9)$ from $R$. The downward pass removes $(9,9)$ from $U$. The output is $(1,1,3,6,8)$, $(2,2,5,6,8)$ and $(3,2,5,6,8)$. The plan builds 5 tuples for $R \bowtie S$ and 5 for the join with $T$, 10 intermediate tuples for 3 output tuples.

9. The codes are $r(0, 15, 0)$, $a_1(1, 6, 1)$, $b_1(2, 3, 2)$, $c_1(4, 5, 2)$, $a_2(7, 14, 1)$, $a_3(8, 11, 2)$, $c_2(9, 10, 3)$ and $b_2(12, 13, 2)$. The matches are $(a_1, b_1, c_1)$ and $(a_2, b_2, c_2)$. When $a_3$ is the head of its stream, the head of the $b$ stream is $b_2$, which starts at 12 after $a_3$ ends at 11, so $a_3$ is skipped. The path solutions are $(a_1, b_1)$, $(a_1, c_1)$, $(a_2, b_2)$ and $(a_2, c_2)$, and all of them are used. The binary join gives $(a_1, c_1)$, $(a_2, c_2)$ and $(a_3, c_2)$; the last belongs to no match.

10. The lists are $a, b, f, e, d, c$ and $c, d, e, f, a, b$. TA stops at depth 3, when the threshold $0.4 + 0.8 = 1.2$ is below $a$'s 1.7, after 6 sorted and 6 random accesses. FA stops at depth 4, when $e$ and $f$ have been seen in both lists. Both return $a$.

12. The keys are 2 for the root (corner $(1, 1)$), 7 for $L_1$ (corner $(1, 6)$), 4 for $L_2$ (corner $(3, 1)$) and 9 for $L_3$ (corner $(5, 4)$). BBS reads the root and $L_2$ and outputs $c$ with key 6. It then reads $L_1$, where $h$ is dropped because $c$ dominates it, and outputs $d$ and $b$ with key 8. At key 9 it drops $L_3$, whose corner $c$ dominates, and outputs $e$ and $a$. The skyline is output in the order $c, d, b, e, a$, after reading 3 of the 4 nodes.

13. Grace needs $12{,}000 \le (B - 1)(B - 2)$: $B = 111$ gives 11,990 and $B = 112$ gives 12,210, so $B = 112$. Sort-merge needs $\lceil 10{,}000/B \rceil + \lceil 40{,}000/B \rceil \le B - 2$: $B = 224$ gives $45 + 179 = 224$, too many, and $B = 225$ gives $45 + 178 = 223$, so $B = 225$.

15. A cluster may hold $2^{18}/32 = 2^{13}$ tuples, so $2^{26}/2^b \le 2^{13}$ gives $b = 13$. Each pass uses at most 6 bits, so 3 passes are needed, for example with 5, 4 and 4 bits. All tuples of a cluster share their low 13 bits, so a table indexed by those bits would put them all in one bucket.

16. For $B = 101$ there are 100 runs, $P = 2$ and the cost is 30,000. For $B = 21$ there are 477 runs, $P = 4$ and the cost is 70,000. With early aggregation no run holds more than 1000 states, that is 10 pages. Pass 0 reads 10,000 and writes at most 4770; merging 20 runs at a time gives 24 runs (read 4770, write at most 240), then 2 runs (read 240, write at most 20), and the last merge reads 20. The total is at most 20,060.

17. The ten cells are ALL with 6, $(x)$ with 3, $(x, p)$ with 2, $(x, \cdot, 1)$ with 2, $(y)$ with 2, $(\cdot, p)$ with 4, $(\cdot, p, 1)$ with 3, $(\cdot, q)$ with 2, $(\cdot, \cdot, 1)$ with 4 and $(\cdot, \cdot, 2)$ with 2. For AVG, a group with the values 1 and 5 has average 3, below $t = 4$, but its subgroup with the value 5 has average 5; pruning the group would lose that cell.

22. The join has 10 tuples and 30 values. With root $B$ the representation has $(1 + 3 + 3) + (1 + 1 + 1) = 10$ singletons, on the path $A$–$B$–$C$ it has 18, and on $B$–$A$–$C$ it has 16. In the tree with root $A$, the attributes $B$ and $C$ of $S$ are not on one root-to-leaf path, which breaks the path condition.

23. The pair $(b, 5)(b, 8)$ with score 13 is formed at read 4. The bound after the nine reads is $19, 19, 19, 18, 18, 17, 17, 16$ and then $-\infty$, so the pair is output only after read 9, when both inputs are exhausted. The term $10 + \text{bottom}_R$ allows for an unread tuple of $R$ that joins $a$, and $R$ has scores above 3 until its last tuple.

24. After step 1 the estimate is $6$ times the price of the pair if it joins: the six equally likely pairs give $18, 0, 30, 0, 0, 24$, with mean 12 and variance 156. After step 2 all of $S$ is read and the estimate is $\frac{6}{4}$ times the sum of the two prices read: $12$, $10.5$ or $13.5$, with mean 12 and variance $3/2$. After the last tuple of $R$ it is the exact sum 12.

25. Each level reads and writes both inputs, $2(M + N)$, and the final join reads them once more. After $L$ levels a part of $R$ has $M/(B - 1)^L$ pages. For the numbers given, $9 \cdot 10^L \ge 100{,}000$ first holds at $L = 5$, so the cost is $11(M + N)$.

26. With minsup $= 1$ every row is in one partition of every group-by, and every partition is expanded, so the row is sorted once for each pair $(S, d)$ with $d > \max S$. Map the pair to the nonempty set $S \cup \{d\}$; the map is a bijection, because $d$ is recovered as the largest element. For $D = 3$, grouping the sets by their largest element gives $3 + 2 + 2 + 0 = 7$.

27. The work at level $C$ is a sum over the pairs $(a, b)$ of $R$ that survive level $B$ of $\min(|S[b]|, |T[a]|)$. A pair with a light $a$ adds at most $\sqrt{N}$, and there are at most $N$ pairs. There are fewer than $\sqrt{N}$ heavy values, and for each, the pairs $(a, b)$ have distinct $b$, so they add at most $\sum_b |S[b]| \le N$.

28. Each pair of $A$, $B$ and $C$ appears together in some relation, so by the path condition all three lie on one root-to-leaf path, and the tree is a path. The deepest node has the whole query on its path, with $\rho^* = 3/2$. For the star, take $A$ as root with children $B$, $C$ and $D$: every path is covered by one relation. The full query needs weight 1 on each relation, because each of $B$, $C$ and $D$ is in only one.

29. The top $d$ of the second list is a uniform $d$-subset, independent of the top $d$ of the first. Use $E[D] = \sum_{d \ge 0} \Pr[D > d]$ and $\Pr[D > d] \le (1 - d/N)^d \le e^{-d^2/N}$, with a matching lower bound for $d \le \sqrt{N}$. For $N = 10{,}000$, exact summation gives $E[D] \approx 88.63$, against $\sqrt{\pi N}/2 \approx 88.62$.

30. A node's corner is no greater than the corners of its children, so an undominated node has undominated ancestors. If any point dominates a corner, some skyline point does, and it has a smaller key, so it is output before the node leaves the heap and the node is dropped. For the lower bound, add a point at the corner of an unread node: the rectangles do not change, the new point is in the skyline, and the algorithm cannot tell the two inputs apart.
