1. ◦ A directed graph has the weighted edges $s \to a$ (4), $s \to b$ (1), $b \to a$ (2), $a \to c$ (1), $b \to c$ (5), $c \to d$ (3), $a \to d$ (6), $d \to t$ (1), $c \to t$ (6) and $b \to d$ (8). Run [Dijkstra's algorithm](/dijkstra/) from $s$. Give the order in which vertices are finished, the final distances and the parent of each vertex.

2. ◦ A directed graph on $\{0, \ldots, 4\}$ has its edges listed in this order: $(3, 4, 2)$, $(2, 3, -1)$, $(1, 2, 3)$, $(0, 1, 4)$, $(0, 2, 6)$, $(1, 3, 5)$, $(4, 2, -2)$, $(0, 4, 9)$, where $(u, v, w)$ is an edge $u \to v$ of weight $w$. Run [Bellman-Ford](/bellman-ford/) from 0, relaxing the edges in this order in each pass and updating in place. Give the distance array after each of the four passes, then say what the check pass finds.

3. ◦ The graph has the edges $s \to a$ (2), $s \to b$ (4), $a \to c$ (1) and $b \to a$ ($-3$). Run Dijkstra's algorithm from $s$ as if the weights were nonnegative, relaxing the out-edges of each vertex when it is extracted. Which final values are wrong, and why is $d(a)$ correct while $d(c)$ is not?

4. ◦ Run [Floyd-Warshall](/floyd-warshall/) on the graph with vertices $0, \ldots, 3$ and the edges $(0, 1, 3)$, $(0, 2, 8)$, $(1, 2, -2)$, $(2, 3, 1)$, $(3, 0, 2)$, $(1, 3, 7)$. Give the matrix after the last round.

5. ◦ A DAG has the edges $a \to b$ (2), $a \to c$ (6), $b \to c$ (3), $b \to d$ ($-4$), $c \to e$ ($-2$), $d \to c$ (1), $d \to e$ (5), $e \to f$ (1), $d \to f$ (4). Find a topological order, then run the [DAG shortest-path algorithm](/dag-shortest-paths/) from $a$. Give the distances and the shortest-path tree.

6. ◦ Solve the system of [difference constraints](/difference-constraints/) $x_1 - x_2 \le 3$, $x_2 - x_3 \le -2$, $x_3 - x_1 \le 1$, $x_2 - x_4 \le 0$, $x_4 - x_1 \le -1$. Draw the constraint graph, add a source joined to every variable by an edge of weight 0, and read a solution off the distances.

7. ◦ A bank quotes 1 USD = 0.9 EUR, 1 EUR = 0.9 GBP and 1 GBP = 1.25 USD. Turn the rates into edge weights so that [arbitrage](/currency-arbitrage-detection/) becomes a negative cycle, and find the cycle and the profit on one dollar.

8. ◦ Run [Johnson's algorithm](/johnson/) on the graph with vertices $0, \ldots, 3$ and the edges $(0, 1, -2)$, $(1, 2, 3)$, $(0, 2, 4)$, $(2, 3, -1)$, $(3, 1, 2)$, $(1, 3, 5)$. Give the potentials $h$, the reweighted edges, and the true distances from vertex 0.

9. ◦ How many min-plus matrix products does [repeated squaring](/apsp-repeated-squaring/) need to compute all-pairs distances on a graph with 1000 vertices and no negative cycle? Why may the method stop squaring once the number of edges allowed reaches $n - 1$?

10. • Change Dijkstra's algorithm so that it also counts the shortest paths from $s$ to every vertex, when all weights are positive. Show by an example that your counts can be wrong if zero-weight edges are allowed, and say what extra condition repairs them.

11. • A variant of Bellman-Ford runs only $k$ passes, to get the least weight of a path from $s$ that uses at most $k$ edges. Show on the path $s \to a \to b \to c$, with the edges listed in that order, that updating the array in place gives the wrong answer for $k = 1$. How must the passes be changed?

12. • In some networks the cost sits on the vertices: passing through $v$ costs $c(v) \ge 0$, and edges are free. Reduce this problem to an ordinary shortest-path problem with weights on the edges, and give the running time with Dijkstra.

13. • An undirected graph has one edge of negative weight. Explain why replacing each undirected edge by two opposite directed edges and running Bellman-Ford does not find shortest simple paths.

14. • Prove that a graph has a negative cycle if and only if Floyd-Warshall, run on it with $D[i][i] = 0$ at the start, ends with some diagonal entry below zero.

15. • A student writes Floyd-Warshall with the loop over $k$ innermost: for each $i$, for each $j$, for each $k$, set $D[i][j] \gets \min(D[i][j], D[i][k] + D[k][j])$. Give a graph with four vertices and unit weights on which one entry stays wrong.

16. • Use Floyd-Warshall to find a directed cycle of least total weight in a graph with no negative cycle, in $\Theta(n^3)$ time. Say how to recover the cycle itself.

17. • Each link of a network works with probability $p(u, v)$, independently of the others. Show how to find the path most likely to work with a shortest-path algorithm. Apply it to the links $s \to a$ (0.9), $a \to t$ (0.8), $s \to b$ (0.95), $b \to t$ (0.7), $s \to t$ (0.7), $a \to b$ (0.99).

18. • A traveller may use one edge for free. Find the least cost of a trip from $s$ to $t$ with nonnegative weights in $O((n + m) \log n)$ time.

19. • In a graph, every negative edge leaves the source $s$, and no edge enters $s$. Is Dijkstra's algorithm from $s$ still correct? Prove your answer.

20. • All weights are 1 or 2. Find all distances from $s$ in $\Theta(n + m)$ time without a priority queue.

21. ★ Number the vertices $1, \ldots, n$. Split the edges into those that go from a lower number to a higher one, and the rest. A pass relaxes the first kind with the tails in increasing order, then the second kind with the tails in decreasing order. Show that Bellman-Ford with such passes needs at most $\lceil n/2 \rceil$ passes when no negative cycle exists.

22. ★ Let a system of difference constraints be solved by Bellman-Ford from a source joined to every variable by edges of weight 0. Show that the solution $x$ found satisfies $x \le 0$, and that every other solution $y$ with $y \le 0$ has $y \le x$ in every coordinate.

23. ★ Two $n \times n$ matrices have entries in $\{0, 1, \ldots, M\} \cup \{\infty\}$. Show how to compute their [min-plus product](/min-plus-matrix-multiplication/) with one ordinary product of integer matrices, and discuss the size of the numbers involved.

24. ★ The [optimality conditions](/shortest-path-optimality-conditions/) say $d(s) = 0$ and $d(v) = \min_u (d(u) + w(u, v))$ for $v \ne s$. Show that when every cycle has positive weight and every vertex is reachable from $s$, these equations have exactly one solution. Give a graph with a cycle of weight 0 where they have more than one.
