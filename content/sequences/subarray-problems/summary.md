## What to remember

- A **subarray** $A[i..j)$ is fixed by its two ends, so an array has $\Theta(n^2)$ of them. With [prefix sums](/prefix-sums/) its sum is $P_j - P_i$, and most problems of the chapter become problems about pairs of prefix sums.
- **Kadane's algorithm** solves the maximum subarray problem in $\Theta(n)$ time and $O(1)$ space by the recurrence $E(j) = A[j] + \max(E(j-1), 0)$ for the best sum ending at $j$. Linear time is optimal: every item must be read. The divide-and-conquer method takes $\Theta(n \log n)$, or $\Theta(n)$ if each call also returns its total, best prefix and best suffix.
- A **wrapping run** of a ring is the ring minus a plain run, so the circular answer is $\max(\text{best}, T - \text{worst})$, unless every item is negative. For **products**, keep both the largest and the smallest product ending at each item, since a negative item swaps them.
- The **maximum sum submatrix** takes $\Theta(m^2 n)$ time by Kadane on the column sums of each band of rows. An $O(n^{3-\varepsilon})$ algorithm for $n \times n$ matrices would refute the APSP conjecture.
- A **sliding window** with two pointers is linear when the condition is monotone: a good window stays good when it grows (sum at least $s$ with items $\ge 0$) or when it shrinks (at most $k$ distinct values). With negative items, the sum condition is not monotone and the window gives wrong answers.
- For an **exact target**, count the earlier prefix sums equal to $P_j - k$ in a hash table: $\Theta(n)$ expected time. Without hashing, deciding whether a zero-sum subarray exists needs $\Omega(n \log n)$ time in the algebraic decision tree model, by a reduction from element distinctness.
- For a **threshold with negative items**, such as the shortest run with sum at least $K$ or a length between $L$ and $U$, a deque of increasing prefix sums gives $\Theta(n)$ time, since each index enters and leaves once.
- The **largest rectangle in a histogram** is $\max_k h_k (R_k - L_k - 1)$, with $L_k$ and $R_k$ the nearest strictly lower bars. One monotonic stack pass finds them all in $\Theta(n)$, and row histograms extend it to binary matrices in $\Theta(rc)$.

## The main algorithms side by side

| Algorithm | Problem | Time | Extra space | Items |
|---|---|---|---|---|
| [Kadane's algorithm](/kadane-algorithm/) | maximum subarray | $\Theta(n)$ | $\Theta(1)$ | any sign |
| [Divide and conquer](/maximum-subarray-divide-and-conquer/) | maximum subarray | $\Theta(n \log n)$ | $\Theta(\log n)$ | any sign |
| [Circular Kadane](/circular-kadane-algorithm/) | maximum on a ring | $\Theta(n)$ | $\Theta(1)$ | any sign |
| [Max-product scan](/kadane-max-product/) | maximum product | $\Theta(n)$ | $\Theta(1)$ | any sign |
| [Bentley column sweep](/bentley-column-sweep/) | maximum submatrix, $m \le n$ | $\Theta(m^2 n)$ | $\Theta(n)$ | any sign |
| [Window for positive sums](/sliding-window-positive-sum/) | shortest sum $\ge s$ | $\Theta(n)$ | $\Theta(1)$ | not negative |
| [Distinct-count two pointers](/distinct-count-two-pointers/) | longest with $\le k$ distinct | $O(n)$ expected | $O(\min(n, k))$ | hashable |
| [Prefix sum hash counting](/prefix-sum-hash-counting/) | count sums equal to $k$ | $\Theta(n)$ expected | $\Theta(n)$ | any sign |
| [Monotonic deque](/monotonic-deque-prefix-sums/) | shortest sum $\ge K$ | $\Theta(n)$ | $\Theta(n)$ | any sign |
| [Histogram stack](/histogram-stack-algorithm/) | largest rectangle | $\Theta(n)$ | $\Theta(n)$ | heights $\ge 0$ |

: The main algorithms of the chapter. The hash-based bounds are expected times with a random hash function; with adversarial collisions both can reach $\Theta(n^2)$, and a direct table over small integer values makes them worst-case linear.

## Choosing a method

Start by asking what the condition on the run looks like.

- **Largest or smallest sum, no length bound.** Use Kadane's algorithm. On a ring, run it for the maximum and the minimum at once.
- **A fixed length.** Use a rolling sum. All windows have the same length, so the largest sum is also the largest average.
- **A threshold, items not negative.** Use two pointers. They need $O(1)$ space and no prefix array.
- **A threshold or a length range, items of any sign.** Use prefix sums with a monotonic deque.
- **An exact sum, or counting.** Use prefix sums with a hash table, or a direct table when the prefix sums lie in a small range.
- **A bound on a property that only gets worse as the window grows,** such as the number of distinct values. Use two pointers with a count table.
- **A minimum over the run times its width.** Use a monotonic stack to find how far each item reaches.
- **Many queries on ranges of a changing array.** Leave this chapter for the [segment tree for maximum subsegment sum](/segment-tree-maximum-subsegment-sum/), which keeps the four values of the divide-and-conquer combine in each node.
