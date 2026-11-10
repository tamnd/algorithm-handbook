1. The string is $01010110$: $f$ is 1 at $a = 1, 3, 5, 6$, so it has 4 models.

2. $f|_{x_2=0} = x_1$ and $f|_{x_2=1} = x_1 \oplus x_3$. Their XOR is $x_3$, which is not the constant 0, so $f$ depends on $x_2$.

4. In the order $x_1, x_2, x_3$ the root tests $x_1$; its low child is the node of $x_3$ and its high child the node of $x_2$, each with children 0 and 1: 5 nodes. In the order $x_2, x_3, x_1$ the two cofactors by $x_2$ are $\neg x_1 \wedge x_3$ and $x_1 \vee x_3$; they need two $x_3$ nodes, and below them two $x_1$ nodes, one for $x_1$ and one for $\neg x_1$: 7 nodes.

5. The high edge of the root goes to 1 and skips $x_2$ and $x_3$, so it counts $2^2 = 4$ models. The low edge goes to the $x_3$ node and skips $x_2$, so it counts $2 \cdot 1 = 2$. The total is 6, and indeed only the two inputs with $x_1 = x_3 = 0$ are not models.

6. One, three and $n + 2$.

8. $\exists x_2\, f = f|_{x_2=0} \vee f|_{x_2=1} = x_3 \vee x_1$, and $\forall x_2\, f = x_1 \wedge x_3$.

9. In the interleaved order each pair needs one $x_i$ node and two $y_i$ nodes, so the size is $3n + 2$. In the other order the $x$ levels form a complete tree with $2^n - 1$ nodes, because the $x$ values must all be remembered, and level $y_j$ has $2^{n-j+1}$ nodes, one per value of $x_j, \ldots, x_n$. The total is $3 \cdot 2^n - 1$.

11. Write nodes as (variable, low child, high child). The result is the root $(x_1, P, Q)$ with $P = (x_2, 0, (x_3, 1, 0))$ and $Q = (x_2, (x_3, 0, 1), 0)$: five inner nodes and two terminals, 7 in all. Its two models are $x_1x_2x_3 = 010$ and $101$.

13. The ZDD has a root for element 1 whose high edge goes to the terminal 1 (the set $\{1\}$) and whose low edge goes to a node for element 3 with children 0 and 1: 4 nodes. The ROBDD must test every absent element on both paths: 6 inner nodes and 8 nodes in all.

14. One node per level and the terminal 1: $n + 1$ nodes. Each node stands for the parity of $x_i, \ldots, x_n$ or its complement, whichever makes its then-edge regular, and the other polarity is reached by a complemented edge.

16. 37. An assignment is not a model when no pair is $11$; each pair then has 3 values, so there are $2^6 - 3^3 = 64 - 27 = 37$ models.

17. While the pairs read so far are equal, the remaining function is the same, so each level $x_i$ has one node. Level $y_i$ has two: after $x_i = 0$ it is 0 or continues, after $x_i = 1$ it is 1 or continues. At the last pair "continue" means 0, so the node after $x_n = 0$ is the constant 0 and disappears. That gives $3(n-1) + 2$ inner nodes and two terminals.

18. With the address first, the address levels form a complete tree of $2^k - 1$ nodes, each path selects one data bit, and each data bit needs one node: $2^{k+1} - 1$ inner nodes. With the data first, fixing all data bits leaves the function $a \mapsto d_a$, which can be any of the $2^{2^k}$ functions of the address; distinct subfunctions need distinct nodes.

19. Take the top $m$ levels, with at most $2^m - 1$ nodes, and the rest, with at most $2^{2^{n-m}}$ nodes because the bounds of Exercise 15 telescope. Choose $m = n - \lfloor \lg(n - \lg n) \rfloor$; then both parts are $O(2^n / n)$.

20. By the [canonicity](/bdd-canonicity/) argument, the nodes on the level of $x_i$ are in one-to-one correspondence with the distinct subfunctions of $f$, obtained by fixing all variables above, that depend on $x_i$. That set of subfunctions depends only on which variables are fixed. So the cost of putting a set $S$ of variables on top, in the best order, satisfies $c(S) = \min_{x \in S} \bigl( c(S \setminus \{x\}) + \mathrm{nodes}(x, S \setminus \{x\}) \bigr)$, a recursion over the $2^n$ subsets.

21. A node is determined by the next element $i$ and the number $r \ge 1$ of elements still to choose; it stands for the $r$-subsets of $\{i, \ldots, n\}$. Such a node exists when $r \le n - i + 1$ and $k - r \le i - 1$. For each $r = 1, \ldots, k$ there are $n - k + 1$ values of $i$, and all these families are different and reachable from the root.
