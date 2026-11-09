1. ◦ In the graph with the vertices $1, \ldots, 5$ and the edges $12, 23, 34, 45, 51, 13$, classify each sequence as a [walk](/walk/), a [trail](/trail/), a [simple path](/simple-path/), a [simple cycle](/simple-cycle/) or none of these: $1, 2, 3, 1, 5$; $1, 3, 2, 1, 3$; $2, 3, 4, 5$; $1, 3, 4, 5, 1$; $1, 2, 4$; $3, 1, 2, 3, 4, 5, 1, 3$.

2. ◦ The diamond graph has the vertices $a, b, c, d$ and the edges $ab, ac, bc, bd, cd$. Compute $A^2$ and $A^3$ for its adjacency matrix, and read off the number of walks of length 3 from $a$ to $d$ and from $a$ to $b$. List the walks of length 3 from $a$ to $d$. See [counting walks](/counting-fixed-length-paths/).

3. ◦ A directed graph has the arcs $1 \to 2$, $1 \to 3$, $2 \to 4$, $3 \to 4$, $5 \to 1$, $5 \to 6$, $6 \to 7$, $7 \to 3$, $7 \to 5$. Run [DFS-based cycle detection](/dfs-cycle-detection/), starting new searches at the smallest white vertex and scanning arcs in the order listed. Classify every arc as tree, back, forward or cross, and give the cycle found.

4. ◦ A graph has the vertices $1, \ldots, 6$ and the edges $12, 13, 23, 24, 25, 34, 35, 45, 46, 56$. Use [Euler's theorem](/eulers-theorem-eulerian-graphs/) to decide whether it has an Eulerian circuit. Then delete the edge $23$ and decide again, this time for an Eulerian path, with its two possible ends.

5. ◦ Run [Hierholzer's algorithm](/hierholzer-algorithm/) on the graph of Exercise 4, starting at vertex 1 and always leaving a vertex by the unused edge to the smallest neighbour. Give the first closed tour, where it gets stuck, and the final circuit.

6. ◦ A graph has the vertices $a, b, c, d$ and the weighted edges $ab$ 3, $bc$ 2, $cd$ 4, $da$ 1, $ac$ 5, $bd$ 6. Solve the [Chinese postman problem](/chinese-postman-problem/): find the odd vertices, the shortest-path distances between them, the best pairing, and the length of the shortest closed walk through every edge.

7. ◦ A DAG has the weighted arcs $s \to a$ 3, $s \to b$ 2, $a \to c$ 4, $b \to c$ 6, $a \to d$ 2, $c \to d$ 1, $c \to t$ 3, $d \to t$ 5. Compute the [longest path](/dag-longest-path/) from $s$ to each vertex in topological order, and give a longest path to $t$.

8. ◦ A DAG has the vertices $1, \ldots, 6$ and the arcs $1 \to 2$, $1 \to 3$, $2 \to 4$, $3 \to 4$, $3 \to 6$, $4 \to 5$, $4 \to 6$. Build the split bipartite graph, find a maximum matching, and read off a [minimum path cover](/path-cover-by-bipartite-matching/).

9. ◦ Run breadth-first search from vertex 0 of the Petersen graph, whose edges are the outer cycle $0, 1, 2, 3, 4$, the spokes $i, i + 5$, and the inner edges $5\,7, 7\,9, 9\,6, 6\,8, 8\,5$. Give the layers. Which non-tree edges are there, and what does each one say about the [girth](/girth/)?

10. • Prove that every walk from $u$ to $v$ contains a simple path from $u$ to $v$, and that every closed walk of odd length contains a simple cycle of odd length. Show by an example that a closed walk of even length need not contain any cycle.

11. • State the condition for an Eulerian circuit in a directed graph. The de Bruijn graph of order 2 over $\{0, 1\}$ has the four vertices $00, 01, 10, 11$ and an arc $xy \to yz$ for each string $xyz$. Find an Eulerian circuit and turn it into a cyclic binary string of length 8 that contains every string of length 3 exactly once.

12. • Show that [Fleury's algorithm](/fleury-algorithm/) with a bridge test by graph search takes $O(m(n + m))$ time. Then give a small graph and a start vertex where crossing a bridge too early leaves edges that can no longer be reached.

13. • Show that [Ore's theorem](/ore-theorem/) implies [Dirac's theorem](/dirac-theorem/). Then show that Dirac's bound is tight: for each $k \ge 1$, the complete bipartite graph $K_{k, k + 1}$ has minimum degree $k = (n - 1)/2$ and no Hamiltonian cycle.

14. • Prove that a DAG has a [Hamiltonian path](/hamiltonian-path/) exactly when it has a unique topological order, and that this holds exactly when each two consecutive vertices of some topological order are joined by an arc. Turn this into a linear-time test.

15. • Run [Karp's algorithm](/karp-minimum-mean-cycle/) on the directed graph with the arcs $a \to b$ 2, $b \to c$ 1, $c \to a$ 3, $b \to d$ 4, $d \to b$ 0, $c \to d$ 1, $d \to a$ 2. Use $D_0(v) = 0$ for every $v$, compute $D_k(v)$ for $k = 0, \ldots, 4$, apply the formula, and name the cycle that reaches the minimum mean.

16. • The graph of Exercise 4 is connected with 6 vertices and 10 edges. How many cycles are in a [cycle basis](/cycle-basis/)? Give the fundamental cycles of the breadth-first tree from vertex 1 with the edges $12, 13, 24, 25, 46$, and write the cycle $3, 4, 5$ as a sum of them over GF(2).

17. • In the [Itai-Rodeh](/itai-rodeh-girth-algorithm/) method, each non-tree edge $xy$ found by breadth-first search from $r$ gives the bound $d(x) + d(y) + 1$ on the girth. Show that the bound is always the length of some closed walk that contains a cycle, and that it is exact when $r$ lies on a shortest cycle.

18. • Show that for any order of the vertices of a directed graph, either the arcs pointing forward or the arcs pointing backward number at least $m/2$, which gives a $\frac12$-approximation for the [maximum acyclic subgraph](/maximum-acyclic-subgraph/). Why does this not give a good approximation for the [feedback arc set](/feedback-arc-set-problem/)?

19. • Find the size of a minimum [feedback vertex set](/feedback-vertex-set-problem/) of $K_n$, of the wheel with a hub and a 5-cycle, and of the Petersen graph, each with a set that reaches it and an argument that nothing smaller works.

20. • Reduce the [Hamiltonian path problem](/hamiltonian-path-problem/) to the [longest path problem](/longest-path-problem/). Explain why negating all weights and running Bellman-Ford does not find a longest simple path in a graph with cycles, although it works in a DAG.

21. • Show that the trace of $A^3$ is 6 times the number of triangles of a simple undirected graph, and check it on the diamond graph of Exercise 2. What does the trace of $A^4$ count?

22. ★ Glue $k$ copies of a 4-cycle into a chain, identifying one vertex of each copy with the opposite vertex of the previous copy, and let $s$ and $t$ be the two free ends of the chain. Count the simple $s$-$t$ paths. Then show that plain backtracking, with no test that the current path can still reach $t$, can spend time exponential in $n$ before its first output on a suitable graph, and explain how the test in [Read-Tarjan](/read-tarjan-path-enumeration/) prevents this.

23. ★ Prove [Ore's theorem](/ore-theorem/) by contradiction: take a maximal non-Hamiltonian graph that satisfies the condition, take a Hamiltonian path between two non-adjacent vertices, and find a rotation that closes it.

24. ★ In a DAG, let paths share vertices. Show that the fewest paths that cover all vertices equals the minimum path cover of the transitive closure, and that this equals the largest set of vertices no two of which lie on a common path.

25. ★ Reduce the directed [Hamiltonian cycle problem](/hamiltonian-cycle-problem/) to the undirected one by replacing each vertex with a path of three vertices. Prove both directions.
