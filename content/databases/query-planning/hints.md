3. The lower bound is $\max(0, 0.7 + 0.6 - 1) \cdot 1000 = 300$, the upper bound is $\min(0.7, 0.6) \cdot 1000 = 600$, and independence gives 420. The upper bound is reached when every row that satisfies the second predicate also satisfies the first. The lower bound is reached when the 300 rows that fail the first predicate all satisfy the second.

8. The q-errors are 4, 5 and 1. The ratio treats an estimate 4 times too small and one 4 times too large alike, and errors in a plan multiply along the joins, so a ratio measures them in the way that matters for cost.

9. Independence gives $2000 \cdot 0.1 \cdot 0.09 = 18$ rows, and the true count is 180, ten times more. The largest possible ratio is $1/\max(s_1, s_2) = 1/0.1 = 10$, reached when one set of rows contains the other, as here. A model equal to the joint distribution returns $2000 \cdot P(\text{Denver}) \cdot P(\text{DEN} \mid \text{Denver}) = 2000 \cdot 0.1 \cdot 0.9 = 180$, the exact count.

10. The full scan costs 2000. The index on $a$ costs $3 + 1 + 40 = 44$, since 40 tuples match and each costs one page. The clustered index on $b$ costs $3 + 100 + 400 = 503$. The unclustered index wins while $3 + 300F + 80{,}000F < 2000$, that is $F < 1997/80{,}300 \approx 0.0249$, close to the rule of thumb $F < N/T = 1/40$.

11. With $\sqrt{n/r} = 10$, the estimate is $10 \cdot 30 + 10 + 5 + 1 = 316$. The guarantee gives $D \ge 31.6$, which is weaker than the 46 values the sample already shows. The guarantee is about overestimates; it says the estimate is never more than 10 times too high.

13. The cycle has 21 connected sets: the $n(n-1)$ arcs that are not the whole cycle, and the cycle itself. It has 40 csg-cmp pairs, twice as many as the chain and fewer than half of the clique. The pairs of a cycle number $n(n-1)^2/2$, which gives 6, 18, 40, 75 for $n = 3, 4, 5, 6$; a script that lists all pairs of disjoint connected sets checked $n = 3$ to 8.

14. The best split is $(1, 1) \mid (9, 10) \mid (2, 2, 3)$, with sum of squares $0 + 1/2 + 2/3 = 7/6$. The next best split, $(1, 1) \mid (9, 10, 2) \mid (2, 3)$, has $77/2$. A script that tried all 15 splits with exact fractions checked this. The point is that a bucket should hold values of similar frequency, not a fixed number of rows.

15. In the first round the benefits are 100 for $a$, 120 for $b$ and 99 for $\emptyset$, so $b$ is chosen. In the second round $a$ saves 50 and $\emptyset$ saves 39, so $a$ is chosen, for a total cost of $100 + 50 + 40 + 40 = 230$. The pairs $\{a, \emptyset\}$ and $\{b, \emptyset\}$ cost 251 and 241, so greedy is optimal here.

19. GOO first joins $A$ and $B$ (50 rows), then $C$ and $D$ (200 rows), then the two halves (100 rows), for $C_{\mathrm{out}} = 350$. The best plan is $A \bowtie ((B \bowtie C) \bowtie D)$, with $100 + 20 + 100 = 220$. The ratio is $35/22 \approx 1.59$. A script that tried every bushy plan without cross products checked this.

22. The plan $5c$ is cheapest for $c \le 5000$, the plan $20{,}000 + c$ for $5000 \le c \le 12{,}500$, and $30{,}000 + 0.2c$ beyond. For $c = 800$ the optimizer takes the first plan, with validity range $c \le 5000$; the crossing with the third plan, at 6250, comes later and does not matter. At $c = 20{,}000$ the chosen plan costs 100,000 and the best one 34,000, which is 66,000 more, a factor of about 2.94.

24. In the order $R, S$ a walk returns 4 with probability $1/2$ (from rows 1 and 2), 12 with probability $1/4$ (from row 3, whatever match it picks) and 0 with probability $1/4$ (row 4 has no match). The mean is 5 and the variance 19. In the order $S, R$ it returns 8 with probability $1/4$ and 4 with probability $3/4$, with mean 5 and variance 3. The standard error after $W$ walks is $\sqrt{\mathrm{Var}/W}$, so the two orders need about 76 and 12 walks.

25. A connected set of a path is a subpath. For an interval $[i, j]$ try each split point $k$ with $i \le k < j$, add the costs of $[i, k]$ and $[k+1, j]$ and the size of $[i, j]$, and keep the minimum. There are $O(n^2)$ intervals and $O(n)$ splits each. A chain is a tree query, and the hardness proofs need general query graphs or cross products.

26. Swapping two neighbors $R_a$ and $R_b$ changes only the size after the first of them, from $P n_a f_a$ to $P n_b f_b$, where $P$ is the size before both. All other terms of the sum stay the same.

28. The groups are the connected sets, the $n(n+1)/2$ intervals. An interval of length $L$ has $L - 1$ split points, each giving two ordered expressions, so the count is $\sum_{L=1}^{n} (n - L + 1) \cdot 2(L - 1) = (n^3 - n)/3$. The memo, and so the work of a top-down search, is cubic in $n$ on a chain instead of exponential.

29. The connected sets are $A$, $B$, $C$, $D$, $AB$, $BC$, $ABC$ and $ABCD$, and the pairs are $(A, B)$, $(B, C)$, $(AB, C)$, $(A, BC)$ and $(ABC, D)$. $D$ is linked only through the hyperedge, which needs both $A$ and $C$ on the other side, and $A$ and $C$ are connected only through $B$. With simple edges the graph is a cycle of 4, with 18 pairs, and plans such as $A \bowtie D$ appear in which the predicate cannot be checked, so they are cross products priced as joins.

30. For a result $(r, s)$, let the later of the two arrive at time $t$. The earlier tuple was built before $t$, and the later one probes after $t$, so it finds the earlier one; the earlier one never finds the later one, whose timestamp is larger. Without the test, let both arrive before either is routed: each probe finds the other. A result can come only from the probe of $r$ or the probe of $s$, and each tuple probes once, so it comes out at most twice.
