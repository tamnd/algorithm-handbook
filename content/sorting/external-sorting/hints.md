1. The descents are $6 > 2$, $9 > 4$, $4 > 1$ and $8 > 3$; the equal pair $9, 9$ is not a descent. So there are five runs: $(6)$, $(2, 9, 9)$, $(4)$, $(1, 7, 8)$ and $(3)$. On average a random permutation of $n$ distinct keys has $(n+1)/2$ runs, which is also 5 for $n = 9$.

2. The runs are $(2, 4, 7, 8, 9)$ and $(1, 3, 5, 6, 10)$. The item 1 is read when 4 is written, so it waits for run 2; so do 5 and 3. Sorting each memoryload gives $\lceil 10/3 \rceil = 4$ runs.

3. After the build, the node of runs 1 and 2 holds the loser 5, the node of runs 3 and 4 holds 3, the root holds 2, and the winner is 1. Then 8 enters from run 3: it loses to 3 at its node, and 3 loses to 2 at the root. Now the nodes hold 5, 8 and 3, and the winner is 2. Each replay makes $\lg 4 = 2$ comparisons.

4. 400 runs and fan-in $5000/100 - 1 = 49$. The passes take 400 runs to 9, then to 1: two passes. With $n = 20000$ blocks the sort makes $2n \cdot 3 = 120000$ transfers. Two-way merges need $\lceil \lg 400 \rceil = 9$ passes and $2n \cdot 10 = 400000$ transfers.

7. The counts go $(5, 3, 0)$, $(2, 0, 3)$, $(0, 2, 1)$, $(1, 1, 0)$, $(0, 0, 1)$: four phases. In units of one run, the phases move $6$, $6$, $5$ and $8$, so $25N/8 \approx 3.1N$ items. The balanced merge on 4 tapes needs $\lceil \lg 8 \rceil = 3$ passes, which move $3N$.

8. Polyphase: $1, 4, 7, 13, 25, 49$, so 5 phases and $49 - 30 = 19$ dummy runs. Cascade: $1, 4, 10, 30$, so 3 passes and no dummy run. Remember that a polyphase phase is not a pass over all the data.

11. Show by induction that the $t$-th output is the key of rank $t$ and goes to run 1. Before output $t$, the heap has seen the input positions $1, \ldots, P + t - 1$, and the key of rank $t$ sits at a position below $t + P$. The key read after output $t$ sits at position $P + t$, so its rank is at least $t + 1$, and it is larger than the key just written.

13. The $j$-th merge writes $(j+1)n/k$ items, for $j = 1, \ldots, k - 1$. Sum these. A tree of two-way merges moves every item once on each of its $\lg k$ levels, so it moves $n \lg k$ items.

14. A merge of $j$ runs lowers the count by $j - 1$, and the count must fall by 20. Two merges of 10 runs and one of 3 do it, so the first pass touches 23 runs, $23/30$ of the data. Any plan needs at least $\lceil 20/9 \rceil = 3$ merges, so it touches at least $20 + 3$ runs.

16. The key sort costs $n + (N + n) = n(B + 2)$ transfers and the merge sort $2n(p + 1)$. With $p = 1$ the key sort wins only for $B = 1$, when each record fills a block.

20. Write $R = 1 + \sum_{i=1}^{n-1} I_i$, where $I_i$ marks a descent at $i$. Each $I_i$ has variance $1/4$. Two neighbours $I_i$ and $I_{i+1}$ are both 1 with probability $1/6$, so their covariance is $1/6 - 1/4 = -1/12$, and indicators further apart are independent. So $\operatorname{Var}(R) = (n-1)/4 - 2(n-2)/12 = (n+1)/12$.

21. The rule $(a_1, a_2, a_3) \mapsto (a_1 + a_2,\ a_1 + a_3,\ a_1)$ gives $a_3^{(\ell)} = a_1^{(\ell-1)}$ and $a_2^{(\ell)} = a_1^{(\ell-1)} + a_1^{(\ell-2)}$, so $a_1^{(\ell)} = a_1^{(\ell-1)} + a_1^{(\ell-2)} + a_1^{(\ell-3)}$. Each entry, and so the total, is a fixed sum of shifts of $a_1$, so it satisfies the same recurrence. Its solutions grow like $\lambda^\ell$.

22. Write $S(k)$ for the space. Then $S(k) \le (\sqrt k + 1)\, S(\sqrt k) + c\, k^2$, because the $\sqrt k$ middle buffers hold $k^{3/2}$ items each. Check by induction that $S(k) \le C k^2$ for a large enough constant $C$: the recursive part is only $C(k + k^{3/2})$.

23. Each step of the median of medians is a scan: one pass finds the medians of groups of 5 and writes them, $n/5$ blocks; one pass partitions around the pivot. This gives $T(N) = T(N/5) + T(7N/10) + O(N/B)$, with $T(N) = O(N/B + 1)$ once $N \le M$. Since $1/5 + 7/10 < 1$, the sum is $O(N/B)$.
