1. Look for a counterexample with three small numbers first: $(5 - 3) - 1 = 1$ but $5 - (3 - 1) = 3$, and $(0 \oplus 0) \oplus 4 = 2$ but $0 \oplus (0 \oplus 4) = 1$ for the average. For (c), note that $1 + (a \oplus b) = (1 + a)(1 + b)$, so the identity is 0. Max has no identity in the integers until $-\infty$ is added, and "keep the second" has none on two or more elements. The identity of gcd is 0.

3. The up-sweep ends with $[2, 7, 1, 12, 3, 9, 0, 28]$. After the root is set to 0, each down-sweep step passes a node's value to its left child and the sum of that value and the old left child to its right child. The result is $[0, 2, 7, 8, 12, 15, 21, 21]$, the exclusive scan, after 14 combines in 6 rounds.

5. $F = [0, 1, 0, 1, 1, 0, 1, 0, 1]$ and $X = [0, 0, 1, 1, 2, 3, 3, 4, 4]$. The output length is $X[8] + F[8] = 5$, not $X[8] = 4$, because the last item is kept. With $n = 9$, $K = 4$ and $m = 16$, the work is 48 and the span is 10.

7. After round 1, $rank = [2, 0, 2, 1, 2]$ and $next = [1, \mathit{nil}, 3, \mathit{nil}, 0]$. After round 2, $rank = [2, 0, 3, 1, 4]$ and only node 4 still has a successor. In round $k + 1$ the active nodes are those at distance at least $2^k$ from the tail, so there are $4 + 3 + 1 = 8$ updates.

9. A matrix of size 8 has $L = 3$. There are 28 swaps, the work is $n^2 + n - 1 = 71$ and the span is $2L + 1 = 7$. From $2^S - 1 \ge 28$ the span is at least 5. $W_s(n) = 2n^2 - 1$, and the misses are $n^2/B$.

11. (a) $H = [2, 5, 2, 3]$, the work is 40 and the span is 16. (b) With $\lceil \lg p \rceil = j$ fixed, the span $10j + 256 + \lceil 10^6/p \rceil$ is least at the largest $p$, so compare $j = 14, \ldots, 17$. The best value is 432, at $j = 16$, and every $p$ from 62,500 to 65,536 reaches it.

12. Tabulate both counts for $n \le 20$. Inside one block $2^{K-1} < n \le 2^K$ the Blelloch count is constant and the Hillis-Steele count grows by $K$ with each step of $n$, so the Hillis-Steele scan has its best chance at $n = 2^{K-1} + 1$. There the difference is $2^{K-1}(K - 6) + K + 3$.

14. Bits 0, 2 and 5 generate, bits 1, 3, 4 and 6 propagate, and bit 7 does neither. So all carries $c_1, \ldots, c_7$ are 1 and $c_8 = 0$. The sum is $10100100 = 164$.

18. Each piece has about $\lg N$ items, and its two co-ranks take $O(\log N)$ steps, so one merge has work $O(N)$ and span $O(\log N)$. Then the sort has $W(n) = 2W(n/2) + O(n)$ and $S(n) = S(n/2) + O(\log n)$.

20. In round 1 the odd leaves are those numbered 1, 3 and 5, with the values 3, 5 and 6. The value 3 is a left child, and its rake gives its sibling, the leaf with value 4, the function $x + 3$. The rakes of the values 5 and 6 come next, at the same time. In round 2 the leaf with value 4 sends up 7, and in round 3 the leaf with value 1 sends up 7.

21. An interior node is a local minimum with probability $1/3$ and an end with probability $1/2$. Then $\mathbb{E}[m_{r+1}] \le \tfrac23 \mathbb{E}[m_r]$, and the argument of the entry with $3/2$ in place of $4/3$ bounds the rounds.

22. Prove by induction that DOWN($v$, $acc$) writes the correct prefixes for the leaves of $v$ whenever $acc$ is the sum of all items to the left of $v$'s subtree. The right child gets $acc \oplus sum[left]$. Both passes satisfy $T(n) = 2T(n/2) + O(1)$ for the work and $T(n) = T(n/2) + O(1)$ for the span.

23. The down phase has $n/(2s) - 1$ gates at stride $s$, so $\sum_{t=1}^{K-1} (2^t - 1)$ in all. For the depth, the gate at stride $n/4$ reads a value of depth $K - 1$, so it has depth $K$, and it can run at the same time as the root gate of the up-sweep. Each smaller stride adds one level.

24. The best subarray of a concatenation lies in the left part, in the right part, or crosses the cut, and then it is a best suffix of the left part followed by a best prefix of the right part. The best prefix is the left part's best prefix or the whole left part followed by the right part's best prefix.
