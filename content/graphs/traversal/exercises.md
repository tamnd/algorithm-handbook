1. ◦ The $3 \times 3$ grid graph has the vertices $0, \ldots, 8$, numbered row by row, and the edges $01, 03, 12, 14, 25, 34, 36, 45, 47, 58, 67, 78$. Run [breadth-first search](/breadth-first-search/) from vertex 0 with adjacency lists in increasing order. Give the order in which vertices leave the queue, the distance and the parent of each vertex, and the [layers](/bfs-layers/).

2. ◦ A directed graph on $\{0, \ldots, 6\}$ has the adjacency lists $0: 1, 2, 3$; $1: 3$; $2: 1, 4$; $3: 0, 5$; $4: 5$; $5:$ (empty); $6: 4, 5$. Run [depth-first search](/depth-first-search/) over all vertices, with the outer loop and the lists in the order given and a clock that starts at 1. Give $d$ and $f$ for each vertex, and [classify](/edge-classification/) each of the 11 edges.

3. ◦ A directed acyclic graph on $\{a, \ldots, h\}$ has the adjacency lists $a: e$; $b: a, d$; $c: d, f$; $d: e, g$; $e: h$; $f: g$; $g: h$; $h:$ (empty). (a) Run [Kahn's algorithm](/kahns-algorithm/) with a FIFO queue, starting with the sources in alphabetical order and appending new sources in the order they appear. (b) Run the DFS [topological sort](/topological-sort/) with the outer loop in alphabetical order. Give both orderings.

4. ◦ Let $G$ have the vertices $0, \ldots, 7$ and the edges $01, 12, 23, 34, 45, 50, 25, 16, 67$. Is $G$ bipartite? Answer the same question for $G$ with the edge $37$ added. In each case give the two sides or an odd cycle.

5. ◦ Which of these lists of (discovery, finish) intervals can come from one depth-first search of some directed graph? (a) $u: [1, 8]$, $v: [2, 5]$, $w: [3, 4]$, $x: [6, 7]$. (b) $u: [1, 6]$, $v: [2, 7]$, $w: [3, 4]$, $x: [5, 8]$. (c) $u: [1, 4]$, $v: [2, 3]$, $w: [5, 8]$, $x: [6, 7]$. For each valid list, draw the depth-first forest.

6. ◦ On the $5 \times 5$ grid with rows $11001$, $01010$, $00100$, $10011$, $11001$, how many regions of 1-cells does [flood fill](/flood-fill/) find with 4-neighbour moves, and how many with 8-neighbour moves?

7. ◦ A maze is the $3 \times 3$ grid graph of Exercise 1. How many edge walks does [Trémaux's traversal](/tremaux-traversal/) make before it stops, whatever free passage it picks at each step?

8. ◦ Run [lexicographic BFS](/lexicographic-bfs/) on the 4-cycle $0, 1, 2, 3$ starting at 0, breaking ties by the smaller vertex. Give the order, and show that its reverse is not a perfect elimination ordering.

9. • Extend breadth-first search so that it also computes, for each vertex $v$, the number of shortest paths from the source to $v$, in $O(n + m)$ time. Prove the rule you use. How many shortest paths go from vertex 0 to vertex 8 in Exercise 1, and how many from one corner to the opposite corner of the $4 \times 4$ grid graph?

10. • A knight moves on an $8 \times 8$ chessboard. Write a breadth-first search on the [implicit graph](/implicit-graph/) of its moves, and find the least number of moves from a1 to h8. Which squares are farthest from a1, and how far?

11. • In a directed graph, give an $O(n + m)$ algorithm that finds all vertices that lie on some walk from $s$ to $t$. Give a small example where such a vertex lies on no simple path from $s$ to $t$.

12. • Prove that a directed acyclic graph has exactly one topological ordering if and only if every two consecutive vertices of that ordering are joined by an edge.

13. • Count the topological orderings of the graph of Exercise 3. A short program that tries all orders is acceptable.

14. • Show how to change Kahn's algorithm so that it returns the lexicographically smallest topological ordering in $O(m + n \log n)$ time, and prove that it does. What is that ordering for the graph of Exercise 3?

15. • Suppose Kahn's algorithm stops with some vertices never output. Prove that each of them has an incoming edge from another of them, and use this to output a directed cycle in $O(n + m)$ time.

16. • Prove that every connected graph with $n \ge 2$ vertices has at least two vertices whose removal leaves the graph connected.

17. • A tournament is a directed graph with exactly one edge between each pair of distinct vertices. Prove that a tournament is acyclic if and only if it has no directed cycle of length 3, and that an acyclic tournament has out-degrees $n - 1, n - 2, \ldots, 0$ in its unique topological ordering.

18. • Prove that if every vertex of an undirected graph has degree at least $k \ge 2$, the graph has a path with $k$ edges and a cycle with at least $k + 1$ vertices. Use the fact that a depth-first search of an undirected graph has no cross edges.

19. • Give an $O(n + m)$ algorithm that finds, in a directed graph, a shortest walk from $s$ to $t$ with an even number of edges, or reports that none exists.

20. • Run [Morris traversal](/morris-traversal/) on the binary search tree built by inserting $4, 2, 6, 1, 3, 5, 7$ in this order. Give the sequence of nodes that the current pointer takes, and the number of threads created. Then show that on any binary tree with $n$ nodes, of which $\ell$ have a left child, the current pointer takes $n + \ell$ values.

21. • Show that the DFS of an undirected connected graph with $n$ vertices may need a recursion depth of $n - 1$ even when the BFS queue from the same start never holds more than 2 vertices, and that the BFS queue may hold $n - 1$ vertices when the recursion depth is 1.

22. ★ You are given an undirected connected graph and an ordering of all its vertices. Give an $O(n + m)$ algorithm that decides whether some breadth-first search from the first vertex, with some order of the adjacency lists, visits the vertices in exactly this order. Prove it correct.

23. ★ Solve the same problem as Exercise 22 for depth-first search and preorder.

24. ★ A vertex of a directed graph is a root if every vertex is reachable from it. Give an $O(n + m)$ algorithm that finds a root or reports that there is none, using one complete depth-first search and one more search.

25. ★ Prove that an undirected graph can be oriented so that every vertex has in-degree at least 1 if and only if no connected component is a tree, and give an $O(n + m)$ algorithm that finds such an orientation.

26. ★ A topological ordering of a directed acyclic graph on $\{1, \ldots, n\}$ is wanted in which vertex 1 is as early as possible, then, subject to that, vertex 2 is as early as possible, and so on. Show by a graph on three vertices that this is not the lexicographically smallest ordering, and give an $O(m + n \log n)$ algorithm for it.
