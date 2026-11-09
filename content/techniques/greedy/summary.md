## What to remember

- **A greedy algorithm** sorts the candidates by a key, or keeps them in a priority queue, and accepts each one that still fits. It is correct when the problem has the [greedy-choice property](/greedy-choice-property/), some optimal solution contains the greedy choice, and optimal substructure, the rest is an optimal solution of a smaller instance.
- **An exchange argument** turns an optimal solution into the greedy one by swaps that never make it worse. For adjacent jobs $a, b$ in Smith's problem the swap changes the cost by exactly $w_a p_b - w_b p_a$, and each swap removes one inversion, so at most $\binom{n}{2}$ swaps are needed.
- **Greedy stays ahead** picks a measure $f_k$ of progress after $k$ steps and proves $f_k(G) \ge f_k(O)$ by induction for every solution $O$.
- **Intervals.** Earliest finish time first gives a largest set of disjoint intervals in $\Theta(n \log n)$ time. The fewest resources that hold all intervals equal the depth $d(S)$, the largest number of intervals with a common point, and greedy by start time with a min-heap reaches it.
- **Divisible items and merges.** The fractional knapsack takes items by $v_i / w_i$, with at most one item cut. Its value bounds the 0-1 optimum $z$ by $z_{LP} \le z + \max_i v_i$. Merging the two smallest files is optimal, with cost $\sum_i q_i \ell_i$ for file sizes $q_i$ at depths $\ell_i$ of the merge tree, the same sum that Huffman's code minimizes.
- **Coins.** Paying largest coin first is optimal only for canonical systems. If a system with $n$ coins is not canonical, its smallest counterexample $x$ satisfies $c_3 + 1 < x < c_n + c_{n-1}$, and Pearson's test decides canonicity in $O(n^3)$ time.
- **One machine.** Smith's rule orders jobs by $p_j / w_j$ and minimizes $\sum w_j C_j$; tape storage is the same problem. Earliest due date first minimizes $L_{\max} = \max_k \bigl(\sum_{i \le k} p_i - d_k\bigr)$. Moore-Hodgson keeps due date order and drops the longest kept job whenever one is late, which maximizes the number of on-time jobs.
- **Matroids.** A matroid is a family of sets closed under subsets in which a smaller set can always grow by an element of a larger one. The greedy algorithm finds a maximum-weight independent set for every nonnegative weighting exactly when the family is a matroid, in $O(n \log n + n f)$ time with $f$ the cost of one independence test.

## The greedy rules side by side

| Problem | Greedy key | Proof | Time |
|---|---|---|---|
| [Activity selection](/activity-selection/) | earliest finish time | stays ahead or exchange | $\Theta(n \log n)$ |
| [Interval partitioning](/interval-partitioning/) | earliest start, resource free first | depth is a lower bound | $O(n \log n)$ |
| [Fractional knapsack](/fractional-knapsack/) | largest $v_i / w_i$ | exchange, LP duality | $O(n \log n)$; $O(n)$ by weighted median |
| [Optimal merge pattern](/optimal-merge-pattern/) | two smallest sizes | exchange in the merge tree | $O(n \log n)$; $O(n)$ if sorted |
| Coin change, [canonical systems](/canonical-coin-system/) | largest coin that fits | holds only if canonical | canonicity test $O(n^3)$ |
| [Weighted completion time](/smith-rule/) | smallest $p_j / w_j$ | adjacent exchange | $\Theta(n \log n)$ |
| [Maximum lateness](/minimizing-maximum-lateness/) | earliest due date | exchange of inversions | $O(n \log n)$ |
| [Number of late jobs](/minimizing-number-of-late-jobs/) | due date, drop the longest | induction on a stronger invariant | $O(n \log n)$ |
| [Maximum-weight basis](/matroid-greedy-algorithm/) | largest weight | matroid greedy theorem | $O(n \log n + n f)$ |
| [Job sequencing](/job-sequencing-with-deadlines/) | largest profit, latest free slot | matroid greedy theorem | $O(n \log n)$ |

: Worst-case times in the comparison model. Here $n$ is the number of items and $f$ the time of one independence test.

## Choosing a method

- Before proving anything, try a few keys on small instances. If a key fails on five items, no proof will save it.
- If the solution is a sequence and the cost changes in a simple way when two neighbours swap, use an exchange argument on adjacent pairs. If the solution is a set chosen step by step and there is a natural measure of progress, use greedy stays ahead.
- If the feasible sets are closed under subsets and every weighting must work, check the augmentation axiom. When it holds, the matroid greedy theorem gives the proof at once, as for spanning trees and unit jobs with deadlines.
- If the problem needs whole items, the greedy key of the divisible version gives a bound, not an answer. Use dynamic programming or [branch and bound](/knapsack-branch-and-bound/) for the optimum.
