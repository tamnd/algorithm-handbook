1. ◦ The graph $G$ has the vertices $a, \ldots, g$ and the weighted edges $ab$ 7, $ad$ 5, $bc$ 8, $bd$ 9, $be$ 4, $ce$ 3, $de$ 15, $df$ 6, $ef$ 10, $eg$ 12, $fg$ 11. Run [Kruskal's algorithm](/kruskal/). List the edges in the order they are examined, say which are kept, and give the weight of the tree.

2. ◦ Run [Prim's algorithm](/prim/) on the graph $G$ of Exercise 1, starting at $a$. Give the edges in the order they join the tree.

3. ◦ Run [Borůvka's algorithm](/boruvka/) on $G$. For each round, give the cheapest edge leaving each component and the components after the round.

4. ◦ Let $T$ be the minimum spanning tree of $G$ found in Exercise 1. Give the [fundamental cycle](/fundamental-cycle/) of each of the five non-tree edges, and check that each non-tree edge is the heaviest edge on its cycle.

5. ◦ Run [reverse-delete](/reverse-delete/) on $G$. Which edges are deleted, and which heavy edge is kept because removing it would disconnect the graph?

6. ◦ Every spanning tree of $G$ contains an edge of weight at least 11. Explain why from the edges at $g$, and conclude that the tree of Exercise 1 is a [minimum bottleneck spanning tree](/minimum-bottleneck-spanning-tree/).

7. ◦ Use the [matrix-tree theorem](/matrix-tree-theorem/) to count the spanning trees of the graph on $\{a, b, c, d\}$ with the edges $ab, bc, cd, da, ac$. Check the answer by listing the trees.

8. ◦ Find the [second-best spanning tree](/second-best-mst/) of $G$ and its weight.

9. ◦ A directed graph has a root $r$ and the arcs $r \to a$ 5, $r \to b$ 7, $r \to c$ 8, $a \to b$ 2, $b \to c$ 1, $c \to a$ 3. Run [Edmonds' algorithm](/edmonds-arborescence/): pick the cheapest arc into each of $a, b, c$, contract the cycle they form, adjust the costs of the arcs that enter it, and expand. Give the minimum arborescence and its cost.

10. • Show that every minimum spanning tree is a minimum bottleneck spanning tree. Then give a graph with a minimum bottleneck spanning tree that is not a minimum spanning tree.

11. • Let $f$ be a strictly increasing function on the reals. Show that a spanning tree is minimum for the weights $w$ if and only if it is minimum for the weights $f(w)$. Deduce that a minimum spanning tree also minimizes the product of the weights when all weights are positive.

12. • A new edge $uv$ of weight $w$ is added to a graph whose minimum spanning tree $T$ is known. Show how to find a minimum spanning tree of the new graph in $O(n)$ time.

13. • The weight of one edge $e$ changes, and $T$ was a minimum spanning tree before the change. In which of the four cases (tree edge or not, weight up or down) does $T$ stay minimum? For each other case, show how to repair $T$ in $O(m)$ time.

14. • All weights are integers in $\{1, \ldots, W\}$ with $W = O(m)$. Make Kruskal's algorithm run in $O(m \, \alpha(m, n))$ time.

15. • Implement Prim's algorithm with an array of keys instead of a heap, and show that it runs in $\Theta(n^2)$ time. For which densities $m$ is this better than the binary-heap version?

16. • Show that each round of Borůvka's algorithm at least halves the number of components. Then give a triangle with equal weights on which the rounds go wrong if ties are broken carelessly, and state a tie-break that fixes it.

17. • To split a set of points into $k$ clusters, run Kruskal on the complete graph of distances and stop when $k$ components remain. Prove that this maximizes the spacing, the least distance between points in different clusters.

18. • Two vertices are joined by three internally disjoint paths with $p$, $q$ and $r$ edges. Show that the graph has $pq + qr + rp$ spanning trees.

19. • Use the [Nash-Williams arboricity theorem](/nash-williams-arboricity-theorem/) to show that the [arboricity](/arboricity/) of $K_n$ is $\lceil n/2 \rceil$, and that the arboricity of a simple planar graph is at most 3.

20. • A connected graph has $n$ vertices and exactly $n$ edges, with distinct weights. Find its minimum spanning tree in $O(n)$ time.

21. • For a [Steiner tree](/steiner-tree-problem/) instance, take a wheel: a centre $c$ joined to $k$ terminals $t_1, \ldots, t_k$ by spokes of weight 1, and the rim edges $t_i t_{i+1}$ for $1 \le i < k$ of weight $2 - \varepsilon$. The centre is the only vertex that is not a terminal. Compute what the [Kou-Markowsky-Berman](/kou-markowsky-berman/) method returns and the optimum, and show that the ratio tends to 2.

22. ★ Show that an edge $e = uv$ of weight $w$ lies in some minimum spanning tree if and only if $u$ and $v$ are not joined by a path of edges lighter than $w$, and in every minimum spanning tree if and only if they are not joined by a path of edges of weight at most $w$ that avoids $e$. Use this to classify all edges in $O(m \log m)$ time.

23. ★ The Laplacian of $K_n$ has the eigenvalue 0 once and the eigenvalue $n$ with multiplicity $n - 1$. Derive Cayley's formula $n^{n-2}$ from this and the matrix-tree theorem.

24. ★ Use the [Nash-Williams-Tutte theorem](/nash-williams-tutte-theorem/) to show that every $2k$-edge-connected graph contains $k$ edge-disjoint spanning trees.

25. ★ Show that Borůvka's algorithm, with each round contracting the chosen edges and removing loops and parallel edges, runs in $O(n)$ time on planar graphs.

26. ★ For directed graphs, consider the rule that grows an arborescence from $r$ by adding the cheapest arc that leaves the current tree. Find a graph with three vertices where this rule fails, and explain which step of the proof of Prim's algorithm breaks.
