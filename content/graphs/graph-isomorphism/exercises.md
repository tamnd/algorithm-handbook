1. ◦ The cycle $C_6$ and two disjoint triangles have the same degree sequence, and so do $K_{3,3}$ and the triangular prism. For each pair, find an [invariant](/isomorphism-invariant/) that proves the two graphs are not isomorphic.

2. ◦ Show that the 5-cycle with the edges $01, 12, 23, 34, 40$ is isomorphic to its complement by giving an explicit [isomorphism](/graph-isomorphism-definition/) as a formula in $i$.

3. ◦ Find the order of the [automorphism group](/graph-automorphism-group/) of each of $P_4$, $K_{1,3}$, $C_6$, $K_{2,3}$, $K_{3,3}$ and the cube $Q_3$.

4. ◦ The bull graph is a triangle $a, b, c$ with a pendant vertex $d$ joined to $a$ and a pendant vertex $e$ joined to $b$. Find its automorphism group and its [orbits](/automorphism-orbit/).

5. ◦ The graph $X$ is the path $1, 2, 3, 4, 5$ with a sixth vertex joined to 3 and 4. Show that $X$ is [asymmetric](/asymmetric-graph/).

6. ◦ Encode rooted trees in the AHU style: a leaf is $()$, and an inner vertex is $($, the sorted codes of its children, and $)$. Compute the code of the root for three trees. In $T_1$ the root has children $a$ and $b$, $a$ has children $c$ and $d$, and $b$ has a child $e$. In $T_2$ the root has children $x$ and $y$, $x$ has a child $z$, and $y$ has children $u$ and $v$. In $T_3$ the root has children $a$ and $b$, $a$ has a child $c$, $c$ has a child $d$, and $b$ has a child $e$. Which of the trees are [isomorphic](/ahu-algorithm/)?

7. ◦ The tree $T$ is the path $1, 2, 3, 4, 5$ with a vertex 6 joined to 2, and the tree $T'$ is the same path with 6 joined to 3. Show that they have the same degree sequence, and run [color refinement](/weisfeiler-leman/) on both, starting from colors by degree. After how many rounds do the color histograms differ?

8. ◦ Show that color refinement gives the same stable coloring to $C_6$ and to two disjoint triangles, and likewise to $K_{3,3}$ and the prism. What property of these graphs causes the failure?

9. ◦ A [subgraph isomorphism](/subgraph-isomorphism/) search can count embeddings, that is injective maps that send edges to edges, or subgraphs. How many embeddings of a triangle into $K_4$ are there, and how many triangle subgraphs? How many embeddings of the path on 3 vertices into the Petersen graph, and how many such paths?

10. • Show that if $G \cong H$, then the number of isomorphisms from $G$ to $H$ equals $|\mathrm{Aut}(G)|$. Deduce that the number of graphs on the vertex set $\{1, \ldots, n\}$ isomorphic to $G$ is $n!/|\mathrm{Aut}(G)|$, and check it for $P_4$ and $C_5$.

11. • Use the orbit-stabilizer theorem to compute $|\mathrm{Aut}(Q_3)|$: find the orbit of a vertex and the stabilizer of that vertex in the automorphism group of the cube.

12. • In the Petersen graph, fix a vertex $v$. Show that the partition into $\{v\}$, the three neighbours of $v$ and the remaining six vertices is [equitable](/equitable-partition/), give its quotient matrix, and find the eigenvalues of that matrix.

13. • Use rooting at the [center](/tree-center/) and AHU codes to list the non-isomorphic trees on 6 vertices. How many are there?

14. • Show that subgraph isomorphism is NP-complete by reductions from the clique problem and from the Hamiltonian cycle problem. Why does neither reduction work for the graph isomorphism problem?

15. • Count the 5-cycles of the Petersen graph, first as embeddings of $C_5$ and then as subgraphs.

16. • Let $G_1$ be the paw (a triangle $b, c, d$ with a pendant vertex $a$ joined to $b$) and $G_2$ the path $1, 2, 3, 4$. Find a largest common induced subgraph, as a [maximum common subgraph](/maximum-common-subgraph/) algorithm would by a clique search in the association graph. Then find a largest common subgraph when induced is not required, and compare.

17. • With unit costs and only edge insertions and deletions allowed, compute the [graph edit distance](/graph-edit-distance/) between $C_4$ and $K_{1,3}$.

18. • Sort the 64 labeled graphs on the vertex set $\{1, 2, 3, 4\}$ into isomorphism classes. Check that the class sizes $4!/|\mathrm{Aut}(G)|$ add up to 64. Is any graph on 4 vertices asymmetric?

19. • The [2-dimensional Weisfeiler-Leman](/k-dimensional-weisfeiler-leman/) method colors ordered pairs of vertices. Show that its stable coloring determines the distance between the two vertices of each pair, and conclude that it distinguishes $C_6$ from two disjoint triangles.

20. • Subdivide every edge of a graph once. Show that, for graphs of minimum degree at least 3, $G \cong H$ if and only if their subdivisions are isomorphic. Conclude that isomorphism of bipartite graphs is [GI-complete](/gi-completeness/).

21. • Show that the number of isomorphism classes of graphs on $n$ vertices is at least $2^{\binom{n}{2}}/n!$, and that its logarithm is $\binom{n}{2} - O(n \log n)$.

22. ★ A 3-connected planar graph has essentially one embedding, so its rotation system is fixed up to reflection. Use this to give an $O(n^2)$-time isomorphism test for 3-connected [planar graphs](/planar-graph-isomorphism/) that tries every starting dart.

23. ★ In colored graph isomorphism the vertices carry colors and an isomorphism must preserve them. Reduce colored graph isomorphism to plain graph isomorphism by attaching gadgets to the vertices, and check that the reduction is polynomial.

24. ★ Show that computing the graph edit distance with unit edge costs is NP-hard, by relating the distance from $G$ to a $k$-clique plus $n - k$ isolated vertices to the densest $k$-vertex subgraph of $G$.

25. ★ Let $G$ be a connected graph with maximum degree 3 and let $e$ be an edge. Show that the stabilizer of $e$ in $\mathrm{Aut}(G)$ has order a power of 2. Check the claim on the Petersen graph and on the cube, whose automorphism groups have orders 120 and 48. This is the fact on which [Luks's algorithm](/luks-algorithm/) is built.
