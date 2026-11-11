1. ◦ [Hopping windows](/hopping-window/) of size $s = 10$ start every $h = 4$ time units at the offset $o = 0$. List the windows that contain the timestamps 17 and 19, and the [tumbling window](/tumbling-window/) of size 10 that contains each. Over a long run of integer timestamps, what fraction of the items is in three hopping windows? How large are the panes, and how many panes make one window?

2. ◦ [Session windows](/session-window/) with the gap $g = 4$ receive the timestamps $2, 3, 8, 9, 15, 21, 22$ of one key. Give the sessions. A late item with timestamp 12 then arrives. Which sessions does it merge, and what are the sessions afterwards?

3. ◦ Compute the [moving average](/moving-average/) with $W = 4$ of the stream $6, 2, 8, 4, 10, 0, 5$, averaging over the items seen so far while $t < W$. Then compute the weighted sum $N_t = \sum_{j=0}^{W-1} (W - j)\, x_{t-j}$ at each step with the update $N_t = N_{t-1} + W x_t - S_{t-1}$, where $S_{t-1}$ is the window sum at the step before, and check $N_5$ directly.

4. ◦ An [exponential moving average](/exponential-moving-average/) has the span $N = 9$. Give $\alpha$, the centre of mass, the half-life and the total weight of the last 9 items once the start no longer matters. Check that the mean age of the weights is $(N - 1)/2$.

5. ◦ Run the monotone deque of the [sliding window maximum](/sliding-window-maximum/) with $W = 3$ on the stream $2, 7, 3, 5, 5, 1, 6$. An insert pops from the back every item with a value at most the new value, and a query pops expired items from the front. Give the deque as (position, value) pairs and the maximum after each step.

6. ◦ Give the [sliding window median](/sliding-window-median/) with $W = 4$ of the stream $5, 1, 4, 8, 9, 2, 6, 3$. Use the lower median $y_{\lceil n/2 \rceil}$ of the $n = \min(t, W)$ items of the window.

7. ◦ Use the bound $(L + 1)(\rho + 1)$ on the number of buckets of the [DGIM algorithm](/dgim-algorithm/), with $L = \lceil k/2 \rceil$ and $\rho = \lfloor \log_2((W - 1)/L + 1) \rfloor$. How many buckets can there be for $k = 2$ and $W = 100$, and for $k = 4$ and $W = 1000$? How many bits do their timestamps take, at $\lceil \log_2 W \rceil$ bits each?

8. ◦ For which $\beta$ is $F_2$ a $(0.1, \beta)$-[smooth function](/smooth-function/), and $F_3$ a $(0.3, \beta)$-smooth function? How many instances can a [smooth histogram](/smooth-histogram/) for the count of 1s with $\beta = 0.1$ and $W = 1000$ hold? Then show with the stream $6, 0, 6$ that the variance is not smooth.

9. ◦ A [sliding window join](/sliding-window-join/) receives $\lambda_A = 100$ tuples per second on stream $A$, with a window of $T_A = 30$ seconds, and $\lambda_B = 20$ tuples per second on $B$, with $T_B = 60$ seconds. A pair of tuples has equal keys with probability $\sigma = 0.001$. How many tuples does each window hold on average, how many results come out per second, and how many comparisons per second do nested loops in both directions make? By the cost model of the entry, how cheap must an index be, in comparisons per tuple, to pay off on $B$, and on $A$?

10. • Run the exponential moving average with $\alpha = 1/2$ on $6, 2, 10, 4$ from $s_0 = 0$. Give $s_t$ and the bias-corrected $s_t/(1 - (1 - \alpha)^t)$, and check $t = 3$ against the weighted average of $x_1, x_2, x_3$ with the weights $\alpha(1 - \alpha)^j$. Then run it from $s_1 = x_1$ instead.

11. • Items $(\text{time}, \text{value}) = (0, 8), (2, 4), (4, 4), (4, 2)$ arrive under [exponential decay](/exponential-decay/) with a half-life of 2. Give the decayed count $C$, the decayed sum $S$ and the decayed average at $t = 4$ and at $t = 8$, and the one multiplication that takes $C$ from $t = 4$ to $t = 8$. If one item arrived at each integer time for ever, what would the count be just after an arrival? Compare it with $1/\lambda + 1/2$.

12. • Use [forward decay](/forward-decay/) with $g(n) = n^2$ and the landmark $L = 0$. Items arrive at the times 1, 2 and 4. Give their weights at $t = 4$ and at $t = 8$. An item that arrived at time 6 would have the same age at $t = 8$ as the item of time 2 at $t = 4$; compare their weights. With $g(n) = e^{\lambda n}$, $\lambda = 0.1$ per second and $L = 0$, after how many seconds does $g$ overflow binary64?

13. • Run DGIM with $W = 8$ and $k = 2$ on the bits $1, 1, 1, 0, 1, 1, 0, 1, 1, 1$. Give the buckets as (timestamp, size) pairs, the estimate and the true count at $t = 6$, $t = 9$ and $t = 10$, and the number of merges over the 10 steps.

14. • Run DGIM with $k = 6$ and a large window on five 1s. Give the buckets. Compare the estimate $S + (2^r + 1)/2$ with the half-bucket estimate $S + 2^r/2$, where $2^r$ is the size of the oldest bucket. Which of the two breaks the guarantee of [basic counting](/basic-counting/) with relative error below $1/k$?

15. • Run the [exponential histogram](/exponential-histogram/) with $W = 5$, $k = 2$ and $R = 3$ on the values $3, 1, 0, 2, 3, 1$. Give the buckets, the estimate and the true sum at $t = 5$ and $t = 6$.

16. • Take the [two-stacks queue](/two-stacks-queue/) with string concatenation. Apply insert(p), insert(q), insert(r), insert(s), evict, evict, insert(t), evict, evict, evict. Give the stacks after the first evict, the query after each operation, and the calls of $\otimes$ by each operation. How does the total compare with the bound $2I$ for $I$ inserts?

17. • [Sliding window sampling](/sliding-window-sampling/) with priorities uses a time window of length $T = 4$, $(t - 4, t]$. The items (time, item, priority) are $(1, a, 0.3)$, $(2, b, 0.8)$, $(3, c, 0.5)$, $(3, d, 0.6)$, $(5, e, 0.1)$, $(7, f, 0.4)$. Give the deque after each insert and the sample at $t = 3$, $5$ and $7$.

18. • For [chain sampling](/chain-sampling/) with $W = 4$, give the expected chain length for $t \ge W$ and at $t = 2$. If the sample has $m = 3$ newer items in the window, what is the probability that the chain has more than two elements?

19. • Run the smooth histogram for the sum with $W = 3$ and $\beta = 1/2$ on the stream $2, 2, 1, 4, 0, 1, 3$. Give the list of (start, value) pairs, the answer and the true sum after each step. Where is the answer below the true sum, and is it within the factor $1 - \beta$?

20. • One register of [Sliding HyperLogLog](/sliding-hyperloglog/) with $W = 6$ receives items at the times $1, 2, 4, 5, 6, 9, 10, 12$ with the ranks $1, 3, 2, 2, 1, 4, 1, 2$. Give the list after each update. What is the register value $M_j$ for $w = 6$ and for $w = 3$ at $\tau = 6$, and for $w = 6$ and for $w = 2$ at $\tau = 12$?

21. • [Sliding window heavy hitters](/sliding-window-heavy-hitters/) with $W = 10$ and $\varepsilon = 1/2$ use blocks of $b = \lfloor \varepsilon W/2 \rfloor$ items and Misra-Gries summaries of $k = \lceil 2/\varepsilon \rceil$ counters. The stream is b a b b c a b c c b a c b. At $t = 13$, which blocks are kept, and what are the estimates and the true frequencies of a, b and c in the window?

22. ★ Take the [DABA queue](/daba-queue/) with string concatenation. Apply insert(a) to insert(f), then evict, insert(g), evict. Give the cases of FIXUP and the calls of $\otimes$ for each operation, and the positions $F, L, R, A, B, E$ (relative to $F$) and the aggregates after insert(g) and after the last evict.

23. ★ Chain sampling with $W = 3$ is run in the wrong order: in a step where the sample expires, its successor takes over, and then the new item still gets its chance $1/\min(t, W)$. Compute the distribution of the sample at step 4. Compare it with the correct order.

24. ★ In the [exponential histogram space bound](/exponential-histogram-bound/) take $\varepsilon = 1/7$ and $W = 2^{20}$. Compute $m$, $q$, the number of bits $mq^2$, the length $T$ of the strings of the proof, and the bound $\log_2^2(3\varepsilon W)/(128\varepsilon)$. Compare them with the space of DGIM for $k = 7$: the bucket bound of Exercise 7 times 20 bits.

25. ★ Run the smooth histogram with $W = 8$ and $\beta = 1/2$ for the largest frequency $F_\infty$ on the stream x x x y y y x x x. Give the list at $t = 6$ and at $t = 9$, the answer and the true value at $t = 9$. Which property of smooth functions fails?

26. ★ Show that the exponential moving average with $\alpha = 2/(N + 1)$ has the mean age $(N - 1)/2$ of an $N$-item moving average, and that for independent items of variance $\sigma^2$ its steady-state variance $\alpha\sigma^2/(2 - \alpha)$ equals $\sigma^2/N$, the variance of the moving average. For $N = 19$, give the weight of the last 19 items, its limit as $N \to \infty$, and the half-life.
