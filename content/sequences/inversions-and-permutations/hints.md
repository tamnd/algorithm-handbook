1. The cycles are $(1\,2\,4\,3)(5\,6)$ and the inverse is $3\,1\,4\,2\,6\,5$. There are 4 inversions, $(2,1)$, $(4,1)$, $(4,3)$ and $(6,5)$ as pairs of values. The descents are at positions 2 and 5, so the major index is 7. The sign is $+1$: 4 inversions is even, and so is $n - c = 6 - 2$.

3. The reversal has $\binom n2$ inversions. Its cycles are $\lfloor n/2 \rfloor$ swaps $(i\ \ n+1-i)$, plus a fixed point when $n$ is odd, so $n - c = \lfloor n/2 \rfloor$. Both numbers are even exactly when $n \bmod 4$ is 0 or 1.

5. $2026 = 2 \cdot 6! + 4 \cdot 5! + 4 \cdot 4! + 1 \cdot 3! + 2 \cdot 2! + 0 \cdot 1!$, so the digits are $2\,4\,4\,1\,2\,0$. With a final 0, the Lehmer code $(2, 4, 4, 1, 2, 0, 0)$ gives $3\,6\,7\,2\,5\,1\,4$, which has $2 + 4 + 4 + 1 + 2 = 13$ inversions.

8. A stack can produce every permutation of $[3]$ except $3\,1\,2$: once 3 is out, 1 and 2 are still in the stack with 2 on top. It can sort every permutation except $2\,3\,1$: the 2 must stay in the stack until 1 comes out, but the 3 comes next, must be pushed on top of the 2, and must leave after it.

10. With the items numbered by the first ranking, the second reads $3\,1\,2\,5\,4$. The footrule is $1 + 1 + 2 + 1 + 1 = 6$. The cycles are $(1\,3\,2)(4\,5)$, so the Cayley distance is $5 - 2 = 3$. The longest increasing subsequence has length 3, so the Ulam distance is 2. Both bounds hold with equality: $3 + 3 = 6 = 2 \cdot 3$.

12. A descent is an inversion between neighbours. Equality means that every inversion is between neighbours, and then no item moves more than one place. Such permutations are made of disjoint swaps of neighbours, like $2\,1\,3\,5\,4$. Their number satisfies $f(n) = f(n-1) + f(n-2)$, which gives the [Fibonacci numbers](/fibonacci-numbers/).

14. There are $n(n-1)\cdots(n-k+1)/k$ possible cycles of length $k$. Each one is a cycle of a random permutation with probability $(n-k)!/n!$, because the other $n - k$ items may go anywhere among themselves. The sum over $k$ is the harmonic number $H_n$.

17. A stack never looks at the values it moves. If a run of pushes and pops turns $1, 2, \ldots, n$ into $\pi$, the same run turns any relabeling of the input into the same relabeling of $\pi$. Relabel each value $v$ as $\pi^{-1}(v)$.

19. A step rewrites the last $k$ positions when the last $k - 1$ items are decreasing and the last $k$ are not. Count the permutations of each kind. The average is $\sum_{j=0}^{n-2} 1/j!$, up to the factor $n!/(n!-1)$, so it tends to $e$.

20. A swap of two equal neighbours leaves the sequence as it was, so a shortest solution never makes one. Then equal items never pass each other, and the $k$-th copy of a value in $a$ must end where the $k$-th copy is in $b$. Count the inversions with a [Fenwick tree](/inversion-count-with-fenwick-tree/).

21. If $a_i < a_j$, the swap adds $2m + 1$ inversions, where $m$ is the number of positions strictly between $i$ and $j$ with values strictly between $a_i$ and $a_j$. If $a_i > a_j$, it removes $2m + 1$. So each swap needs one count of points in a rectangle, with points that move. A Fenwick tree over positions whose cells hold [order-statistic trees](/order-statistic-tree/) of values answers and updates in $O(\log^2 n)$ time.

22. Inserting $n$ at the end adds 0. Number the gaps inside descents from right to left $1, 2, \ldots, d$, and the other gaps, including the front, from left to right $d + 1, \ldots, n - 1$. Check that inserting $n$ in the gap numbered $t$ adds exactly $t$ to the major index. The inversion count obeys the same recurrence, because inserting $n$ with $t$ items after it adds $t$ inversions.

23. Avoiding both patterns means that no item is followed by two larger items. So the item 1 is last or next to last, and the rest is again such a permutation. This gives $f(n) = 2f(n-1)$ for $n \ge 2$.

24. Bring to the front the smallest of the first $K + 1$ items, pay its distance from the front, and repeat on the rest with the budget that is left. Moving one item forward does not change the order of the others. Keep the remaining items in a Fenwick tree over their original positions to find each window, and a [segment tree](/segment-tree/) to find the smallest item in it.
