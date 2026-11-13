## What to remember

- An object is [garbage](/garbage/) when no path of pointers from a [root](/gc-roots/) reaches it. A collector is safe when it frees only unreachable objects, and each entry proves this in its own model of the mutator and the heap.
- [Tracing](/tracing-garbage-collection/) computes the least fixed point of the reachability equations. [Reference counting](/reference-counting/) keeps the greatest: the reachable objects plus the garbage that a dead cycle reaches. It needs a [cycle collector](/cycle-collection/), such as [trial deletion](/trial-deletion/) in $O(N + E)$.
- [Mark-and-sweep](/mark-and-sweep/) works in the heap size, [copying](/copying-collection/) in the live data only, but keeps half the memory empty. With $k = H/L$, the [space-time tradeoff](/gc-space-time-tradeoff/) gives $2c/(k-2)$ per allocated word for copying and $(m + sk)/(k-1)$ for mark-and-sweep, exactly, in a model with fixed $L$ and no fragmentation. That a collector needs about five times the memory to match explicit freeing is a measurement (Hertz and Berger).
- A [generational collector](/generational-garbage-collection/) is correct if every old-to-young slot is in the [remembered set](/remembered-set/), which a [write barrier](/write-barrier/) or [card marking](/card-marking/) maintains. It is fast only if $\sigma(N) = \frac1N\sum_{a<N} S(a)$ is small. That is the weak [generational hypothesis](/generational-hypothesis/), a claim about observed programs; the strong form often fails.
- In [tricolor marking](/tricolor-marking/), the strong invariant forbids black-to-white pointers; the weak one allows them while a gray object reaches the white target through white objects. An object is lost only if the mutator both stores a black-to-white pointer and destroys every gray-to-white path to it. The [incremental update](/incremental-update-barrier/) barriers of Dijkstra and Steele keep the strong invariant and rescan the roots at the end. Yuasa's [snapshot-at-the-beginning](/snapshot-at-the-beginning/) barrier keeps the weak one, needs no rescan, and keeps exactly the objects live at the start plus those allocated during the cycle.
- [Baker's collector](/baker-real-time-collector/) scans $k$ cells per allocation and never runs out of space if $S \ge L + \lceil L/k \rceil$. The bound counts work on one processor with atomic steps, not time.
- The [production collectors](/garbage-first-collector/) combine regions, barriers and pacing. Their entries model the mechanism, and their pause times are measurements.

| Method | Time per collection | Extra space | Moves objects | Frees dead cycles | Source |
|---|---|---|---|---|---|
| Mark-and-sweep | $O(r + kn)$, the sweep clearing freed cells | mark bits, $O(n)$ | no | yes | [mark-and-sweep](/mark-and-sweep/) |
| Lazy sweeping | pause $O(r + kL)$, then $1/(1-f)$ visits per allocated cell | as mark-and-sweep | no | yes | [lazy sweeping](/lazy-sweeping/) |
| Schorr–Waite | $3q + 1$ iterations | $O(1)$ words, a flag bit per cell | no | yes | [Schorr–Waite](/schorr-waite-marking/) |
| Cheney | $O(r + L)$ | second semispace, $O(1)$ beside it | yes | yes | [Cheney](/cheney-copying-collector/) |
| Two-finger | $O(n + kL + r)$ | $O(1)$ | at most $\min(L, n - L)$ cells | yes | [two-finger](/two-finger-compaction/) |
| Lisp 2 | $O(m + L + r)$ | one word per object | yes, in order | yes | [Lisp 2](/lisp2-compaction/) |
| Reference counting | $O(1 + k)$ per write, $O(1)$ amortized | a count per object | no | no | [reference counting](/reference-counting/) |
| Deferred counting | $O(r + z + k)$ | the ZCT, $O(z)$ | no | no | [deferred RC](/deferred-reference-counting/) |
| Minor generational | $O(\rho + \lvert R\rvert + s)$ | remembered set | yes | young ones | [generational GC](/generational-garbage-collection/) |
| Baker | $O(kp^2 + rp)$ per mutator operation | $2S$ cells | yes | yes | [Baker](/baker-real-time-collector/) |

: Bounds proved in each entry's model, none of them a measured time. $r$ roots ($\rho$ root slots), $L$ live cells or words, $n$ cells or $m$ objects in the heap, $k$ fields per cell (for Baker, cells scanned per allocation, with $p$ fields per cell), $f$ the live fraction of a block, $q$ the cells one Schorr–Waite call marks, $z$ objects through the zero count table, $s$ the size of the young survivors.

## Choosing a method

With exact pointer maps and memory to spare, start with a generational collector: a copying nursery with [bump allocation](/bump-pointer-allocation/), card marking, and mark-and-sweep or [mark-compact](/mark-compact/) for the old generation. In the [pause model](/generational-collector-pause-tradeoff/), a larger nursery gives longer pauses and less work per allocation. Without pointer maps, as in C, use a [conservative](/conservative-garbage-collection/) collector such as the [Boehm collector](/boehm-gc/).

For short pauses, mark concurrently with a snapshot barrier, as [G1](/garbage-first-collector/) and [Shenandoah](/shenandoah-collector/) do, and move objects behind a load barrier, as [ZGC](/z-garbage-collector/) and [C4](/c4-collector/) do; their pause times are measured, so check them on your own heap. Choose reference counting when objects must be freed promptly, or the [weighted](/weighted-reference-counting/) form across machines, and add a cycle collector unless the data are acyclic. Close resources explicitly rather than in a [finalizer](/finalization/).
