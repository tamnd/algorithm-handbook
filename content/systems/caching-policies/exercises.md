1. ◦ A cache holds $k = 3$ items and starts empty. Count the misses of [MIN](/belady-optimal/), [LRU](/lru/) and [FIFO](/fifo-replacement/) on the trace a b c a b d a d c b d a b.

2. ◦ Write down the [reuse distance](/reuse-distance/) of each request in the trace of Exercise 1. From their histogram alone, give the number of LRU misses for $k = 1, 2, 3, 4$, and say why every policy has the same number of misses at $k = 4$.

3. ◦ A [set-associative cache](/set-associative-cache/) holds 32 KiB in lines of 64 bytes, with 8 ways, and addresses have 48 bits. How many sets does it have, and how many bits go to the offset, the index and the tag? Find the offset, the set and the tag of the address 0x12345.

4. ◦ An L1 cache has a hit time of 1 cycle and a miss rate of 5%. The L2 cache behind it has a hit time of 10 cycles and a local miss rate of 20%, and memory takes 100 cycles. Compute the average memory access time and the global miss rate of L2, using the definitions of [multilevel caching](/multilevel-caching/). How many distinct bytes can the two levels hold together if L1 has 32 KiB and L2 has 256 KiB, when the hierarchy is inclusive, and when it is exclusive?

5. ◦ A direct-mapped cache has 4 blocks, and block $b$ goes to set $b \bmod 4$. Split the misses on the trace 0 1 4 0 1 4 2 0 into the [three Cs](/three-cs-model/). Do the same for a 2-way set-associative cache of 4 blocks with LRU in each of its 2 sets.

6. ◦ A line x is not cached. The program writes x three times, reads it once, and then x is evicted. Count the writes to the store, the lines read from the store, and the read hits under [write-through](/write-through/) with no-write-allocate and under [write-back](/write-back/) with write-allocate.

7. ◦ Run [GreedyDual-Size](/greedy-dual/) with capacity $k = 4$ on the trace a b c b d a. The objects have the sizes and costs a (2, 2), b (1, 3), c (2, 4) and d (1, 1). Give the evictions, the value of $L$ after each request, and the number of misses.

8. ◦ A value takes $\Delta = 2$ seconds to recompute and [XFetch](/cache-stampede/) runs with $\beta = 1$. What is the probability that a request 1 second before the expiry triggers a recompute? A request 4 seconds before? And 4 seconds before with $\beta = 2$?

9. ◦ Requests for one key form a Poisson process of rate 2 per second. Which [TTL](/ttl-expiration/) gives a long-run hit probability of 95% when the TTL is absolute and restarts at each miss? Which TTL gives the same when it is sliding? Which of the two bounds the age of the values served?

10. ◦ By the [competitive bound for LRU](/lru-competitiveness/), how many misses can LRU with $k = 8$ items have on a sequence where the optimum with $h = 4$ items has 1000 misses? What is the largest $h$ for which the factor is below 2?

11. • With $k = 3$, run [CLOCK](/clock/) and [SIEVE](/sieve/) on the trace a b a c d a e b a f a g. In CLOCK a page is loaded with its bit set, a hit sets the bit, and the hand starts at frame 0 and moves one frame past each page it loads. In SIEVE a new object enters at the head with its bit clear, and the hand moves from the tail toward the head. Count the misses of each, and compare with LRU, FIFO and MIN.

12. • A program cycles through $k + 1$ pages, 1 2 … $k+1$ 1 2 …, with a cache of $k$ pages. Show that in the long run LRU misses on every request, [MRU](/mru/) and MIN miss on a fraction $1/k$ of the requests, and [random replacement](/random-replacement/) misses on a fraction exactly $2/(k+1)$.

13. • In the [independent reference model](/independent-reference-model/), three items have the probabilities $1/2$, $1/4$ and $1/4$, and $k = 2$. Find the stationary distribution of the LRU cache, ordered by recency, and its hit ratio. Find the hit ratio of FIFO, and of A0, which on a miss evicts the cached item of least probability.

14. • An [SLRU](/slru/) cache has $k = 4$ and a protected segment of $p = 2$. Run it and LRU on a b a b w x y z a b. Show that the scan w x y z does not touch the protected segment however long it is, and that SLRU with $p = 0$ is LRU.

15. • Run [ARC](/arc/) with $c = 2$ on a b a c b c a b, following the pseudocode of its entry. Give the lists $T_1$, $T_2$, $B_1$, $B_2$ and the target $p$ after each request, and say where $p$ moves and why.

16. • With $k = 2$, give a sequence on which MRU misses on every request after the second while MIN misses 3 times in all. Do the same for [LFU](/lfu/) that counts requests since the load and breaks ties by LRU. Conclude that neither policy is competitive, although MRU is optimal on Exercise 12 and LFU is the right idea under the independent reference model.

17. • A cache of capacity 4 holds objects of [different sizes](/variable-size-caching/): a has size 3, and b, c and d have size 1. Every miss costs 1. On the trace a b c d c a b, run the rule "while the new object does not fit, evict the cached object whose next request is furthest", and find the optimum. Why does the rule fail?

18. • Write a program that computes all reuse distances of a trace of $n$ requests in $O(n \log n)$ time with a [Fenwick tree](/fenwick-tree/) indexed by time, which marks the last request of each item. Check it on the trace of Exercise 1.

19. • A cache-aside application runs one reader and one writer on one key, and the store holds $v_0$. Using the [cache-aside pattern](/cache-aside-pattern/), give an interleaving that leaves the old value in the cache for good when the writer sets the cache key after writing the store, and two writers that do the same. Then show that the remaining race of "write the store, then delete the key" is closed by a lease from the cache, as in [cache invalidation](/cache-invalidation/).

20. • [TinyLFU](/tinylfu/) halves all its counters and the counter $n$ of additions whenever $n$ reaches $W$. Ignore the cap, the doorkeeper and collisions, and let an object take a fraction $f$ of the requests. Show that its expected count just before a reset tends to $fW$. What would the limit be if the reset set $n$ to 0 instead of halving it?

21. • Requests for a key arrive as a Poisson process of rate $r$, and XFetch runs with $\Delta$ and $\beta$. Assume the value was stored long before its expiry. Show that the probability that no request recomputes early is about $e^{-r\Delta\beta}$. For $r = 100$ per second and $\Delta = 0.05$ seconds, which $\beta$ makes this probability at most $10^{-3}$?

22. • Add to the [LRU cache](/lru-cache/) an operation that changes its capacity from $c$ to $c'$. Give its cost when $c' < c$ and when $c' > c$. Explain why a singly linked list would make a hit cost $\Theta(c)$ unless each node also stores a pointer you can update.

23. ★ Prove that under the independent reference model, the stationary distribution of a FIFO cache of $k$ items, as an ordered queue $(i_1, \ldots, i_k)$, is proportional to $p_{i_1} \cdots p_{i_k}$. Prove that the set held by random replacement has a stationary distribution proportional to the same product, and conclude that the two policies have the same hit ratio.

24. ★ In the independent reference model, show that the expected size of the [working set](/working-set-model/) with window $\tau$ is $s(\tau) = \sum_i \bigl(1 - (1 - p_i)^\tau\bigr)$. Show that the working set policy misses on a fraction $s(\tau + 1) - s(\tau)$ of the requests, and that $s$ is concave.

25. ★ Let the requests for one key form a renewal process, with independent gaps of distribution $F$, and let $m(T)$ be the expected number of requests in an interval of length $T$ that starts just after a request. Show that an absolute TTL that restarts at each miss has hit ratio $m(T)/(1 + m(T))$ and that a sliding TTL has hit ratio $F(T)$, for gaps that do not take the value $T$. Check both against the Poisson formulas, and compute them when every gap is exactly $g < T$.

26. ★ Prove that LFU with counts kept for all past requests, ties broken by LRU, has the [inclusion property](/inclusion-property/). Then show that LFU with counts kept only since the load does not: on a a b c b c d, compare its caches of sizes 2 and 3 at the end. Show that it has Belady's anomaly on a a b c b c d a d a.

27. ★ [SHARDS](/shards/) samples each item with probability $R$ by a hash. Model the hash as independent coin flips per item. Show that a sampled request whose reuse distance is $d$ has a sampled distance with the binomial distribution of $d$ trials and success probability $R$, so that dividing by $R$ gives an unbiased estimate of $d$. Find its relative standard deviation, and evaluate it for $R = 0.001$ and $d = 10^6$.
