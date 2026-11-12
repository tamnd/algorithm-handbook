Every computer runs algorithms that no user calls by name. When a program reads a file, the operating system looks for the block in its page cache and, if it is not there, picks a page to drop. The scheduler decides which of a hundred ready threads runs next. The allocator finds 48 free bytes for a new object, and later the garbage collector finds that the object is dead. A database chooses the order of three joins. TCP decides how fast to send by watching for lost packets, a load balancer sends each request to one of forty servers, and an API gateway refuses the hundred-and-first request in a second. Each of these is an algorithm with a precise rule and a cost.

This volume is about those algorithms. It starts with caching and goes on to scheduling, memory allocation, garbage collection, the algorithms inside a database, the algorithms of networks, load balancing and rate limiting.

This edition contains the entries of the first chapter, *Caching policies*. The entries of the other seven chapters are being written; in this edition each of them has an opening page only saying what the chapter will cover and which entries elsewhere in the set to read meanwhile.

## Why systems algorithms get a volume of their own

A systems algorithm is judged on a machine and a workload. A few ideas come back in every chapter:

- **The cost model is the machine.** Cost is counted in misses, disk seeks, round trips, pauses or bytes sent. The [memory hierarchy](/memory-hierarchy/) makes a miss in a [cache](/cache/) a hundred times dearer than a hit.
- **Decisions are made online.** A cache must evict before it sees the next request, and a scheduler must run a job before it knows how long the others will take. The worst-case tool is the [competitive ratio](/competitive-ratio/) of Volume 19: on any request sequence, [LRU](/lru/) with a cache of $k$ pages misses at most about $k$ times as often as the optimal offline policy, and no deterministic policy does better.
- **Every bound names its model.** A guarantee is either a worst case over all inputs or an average over a stated workload: the [independent reference model](/independent-reference-model/), a Zipf popularity law, or a recorded trace. Since no deterministic policy beats LRU in the worst case, the caching policies that followed it were chosen because they hit more often on traces.
- **Each decision must be cheap.** A rule that runs on every memory access or every packet can spend a few nanoseconds and a few bits. [CLOCK](/clock/) keeps one bit per page instead of an ordered list, and [TinyLFU](/tinylfu/) keeps a sketch instead of exact counts.
- **Many users share one resource.** Threads share a processor, flows share a link and tenants share a cache. Fairness and tail latency matter as much as the mean.
- **Correctness comes before speed.** A cache can serve a stale value after a race, a collector must never free a live object, and a database must keep its committed data through a crash.

## How this volume relates to the others

- **Volume 1, foundations**, has the memory hierarchy, the [external memory model](/external-memory-model/), and [balls into bins](/balls-into-bins/), the model behind load balancing.
- **Volume 3, data structures**, gives the [hash table](/hash-table/), the [binary heap](/binary-heap/), the [B-tree](/b-tree/) of database indexes and the [Bloom filter](/bloom-filter/).
- **Volume 17, randomized algorithms**, has the [Markov chain](/markov-chain/), the tool for hit ratios under a workload model.
- **Volume 18, approximation**, has [list scheduling](/list-scheduling/), one of the first proved ratios for scheduling jobs on machines.
- **Volume 19, online and streaming**, has the theory of paging: the [paging problem](/paging-problem/), the [Sleator-Tarjan bound](/sleator-tarjan-paging-bound/), [Belady's algorithm](/belady-algorithm/) and randomized paging. The [count-min sketch](/count-min-sketch/) of Volume 19 is the counter inside TinyLFU.
- **Volume 21, distributed algorithms**, has consensus by [Paxos](/paxos/) and [Raft](/raft/), on which replicated databases rest.
- **Volume 22, concurrency**, has [linearizability](/linearizability/) and memory reclamation with [hazard pointers](/hazard-pointers/) and [epochs](/epoch-based-reclamation/), the lock-free cousins of garbage collection.

## The chapters

**Chapter 26.1, Caching policies**, covers the cache, the [hit ratio](/cache-hit-ratio/) and [locality of reference](/locality-of-reference/); [Belady's MIN](/belady-optimal/), [FIFO](/fifo-replacement/), LRU, [LFU](/lfu/), CLOCK and [random replacement](/random-replacement/); write policies and prefetching; [reuse distance](/reuse-distance/) and [miss ratio curves](/miss-ratio-curve/); the [competitive bound for LRU](/lru-competitiveness/) and the independent reference model; the policies that combine recency and frequency, from [LRU-K](/lru-k/) and [2Q](/two-q/) to [ARC](/arc/) and [LIRS](/lirs/); admission and quick demotion with TinyLFU, [S3-FIFO](/s3-fifo/) and [SIEVE](/sieve/); [objects of different sizes](/variable-size-caching/) and [GreedyDual](/greedy-dual/); and the application caches of [TTL expiration](/ttl-expiration/), the [cache-aside pattern](/cache-aside-pattern/) and [invalidation](/cache-invalidation/).

**Chapter 26.2, Scheduling**, decides which job runs next. It will cover first-come first-served, shortest job first, round robin, priorities with aging, multilevel feedback queues, lottery and stride scheduling and the Completely Fair Scheduler; for real-time systems, rate-monotonic scheduling with the Liu-Layland bound, earliest deadline first, response-time analysis and priority inversion; disk scheduling from SSTF to C-SCAN; Smith's rule, Johnson's rule and the critical path method; and cluster scheduling with backfilling and dominant resource fairness.

**Chapter 26.3, Memory allocation**, finds room for objects of many sizes in one heap. It will cover free lists and the fits, size classes, the buddy system, boundary tags and coalescing, fragmentation with Knuth's fifty-percent rule and Robson's bound, slab, arena and bump-pointer allocation, TLSF, and the designs of dlmalloc, jemalloc, tcmalloc and mimalloc.

**Chapter 26.4, Garbage collection**, frees the objects a program can no longer reach. It will cover mark-sweep, Cheney's copying collector, mark-compact, reference counting and cycle collection, tricolor marking with read and write barriers, generational collection with remembered sets and card marking, incremental, concurrent and real-time collectors, conservative collection, the collectors G1, Shenandoah and ZGC, and weak references and finalization.

**Chapter 26.5, Database algorithms**, covers the algorithms inside a database system. It will cover the relational algebra and the joins, from nested loops and hash joins to worst-case optimal joins; query optimization with cost models and cardinality estimates; indexes; normalization; transactions with two-phase locking, timestamp ordering, multiversion concurrency and snapshot isolation; recovery with write-ahead logging and ARIES; Datalog with semi-naive evaluation; and top-$k$ queries with Fagin's threshold algorithm.

**Chapter 26.6, Networking algorithms**, moves packets between computers. It will cover sliding-window protocols, TCP congestion control from Tahoe and Reno to CUBIC and BBR, active queue management with RED and CoDel, fair queueing, distance-vector, link-state and path-vector routing, longest prefix match, switch scheduling, medium access from ALOHA to CSMA/CA, and Chord and Kademlia.

**Chapter 26.7, Load balancing and hashing**, spreads work over many servers. It will cover consistent hashing with virtual nodes and bounded loads, rendezvous, jump and Maglev hashing, the power of two choices, rules from round robin and least connections to Peak EWMA, health checks and connection draining, and sharding by hash and by range.

**Chapter 26.8, Rate limiting**, bounds how fast a client may send. It will cover the token bucket, the leaky bucket and the generic cell rate algorithm, fixed and sliding windows, the three-color markers, policing and shaping, admission control and backpressure, and rate limiting across many servers.

## How to read this volume

If this is your first course, read these entries of Chapter 26.1 in this order: the cache, the cache hit ratio, locality of reference, Belady's MIN, FIFO, [Belady's anomaly](/belady-anomaly/), LRU, the [LRU cache](/lru-cache/), CLOCK, [write-back](/write-back/), reuse distance, the miss ratio curve, the competitive bound for LRU, the independent reference model, ARC, S3-FIFO, TTL expiration and the cache-aside pattern. Then read the paging problem and the Sleator-Tarjan bound in Volume 19, which prove the worst-case bounds. Do the exercises marked ◦ and • at the end of Chapter 26.1. That is a complete first unit on caching.

If you already know the basic algorithms, start with the opening page of each chapter. It names the groups in the chapter and the order to read them.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need the memory hierarchy and expected values, and from Volume 3 hash tables, linked lists and heaps. The worst-case bounds use the paging problem and the competitive ratio of Volume 19, and the average-case results use Markov chains. Later chapters add basic probability and some knowledge of threads and locks.

## The exercises

In this edition only Chapter 26.1 has exercises; the other chapters will have them when their entries are written. They come in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
