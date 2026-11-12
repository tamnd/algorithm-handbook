## What to remember

- An implementation is correct if it is [linearizable](/linearizability/): each operation seems to take effect at one instant between its call and its return. Linearizability is local. A proof names a [linearization point](/linearization-point/) for each operation, though some objects, such as the [Herlihy-Wing queue](/herlihy-wing-queue/), have no fixed one.
- Wait-free implies [lock-free](/lock-freedom/), which implies [obstruction-free](/obstruction-freedom/), and no arrow reverses. Lock-free: some operation completes in every infinite run. [Wait-free](/wait-freedom/): every operation completes in a bounded number of its own steps.
- A CAS loop fails only when another CAS succeeds. With $n$ processes that each add one, a process makes at most $n$ attempts and all of them at most $n(n+1)/2$. So the [Treiber stack](/treiber-stack/) and the [Michael-Scott queue](/michael-scott-queue/) take $O(k)$ amortized steps under $k$-way contention, with no bound for one operation.
- A list deletes in two steps: mark the node's own next pointer, then unlink. A CAS on a marked word fails, so no insert lands behind a deleted node. The [Harris list](/harris-linked-list/) does this, and the hash tables, skip list and priority queue of the chapter build on it.
- [Consensus numbers](/consensus-number/): registers and snapshots 1; test-and-set, swap, [fetch-and-add](/fetch-and-add/), queues and stacks 2; $m$-register assignment $2m - 2$; [CAS](/compare-and-swap/) and [LL/SC](/load-linked-store-conditional/) $\infty$. Objects of number $k$ cannot build, wait-free for more than $k$ processes, an object of larger number.
- Consensus for $n$ processes is universal through the [universal construction](/universal-construction/). Wait-freedom usually costs [helping](/helping/): $O(n^2)$ steps per operation in the [Kogan-Petrank queue](/kogan-petrank-queue/), at most $2n^2$ reads per scan in the [Afek et al. snapshot](/afek-atomic-snapshot/).
- Publishing a node needs a release CAS and an acquire read. The [Chase-Lev deque](/chase-lev-deque/) also needs a full fence between the owner's write of `bottom` and its read of `top`, even on x86, or an item can be returned twice.

## The main structures side by side

| Structure | Primitives | Progress | Linearization point | Steps alone | Memory order |
|---|---|---|---|---|---|
| [Treiber stack](/treiber-stack/) | CAS | lock-free | CAS on `top` | push 4, pop 5 | release CAS, acquire read |
| [Michael-Scott queue](/michael-scott-queue/) | CAS | lock-free | CAS on `t.next`; CAS on `Head` | 6 each | release CAS, acquire reads |
| [Herlihy-Wing queue](/herlihy-wing-queue/) | fetch-and-add, swap | enqueue wait-free; dequeue waits on empty | none fixed | enqueue 2; scan $1 + r$ | SC |
| [Lamport queue](/lamport-spsc-queue/) | read, write | wait-free | write of own counter | 4 each | release and acquire on counters |
| [Vyukov queue](/vyukov-bounded-mpmc-queue/) | CAS | try operations lock-free | CAS on `enqPos`, `deqPos` | 5 each | release and acquire on `seq` |
| [Kogan-Petrank queue](/kogan-petrank-queue/) | CAS | wait-free | the CAS steps, by anyone | $2n + 18$, $2n + 24$ | SC |
| [Chase-Lev deque](/chase-lev-deque/) | CAS on the last item | wait-free, steal may abort | write of `bottom`; CAS on `top` | push 6, pop at most 8 | full fences |
| [Harris list](/harris-linked-list/) | CAS, mark bit | lock-free | link CAS; the mark | at most $n + 6$ | release CAS, acquire loads |
| [Non-blocking BST](/non-blocking-bst/) | CAS, Info records | lock-free | CAS on a child pointer | at most $2d + 7$ | release publication |
| [Afek et al. snapshot](/afek-atomic-snapshot/) | read, write | wait-free | update: its write | scan $2n$ to $2n^2$ | SC |
| [Bitonic network](/bitonic-counting-network/) | RMW per balancer | wait-free | none; not linearizable | $m(m+1)/2 + 1$ | relaxed |

: The structures in the model of their entries. $n$ counts keys for the list and processes elsewhere; $r$ is the value of `back` a scan reads, $d$ the depth of a leaf, $2^m$ the width. Steps alone: shared memory steps with no other process running. SC: sequential consistency.

## Choosing a structure

For a shared stack or queue, use the Treiber stack or the Michael-Scott queue, and choose how to free nodes: in C and C++, [hazard pointers](/hazard-pointers/) or [epoch-based reclamation](/epoch-based-reclamation/). If one hot word limits throughput, the [elimination stack](/elimination-backoff-stack/) and [flat combining](/flat-combining/) take load off it. With a fixed capacity, a ring buffer allocates nothing: the Lamport queue for one producer and one consumer, the Vyukov queue for many, if a stalled producer may hold up consumers.

For a set or a map, use a list with [logical deletion](/logical-deletion/): the [Michael hash table](/michael-hash-table/) for a known size, the [split-ordered list](/split-ordered-list/) to grow, the [lock-free skip list](/lock-free-skip-list/) for ordered keys. A work-stealing scheduler wants the Chase-Lev deque.

Ask for wait-freedom only when each operation needs a bound; it costs helping and speed. Use linearizability as the default specification, and accept a weaker one, such as a queue that may answer EMPTY spuriously, only with a reason.
