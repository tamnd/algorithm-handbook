## What to remember

- In the [sliding window model](/sliding-window-model/) the queries ask about the last $W$ items or the last $W$ time units, and items expire silently. A window algorithm is interesting when it uses $o(W)$ space. Exact counts and distinct counts need $\Omega(W)$ bits.
- **Running sums and decay.** A [moving average](/moving-average/) keeps $S_t = S_{t-1} + x_t - x_{t-W}$ and needs the stored window. The [exponential moving average](/exponential-moving-average/) $s_t = \alpha x_t + (1 - \alpha) s_{t-1}$ needs one number; $\alpha = 2/(N + 1)$ matches an $N$-item window, and $s_t/(1 - (1 - \alpha)^t)$ removes the bias of the start $s_0 = 0$.
- **Exact aggregates in $O(1)$.** The monotone deque gives the [maximum](/sliding-window-maximum/) in $O(1)$ amortized time. For any associative operator, the [two-stacks queue](/two-stacks-queue/) makes at most $2I + Q$ operator calls for $I$ inserts and $Q$ queries, and the [DABA queue](/daba-queue/) makes at most 1, 4 and 3 calls per query, insert and evict in the worst case.
- **[Basic counting](/basic-counting/)** with relative error $\varepsilon$ needs $\Theta(\frac{1}{\varepsilon}\log^2 W)$ bits. The [DGIM algorithm](/dgim-algorithm/) keeps $L$ or $L + 1$ buckets of each size $2^j$, $L = \lceil k/2 \rceil$, answers $S + (2^r + 1)/2$, and has error below $1/k$.
- **The [exponential histogram](/exponential-histogram/)** does the same for sums of integers in $\{0, \ldots, R\}$ in $O(k(\log W + \log R)\log W)$ bits. Negative values bring the cost back to $\Omega(W)$.
- **Sampling.** [Chain sampling](/chain-sampling/) keeps a uniform sample of the last $W$ items with an expected chain of $(1 + 1/W)^W - 1 < e - 1$ items.
- **Smooth functions.** If $f$ is $(\alpha, \beta)$-smooth, the [smooth histogram](/smooth-histogram/) keeps at most $2\lceil \ln(F + 1)/\beta \rceil + 3$ instances and answers within $[(1 - \alpha) f, f]$. Sums and $F_0$ are $(\alpha, \alpha)$-smooth, $F_p$ with $p \ge 1$ is $(\alpha, (\alpha/p)^p)$-smooth, and the variance is not smooth.
- **Sketches over windows.** Per-block summaries give [heavy hitters](/sliding-window-heavy-hitters/) and [quantiles](/sliding-window-quantiles/) within $\varepsilon W$. [Sliding HyperLogLog](/sliding-hyperloglog/) keeps, per register, the pairs (time, rank) that no later pair dominates, about $m \ln(n/m)$ pairs in all, with standard error $1.04/\sqrt{m}$.

## The methods side by side

| Method | Problem | Space | Time per item | Answer |
|---|---|---|---|---|
| running sum | [moving average](/moving-average/) | the window | $O(1)$ worst | exact |
| monotone deque | maximum | up to $W$ items, $H_W$ expected | $O(1)$ amortized | exact |
| two-stacks queue | any monoid | $2n + 1$ values | $O(1)$ amortized | exact |
| DABA queue | any monoid | $2n$ values | $O(1)$ worst | exact |
| two heaps, lazy deletion | [median](/sliding-window-median/) | $O(W)$ items | $O(\log W)$ amortized | exact |
| DGIM algorithm | basic counting | $O(k \log^2 W)$ bits | $O(1)$ amortized | relative error $< 1/k$ |
| exponential histogram | sum of values in $\{0, \ldots, R\}$ | $O(k(\log W + \log R)\log W)$ bits | $O(R)$ amortized | relative error $< 1/k$ |
| chain sampling | uniform sample | $< e - 1$ items expected | $O(1)$ worst | exactly uniform |
| smooth histogram | smooth $f$ | $O(\frac{1}{\beta}\log F)$ instances | $O(\frac{1}{\beta}\log F)$ instance updates | within $1 - \alpha$, from below |
| Misra-Gries per block | frequencies | $O(1/\varepsilon^2)$ words | $O(1)$ amortized | within $\varepsilon W$ |
| Sliding HyperLogLog | distinct count | $O(m \log n)$ pairs | $O(1)$ amortized | standard error $1.04/\sqrt{m}$ |

: Methods of this chapter. $W$ is the window size, $n$ the number of items in the window or of distinct items, $k$ the accuracy parameter of DGIM, $m$ the number of registers, and $F$ the largest value of $f$ on a window.

## Choosing a method

- If the window fits in memory and the answer must be exact, store it in a [circular buffer](/circular-buffer/) and keep the aggregate with a running sum (for sums), a monotone deque (for the maximum) or a two-stacks queue (for any associative operator). Use DABA when one slow step matters.
- If a weighted answer is acceptable, use the exponential moving average or [exponential decay](/exponential-decay/), with one number per statistic.
- For counts and sums of nonnegative values in small space, use DGIM or the exponential histogram.
- For a smooth function that is not a sum, such as $F_2$, use a smooth histogram.
- For a uniform sample of the last $W$ items, use chain sampling; for a time-based window, use priority sampling.
- For the distinct count with a large window, use Sliding HyperLogLog; for frequencies, use one summary per block of $\varepsilon W/2$ items.
