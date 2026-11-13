1. Page-at-a-time nested loops cost $400 + 400 \cdot 1000 = 400{,}400$ with $S$ outer and $1000 + 1000 \cdot 400 = 401{,}000$ with $R$ outer. Block nested loops cost $400 + \lceil 400/50 \rceil \cdot 1000 = 8400$ with $S$ outer and $1000 + 20 \cdot 400 = 9000$ with $R$ outer. Grace, building on $S$, makes partitions of $400/51 < 8$ pages, which fit in 50, so it costs $3 \cdot 1400 = 4200$. Sort-merge makes $20 + 8 = 28 \le 50$ runs, so its combined plan also costs 4200. An in-memory hash join needs $400 \le B - 2$ and is not possible.

3. The bucket $[20, 40)$ gives half of 4000 and $[40, 60)$ half of 3000, so the estimate is 3500. With the second predicate it is 350, assuming the two predicates are independent.

4. The edges are $T_1 \to T_2$ and $T_1 \to T_3$ on $x$, $T_3 \to T_2$ from $r_3(x)$ before $w_2(x)$, and $T_2 \to T_3$ from $r_2(y)$ before $w_3(y)$. The cycle between $T_2$ and $T_3$ means it is not conflict serializable. It is not view serializable either: $r_3(x)$ reads from $T_1$ and $T_2$ writes $x$ last, so $T_3$ must come before $T_2$, while $r_2(y)$ reads the initial $y$, which $T_3$ overwrites. Without $r_2(y)$ the only serial order is $T_1\, T_3\, T_2$.

7. Analysis gives the transaction table $\{T_1{:}80, T_3{:}70\}$, with $T_2$ ended, and the dirty page table $\{P_1{:}10, P_2{:}80, P_3{:}50\}$. Redo starts at 10 and skips 20 without a fetch, since $P_2$ has recLSN 80. Undo processes 80, 70, 50 and 10 in that order and writes four compensation records.

8. $C$ is on no right side, so it is in every key, and $C^+ = C$. The keys are $AC$, $BC$, $CD$ and $CE$. Every attribute is prime, so $R$ is in 3NF; it is not in BCNF, because $A^+ = AB$.

10. TA stops at depth 3, when the threshold $0.4 + 0.8 = 1.2$ is below $a$'s 1.7. FA stops at depth 4, when $e$ and $f$ have been seen in both lists. Both return $a$.

13. Grace needs $12{,}000 \le (B - 1)(B - 2)$: $B = 111$ gives 11,990 and $B = 112$ gives 12,210, so $B = 112$. Sort-merge needs $\lceil 10{,}000/B \rceil + \lceil 40{,}000/B \rceil \le B - 2$: $B = 224$ gives $45 + 179 = 224$, too many, and $B = 225$ gives $45 + 178 = 223$, so $B = 225$.

15. The only conflicts give $T_1 \to T_2$ and $T_3 \to T_1$, so $T_3\, T_1\, T_2$ is equivalent. Under 2PL, $T_1$ must release $x$ before $w_2(x)$, and it cannot lock $y$ until $r_3(y)$ has run, so it would lock after it unlocks. Basic TO aborts $T_1$ at $w_1(y)$, since $y$ was read with timestamp 3. Serialization graph testing accepts it, because it accepts every conflict-serializable schedule.

17. BCNF gives $AB$, $CD$, $DE$ and $EA$, and loses $BC \to D$. The dependencies are already a minimal cover, so synthesis gives $AB$, $BCD$, $DE$ and $EA$, and $BCD$ contains the key $BC$. $BCD$ is not in BCNF, because $D \to B$ holds and $D$ is not a key of it.

20. A closed walk of length $m$ maps onto a directed cycle of length $n$ exactly when $n$ divides $m$. A homomorphism from the body of $Q_6$ to the body of $Q_3$ exists, so $Q_3 \subseteq Q_6$: go round the triangle twice. No other inclusion holds.

21. Semi-naive fires each instance once, one per path fact: $n(n-1)/2$. Naive runs $n$ rounds. It fires the exit rule $n - 1$ times in each, and in round $r$ it fires $\sum_{d < r} (n - 1 - d)$ recursive instances. The total is $(n^3 - n)/3$.

22. NRA stops at depth 5, when $a$'s grades are both known, $1.7$, and the best case of $b$ is $0.9 + 0.7 = 1.6$. It makes 10 sorted accesses and no random ones. TA made 6 sorted and 6 random accesses.

25. Each level reads and writes both inputs, $2(M + N)$, and the final join reads them once more. After $L$ levels a part of $R$ has $M/(B - 1)^L$ pages. For the numbers given, $9 \cdot 10^L \ge 100{,}000$ first holds at $L = 5$, so the cost is $11(M + N)$.

26. Join $R$, $S$ and $T$ on one attribute $A$. For $\{R, S\}$, let a hash join cost 100 and a merge join cost 120, the latter with output sorted on $A$. If $T$ is stored sorted on $A$, a merge with sorted input costs 50, while unsorted input must first be sorted, at 100. Keeping only the hash plan gives 250; the merge plan gives 170.

27. There are at most $\sqrt{N}$ heavy values. A heavy $a$ and a tuple of $S$ make at most one triangle, which gives $N^{3/2}$. A tuple $(c, a)$ of $T$ with light $a$ extends in fewer than $\sqrt{N}$ ways, which gives another $N^{3/2}$. For the instance, let each relation be all pairs over $\sqrt{N}$ values.

28. The triangles are $(0, b, 0)$, $(0, 0, c)$ and $(a, 0, 0)$, so there are $3N + 1$. Any two of the relations share one attribute, and both have $N + 1$ tuples with 0 there, which gives $(N + 1)^2$ pairs. Generic join with the order $A, B, C$, intersecting in time proportional to the smaller set, does $O(N)$ work: only $a = 0, b = 0$ has more than one candidate for $C$.

29. Snapshot isolation forbids a cycle of write–write and write–read edges alone, because they follow commit order. So some edge is a read–write edge between concurrent transactions. Take the transaction $T$ of the cycle that commits first. Show that the edge into $T$ and the edge before it are both read–write edges between concurrent transactions.
