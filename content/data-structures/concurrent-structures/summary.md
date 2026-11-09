## What to remember

- A concurrent structure needs two things beyond its sequential code: a correctness condition for overlapping calls, and a progress condition.
- One lock around a sequential structure is linearizable at once, with the lock acquisition as the linearization point. But only one call runs at a time.
- [Lock striping](/lock-striping/) keeps the lock design but splits the data. Each piece of state has one stripe, the stripe of an element never moves, and several locks are taken in one fixed order. The [concurrent hash table](/concurrent-hash-table/) keeps $L$ dividing the capacity, so that doubling does not move any key to another stripe.
- A hot spot can be removed in three ways. Combine many calls into one, as the [combining tree](/combining-tree/) and the [combining funnel](/combining-funnel/) do; spread them over many places, as the [diffracting tree](/diffracting-tree/) and the [sloppy counter](/sloppy-counter/) do; or replace a compare-and-swap loop by fetch-and-add, which never fails, as the [LCRQ](/lcrq/) does.
- Spreading often costs a guarantee: the diffracting tree is only [quiescently consistent](/quiescent-consistency/), the sloppy counter has an approximate read that may be up to $p(S - 1)$ low, and a [relaxed priority queue](/relaxed-priority-queue/) returns an item near the minimum, not the minimum.
- [Sequential consistency](/sequential-consistency/) keeps program order only; quiescent consistency keeps real-time order only across quiet moments. Linearizability implies both, and neither implies the other. Quiescent consistency is compositional, sequential consistency is not.
- An exact priority queue does not scale, because every delete-min goes to the same item. The [MultiQueue](/multiqueue/) with two random choices has expected rank $O(c)$ for $c$ heaps, and the [SprayList](/spraylist/) lands among the first $O(p \log^3 p)$ items with high probability.
- In search structures a half-done change must be safe to see. The [B-link tree](/blink-tree/) splits in two steps joined by a right link; the [Ctrie](/ctrie/) copies a small node and swings one word with compare-and-swap.

| structure | correctness | progress | contention point | cost of one call, alone |
|---|---|---|---|---|
| one-lock [queue](/concurrent-queue/) | linearizable | deadlock-free | the one lock | $O(1)$ |
| [two-lock queue](/two-lock-queue/) | linearizable | deadlock-free | head lock, tail lock | 4 shared steps |
| [Disruptor](/disruptor-ring-buffer/), one producer | linearizable | waits only when full or empty | none besides the gate | $O(1)$ plus $O(k)$ gate reads |
| LCRQ | linearizable | lock-free | head and tail counters, by fetch-and-add | one fetch-and-add, one read, one CAS2 |
| striped hash table | linearizable | deadlock-free | one stripe; all stripes at a resize | expected $O(1 + \alpha)$ |
| sloppy counter | inc and exact read linearizable | deadlock-free | global lock, once per $S$ increments | $O(1)$ inc, $O(p)$ exact read |
| combining tree | linearizable | deadlock-free, not lock-free | the root, once per batch | $O(\log w)$ |
| diffracting tree | quiescently consistent | lock-free | the root toggle, relieved by the prism | $\log_2 w$ balancers |
| fine-grained heap | neither linearizable nor quiescently consistent | deadlock-free | the root slot | $O(\log n)$ lock pairs |
| MultiQueue | linearizable for the relaxed type | deadlock-free | none; expected rank $O(c)$ | $O(\log m)$ |
| SprayList | linearizable for the relaxed type | lock-free | none; rank $O(p \log^3 p)$ w.h.p. | $O(\log n)$ expected |
| B-link tree | linearizable | searches take no locks | at most 3 locks per update | $O(\log_C n)$ page reads |
| Ctrie | linearizable | lock-free | one I-node per update | $O(\log_{2^W} n)$ levels |

: The structures side by side. $p$ is the number of threads, $w$ the width of a counter tree, $S$ the threshold of the sloppy counter, $k$ the number of gating consumers, $c$ the number of heaps and $m$ the size of one heap.

## Choosing a structure

- **A queue between threads.** Start with the two-lock queue. For a pipeline with one producer and a fixed set of stages, use a Disruptor ring. Under very high contention, the LCRQ is several times faster than compare-and-swap queues.
- **A map.** A striped hash table is the simple choice, with $L$ well above the number of threads. If ordered scans or range queries are needed, use a B-link tree. For snapshots, use a Ctrie.
- **A counter.** If reads may be approximate, a sloppy counter is the cheapest. If every call needs a distinct value under heavy load, use a combining tree or funnel for linearizable values, or a diffracting tree if quiescent consistency is enough.
- **A priority queue.** If the algorithm tolerates some disorder, as label-correcting shortest paths and schedulers do, use a MultiQueue. Keep an exact heap only for few threads; the fine-grained heap gives weaker guarantees than one lock.
