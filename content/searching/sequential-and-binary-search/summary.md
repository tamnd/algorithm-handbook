## What to remember

- **Search without order costs $n$.** In the comparison model, every algorithm that searches an unordered array of $n$ items makes $n$ comparisons in the worst case, and [linear search](/linear-search/) makes exactly $n$. A successful search for a key at a uniform random position costs $(n+1)/2$ on average.
- **Binary search is optimal.** On a sorted array it makes at most $\lfloor \lg n \rfloor + 1 = \lceil \lg(n+1) \rceil$ comparisons, and the [decision tree](/search-decision-tree/) argument shows that no comparison algorithm needs fewer in the worst case, or fewer than $\lg(n+1)$ on average over the gaps.
- **Search for a boundary, not a key.** The [lower bound query](/lower-bound-query/) (first $A[i] \ge x$) and the [upper bound query](/upper-bound-query/) (first $A[i] > x$) cover membership, insertion points, predecessor, successor and counting: the key occurs $u - \ell$ times. One loop with the half-open range $[lo, hi)$ and the invariant "false left of $lo$, true from $hi$ on" answers them all.
- **Cost can depend on the answer, not on $n$.** [Exponential search](/exponential-search/) makes at most $2\lfloor \lg i \rfloor + 3$ comparisons for a key whose lower bound is $i \ge 1$, so it works when the length is unknown.
- **Values can do better than comparisons, on average.** [Interpolation search](/interpolation-search/) makes $\lg \lg n + O(1)$ expected probes on uniform random keys, but $\Theta(n)$ in the worst case.
- **Halving needs only a test that points the right way.** A rotated array, a sequence with a [peak](/peak-finding/), a [unimodal](/unimodal-maximum/) sequence and the cut between [two sorted arrays](/median-of-two-sorted-arrays/) all admit a $\Theta(\log n)$ search, as long as the items are distinct. With repeated items, the rotated cases fall back to $\Theta(n)$.
- **Partial order costs more.** In an $m \times n$ matrix with sorted rows and columns, [staircase search](/staircase-search/) reads at most $m + n - 1$ cells, which is optimal for a square matrix; for $m \ll n$ the right order is $\Theta(m \log(2n/m))$.
- **The same comparisons can cost very different times.** [Branchless binary search](/branchless-binary-search/) and the [Eytzinger layout](/eytzinger-layout/) keep the comparison count of binary search but avoid branch mispredictions and cache misses.

## The main methods side by side

| Method | Needs | Worst case | Average | Extra space |
|---|---|---|---|---|
| [Linear search](/linear-search/) | nothing | $n$ | $(n+1)/2$, key present | $\Theta(1)$ |
| [Binary search](/binary-search/) | sorted array | $\lfloor \lg n \rfloor + 1$ | $\Theta(\log n)$ | $\Theta(1)$ |
| [Jump search](/jump-search/), $m = \lfloor \sqrt{n} \rfloor$ | sorted array | $\lceil n/m \rceil + m \approx 2\sqrt{n}$ | $\Theta(\sqrt{n})$ | $\Theta(1)$ |
| [Exponential search](/exponential-search/) | sorted array, length optional | $2\lfloor \lg i \rfloor + 3$ | $\Theta(\log i)$ | $\Theta(1)$ |
| [Interpolation search](/interpolation-search/) | sorted numbers | $\Theta(n)$ | $\lg \lg n + O(1)$, uniform keys | $\Theta(1)$ |
| [Fibonacci search](/fibonacci-search/) | sorted array | $\approx 1.44 \lg n$ | about 4% above binary search | $\Theta(1)$ |
| [Uniform binary search](/uniform-binary-search/) | sorted array | $\lceil \lg(n+1) \rceil$ | $\lceil \lg(n+1) \rceil$ | $\Theta(1)$ |
| [Staircase search](/staircase-search/) | sorted rows and columns | $m + n - 1$ | $\Theta(m + n)$ | $\Theta(1)$ |

: The main search methods of the chapter, with costs in comparisons or probes of items. Here $n$ is the number of items, $i \ge 1$ the lower bound of the key, and $m \times n$ the shape of the matrix. The count for uniform binary search leaves out its one final equality test; the count for staircase search is in cells read.

## Choosing a method

- If you search an array once, scan it. Sorting it first costs more than the scan.
- If you search a sorted array many times, use the lower bound form of binary search from your library (`bisect_left` in Python, `std::lower_bound` in C++) and test the result for equality. Write your own only when you must, and copy the invariant, not the code.
- If the key is likely near the start, or the length is unknown, use exponential search.
- If the keys are numbers spread close to evenly and each probe is slow, as on a disk, try interpolation search, mixed with binary search steps so that the worst case stays $O(\log n)$.
- If the searches are the hot loop of a program, measure the branchless loop and the Eytzinger layout against the plain one.
- If the data changes often, leave this chapter: a [hash table](/hash-table/) or a balanced search tree keeps search fast under updates.
