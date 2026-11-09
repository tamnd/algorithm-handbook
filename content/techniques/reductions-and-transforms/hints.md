10. Only (a) and (c) follow. An algorithm runs forward along the reduction, from $B$ to $A$, and a lower bound runs backward, from $A$ to $B$. For element distinctness reduced to sorting, this gives an $O(n \log n)$ algorithm for distinctness, and nothing about a lower bound for it; its $\Omega(n \log n)$ bound needs its own proof in the algebraic decision tree model.

11. The first call says yes, since $4 + 9 = 13$ and $4 + 7 + 2 = 13$. Deleting 4 leaves $(7, 9, 2)$, with no subset of sum 13, so 4 stays. Deleting 7 leaves $4 + 9$, so 7 goes. Deleting 9 leaves $(4, 2)$, so 9 stays. Deleting 2 leaves $(4, 9)$, so 2 goes. The result is $\{4, 9\}$ after $n + 1 = 5$ calls.

12. A clause $(a \lor b)$ gives $\lnot a \to b$ and $\lnot b \to a$. The arcs are $\lnot x_1 \to x_2$, $\lnot x_2 \to x_1$, $x_1 \to x_2$, $\lnot x_2 \to \lnot x_1$, $x_2 \to x_3$, $\lnot x_3 \to \lnot x_2$, $x_3 \to \lnot x_2$, $x_2 \to \lnot x_3$. The cycle $x_2 \to x_3 \to \lnot x_2 \to x_1 \to x_2$ puts $x_2$ and $\lnot x_2$ in one component, so the formula is unsatisfiable.

16. Leaves are `()`. In $T_1$, $a$ is `(()())` and $b$ is `(())`; the first comes first, since they differ at the fourth symbol. So $T_1$ is `((()())(()))`. In $T_2$, $x$ is `(())` and $y$ is `(()())`, and after sorting $T_2$ gets the same code. $T_3$ is `((()()())())`. So $T_1$ and $T_2$ are isomorphic and $T_3$ is not, though all three have 6 nodes.

17. $K = \lfloor \lg 7 \rfloor + 1 = 3$. Phase 1 uses $w_1 = \lfloor w/4 \rfloor = (1, 0, 0, 1, 1)$, so $d_1 = (0, 0, 0, 1)$. Phase 2 uses $w_2 = (3, 1, 1, 2, 3)$; then $r = (3, 1, 1, 0, 1)$, $\delta = (0, 2, 1, 2)$ and $d_2 = (0, 2, 1, 4)$. Phase 3 uses $w$; then $r = (2, 1, 0, 1, 1)$, $\delta = (0, 1, 1, 2)$ and $d_3 = (0, 5, 3, 10)$, which Dijkstra on $w$ confirms.

18. Add a variable $t_i$ with $t_i \ge x_i - c_i$ and $t_i \ge c_i - x_i$, minimize $\sum_i t_i$, and add $x_i \le x_{i+1}$. At an optimum, $t_i = |x_i - c_i|$. For $c = (3, 1, 2)$, $x = (2, 2, 2)$ costs 2. For the bound, $|x_1 - 3| + |x_2 - 1| \ge (3 - x_1) + (x_2 - 1) \ge 2$, since $x_2 \ge x_1$.

19. $G$ has a 4-cycle $0, 1, 2, 3$, a 5-cycle $0, 3, 4, 5, 6$ and the 7-cycle. The distance from $(v, 0)$ to $(v, 1)$ is the length of a shortest odd closed walk through $v$: 5 for $v = 0, 3, 4, 5, 6$, and 7 for $v = 1, 2$, either around the 7-cycle or by one step to 0 or 3, around the 5-cycle and back. The shortest odd cycle has length 5.

20. Put $u^+$ on the left and $v^-$ on the right for each arc $u \to v$. The matching $1^+2^-$, $2^+4^-$, $4^+5^-$ has size 3, and no larger one exists, since $2^+$ and $3^+$ both need $4^-$. The cover has $6 - 3 = 3$ paths: $1, 2, 4, 5$, then $3$, then $6$.

21. Write the bits in the order $a_{12} a_{13} a_{23}$. The path on 3 vertices has the strings 110, 101 and 011 as its middle vertex is 1, 2 or 3, so its form is 011. One edge gives 001, the triangle 111 and the empty graph 000. For $n = 10$ the method tries $10! = 3{,}628{,}800$ relabellings, each with a string of 45 bits.

22. From the ranks of $n$ distinct values, put each value at the position of its rank. This takes $O(n)$ steps and no comparisons, and the result is the sorted order. So every compression algorithm is also a sorting algorithm with the same comparisons, and needs at least $\lceil \lg n! \rceil$ of them in the worst case, which is $\Omega(n \log n)$.

23. Add up the $\binom{n}{2}$ constraints $x_u + x_v \ge 1$. Each $x_v$ appears in $n - 1$ of them, so $(n - 1)\sum_v x_v \ge n(n - 1)/2$, and $\sum_v x_v \ge n/2$, reached by $x = (1/2, \ldots, 1/2)$. An integer cover may leave out at most one vertex, since two left-out vertices would be an uncovered edge, so the integer optimum is $n - 1$. The ratio $2(n - 1)/n$ tends to 2.

24. A cycle cover is a choice of one successor $\sigma(i)$ for each vertex with $i \to \sigma(i)$ an arc and $\sigma$ a permutation. Put $i^+$ on the left and $j^-$ on the right for each arc $i \to j$; a perfect matching is such a $\sigma$. Here $\sigma(1) = 2$ and $\sigma(3) = 4$ are forced, and $\sigma(2), \sigma(4)$ are $1, 3$ or $3, 1$. The two covers are the cycles $(1\,2)(3\,4)$ and the cycle $1, 2, 3, 4$.

25. A maximum flow sends one unit along $s, 1, a, t$ and one along $s, 3, b, t$; its value is 2. In the residual graph, $s$ reaches 2, then $a$, then 1 by the reverse arc, and nothing else, so $S = \{s, 1, 2, a\}$. The cut arcs are $s \to 3$ and $a \to t$, and the cover is $\{3, a\}$, of size 2. Any other maximum flow gives the same $S$.
