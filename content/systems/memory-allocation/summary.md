## What to remember

- An [allocator](/allocator/) places each block online and never moves it. It wastes memory by [external fragmentation](/external-fragmentation/), free space in pieces too small to use, and by [internal fragmentation](/internal-fragmentation/) from rounding. If each [size class](/size-classes/) is at most $r$ times the one below, a block wastes less than $(r-1)/r$ of itself: less than $1/(g+1)$ with $g$ classes per doubling, less than $1/2$ for powers of two.
- Worst case, with at most $M$ words live and sizes from 1 to $n$: every allocator that never moves blocks can be forced to use about $\tfrac12 M \log_2 n$ words; for power-of-two sizes with $n \mid M$ the optimum is exactly $M(1 + \tfrac12 \log_2 n) - n + 1$, and one region per size needs at most $M(\log_2 n + 1)$ ([Robson's bound](/robson-bound/)). Address-ordered [first fit](/first-fit-allocation/) can be forced to about $M \log_2 n$, [best fit](/best-fit-allocation/) to about $Mn$.
- With all lifetimes known, placement is [strongly NP-hard](/offline-dynamic-storage-allocation/), yet the optimum is at most $3 \cdot \mathrm{LOAD}$, the most memory live at one time.
- A [sequential fit](/sequential-fit/) scans the free list in $O(F)$ time for $F$ free blocks. Immediate [coalescing](/coalescing/) keeps free blocks from touching, and [boundary tags](/boundary-tags/) make a free $O(1)$.
- With $N$ blocks in use, uniformly random frees, a steady state and a fraction $p$ of allocations that split, the expected number of free blocks lies between $pN/2$ and $pN/2 + 1$ ([fifty-percent rule](/knuth-fifty-percent-rule/)). It counts blocks, not words.
- On eight real programs, address-ordered first fit and best fit had almost no fragmentation once headers were counted apart (Johnstone and Wilson). This is a measurement, not a theorem.
- [TLSF](/tlsf/) takes $O(1)$ time per call in the worst case, but may fail while a block slightly above the request is free. [Hoard](/hoard-allocator/) proves that its memory stays $O(U + P)$ for peak use $U$ and $P$ processors; tcmalloc, jemalloc and mimalloc limit their caches by tuning.

| Method | Time per call | Memory guarantee | Source |
|---|---|---|---|
| First fit, address order | $O(F)$ | about $M \log_2 n$, worst case | [Robson's bound](/robson-bound/) |
| Best fit | $O(F)$; $O(\log F)$ with a tree | about $Mn$, worst case | [Robson's bound](/robson-bound/) |
| Segregated free lists | malloc $O(l + k)$, free $O(1)$ | none proved | [segregated free lists](/segregated-free-lists/) |
| Binary buddy | $O(m)$ | block less than twice the request | [buddy system](/buddy-system/) |
| TLSF | $O(1)$ | rounding below $2^{-J}$ of the request, plus fewer than $2^J$ words not split off | [TLSF](/tlsf/) |
| Memory pool | $O(1)$ | no external fragmentation, one size | [memory pool](/memory-pool/) |
| Slab | $O(1)$; $O(p)$ to grow | fewer than $s$ words lost per slab | [slab allocator](/slab-allocator/) |
| dlmalloc | $O(w)$ | none proved | [dlmalloc](/dlmalloc/) |
| Hoard | $O(c + g)$ | $A(t) = O(U(t) + P)$ | [Hoard](/hoard-allocator/) |
| tcmalloc | $O(1)$ fast path | none proved | [tcmalloc](/tcmalloc/) |
| mimalloc | $O(1)$ fast path | none proved | [mimalloc](/mimalloc/) |
| Lock-free (Michael) | $O(k + 1)$ | constant factor, as the paper states | [lock-free allocator](/lock-free-memory-allocator/) |

: Allocation methods. $F$ free blocks; $l$ the length of a class list and $k$ classes; a buddy heap of $2^m$ words; $p$ objects of $s$ words per slab; $w$ the word length; $c$ classes and $g$ fullness groups in Hoard; $k$ updates by other threads in the lock-free allocator. Worst-case memory bounds are in Robson's model. "None proved" means the entry gives invariants and measurements only.

## Choosing a method

For objects that die together, such as the nodes built while compiling one function, use an [arena](/arena-allocation/) or a [bump pointer](/bump-pointer-allocation/). For many objects of one size, use a memory pool, and in a kernel a slab cache. For a hard real-time system, use TLSF. A general `malloc` for one thread should be close to best fit with coalescing, as dlmalloc is; avoid worst fit. For many threads, use an allocator with thread or CPU caches such as tcmalloc, [jemalloc](/jemalloc/) or mimalloc, or Hoard when the memory bound must be proved. No placement policy keeps memory within $O(M)$ in the worst case; for that, blocks must move, by [memory compaction](/memory-compaction/) or a moving garbage collector.

Judge an allocator on traces of your own program: most numbers in the entries come from small seeded simulations, and random traces predict real fragmentation badly.
