2. (a) 1: only the row 1 passes, since NULL <> 2 is UNKNOWN. (b) 2 and NULL, because set operations treat two NULLs as equal. (c) Only 2, because NULL = NULL is UNKNOWN in a join condition. (d) NULL: no row passes, and the SUM of no values is NULL.

3. $C$ is on no right side, so it is in every key, and $C^+ = C$. The keys are $AC$, $BC$, $CD$ and $CE$. Every attribute is prime, so $R$ is in 3NF; it is not in BCNF, because $A^+ = AB$.

8. In the first hypergraph, $B$, $D$ and $F$ each lie in one edge. Deleting them leaves $AC$, $CE$ and $EA$, each inside $ACE$, and after deleting those the last edge goes too: acyclic. In the second, the same deletions leave $AC$, $CE$ and $EA$, a triangle in which every vertex lies in two edges and no edge contains another, so the reduction is stuck: cyclic.

9. $Q(1) = ps + qt$ and $Q(2) = rs$. As bag counts, $2 \cdot 3 + 1 \cdot 1 = 7$ and $1 \cdot 3 = 3$. The why-provenance of $(1)$ is $\{\{p, s\}, \{q, t\}\}$.

10. BCNF gives $AB$, $CD$, $DE$ and $EA$, and loses $BC \to D$. The dependencies are already a minimal cover, so synthesis gives $AB$, $BCD$, $DE$ and $EA$, and $BCD$ contains the key $BC$. $BCD$ is not in BCNF, because $D \to B$ holds and $D$ is not a key of it.

11. (a) is lossless: the parts meet in $A$, and $A \to B$ gives $A \to AB$. (b) is lossy: $A^+ = AB$ contains neither $ABC$ nor $ADE$. The relation $\{(1,1,1,1,1),\ (1,1,2,2,2)\}$ satisfies the four dependencies, and the join of its projections also contains $(1,1,1,2,2)$ and $(1,1,2,1,1)$.

12. (a) The row for $AB$ gets the distinguished $C$ from the row for $BC$ by $B \to C$, and then the distinguished $D$ from the row for $CD$ by $C \to D$: lossless. (b) Only $C \to B$ applies, copying the distinguished $B$ into the row for $CD$. No row becomes all distinguished, so the split is lossy. Reading the final tableau with values gives $r = \{(1,0,1,1),\ (2,0,0,2),\ (3,0,0,0)\}$, which satisfies both FDs; the join of its projections contains $(1,0,0,0)$, which is not in $r$.

13. (a) is $R - S$. (b) and (c) are not domain independent: their answers grow with the domain. (d) is domain independent and equals $\pi_1(R) - \pi_1\big((\pi_1(R) \times S) - T\big)$. When $S$ is empty, both give $\pi_1(R)$; the division $T \div S$ would give $\pi_1(T)$ there instead, which is wrong.

17. Semi-naive fires each instance once, one per path fact: $n(n-1)/2$. Naive runs $n$ rounds. It fires the exit rule $n - 1$ times in each, and in round $r$ it fires $\sum_{d < r} (n - 1 - d)$ recursive instances. The total is $(n^3 - n)/3$.

20. The query is hierarchical, with $x$ in every atom, so go value by value. For $x = a$: $\tfrac12 \cdot \big(1 - \tfrac12 \cdot \tfrac12\big) \cdot \tfrac13 = \tfrac18$. For $x = b$: $\tfrac12 \cdot \tfrac14 \cdot \big(1 - \tfrac12 \cdot \tfrac12\big) = \tfrac{3}{32}$. The two values use disjoint tuples, so $P = 1 - \tfrac78 \cdot \tfrac{29}{32} = \tfrac{53}{256}$, which a sum over the 256 worlds confirms. The third query is hierarchical, since $\mathrm{at}(x) \subseteq \mathrm{at}(y)$; the second is not, since $\mathrm{at}(x) = \{R, S\}$ and $\mathrm{at}(y) = \{S, T\}$ overlap without nesting.

21. Start with $(0,0,0,0)$ and $(0,1,1,1)$, which agree only on $A$. The MVD adds $(0,0,0,1)$ and $(0,1,1,0)$. Then $(0,1,1,1)$ and $(0,0,0,1)$ agree on $D$, so $D \to C$ turns the symbol 1 in column $C$ into 0. Column $C$ is now all 0, so $A \to C$ follows. Column $B$ keeps its 1 to the end. The two tuples $(0,0,0,0)$ and $(0,1,0,0)$ satisfy both dependencies and violate $A \to B$.

22. Let $X \to A$ be nontrivial with $X$ not a superkey. 3NF makes $A$ prime, so $A$ lies in a key, which then is $\{A\}$. So $X \to A \to U$ and $X$ is a superkey after all. The schema $\mathrm{Addr}(C, S, Z)$ with $CS \to Z$ and $Z \to C$ has the keys $CS$ and $SZ$ and is in 3NF but not in BCNF.

23. By the Chandra-Merlin theorem, $Q_1 \subseteq Q_2$ exactly when $Q_2$ is true on the canonical database of $Q_1$. That database has size $O(|Q_1|)$, and an acyclic Boolean query is evaluated on it by the semijoin passes of the [Yannakakis algorithm](/yannakakis-algorithm/) in polynomial time. The hard cases of containment need a cyclic $Q_2$.

24. $\rho^*(H) = 4/3$: weight $1/3$ on each edge covers each vertex, which lies in three edges, and weight $1/3$ on each vertex is a fractional packing of value $4/3$, so LP duality closes the gap. $H$ is cyclic, since no vertex lies in one edge only and no edge contains another, so its hypertree width is at least 2; one bag $ABCD$ covered by the two edges $ABC$ and $ABD$ gives 2. The primal graph is $K_4$, so every tree decomposition has a bag with all four vertices, and the fractional hypertree width is $\rho^*(H) = 4/3$.

25. A true instance of the recursive rule is a triple $x < z < y$ of nodes, and there are $\binom{n}{3}$ of them, plus the $n - 1$ exit instances. By induction, the facts new in round $t$ after the exit round are the pairs at distance $d$ with $2^{t-1} < d \le 2^t$, because a path of length $d$ splits into two of length at most $\lceil d/2 \rceil$. The largest distance is $n - 1$. The linear program adds one distance per round. At $n = 10$ the counts are 129 instances and 4 rounds, against 8.
