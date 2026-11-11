1. $|W| \ge 80 - 1 = 79$ ms. For the linearizable register, $|R| \ge 20/4 = 5$ ms and $|W| \ge 20/2 = 10$ ms.

2. The orders $abc, acb, bac, bca, cab, cba$ give $9, 8, 6, 6, 8, 5$, so there are four different values: 5, 6, 8 and 9. Only $a$ and $c$ commute, since adding 3 and subtracting 1 can be swapped.

4. $(1,5)$: reads meet writes, writes meet, overlap 1, reads survive 4 crashes, writes 0. $(2,3)$: reads may miss the last write, writes meet, overlap 0, reads survive 3 crashes, writes 2. $(3,3)$: both hold, overlap 1, each survives 2. $(2,4)$: both hold, overlap 1, reads survive 3, writes 1. $(3,2)$: neither holds, overlap 0, reads survive 2 crashes, writes 3, and two writes can miss each other.

5. (a) and (c) are joins; (b) is not idempotent, since $1 + 1 \neq 1$. In (c), $x \le y$ when every 1-bit of $x$ is a 1-bit of $y$, and $0101 \sqcup 0011 = 0111$. In (d), $\lceil(\lceil(0+1)/2\rceil + 4)/2\rceil = \lceil 5/2 \rceil = 3$ but $\lceil(0 + \lceil(1+4)/2\rceil)/2\rceil = \lceil 3/2 \rceil = 2$; the triple $0, 1, 4$ breaks associativity.

6. The entrywise maximum is $(3, 2, 4)$, with value 9. The local values are 4, 3 and 6, which add to 13, because an increment held by several replicas is counted once for each of them.

9. Compare triple by triple, and a proper prefix comes first. The order is $c, r, d, t, s$, so the word is "crdts". $d$ and $t$ differ already in the first triple, by site, so any position that starts with $(5,1,1)$ and has a second triple above $(4,3,7)$ works, such as $\langle(5,1,1),(9,1,4)\rangle$.

10. Write down for each process the order in which it sees all writes, keeping each writer's own order. For causality, follow $w(x)2 \to r(x)2 \to w(y)1$.

15. A node is visited when its parent's hashes differ. Count the differing internal nodes level by level: 1, 2, 2 and 2.

17. The cells are $(1, 5)$, $(0, 12)$, $(0, 9)$, $(-1, 9)$, $(-2, 5)$ and $(-1, 12)$. Cell 0 is pure and gives Alice's 5; removing it makes cell 1 pure with Bob's 9, and then 12 comes out. Cells 1, 2 and 4 have a keySum that is a real element, 12, 9 and 5, but each holds two elements: $5 \oplus 9$, $5 \oplus 12$ and $9 \oplus 12$. Their counts 0, 0 and $-2$ give them away.

20. The OR-Set remove names only the tags it saw. The 2P-Set never takes back a remove. The LWW-Element-Set compares the largest add stamp with the largest remove stamp.

22. Threshold masking quorums exist only for $n > 4f$. For dissemination quorums, the overlap $2q - n \ge f + 1$ and the live quorum $q \le n - f$ together give $n > 3f$.

23. The visited count is $1 + 2k$, where $k$ is the number of internal nodes whose subtree holds a differing bucket. Pack the four buckets under one node of height 2 for the fewest, and spread them over four such nodes for the most.

24. In the counter, the delta $\{A \mapsto 6\}$ already contains everything the lost delta carried. In the set, check whether $B$'s state after the join equals any state that $A$ ever had.

25. Visit the tree depth first, with the children of each atom in decreasing id order: under $H$, the children are $o(3,1)$, $e(3,0)$ and $i(2,0)$.

26. On the TP2 path through $a$, $c$ is first moved past $a$ and then past $b$. On the path through $b$, $c$ is first moved past $b$, which leaves its index at 1, and then meets $T(a, b) = \mathrm{ins}(1, x, 1)$ at the same index.
