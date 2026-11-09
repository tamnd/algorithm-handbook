## What to remember

- **Divide and conquer** has three steps: divide an instance into smaller instances of the same problem, conquer them by recursion, and combine their answers. With $a$ parts of size $n/b$ and a divide-plus-combine cost $f(n)$, the running time is $T(n) = aT(n/b) + f(n)$.
- **Correctness is a strong induction on the size.** The base case must be right, each part must be a valid and strictly smaller instance, and the combine step must turn right answers for the parts into a right answer for the whole. Often the claim must be made stronger than the goal, as when counting inversions also returns the sorted array.
- **The recurrence tells where the work is.** In the leaves when $n^{\log_b a}$ dominates $f(n)$ (Karatsuba, $\Theta(n^{\log_2 3})$), evenly over the $\log_b n$ levels when they balance (merge sort, $\Theta(n \log n)$), at the root when $f(n)$ dominates. A split into fixed fractions whose sizes add up to less than $n$, as in median of medians, gives linear time.
- **Overlapping parts make the method exponential.** The naive Fibonacci recursion makes $2F(n+1) - 1$ calls. When the parts share subproblems, store their answers: that is [memoization](/memoization/), and the method becomes dynamic programming.
- **Decrease and conquer** solves one smaller instance. $T(n) = T(n-1) + f(n)$ is the sum $c + \sum_{i=1}^{n} f(i)$, linear for constant $f$ and quadratic for linear $f$. $T(n) = T(\lfloor n/2 \rfloor) + d$ is exactly $c + d \lfloor \log_2 n \rfloor$. $T(n) = T(n/2) + \Theta(n)$ is linear, because the top step dominates. When the extension only passes the answer up, the recursion is a loop, as in binary search.
- **Offline, the recursion can run over time.** Divide and conquer over time stores an item that lives on $[s, t]$ at $O(\log q)$ nodes of a segment tree over the $q$ operations, so a structure with worst-case add and undo in $T(n)$ gets deletions at a cost of $O(T(n) \log q)$ per item. With [union-find with rollback](/union-find-with-rollback/) this answers connectivity queries under edge insertions and deletions in $O(q \log q \log n)$ time.
- **CDQ divide and conquer** adds the effect of every update in the left half to every query in the right half in one static sweep. Each pair (earlier update, later query) is handled in exactly one call, and the total is $O(n \log^2 n)$ with a sort in each sweep, or $O(n \log n)$ with a merge.

## The recurrences side by side

| Algorithm | Kind | Recurrence | Cost |
|---|---|---|---|
| [Binary search](/binary-search/) | decrease by half | $T(n/2) + \Theta(1)$ | $\Theta(\log n)$ |
| [Exponentiation by squaring](/binary-exponentiation/) | decrease by half | $T(n/2) + \Theta(1)$ | $\Theta(\log n)$ multiplications |
| [Insertion sort](/insertion-sort/), worst case | decrease by one | $T(n-1) + \Theta(n)$ | $\Theta(n^2)$ |
| [Euclid's algorithm](/euclidean-algorithm/) | variable decrease | data dependent | $O(\log \min(m, n))$ steps |
| [Quickselect](/quickselect/), random pivot | variable decrease | data dependent | $\Theta(n)$ expected, $\Theta(n^2)$ worst |
| [Median of medians](/median-of-medians/) | two unequal parts | $T(n/5) + T(7n/10) + O(n)$ | $\Theta(n)$ |
| [Merge sort](/merge-sort/) | two halves | $2T(n/2) + \Theta(n)$ | $\Theta(n \log n)$ |
| [Karatsuba multiplication](/karatsuba-multiplication/) | three halves | $3T(n/2) + \Theta(n)$ | $\Theta(n^{\log_2 3})$ |
| [Strassen's algorithm](/strassen-algorithm/) | seven halves | $7T(n/2) + \Theta(n^2)$ | $\Theta(n^{\log_2 7})$ |
| CDQ, sort in the sweep | two halves of time | $2T(n/2) + O(n \log n)$ | $O(n \log^2 n)$ |

: The costs are worst case unless the line says otherwise. Here $\log_2 3 \approx 1.585$ and $\log_2 7 \approx 2.807$.

## Choosing a method

- If one part of the input is enough to answer the question, use decrease and conquer, and prefer a decrease by a constant factor to a decrease by one: squaring instead of repeated multiplication, binary search instead of a scan.
- If the answer needs several parts, check before you write the code that the parts do not overlap. If they do, use dynamic programming.
- Make the combine step cheaper than the work in the parts. A linear combine with two halves gives $\Theta(n \log n)$; a quadratic combine gives nothing over a direct quadratic method.
- Stop the recursion at a cut-off of a few dozen items and use a simple method below it, and recurse on the smaller part first when the split may be uneven, so that the stack stays short.
- For an offline sequence of operations with deletions that your structure cannot do, use divide and conquer over time, with a structure whose add has a worst-case bound. For contributions of earlier updates to later queries, use CDQ.
