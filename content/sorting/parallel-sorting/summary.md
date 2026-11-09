## What to remember

- A parallel sort has two costs, the **time** or span and the **work**, and each bound names its model. The goal is short time and work $O(n \log n)$. By [Brent's theorem](/brent-theorem/), work $T_1$ and span $T_\infty$ give time at most $T_1/p + T_\infty$ on $p$ processors.
- **Sorting needs $\Omega(\log n)$ steps** wherever one step combines two values: in comparator networks, in the parallel comparison model with $O(n)$ processors, and on the CREW PRAM. [Cole's merge sort](/cole-merge-sort/) meets the bound with $n$ processors and $O(n \log n)$ work. On the CRCW PRAM with polynomially many processors the bound is $\Omega(\log n / \log \log n)$.
- **Merging is easier than sorting.** An item's output position is its index plus its rank in the other list. [Merge path](/merge-path/) and [Shiloach-Vishkin merging](/shiloach-vishkin-merge/) merge in time $O(n/p + \log n)$ with linear work. Counting only comparisons, [Valiant's merge](/valiant-parallel-merge/) needs $O(\log \log n)$ rounds.
- **Divide and conquer is parallel only if its merge or split is.** [Parallel merge sort](/parallel-merge-sort/) with a binary-search merge has span $O(\log^3 n)$. [Parallel quicksort](/parallel-quicksort/) partitions with prefix sums and has span $O(\log^2 n)$ with high probability.
- **Sorts that move each key once** win on real machines. [Sample sort](/sample-sort/) gives every processor at most about $2n/p$ keys with high probability. [Regular sampling](/parallel-sorting-by-regular-sampling/) guarantees at most $2n/p - p$ keys when keys are distinct.
- **Integer keys are sorted by prefix sums.** One pass of [parallel radix sort](/parallel-radix-sort/) on $b$-bit digits takes time $O(n/p + 2^b + \log p)$. The prefix sum runs digit by digit and, within a digit, processor by processor.
- **On a fixed network, distance is a lower bound.** A line of $n$ processors needs $n - 1$ steps; [odd-even transposition sort](/odd-even-transposition-sort/) takes $n$. A $\sqrt n \times \sqrt n$ mesh needs $2\sqrt n - 2$ steps; [shearsort](/shearsort/) takes $\sqrt n (\lg n + 1)$, the best mesh sorts about $3\sqrt n$.
- **Oblivious sorts are proved by the zero-one principle.** Odd-even transposition sort, shearsort and [columnsort](/columnsort/) fix their compare-exchanges in advance, so inputs of zeros and ones suffice.

## The main sorts side by side

| Sort | Model | Time or span | Work | Deterministic | Stable |
|---|---|---|---|---|---|
| [Odd-even transposition sort](/odd-even-transposition-sort/) | line of $n$ processors | $n$ rounds | $\Theta(n^2)$ | yes | yes |
| [Shearsort](/shearsort/) | $\sqrt n \times \sqrt n$ mesh | $\sqrt n (\lg n + 1)$ steps | $O(n^{3/2} \log n)$ | yes | no |
| [Columnsort](/columnsort/) | $s$ processors, $r \ge 2(s-1)^2$ | 4 column sorts | $O(n \log r)$ | yes | no |
| [Parallel merge sort](/parallel-merge-sort/) | work-span | $O(\log^3 n)$ | $\Theta(n \log n)$ | yes | yes |
| [Parallel quicksort](/parallel-quicksort/) | work-span | $O(\log^2 n)$ w.h.p. | $O(n \log n)$ expected | no | yes |
| [Hyperquicksort](/hyperquicksort/) | hypercube, $p$ processors | $O((n/p) \log n + \log^2 p)$ if balanced | $O(n \log n)$ if balanced | yes | no |
| [Sample sort](/sample-sort/) | CREW PRAM or BSP, $p$ processors | $O((n/p) \log n)$ w.h.p. | $O(n \log n)$ | no | with index tags |
| [Regular sampling](/parallel-sorting-by-regular-sampling/) | BSP, $p$ processors, $n \ge p^3$ | $O((n/p) \log n)$ | $O(n \log n)$ | yes | with index tags |
| [Parallel radix sort](/parallel-radix-sort/) | EREW PRAM, $p$ processors | $O(\lceil w/b \rceil (n/p + 2^b + \log p))$ | $O(\lceil w/b \rceil (n + 2^b p))$ | yes | yes |
| [Cole's merge sort](/cole-merge-sort/) | CREW or EREW PRAM, $n$ processors | $O(\log n)$ | $O(n \log n)$ | yes | yes |

: The main parallel sorts. Sample sort needs $\Theta(\log n)$ samples per bucket and $p^2 \log n = O(n)$. Hyperquicksort's bound holds only while the loads stay near $n/p$. Radix sort is for $w$-bit keys cut into $b$-bit digits.

## Choosing a method

- On a shared-memory multicore, use your library's parallel sort. If you write one, use sample sort, or parallel merge sort with [merge path](/merge-path/) merges when the sort must be stable and deterministic.
- On a graphics processor, use parallel radix sort for integer keys and keys that map to integers in order, such as floating-point numbers. For general keys, use merge sort with merge path.
- On a cluster, use sample sort, or regular sampling when $n \ge p^3$ and the load bound must be deterministic. Tag keys with their positions when many may be equal.
- On a fixed grid of processors, use odd-even transposition sort on lines and shearsort on small meshes. For a comparator network in hardware, see [bitonic sort](/bitonic-sort/) in Chapter 4.4.
- Treat Cole's merge sort as a proof that $O(\log n)$ time is possible, not as a program to run.
