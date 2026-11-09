1. For $t = 21$ the loop tests $(2, 20)$, $(2, 15)$, $(5, 15)$, $(7, 15)$, $(7, 12)$ and $(9, 12)$, and returns the pair $9 + 12$ in the 6th iteration. For $t = 30$ it tests $(2, 20)$, $(5, 20)$, $(7, 20)$, $(9, 20)$, $(12, 20)$ and $(12, 15)$, and returns NIL after 6 iterations, which is $n - 1$, the most possible.

2. After the six iterations the array is $[0, 0, 1, 2, 1, 2]$ with $(lo, mid, hi) = (0, 0, 4)$, then the same array with $(1, 1, 4)$ and $(2, 2, 4)$, then $(2, 3, 4)$, then $[0, 0, 1, 1, 2, 2]$ with $(2, 3, 3)$, and last $(2, 4, 3)$. There are 4 swaps, one for each item other than 1; the swaps of iterations 2 and 3 exchange an item with itself. The procedure returns $(2, 4)$.

5. The sequence is $7, 5, 8, 1, 4, 9, 2, 4, 9, 2, \ldots$, so $\mu = 4$ and $\lambda = 3$. Then $\nu$ is the smallest multiple of 3 that is at least 4, so $\nu = 6$, and the pointers meet at $x_6 = x_{12} = 2$. The count is $3\nu + 2\mu + \lambda = 18 + 8 + 3 = 29$ evaluations.

6. $L = 0, 0, 0, 3, 3, 3, 3, 5$, and the answer is 4, for cbad. The faulty version moves the left end back to 1 when it reads the a at position 5, and reports 6 for the window bccbad at positions 1 to 6, which repeats c and b.

10. The answer is 6: one pair $1 + 5$, two pairs $2 + 4$, and three pairs $3 + 3$. When the sum equals $t$ and $A[lo] \ne A[hi]$, count the run $a$ of the value $A[lo]$ and the run $b$ of the value $A[hi]$, add $ab$ and jump over both runs. When $A[lo] = A[hi]$, all $c = hi - lo + 1$ items are equal, so add $c(c-1)/2$ and stop.

12. Dijkstra's loop makes $n_< + n_> = 3 + 3 = 6$ swaps, and 5 of them exchange two different positions. The minimum is 3: the blocks are positions 0 to 2, 3 and 4, and 5 to 7, and the formula gives $\min(1, 0) + \min(1, 2) + \min(1, 0) + 2 \cdot |1 - 0| = 3$.

13. Removing the first or last character lowers the length by one and the largest count by at most one, so the length minus the largest count does not grow. For $k = 2$ the answer is 6, for BBACBB; for $k = 1$ it is 4, for example BBAB at the end.

17. The water at $i$ is zero exactly when $h_i$ is the larger of its prefix maximum or its suffix maximum. Take a position $m$ of a highest bar. Left of $m$, the suffix maximum is the global maximum, so $w_i = 0$ forces $h_i$ to be a prefix maximum, that is, the heights do not decrease up to $m$. The right side is the mirror image, and the converse follows from the same formula.

19. The answer is 4. Let $c(d)$ be the number of pairs with difference at most $d$; here $c(3) = 5$ and $c(4) = 8$, so the 7th smallest is 4. Binary search on $d$ in $[0, D]$ for the smallest $d$ with $c(d) \ge k$. To compute $c(d)$, move a left index $l$ forward while $A[r] - A[l] > d$ and add $r - l$ for each $r$; the predicate $A[r] - A[l] \le d$ is down-closed, so $l$ never moves back.

20. The answer is $[4, 6]$. Keep one index per list and a min-heap of the current items, and track their maximum. The current range runs from the heap minimum to that maximum. Pop the minimum and advance its list; stop when a list runs out. A range that starts at the popped item and contains an item of its list can only be widened by moving any other index, so the best range that starts at that item is the current one.

21. With the prefix sums $P_0, \ldots, P_n$ the task is the largest $j - i$ with $P_i \ge P_j - s$. The running maxima $M_i = \max(P_0, \ldots, P_i)$ do not decrease, and the first $i$ with $M_i \ge P_j - s$ is also the first $i$ with $P_i \ge P_j - s$, so binary search it for each $j$. Here $P = [0, 2, -1, 3, 2, 5, 0, 2]$, and the answer is 6, for $[2, -3, 4, -1, 3, -5]$ and also for $[-3, 4, -1, 3, -5, 2]$.

22. The answer is 8. Fix $i$ and set $lo = i + 1$, $hi = n - 1$. If $A[i] + A[lo] + A[hi] < t$, then every $k$ with $lo < k \le hi$ also gives a sum below $t$, so add $hi - lo$ and move $lo$; otherwise move $hi$. Each triple is counted for its smallest index $i$ and its middle index $j = lo$ only once, since $lo$ never returns.
