## What to remember

- With equal sizes and costs, [Belady's MIN](/belady-optimal/) is optimal offline: evict the item whose next request is furthest away. With [different sizes](/variable-size-caching/) the rule fails, and the offline problem is strongly NP-hard.
- In the worst case, [LRU](/lru/), [FIFO](/fifo-replacement/) and [CLOCK](/clock/) with $k$ items miss at most $k$ times as often as MIN, plus a constant, and no deterministic policy does better. Against an optimum with $h \le k$ items the factor is $k/(k-h+1)$ ([competitive bound](/lru-competitiveness/)). [MRU](/mru/), [LFU](/lfu/), [2Q](/two-q/) and [SLRU](/slru/) have no bounded ratio.
- In the [independent reference model](/independent-reference-model/), no policy hits more often than the $k$ largest request probabilities together. LRU, FIFO and [random replacement](/random-replacement/) have exact hit ratios there, and FIFO and random replacement have the same one.
- An LRU cache of $k$ items hits exactly the requests whose [reuse distance](/reuse-distance/) is less than $k$. LRU, MIN, MRU and an LFU that counts all past requests are stack algorithms: their caches of all sizes are nested, they show no [Belady's anomaly](/belady-anomaly/), and [Mattson's algorithm](/mattson-stack-algorithm/) gives their [miss ratio curve](/miss-ratio-curve/) in one pass. FIFO and CLOCK are not.
- A scan of items used once flushes an LRU cache, and a loop longer than the cache makes it miss every time. The fixes are a probation queue (2Q, SLRU, [S3-FIFO](/s3-fifo/)), older references ([LRU-K](/lru-k/), [LIRS](/lirs/)), [ghost lists](/ghost-lists/) ([ARC](/arc/)) and [admission](/cache-admission-policy/) ([TinyLFU](/tinylfu/)).
- [GreedyDual-Size](/greedy-dual/) ranks objects by $L + c(p)/s(p)$ and is $k$-competitive with any sizes and costs. [GDSF](/gdsf/) adds counts and loses the bound.
- An absolute [TTL](/ttl-expiration/) bounds the age of every value served; a sliding TTL does not. [Cache-aside](/cache-aside-pattern/) writes the store and then deletes the key, and leases close the race that remains.

| Policy | Extra state | Time per request | Resists scans | Ratio against MIN | Source |
|---|---|---|---|---|---|
| MIN | next request times | $O(\log k)$, offline | — | optimal | [Belady optimality](/belady-optimality/) |
| FIFO | queue | $O(1)$ | no | $k$ | [Sleator and Tarjan](/sleator-tarjan-paging-bound/) |
| LRU | list links | $O(1)$ expected | no | $k$ | [Sleator and Tarjan](/sleator-tarjan-paging-bound/) |
| CLOCK | one bit | $O(1)$ amortized | no | $k$ | [CLOCK](/clock/) |
| Random | none | $O(1)$ | no | $k$, adaptive online adversary | [random replacement](/random-replacement/) |
| LRU-K | $K$ reference times | $O(K)$ hit, $O(k)$ miss | yes | none claimed | [LRU-K](/lru-k/) |
| 2Q | ghost queue of ids | $O(1)$ | yes | unbounded | [2Q](/two-q-replacement/) |
| ARC | at most $2c$ keys | $O(1)$ | yes | at least $c$; $4c$ claimed in a preprint | [ARC](/arc/) |
| LIRS | stack with ghosts | $O(1)$ amortized | yes, and loops | at least $k$ | [LIRS](/lirs/) |
| TinyLFU over LRU | count-min sketch | $O(d)$ | yes | at least $c$ | [TinyLFU](/tinylfu/) |
| S3-FIFO | 2-bit counter, ghost queue | $O(1)$ amortized | yes | at least $c$ | [S3-FIFO](/s3-fifo/) |
| SIEVE | one bit | $O(1)$ amortized | no | at least $c$ | [SIEVE](/sieve/) |
| GreedyDual-Size | priority $H$ | $O(\log k)$ | no | $k$ | [Landlord](/landlord-algorithm/) |

: Replacement policies and their costs, for a cache of $k$ (or $c$) items, with $d$ rows in the sketch. "At least" is the lower bound that holds for every deterministic policy; no upper bound is proved. The scan column follows the entries and is not a theorem.

## Choosing a method

For a software cache of objects of one size, start with LRU built from a [hash table and a linked list](/lru-cache/). It is $k$-competitive and a stack algorithm, so its miss ratio curve is cheap to measure. If the workload has scans or many objects requested once, use a probation queue: SLRU or 2Q in a buffer pool, S3-FIFO or [W-TinyLFU](/w-tinylfu/) in a key-value or web cache. A hit in LRU moves a list node, so if many threads share the cache, prefer CLOCK, [SIEVE](/sieve/) or S3-FIFO, whose hits only set a bit or raise a counter. Use ARC or LIRS when the mix of recency and frequency changes, and MRU only for a loop known to be longer than the cache. When objects differ in size or cost, use GreedyDual-Size, and decide first whether the hit ratio or the byte hit ratio matters.

Judge a policy on your own traces at several sizes; the hit ratios in the entries come from small synthetic workloads or the papers' traces. In an application cache, set an absolute TTL, delete keys on writes, and protect expensive hot keys against a [stampede](/cache-stampede/).
