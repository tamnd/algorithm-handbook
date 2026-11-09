## What to remember

- A **priority queue** gives back the item with the smallest key. Any comparison-based one needs $\Omega(\log n)$ amortized time per operation for some mix of insert and extract-min, because $n$ inserts and $n$ extract-mins sort $n$ keys.
- The **heap property** asks only that each parent be at most its children. It puts a smallest key at the root and leaves the rest of the tree loosely ordered, which is why a heap is cheap to keep.
- The **binary heap** stores a complete tree in an array, with the children of $i$ at $2i$ and $2i + 1$. Insert uses [sift-up](/sift-up/) and extract-min uses [sift-down](/sift-down/); each follows one path of at most $\lfloor \lg n \rfloor$ edges. Libraries use it: `heapq` in Python, `PriorityQueue` in Java, `std::priority_queue` in C++.
- **Floyd's construction** sifts down from position $\lfloor n/2 \rfloor$ back to 1 and builds a heap in $\Theta(n)$ time, with at most $n - s_2(n)$ swaps, where $s_2(n)$ is the number of 1 bits of $n$. Inserting the keys one by one takes $\Theta(n \log n)$ in the worst case.
- **Decrease-key needs a handle.** A heap cannot find an item fast, so the program must know where the item is. The [indexed priority queue](/indexed-priority-queue/) keeps a second array with the position of each item.
- **Melding** is linear for the array heap and $O(\log n)$ or better for the linked heaps: leftist, skew, binomial, pairing and Fibonacci.
- The **Fibonacci heap** does decrease-key in $O(1)$ amortized time, so [Dijkstra's algorithm](/dijkstra/) runs in $O(m + n \log n)$ instead of $O((n + m) \log n)$. Its node degrees are at most $\log_\phi n \approx 1.44 \lg n$; the proof goes through the Fibonacci numbers, which give the heap its name.
- **Small integer keys** change the rules. A [bucket queue](/bucket-queue/) does each operation in $O(1)$ plus the buckets it skips, and a run with monotone keys costs $O(n + C)$.

## The main heaps side by side

| Heap | Insert | Extract-min | Decrease-key | Meld |
|---|---|---|---|---|
| [Binary heap](/binary-heap/) | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $\Theta(n)$ |
| [d-ary heap](/d-ary-heap/) | $O(\log_d n)$ | $O(d \log_d n)$ | $O(\log_d n)$ | $\Theta(n)$ |
| [Leftist heap](/leftist-heap/) | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| [Skew heap](/skew-heap/) | $O(\log n)$ am. | $O(\log n)$ am. | | $O(\log n)$ am. |
| [Binomial heap](/binomial-heap/) | $O(1)$ am., $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |
| [Pairing heap](/pairing-heap/) | $O(1)$ | $O(\log n)$ am. | $o(\log n)$ am., not $O(1)$ | $O(1)$ |
| [Fibonacci heap](/fibonacci-heap/) | $O(1)$ | $O(\log n)$ am. | $O(1)$ am. | $O(1)$ |
| [Brodal queue](/brodal-queue/), [strict Fibonacci heap](/strict-fibonacci-heap/) | $O(1)$ | $O(\log n)$ | $O(1)$ | $O(1)$ |
| [Bucket queue](/bucket-queue/), keys in $0 \ldots C$ | $O(1)$ | $O(C)$ | $O(1)$ | |

: Costs are worst case unless marked "am." (amortized); find-min is $O(1)$ for all of them, given a pointer to the minimum. The pairing heap bounds are those of its entry; its exact decrease-key cost is still open.

## Choosing a heap

- For most programs, use the binary heap of the standard library. It has no pointers, and its array is kind to the cache.
- When keys must change, use an [indexed priority queue](/indexed-priority-queue/), or insert a new copy and skip stale copies when they come out.
- For Dijkstra's algorithm on dense graphs, a [d-ary heap](/d-ary-heap/) with $d$ about $m/n$ is simple and fast. The Fibonacci heap gives the better bound, but its constants are large.
- When heaps must merge, use a [leftist heap](/leftist-heap/), or a [pairing heap](/pairing-heap/) if amortized bounds are fine.
- When you need both the minimum and the maximum, use a [min-max heap](/min-max-heap/) or an [interval heap](/interval-heap/).
- When the keys are small integers that never go below the last key removed, use a [bucket queue](/bucket-queue/) or a [radix heap](/radix-heap/).
