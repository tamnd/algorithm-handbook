## What to remember

- A **comparison sort** learns about the input only by comparing pairs of keys. Any such sort needs at least $\lceil \lg n! \rceil = n \lg n - O(n)$ comparisons in the worst case, and on average too. [Merge sort](/merge-sort/), [heapsort](/heapsort/) and [randomized quicksort](/randomized-quicksort/) (in expectation) match this bound up to a constant factor.
- **Insertion sort** runs in $\Theta(n + d)$ time, where $d$ is the number of [inversions](/inversion/). It is the best sort for short or nearly sorted arrays, and the fast sorts use it for their small subproblems.
- **Merge sort** is $\Theta(n \log n)$ on every input and stable, but it needs a second array. Merging is the step that does the work; it costs at most $m + n - 1$ comparisons.
- **Quicksort** does its work before the recursion, in the partition. Its running time depends on the pivots: $\Theta(n^2)$ in the worst case, $\Theta(n \log n)$ expected with random pivots. With many equal keys, use [three-way partitioning](/three-way-quicksort/).
- **Heapsort** is in place and $\Theta(n \log n)$ in the worst case, but it is not stable and its memory access jumps around, so it is slower in practice than quicksort.
- **Stability** and **working in place** are separate properties. The simple stable sorts are insertion sort and merge sort. The fast in-place sorts, quicksort and heapsort, are not stable. Getting both at once in $O(n \log n)$ time is possible but intricate; see [block sort](/block-sort/).
- **Library sorts are hybrids.** [Introsort](/introsort/) is quicksort with a heapsort fallback and insertion sort at the leaves. [Timsort](/timsort/) is a natural merge sort that finds runs and merges them with care.

## The main sorts side by side

| Sort | Best | Average | Worst | Extra space | Stable |
|---|---|---|---|---|---|
| [Insertion sort](/insertion-sort/) | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | yes |
| [Selection sort](/selection-sort/) | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | no |
| [Bubble sort](/bubble-sort/) | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | yes |
| [Shellsort](/shell-sort/), $3h+1$ gaps | $\Theta(n \log n)$ | — | $O(n^{3/2})$ | $\Theta(1)$ | no |
| [Merge sort](/merge-sort/) | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ | yes |
| [Natural merge sort](/natural-merge-sort/) | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ | yes |
| [Quicksort](/randomized-quicksort/), random pivot | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n^2)$ | $O(\log n)$ stack | no |
| [Heapsort](/heapsort/) | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(1)$ | no |
| [Smoothsort](/smoothsort/) | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(1)$ | no |
| [Introsort](/introsort/) | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $O(\log n)$ | no |
| [Timsort](/timsort/) | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $O(n)$ | yes |

: The main comparison sorts. The quicksort stack is $O(\log n)$ when the sort recurses on the smaller side first; see [quicksort stack depth](/quicksort-stack-depth/). The average-case cost of Shellsort is still an open problem for most gap sequences.

## Choosing a sort

Use the sort of your language's library unless you have measured a reason not to. When you must write one:

- For a handful of items, or input that is almost sorted, use insertion sort.
- When you need stability, use merge sort or a natural merge sort.
- When memory is tight and the worst case matters, use heapsort, or introsort for speed.
- When the keys are small integers or fixed-length strings, leave this chapter: a [distribution sort](/counting-sort/) from Chapter 4.2 is faster.
- When writes are very expensive, as in some flash memory, [cycle sort](/cycle-sort/) writes each item at most once.
