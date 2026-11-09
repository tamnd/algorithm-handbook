## What to remember

- **Two indices that only move forward cost $O(n)$.** Each index crosses the input at most once, so a scan does at most about $2n$ moves where a search over all pairs does $\Theta(n^2)$ work. The proof of each scan is an invariant that says the dropped pairs hold no better answer.
- **From both ends, one comparison drops a row or a column.** On a sorted array, a sum that is too small rules out the left item with every partner still in range, and a sum that is too large rules out the right item. The [pair search](/two-pointer-pair-search/) needs at most $n - 1$ iterations, and on an unsorted input it can miss a pair.
- **Move the side that limits the answer.** In the [container](/container-with-most-water/) the shorter wall cannot do better with any closer partner. In [trapping rain water](/trapping-rain-water/) the side with the smaller running maximum already knows its water level.
- **Three indices partition in one pass.** [Dijkstra's loop](/dutch-national-flag-algorithm/) runs exactly $n$ iterations and makes one swap for each item that differs from the pivot. It is not stable, and the unknown item that comes from the right end must be inspected before the middle index moves on.
- **Two speeds find a cycle.** The fast and slow pointers meet after $\nu$ steps, the smallest multiple of the cycle length $\lambda$ that is at least $\max(\mu, 1)$, and the full method uses $3\nu + 2\mu + \lambda$ evaluations of $f$ and constant memory.
- **A window needs a monotone property.** The sliding window is correct when its test stays true on every shorter window (for a longest window) or every longer one (for a shortest window). Then the left end $L(r)$ never decreases. A test such as "the sum is even", or a sum bound with negative items, breaks the method.
- **Keep a summary that updates in $O(1)$.** A count table and one counter of missing characters make the test of the [minimum window](/minimum-window-substring-algorithm/) constant time. A maximum cannot be updated when an item leaves, so it needs a [monotonic deque](/sliding-window-maximum-deque/), with at most $2n - 2$ comparisons.

## The scans side by side

| Entry | Pointers | Time | Extra space | Count |
|---|---|---|---|---|
| [Pair search](/two-pointer-pair-search/) | both ends | $\Theta(n)$ | $\Theta(1)$ | at most $n - 1$ iterations |
| [3SUM scan](/three-sum-two-pointer-scan/) | one fixed, two from the ends | $\Theta(n^2)$ | $\Theta(1)$ | at most $(n-1)(n-2)/2$ iterations |
| [Container with most water](/container-with-most-water/) | both ends | $\Theta(n)$ | $O(1)$ | exactly $n - 1$ iterations |
| [Remove duplicates](/remove-duplicates-from-sorted-array/) | read and write | $\Theta(n)$ | $O(1)$ | $n - 1$ comparisons |
| [Sorted intersection](/sorted-array-intersection/) | one per array | $O(m + n)$ | $O(1)$ | at most $m + n - 1$ comparisons |
| [Three-way partition](/dutch-national-flag-algorithm/) | three | $\Theta(n)$ | $\Theta(1)$ | $n$ iterations, $n_< + n_>$ swaps |
| [Fast and slow pointers](/fast-and-slow-pointers/) | two speeds | $O(\mu + \lambda)$ | $O(1)$ | $3\nu + 2\mu + \lambda$ evaluations |
| [Minimum size subarray sum](/minimum-size-subarray-sum/) | window | $\Theta(n)$ | $O(1)$ | at most $2n$ additions and subtractions |
| [Longest distinct substring](/sliding-window-longest-substring/) | window | $\Theta(n + \sigma)$ | $\Theta(\sigma)$ | |
| [Minimum window substring](/minimum-window-substring-algorithm/) | window | $\Theta(n + m + \sigma)$ | $\Theta(\sigma)$ | |
| [Window maximum](/sliding-window-maximum-deque/) | window and deque | $\Theta(n)$ | $\Theta(k)$ | at most $2n - 2$ comparisons |

: The bounds are worst case. The 3SUM scan sorts first, in $O(n \log n)$ time. Here $\sigma$ is the size of the alphabet, $m$ the length of the second array or of the pattern, $k$ the window length, $\mu$ the length of the tail and $\lambda$ the length of the cycle.

## Choosing a scan

- If the input is sorted, or sorting it does not lose what you need, try the scan from both ends before a hash table. It uses constant space.
- If the answer is a contiguous range, write the property of a good window and check that it is down-closed or up-closed before you write the loop. If it is neither, use prefix sums with a search or a monotonic deque over the prefix sums instead.
- If the summary of the window must support removal of an item, use counts. If it must give a maximum or a minimum, use a deque of candidates.
- For "exactly $k$", count "at most $k$" and "at most $k - 1$" and subtract.
- For a cycle in a sequence that you can only step through, use fast and slow pointers. If memory is not a concern, a hash set of visited items is simpler.
