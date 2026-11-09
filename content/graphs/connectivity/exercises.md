1. ◦ The graph $H$ has the vertices $0, \ldots, 9$ and the edges $01, 02, 12, 23, 34, 45, 35, 46, 67, 78, 68, 89$. Run a [depth-first search](/depth-first-search/) from 0 with adjacency lists in increasing order. Give the discovery time and the [low-link value](/low-link/) of each vertex, then list the [articulation points](/articulation-point/) and the [bridges](/bridge/) with the test that identifies each.

2. ◦ Give the [biconnected components](/biconnected-components/) of the graph $H$ of Exercise 1 and draw its [block-cut tree](/block-cut-tree/). How many nodes and edges does the tree have?

3. ◦ A directed graph $D$ has the arcs $a \to b$, $b \to c$, $b \to h$, $c \to a$, $c \to d$, $d \to e$, $e \to d$, $e \to f$, $g \to f$, $g \to h$, $h \to g$. Run the [Kosaraju-Sharir algorithm](/kosaraju-sharir/), with the outer loop and the adjacency lists in alphabetical order. Give the finishing order of the first pass and the components in the order the second pass finds them.

4. ◦ Run [Tarjan's algorithm](/tarjan-scc/) on the graph $D$ of Exercise 3, in the same orders. In what order are the components popped from the stack? Compare with the order of Exercise 3.

5. ◦ Draw the [condensation](/condensation-graph/) of $D$, and give all its topological orders.

6. ◦ A DAG on $\{1, \ldots, 5\}$ has the arcs $1 \to 2$, $2 \to 3$, $1 \to 3$, $3 \to 4$, $2 \to 4$, $4 \to 5$, $1 \to 5$. Compute its [transitive closure](/transitive-closure/) with [Warshall's algorithm](/warshall-algorithm/), and then its [transitive reduction](/transitive-reduction/).

7. ◦ Process the edges $01, 23, 13, 45, 02, 67, 56, 12$ of a graph on $\{0, \ldots, 7\}$ with a [disjoint-set](/union-find-connectivity/) structure. Which edges merge two sets, which are redundant, and what are the components at the end? Explain why the number of merging edges is always $n$ minus the number of components.

8. ◦ The ladder has the vertices $0, \ldots, 5$ and the edges $01, 12, 34, 45, 03, 14, 25$. Find a [strong orientation](/strong-orientation/) by directing the tree edges of a DFS from 0 away from the root and the back edges towards it. Check that the result is strongly connected.

9. ◦ Two copies of $K_4$ share a single vertex. Find the vertex connectivity $\kappa$, the edge connectivity $\lambda$ and the least degree $\delta$, and check the inequality $\kappa \le \lambda \le \delta$.

10. • Prove that the root of a DFS tree of an undirected graph is an articulation point if and only if it has at least two children. Why does the test for the other vertices not apply to the root?

11. • Show that an edge is a bridge if and only if it lies on no cycle. Deduce that a biconnected graph is 2-edge-connected, and give a 2-edge-connected graph on five vertices that is not biconnected.

12. • Show that a directed graph is strongly connected if and only if some vertex $s$ reaches all vertices in both $G$ and its [transpose](/graph-transpose/). Turn this into an $\Theta(n + m)$ test.

13. • In the second pass of Kosaraju-Sharir, the roots are taken in decreasing order of finishing time. Give a graph with three vertices on which taking them in increasing order merges two components.

14. • A formula in conjunctive normal form has two literals per clause. Build its implication graph, with an arc $\lnot x \to y$ and an arc $\lnot y \to x$ for each clause $x \lor y$. Show that if a variable and its negation lie in one strongly connected component, the formula is unsatisfiable. Apply this to $(x \lor y)(x \lor \lnot y)(\lnot x \lor z)(\lnot x \lor \lnot z)$.

15. • Show that a DAG has exactly one transitive reduction, and that it consists of the arcs $u \to v$ for which no other path leads from $u$ to $v$. Then find two different minimal subgraphs of the complete directed graph on three vertices with the same reachability.

16. • Show that every [ear decomposition](/ear-decomposition/) of a 2-edge-connected graph with $n$ vertices and $m$ edges has exactly $m - n + 1$ ears, counting the first cycle. Give one for $K_4$.

17. • A tournament is a directed graph with exactly one arc between each pair of vertices. Show that its condensation is a transitive tournament, so the components of a tournament come in a single line.

18. • Use [Menger's theorem](/menger-theorem/) to show that any two vertices of a biconnected graph lie on a common cycle.

19. • Edges of a graph are deleted one by one, and after each deletion the question is whether $u$ and $v$ are still connected. All deletions and queries are known in advance. Answer them all in $O((n + m) \, \alpha(n))$ time with a disjoint-set structure.

20. • Let $G$ be a directed graph and $C$ its condensation. Show how to obtain the transitive closure of $G$ from that of $C$, and bound the time beyond the closure of $C$.

21. • Prove that $\kappa(G) \le \lambda(G)$ for every graph that is not complete, by turning a least edge cut into a vertex cut of no larger size.

22. ★ A DAG has $s$ sources and $t$ sinks and more than one vertex. Show that at least $\max(s, t)$ new arcs are needed to make it strongly connected. Then show that $\max(s, t)$ arcs suffice when every source reaches every sink.

23. ★ In a connected undirected graph, find in $\Theta(n + m)$ time all vertices that lie on every path from $s$ to $t$.

24. ★ Let $F_1$ be a maximal spanning forest of $G$, $F_2$ one of $G - F_1$, and so on up to $F_k$. Show that $F_1 \cup \cdots \cup F_k$ has at most $k(n - 1)$ edges and is $k$-edge-connected whenever $G$ is.

25. ★ Let $G$ be $k$-vertex-connected, let $x$ be a vertex and let $U$ be a set of $k$ vertices not containing $x$. Show that there are $k$ paths from $x$ to the vertices of $U$, one ending at each, that share no vertex except $x$.
