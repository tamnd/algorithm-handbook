1. ◦ A bipartite graph has the left vertices $1, \ldots, 5$, the right vertices $a, \ldots, e$, and the adjacency lists $1: a, b$; $2: a$; $3: b, c, d$; $4: c$; $5: c, e$. Run [Kuhn's algorithm](/kuhn-algorithm/), taking the left vertices and the lists in the order given. For each left vertex, give the augmenting path found and the matching after it.

2. ◦ Run [Hopcroft-Karp](/hopcroft-karp/) on the graph of Exercise 1, scanning in the same orders. How many phases are there, how long are the augmenting paths in each, and what is the final matching?

3. ◦ A bipartite graph has the left vertices $1, 2, 3, 4$, the right vertices $a, b, c, d$, and the edges $1a, 2a, 2b, 3a, 3b, 4b, 4c, 4d$. Find a maximum matching, a set $S$ of left vertices that violates [Hall's condition](/hall-theorem/), and a vertex cover of the same size as the matching, as [Kőnig's theorem](/konig-theorem/) promises.

4. ◦ Solve the [assignment problem](/assignment-problem/) with the cost matrix whose rows are $(7, 3, 6, 9)$, $(5, 8, 4, 6)$, $(6, 5, 9, 4)$ and $(8, 7, 5, 6)$, with the [Hungarian algorithm](/hungarian-algorithm/). Give the assignment, its cost, and row and column potentials that prove it optimal.

5. ◦ Four men $A, B, C, D$ and four women $w, x, y, z$ have the preference lists $A: w, x, y, z$; $B: x, w, z, y$; $C: w, y, x, z$; $D: x, z, w, y$; $w: B, C, A, D$; $x: A, D, B, C$; $y: D, A, B, C$; $z: C, B, D, A$. Run [Gale-Shapley](/gale-shapley/) with the men proposing, taking free men in a queue. Give the proposals in order and the result. Then let the women propose, and compare the two matchings.

6. ◦ On the path with the vertices $1, 2, 3, 4$, show that a [maximal matching](/maximal-matching/) can have half the size of a maximum one. Prove that it can never be smaller than half.

7. ◦ Use [Gallai's identity](/gallai-identity/) to find the size of a [minimum edge cover](/minimum-edge-cover/) of the path on 7 vertices and of the cycle on 7 vertices, and give one cover of each.

8. ◦ In the star $K_{1,3}$, and in the graph made of two triangles joined by one edge, either find a perfect matching or find a set $S$ for which the graph minus $S$ has more than $|S|$ odd components, as in [Tutte's theorem](/tutte-theorem/).

9. ◦ Show that the triangle has a maximum matching of size 1 and a minimum vertex cover of size 2, so Kőnig's theorem fails outside bipartite graphs. Which step of its proof uses bipartiteness?

10. • Find all perfect matchings of the Petersen graph, or at least show that it has one. Show that removing any of them leaves two disjoint 5-cycles, and deduce that the Petersen graph has no proper colouring of its edges with three colours.

11. • A graph has the edges $ab, bc, cd, de, ec, dx$, and the matching is $\{bc, de\}$. Show that a search from the free vertex $a$ that alternates between unmatched and matched edges, never visits a vertex twice and tries $d$ before $e$ at $c$, fails to reach the free vertex $x$. Then find the augmenting path by contracting the [blossom](/blossom/) $c, d, e$.

12. • Three people $A$, $B$, $C$ each rank the other two, with $A$ preferring $B$, $B$ preferring $C$ and $C$ preferring $A$; a fourth person $D$ is ranked last by everyone. Show that this [roommates](/stable-roommates-problem/) instance has no stable matching.

13. • Show that every $k$-regular bipartite graph with $k \ge 1$ has a perfect matching.

14. • Show that the $2 \times n$ grid graph has $F_{n+1}$ perfect matchings, where $F_1 = F_2 = 1$ are the Fibonacci numbers.

15. • Derive Hall's theorem from the max-flow min-cut theorem, using the unit network of bipartite matching.

16. • A path cover of a DAG is a set of vertex-disjoint paths that together contain every vertex. Show that the least number of paths in such a cover is $n$ minus the size of a maximum matching in a bipartite graph with two copies of the vertices.

17. • To find a perfect matching of a complete bipartite graph that minimizes the largest edge cost, sort the costs and binary search with a bipartite matching test. Apply it to the matrix of Exercise 4 and give the answer.

18. • Show that the men-proposing matching in Exercise 5 is the best stable matching for every man by listing all stable matchings of the instance.

19. • Write the [Tutte matrix](/tutte-matrix/) of the 4-cycle $1, 2, 3, 4$ and compute its determinant. Check that it is the square of a polynomial with one term per perfect matching.

20. • A maximum matching $M$ of a bipartite graph is known. Show how to find a [maximum independent set](/bipartite-maximum-independent-set/) in $O(n + m)$ more time.

21. • Turn the [$b$-matching](/b-matching/) problem in a bipartite graph into a maximum flow problem, and say what bound integrality gives.

22. ★ Let $M$ be a matching and $M^*$ a maximum matching in a bipartite graph, and let the shortest augmenting path for $M$ have length $\ell$. Show that $|M^*| - |M| \le n/\ell$. Use this to prove that Hopcroft-Karp needs only $O(\sqrt{n})$ phases.

23. ★ Show that the edges of a $k$-regular bipartite graph split into $k$ perfect matchings. Deduce that every bipartite graph of maximum degree $\Delta$ has a proper edge colouring with $\Delta$ colours.

24. ★ In a stable matching instance where preference lists may be incomplete, show that the same people are matched in every stable matching.

25. ★ Build a cubic graph with 16 vertices that has no perfect matching, and explain why it does not contradict [Petersen's theorem](/petersens-theorem/).
