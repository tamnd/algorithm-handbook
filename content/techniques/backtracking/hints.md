2. The pruned tree has 25 nodes: 1, 2, 4, 8 and 10 at depths 0 to 4. No node is cut above depth 4, since $2 + 4 + 5 = 11$; at depth 4 the six leaves that take 9 together with 4 or 5 are cut. The solutions are $\{2, 4, 5\}$ and $\{2, 9\}$.

4. The first solution is $(1, 3, 5, 2, 4)$. The search visits the empty prefix, then $(1)$, $(1, 3)$, $(1, 3, 5)$, $(1, 3, 5, 2)$ and the solution: 6 prefixes. It meets no dead end: every prefix it enters on the way extends to this solution, and the failed tests only reject columns that are attacked.

5. Ten calls, with rows and columns numbered from 0 as in the entry. From $(0, 0)$ the search goes right to $(0, 1)$ and down to $(1, 1)$, then down to $(2, 1)$, left to $(2, 0)$ and down to $(3, 0)$, a dead end. The cells $(2, 1)$, $(2, 0)$ and $(3, 0)$ are entered and left again. Back at $(1, 1)$ it goes right to $(1, 2)$ and $(1, 3)$, then down to $(2, 3)$ and $(3, 3)$. The path is RDRRDD.

8. Let $N \le 0$ and $P \ge 0$ be the sums of the negative and of the positive numbers not yet decided. The undecided numbers that an extension takes add at least $N$ and at most $P$, so every extension of the prefix sums to a value between $s + N$ and $s + P$. The test "$s + N \le t \le s + P$" therefore rejects only prefixes with no solution below them.

9. A node at depth $k$ is an ordered choice of $k$ distinct items, and there are $n!/(n-k)!$ of them. Write the sum as $n! \sum_{j=0}^{n} 1/j!$. The rest $n! \sum_{j > n} 1/j!$ is positive and less than $1/(n+1) + 1/(n+1)^2 + \cdots = 1/n \le 1$. For $n = 3$: $1 + 3 + 6 + 6 = 16 = \lfloor 16.31 \rfloor$; for $n = 4$: $65 = \lfloor 65.24 \rfloor$.

11. The rim is a cycle of odd length, so it needs all three colors, and none is left for the hub. Hub first: for each of the 3 colors of $h$ the rim alternates between the two other colors. Each of the 2 values of $v_1$ forces one value each for $v_2$, $v_3$ and $v_4$, and then $v_5$ fails; that is $3 \cdot (1 + 2 + 2 + 2 + 2) = 27$ assignments. Hub last: the rim alone has $3 + 6 + 12 + 24 + 30 = 75$ consistent assignments, and the hub fails under each of the 30 colorings. The degree rule chooses the hub, of degree 5, first.

14. Chronological backtracking tries $X_1 = 1$ and then runs through all $2^{m-2}$ assignments of $X_2, \ldots, X_{m-1}$: that is $2^{m-1} - 2$ values at those levels and one failing try of $X_m$ under each. Then it tries $X_1 = 2$, and the next $m - 1$ values all succeed. The total is $3 \cdot 2^{m-2} + m - 1$, or 28 for $m = 5$. The jumping search tries $m$ values with $X_1 = 1$ and $m$ with $X_1 = 2$, so $2m$ in all.

17. Let $k$ of the 5 marks be odd. A difference is odd exactly when its two marks have different parities, so there are $k(5 - k)$ odd differences, which is 0, 4 or 6. The numbers 1 to 10 contain 5 odd ones, and 5 is not among these values.

18. Assign the root any value of its domain. When the search reaches a variable $X$ with parent $Y$, the only assigned neighbour of $X$ is $Y$, since the other neighbours of $X$ are its children and come later. Arc consistency gives $X$ a value that the constraint with $Y$ allows for the value of $Y$, so $X$ always has a consistent value and the search never backs up.

19. A node $v_k$ at depth $k$ is on the path with probability $p(v_1) \cdots p(v_k)$ and then adds $1/(p(v_1) \cdots p(v_k))$, so each node adds 1 to the expectation. The variance is zero exactly when every child $v$ of a node $u$ is chosen with probability $T(v)/(T(u) - 1)$, where $T$ counts the nodes of a subtree: then $X = T$ on every path, by induction from the leaves.

20. Under an exact test every visited prefix other than the root lies on the path from the root to some solution. The $S$ paths have $n$ nodes each below the root, so their union has at most $1 + nS$ nodes. Before the first solution the search never enters a prefix with no solution below it, so it goes straight down: the root and $n$ more prefixes.
