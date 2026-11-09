1. The steps give $(cur, best)$: $(3, 3)$, $(-1, 3)$, $(2, 3)$, $(1, 3)$, $(4, 4)$, $(-1, 4)$, $(4, 4)$. Both $A[3..5] = [2, -1, 3]$ and $A[7..7] = [4]$ have sum $4$. The algorithm reports $A[3..5]$, because the strict test $cur > best$ in line L5 does not replace a best of equal value.

3. The largest plain sum is $6$, from $[3, -1, 4]$. The smallest is $-7$, the total is $0$, so the best wrapping sum is $0 - (-7) = 7$, from the arc $5, 2$ that wraps around the end. The answer is $7$.

5. Pops: bar 0 (width 1, area 3) at $i = 1$; bar 2 (width 1, area 3) at $i = 3$; bar 3 (width 2, area 4) at $i = 4$; bar 4 (width 3, area 6) and bar 1 (width 5, area 5) at $i = 5$. The answer $6$ comes from bar 4. Bar 3 has the same height as bar 4 and is closed by it, so its width stops at bar 3; bar 4 is popped later with the full width.

6. The prefix sums are $0, 1, 0, 1, 0, 1$: three $0$s and three $1$s give $\binom{3}{2} + \binom{3}{2} = 6$ zero-sum subarrays. The widest pair of equal values, such as $P_0 = P_4$, gives length $4$.

8. It returns $3$, for the whole array: at $r = 2$ the sum is $5 \ge 4$, the window drops the $3$, and the sum $2$ stops the loop. The right answer is $1$, for $[4]$. Dropping a positive item from the front can make the sum fall below $s$ while a shorter window further right still reaches it: with negative items, shrinking a bad window can make it good.

11. Restart when $cur \le 0$ rather than $cur < 0$, and update the best also when $cur = best$ and the run $c..j$ is shorter. By induction, $c$ is then the largest start of a run ending at $j$ with sum $E(j)$.

14. Add $j + 1 - i$ at each step in place of the maximum. With exactly two values, take the count with at most two ($10$) minus the count with at most one ($5$): the answer is $5$.

15. Item $A[k]$ is the minimum of $(k - L_k)(R_k - k)$ subarrays, where $L_k$ and $R_k$ are the nearest smaller items on the left and on the right. The sum is $3 \cdot 1 + 1 \cdot 6 + 2 \cdot 2 + 4 \cdot 1 = 17$. With repeated items, use "strictly smaller" on one side and "smaller or equal" on the other, so that each subarray is counted for exactly one of its minimal items.

18. Keep two values for each end $j$: $f_0$, the best sum of a run ending at $j$ with no deletion, and $f_1$, the best with one deletion, $f_1(j) = \max(f_1(j-1) + A[j], f_0(j-1))$. The answer for the example is $8$, from $[2, -5, 3, -1, 4]$ with $-5$ deleted.

20. A run with a positive product can be extended by items of absolute value at least $1$ without making the absolute value smaller. If the number of negative items is even, the whole array is best. If it is odd, the best is the larger of the prefix that ends just before the last negative item and the suffix that starts just after the first one.

21. Count the pairs $a < b$ with $lo \le P_b - P_a \le hi$. In merge sort on the prefix sums, before each merge, walk two pointers over the sorted left half for each item of the right half; or use a Fenwick tree over the compressed prefix sums. The example has $4$ such subarrays: $[1]$, $[1, -3, 2]$, $[2]$ and $[-3, 2, 4]$.

22. For each row, build the column heights $h$. The number of all-one rectangles whose bottom-right cell is $(i, j)$ is $c_j = c_{L_j} + h_j (j - L_j)$, where $L_j$ is the nearest column to the left with a strictly lower height, found with a monotonic stack, and $c_{-1} = 0$. The example has $10$ rectangles.

23. A segment of length at least $2L$ splits into two segments of length at least $L$, and its average is a weighted average of theirs, so one of them is at least as dense. For each start, try the lengths $L$ to $2L - 1$ with prefix sums.

24. Keep $c_t$, the best total of at most $t$ closed runs so far, and $o_t$, the best with $t$ runs, the last ending at the current item: $o_t \leftarrow \max(o_t, c_{t-1}) + x$, then $c_t \leftarrow \max(c_t, o_t)$. For the example $g = 9, 14, 16$. The greedy merges $3, -2, 6$ at cost $2$ and then $7, -5, 7$ at cost $5$, so the increments $9, 5, 2$ match.

25. With prefix sums mod $m$, the sum of a run is $(P_j - P_i) \bmod m$. For each $j$ the best start has the smallest earlier $P_i$ that is strictly larger than $P_j$, giving $P_j - P_i + m$, or else $P_0 = 0$, giving $P_j$. A balanced search tree of the earlier values finds it in $O(\log n)$. The example gives $9$, from $[2, 7]$.
