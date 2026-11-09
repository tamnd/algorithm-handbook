## What to remember

- A **permutation** can be read from positions to values or, through its [inverse](/permutation-inverse/), from values to positions. Confusing the two is the most common bug in code that works with permutations. Following each item to where it goes splits the permutation into disjoint [cycles](/permutation-cycles/), and most of its properties can be read from them.
- **Applying a permutation in place** takes $\Theta(n)$ time when each cycle is walked once and a mark bit per position records which cycles are done. Without the marks, as in the read-only form of [the cycle-leader method](/cycle-leader-permutation/), it takes $\Theta(n^2)$ time in the worst case.
- An **inversion** is a pair of items in the wrong order. A sequence has between $0$ and $\binom n2$ of them, and a random permutation has $n(n-1)/4$ on average. The inversion count is the fewest [swaps of neighbours](/sorting-by-adjacent-swaps/) that sort the sequence, and its parity is the [sign](/permutation-parity/) of the permutation, which also equals the parity of $n - c$ for $c$ cycles.
- **Counting inversions** takes $O(n \log n)$ time with a [merge sort that counts](/inversion-count-by-merge-sort/) or a [Fenwick tree](/inversion-count-with-fenwick-tree/). No comparison algorithm does better, but on a word RAM with integer keys a faster method is known.
- The **[Lehmer code](/lehmer-code/)** lists, for each item, the number of smaller items after it. Its digits are independent, they add up to the inversion count, and read in the [factorial number system](/factorial-number-system/) they give the rank of the permutation in lexicographic order. [Ranking and unranking](/permutation-rank-unrank/) take $O(n \log n)$ time.
- The **[next permutation](/lexicographic-successor/)** in lexicographic order comes from one swap and one reversal of a suffix. That costs $O(n)$ in the worst case and $O(1)$ amortized over a full listing.
- Each **distance between rankings** counts the fewest moves of one kind. Swaps of neighbours give the Kendall distance and swaps of any two items give the Cayley distance. Moves of one item to any place give the Ulam distance. The footrule is not a count of moves, but it stays within a factor of 2 of the Kendall distance.
- **Restricted moves make sorting hard.** With prefix flips, reversals or block moves as the only move, finding the fewest moves is NP-hard. [Breakpoints](/breakpoint-distance/) give the basic lower bound, and the known algorithms come within a constant factor of the optimum.
- A **stack** can produce exactly the permutations that avoid the pattern 312 and sort exactly those that avoid 231. Both sets are counted by the [Catalan numbers](/catalan-numbers/). Testing whether a permutation contains a given pattern is NP-complete in general.

## Four distances side by side

| Distance | Move it counts | Formula | Time | Largest value |
|---|---|---|---|---|
| [Kendall tau](/kendall-tau-distance/) | swap of two neighbours | $\operatorname{inv}(\sigma^{-1}\tau)$ | $O(n \log n)$ | $\binom n2$ |
| [Cayley](/cayley-distance/) | swap of any two items | $n - c(\sigma^{-1}\tau)$ | $O(n)$ | $n - 1$ |
| [Ulam](/ulam-distance/) | move of one item | $n - \operatorname{LIS}(\sigma^{-1}\tau)$ | $O(n \log n)$ | $n - 1$ |
| [Spearman footrule](/spearman-footrule/) | none | $\sum_i \lvert \sigma(i) - \tau(i) \rvert$ | $O(n)$ | $\lfloor n^2/2 \rfloor$ |

: Four distances between two rankings $\sigma$ and $\tau$ of $n$ items. Here $c$ is the number of cycles and LIS is the length of the longest increasing subsequence. For the permutation $3\,1\,4\,5\,2$ against the identity, the Kendall distance is 4, the Cayley distance 4, the Ulam distance 2 and the footrule 8.

## Choosing a method

- To count inversions once, use the merge sort method. It needs no compression and sorts the array as a by-product. When the values are small integers, or the count must be updated as items arrive, use the Fenwick tree.
- To compare two rankings of the same items, use the Kendall distance. It is the standard, and its value is easy to explain. When $n$ is large and linear time matters, the footrule is within a factor of 2 of it.
- To number permutations, for a table index or a hash, use the Lehmer code and the factorial number system. To step through all of them in order, use the successor. If any order will do, [Heap's algorithm](/heaps-algorithm/) changes only two items at each step.
- To apply a permutation that you may overwrite, use the cycle-leader method with sign bits. When the permutation is read-only and memory is short, accept the quadratic worst case or spend $n$ bits on marks.
