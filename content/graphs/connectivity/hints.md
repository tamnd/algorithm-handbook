1. Discovery times are $1, \ldots, 10$ for $0, \ldots, 9$. Low-links: $1, 1, 1, 4, 4, 4, 7, 7, 7, 10$. Bridges: $23$, $46$, $89$, each a tree edge $uv$ with $\mathrm{low}(v) > d(u)$. Articulation points: $2, 3, 4, 6, 8$, each with a child $v$ that has $\mathrm{low}(v) \ge d(u)$; the root 0 has one child.

2. Blocks $\{0, 1, 2\}$, $\{2, 3\}$, $\{3, 4, 5\}$, $\{4, 6\}$, $\{6, 7, 8\}$, $\{8, 9\}$. With five cut vertices the tree has 11 nodes and 10 edges.

3. Finishing order $f, e, d, c, g, h, b, a$. Components in order: $\{a, b, c\}$, $\{g, h\}$, $\{d, e\}$, $\{f\}$.

4. $\{f\}$, $\{d, e\}$, $\{g, h\}$, $\{a, b, c\}$: a reverse topological order of the condensation, while Kosaraju-Sharir finds them in a topological order.

5. The condensation has the arcs $abc \to de$, $abc \to gh$, $de \to f$, $gh \to f$. Its topological orders are $abc, de, gh, f$ and $abc, gh, de, f$.

6. The closure adds $1 \to 4$, $2 \to 5$ and $3 \to 5$ to the given arcs. The reduction is the path $1 \to 2 \to 3 \to 4 \to 5$.

7. Merging: $01, 23, 13, 45, 67, 56$. Redundant: $02, 12$. Components $\{0, 1, 2, 3\}$ and $\{4, 5, 6, 7\}$. Each merge lowers the number of sets by one, from $n$.

8. Tree arcs $0 \to 1 \to 2 \to 5 \to 4 \to 3$, back arcs $4 \to 1$ and $3 \to 0$. The cycle $0, 1, 2, 5, 4, 3, 0$ passes through every vertex.

9. $\kappa = 1$ (the shared vertex), $\lambda = 3$, $\delta = 3$.

13. Take $a \to b$, $b \to a$, $b \to c$, with the first search from $a$. The vertex $c$ finishes first and $a$ last.

14. The first two clauses force $x$, and the implication graph contains the paths $\lnot x \to y \to x$ and $x \to z \to \lnot x$.

17. Between two components, all arcs go the same way, and every pair of components has at least one arc.

22. Each new arc can give an incoming arc to at most one source and an outgoing arc to at most one sink.

24. Each $F_i$ has at most $n - 1$ edges. If a cut of $G$ has at least $k$ edges but the union has fewer, some edge $e$ of $G$ across the cut is in no $F_i$. By the maximality of $F_i$, the ends of $e$ are joined in $F_i$, so $F_i$ crosses the cut; the $k$ forests are disjoint.

25. Add a new vertex joined to all of $U$, and apply Menger's theorem between $x$ and it.
