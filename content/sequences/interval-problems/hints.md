1. The sorted order is $[1, 2], [2, 4], [3, 5], [5, 7], [6, 6], [8, 9]$, and the output is $[1, 7], [8, 9]$: the touches at 2 and at 5 merge, and $[6, 6]$ leaves no trace. As sets of integers, $8 \le 7 + 1$, so the output is the single interval $[1, 9]$.

3. The output is $[1, 2], [3, 4], [6, 7], [8, 8], [10, 11], [14, 15]$, after 6 steps, which is $m + n - 1$. As half-open intervals the touch at 8 gives the empty piece $[8, 8)$, so only five pieces remain.

5. Closed: depth 3, first reached at the point 3, where $[1, 4], [2, 3], [3, 5]$ meet. Half-open: depth 2, first reached at 2. The greedy opens three resources: $\{[1, 4], [5, 8]\}$, $\{[2, 3], [4, 6]\}$ and $\{[3, 5]\}$.

7. Sorted by right end the intervals are $[1, 3], [2, 5], [4, 6], [7, 8], [6, 9], [10, 11]$. The points are $3, 6, 8, 11$, and the intervals that opened them, $[1, 3], [4, 6], [7, 8], [10, 11]$, are pairwise disjoint, so four points are needed.

10. The sorted order is $b, a, c, d, f, e$, with $p = 0, 0, 1, 2, 4, 3$ and $M = 2, 3, 6, 7, 9, 9$, so the optimum is 9. Keep a count $C[j]$ with $C[0] = 1$: it is $C[p[j]]$ when taking $j$ is strictly better, $C[j-1]$ when skipping is strictly better, and their sum on a tie. The tie at $e$ gives $C = 2$: the sets $\{b, c, e\}$ and $\{a, d, f\}$.

11. (a) Cover $[0, 10]$ with $[0, 5], [5, 10], [1, 9]$: the longest interval forces three, but two suffice. (b) $[1, 10], [2, 3]$: the rule places 10 and then 3, but the point 3 alone hits both. (c) $[0, 3)$ of weight 1 and $[2, 5)$ of weight 10: the greedy takes the first and gets 1 instead of 10.

12. Remove 3. The piercing greedy, or earliest finish time first, keeps $[1, 2), [2, 4), [5, 7)$, so $\nu = 3$. The kept intervals of any answer are pairwise disjoint, so at least $n - \nu$ must go, and keeping a largest disjoint set reaches this.

14. In a chain, each interval starts no earlier than the one before and, at an equal start, ends earlier, so it comes later in the sorted order and its right end is not larger. Conversely, later in the order and a right end not larger means contained. The right ends are $10, 9, 5, 9, 4, 8, 7$ in sorted order, and a longest non-increasing subsequence is $10, 9, 9, 8, 7$: the chain $[1, 10] \supset [2, 9] \supset [3, 9] \supset [5, 8] \supset [6, 7]$, of length 5.

18. Every piercing set of all the arcs also pierces the arcs that miss $q$, and those form a family of intervals on the cut line, where the greedy is optimal. So the method uses $1 + \tau' \le 1 + \tau$ points.

21. Any such point set and any cover: each point lies in a chosen interval, and no interval holds two of the points, so there are at most as many points as intervals. For equality, let $reach_0 = s, reach_1, \ldots, reach_{m-1}$ be the values of $reach$ before the $m$ choices of the greedy, and take $x_0 = s$ and $x_j = reach_j + \varepsilon$, with $\varepsilon$ smaller than every gap between distinct end points. An interval that contains $x_j$ starts at or before $reach_j$, so the greedy read it at step $j + 1$, and it ends at or before $reach_{j+1} < x_{j+1}$.

22. Sort by right end. Let $D[j]$ be the least cost of a set that covers $[s, r_j]$ and in which $I_j$ has the largest right end: $D[j] = w_j$ if $l_j \le s$, and otherwise $w_j$ plus the least $D[i]$ over the intervals with $l_j \le r_i < r_j$. Those $i$ form a range of the sorted order, found by binary search, so a segment tree with range minimum gives each $D[j]$ in $O(\log n)$. The answer is the least $D[j]$ with $r_j \ge t$. This is a shortest path in a DAG.

23. Keep the invariant that some optimal set contains every integer chosen so far. A later interval $[l', r']$ has $r' \ge r_j$, so it contains a point $x$ of $I_j$ exactly when $x \ge l'$; moving a point of an optimal set to the right inside $I_j$ therefore keeps every later interval satisfied, and the earlier ones are satisfied by the chosen points alone. On the example the greedy chooses $4, 3, 8, 7$, and the disjoint intervals $[0, 4]$ and $[5, 8]$ need two points each, so 4 is optimal.

24. Irreflexive since $l \le r$; transitive since $r_I < l_J \le r_J < l_K$. Two closed intervals are disjoint exactly when one ends before the other starts. By Dilworth, the fewest chains that cover the family, which is the fewest colors, equals the largest antichain, which by Helly is a set of intervals through one point, so its size is the depth. For the last part, $r_A < l_B \le r_C < l_D \le r_A$ is a contradiction.
