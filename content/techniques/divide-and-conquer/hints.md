2. Six for $a^{25}$: the exponents are $1, 3, 6, 12, 25$, with four squarings and two products by $a$, since $25 = 11001_2$ has three 1 bits. Five for $a^{32}$: the exponents are $1, 2, 4, 8, 16, 32$, all squarings.

4. The chain is $100, 50, 25, 12, 6, 3, 1$. From the bottom: $J(1) = 1$, $J(3) = 3$, $J(6) = 5$, $J(12) = 9$, $J(25) = 19$, $J(50) = 37$, $J(100) = 73$. The closed form $2(100 - 64) + 1 = 73$ agrees.

5. For $[2, 7]$: the nodes $[2, 2]$, $[3, 4]$, $[5, 6]$ and $[7, 7]$. For $[3, 6]$: $[3, 4]$ and $[5, 6]$. For $[1, 8]$: the root alone.

7. The lifetimes are 1-2 on $[1, 3]$, 2-3 on $[2, 6]$ and 3-4 on $[6, 8]$. Edge 1-2 is stored at $[1, 2]$ and $[3, 3]$; edge 2-3 at $[2, 2]$, $[3, 4]$ and $[5, 6]$; edge 3-4 at $[6, 6]$ and $[7, 8]$. The answers are yes (at time 3 the edges are 1-2 and 2-3), no (at time 5 only 2-3 is present) and no (at time 8 only 3-4 is present).

10. Each call either returns 1 at a base case or makes exactly two calls, and the value of a call is the number of base cases below it. A tree in which every inner node has two children and which has $L$ leaves has $2L - 1$ nodes. For $\binom{10}{5} = 252$ the procedure makes 503 calls but meets only 35 distinct pairs $(n', k')$: the subproblems overlap, and a table of 35 entries does the same work.

12. Compare $A[i]$ and $B[j]$ with $i + j = k$ and $i$ about $k/2$. If $A[i] < B[j]$, the items $A[1..i]$ are all among the $k - 1$ smallest, so drop them and look for the $(k - i)$-th smallest of the rest. Each step halves $k$ or the range of one array.

13. The global minimum is a local minimum. Keep a range $[lo, hi]$ such that $A[lo]$ is smaller than its left neighbour (if any) and $A[hi]$ is smaller than its right neighbour (if any). Compare $A[mid]$ with $A[mid + 1]$ and keep the side of the smaller one; the invariant holds on that side, and a range with this property contains a local minimum of $A$.

18. With groups of 7, at least half of the about $n/7$ medians are at most the pivot, and each such group gives 4 items at most the pivot, so about $2n/7$ items lie on each side and the larger side has at most about $5n/7$. Since $1/7 + 5/7 = 6/7 < 1$, the recursion tree sums to $O(n)$. With groups of 3, each group gives 2 items, so the larger side may hold $2n/3$ items, and $1/3 + 2/3 = 1$: every level of the tree costs $\Theta(n)$ and there are $\Theta(\log n)$ levels.

19. Any two points on the same side of the line are at least $\delta$ apart. Cover the rectangle of width $2\delta$ and height $\delta$ that starts at a point $p$ and extends upward with eight squares of side $\delta/2$. Each square holds at most one point, since its diagonal is $\delta/\sqrt{2} < \delta$, so at most 7 other points can be within $\delta$ of $p$ above it.

20. Read the pieces as the coefficients of two polynomials of degree 2. Their product has degree 4, so its 5 coefficients are fixed by its values at 5 points, such as $0, 1, -1, 2$ and infinity. Evaluating at these points and interpolating takes linear work with fixed small constants, and the 5 values are 5 products of numbers of about $n/3$ digits. The solution is $\Theta(n^{\log_3 5})$, with $\log_3 5 \approx 1.465$, less than Karatsuba's $\log_2 3 \approx 1.585$.

21. Store at each node the parity of the path to its parent; the parity of a vertex relative to its root is the sum of the parities on its path, mod 2. To add edge $u$-$v$, find both roots and parities. If the roots differ, link one under the other with the parity that makes $u$ and $v$ differ. If they are equal and the parities are equal, the edge closes an odd cycle: increase a counter of such edges. The graph is bipartite while the counter is 0. The undo record holds the changed parent pointer, parity and rank, or the change of the counter. The answers are: not bipartite at time 4 (the triangle 1-2-3), bipartite at time 6.
