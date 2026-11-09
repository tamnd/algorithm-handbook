1. ◦ The network $N$ has the arcs $s \to a$ 9, $s \to b$ 8, $a \to b$ 3, $a \to c$ 4, $b \to c$ 2, $b \to d$ 6, $c \to t$ 8, $d \to c$ 3, $d \to t$ 4, with capacities after the names. Run [Edmonds-Karp](/edmonds-karp/), breaking ties by taking neighbours in alphabetical order. List the augmenting paths with their bottlenecks, give the maximum flow value, and give the minimum cut from the last [residual graph](/residual-graph/).

2. ◦ Run [Dinic's algorithm](/dinic/) on the network $N$ of Exercise 1. For each phase, give the BFS levels, the arcs of the [level graph](/level-graph/) and a [blocking flow](/blocking-flow/).

3. ◦ A flow has the values $s \to a$ 5, $s \to b$ 4, $a \to b$ 2, $a \to t$ 4, $b \to c$ 6, $c \to a$ 1, $c \to t$ 5. Check conservation, give the value, and write the flow as a sum of $s$–$t$ paths and cycles as in [flow decomposition](/flow-decomposition/).

4. ◦ The network has the arcs $s \to a$, $s \to b$, $a \to t$, $b \to t$, each of capacity 1000, and $a \to b$ of capacity 1. Show that [Ford-Fulkerson](/ford-fulkerson/) can take 2000 augmentations if it chooses its paths badly. How many does Edmonds-Karp take?

5. ◦ Find the largest number of [edge-disjoint paths](/edge-disjoint-paths/) between two opposite corners of the cube graph $Q_3$, give the paths, and give a cut that proves no more exist.

6. ◦ In a league, team D has 75 wins and its remaining games are against teams already out of the race. The leaders have A 79 wins, B 78 and C 76, and they still play A–B 4 times, A–C once and B–C once. Build the network of [baseball elimination](/baseball-elimination/) for D, and decide whether D can still finish first or tied for first. Give the set of teams that proves the answer.

7. ◦ The undirected graph on $\{a, b, c, d, e\}$ has the weighted edges $ab$ 2, $ac$ 2, $bc$ 6, $bd$ 4, $cd$ 5, $ae$ 7, $de$ 5, $ce$ 4. Run the [Stoer-Wagner algorithm](/stoer-wagner/), starting every phase at $a$. For each phase give the maximum adjacency order and the cut of the phase, and give the minimum cut.

8. ◦ A graph has 10 vertices. Give a lower bound on the probability that one run of [Karger's algorithm](/karger-min-cut/) returns a fixed minimum cut, and the number of runs that lowers the chance of missing it below 1%.

9. ◦ Draw a [Gomory-Hu tree](/gomory-hu-tree/) for the cycle $a, b, c, d$ with the edge weights $ab$ 1, $bc$ 2, $cd$ 3, $da$ 4, and read off the minimum cut value of all six pairs.

10. • Show that the source sides of minimum $s$–$t$ cuts are closed under union and intersection. Deduce that the set of vertices reachable from $s$ in the final residual graph is the smallest source side of any minimum cut.

11. • Explain how to decide, with one maximum flow and $O(m)$ extra work, whether an arc lies in some minimum cut, and whether it lies in every minimum cut.

12. • A maximum flow is known. The capacity of one arc grows by 1. Show that one search updates the maximum flow. Then do the same when the capacity of one arc falls by 1.

13. • A project has the jobs $p_1$ with profit 10, $p_2$ with profit 6 and $p_3$ with profit 3, and the tools $t_1$ costing 4, $t_2$ costing 7 and $t_3$ costing 2. Job $p_1$ needs $t_1$ and $t_2$, job $p_2$ needs $t_2$, and $p_3$ needs $t_3$. Solve it as a [maximum-weight closure](/maximum-weight-closure/) and give the maximum flow of the network you build.

14. • Edges may carry a lower bound as well as a capacity. Reduce the question whether a [circulation](/circulation-problem/) exists to one maximum flow, and show how to recover the circulation.

15. • In an undirected network, each edge may carry flow in either direction up to its capacity. Show that replacing each edge by two opposite arcs of the same capacity gives the right maximum flow, and that some maximum flow then uses at most one arc of each pair.

16. • A network has several sources and several sinks, and each source has a supply limit. Reduce the maximum flow to a single-source, single-sink problem.

17. • The network has the arcs $s \to a$ (capacity 2, cost 1), $s \to b$ (2, 3), $a \to b$ (1, 1), $a \to t$ (1, 5), $b \to t$ (3, 1). Use [successive shortest paths](/successive-shortest-path/) to send 3 units from $s$ to $t$ at least cost. Give each path, the residual network after it, and the total cost.

18. • Use [vertex capacities](/vertex-capacities-flow/) to find the least number of cells that must be blocked to cut the top-left cell of a $4 \times 4$ grid from the bottom-right one, moving between side-adjacent cells. Check the answer with [Menger's theorem](/menger-theorem/).

19. • Prove that every graph on $n$ vertices has at most $\binom{n}{2}$ minimum cuts, using the analysis of Karger's algorithm, and show that the cycle $C_n$ has exactly that many.

20. • The capacities of a network are integers and some maximum flow is not integral. Show how to turn it into an integral maximum flow by cancelling flow around cycles of fractional arcs.

21. • In a network where every capacity is 1, show that Dinic's algorithm finds each blocking flow in $O(m)$ time. Show also that after $\sqrt{m}$ phases the remaining flow is at most $\sqrt{m}$. What total bound follows?

22. ★ Ford-Fulkerson need not stop with irrational capacities. Let $r = (\sqrt{5} - 1)/2$, so that $r^2 = 1 - r$. Build a network with three arcs of capacities $1$, $r$ and $1$ in the middle and large capacities elsewhere, and choose augmenting paths so that the residual capacities of the middle arcs run through $r^k$, $r^{k+1}$, $0$ in turn. Show that the flow converges to a value below the maximum.

23. ★ The density of a vertex set $S$ in an undirected graph is $|E(S)| / |S|$. Given $g$, decide with one minimum cut whether some $S$ has density greater than $g$, and use this to find a densest subgraph.

24. ★ Prove that for any three vertices $u, v, w$ of an undirected network, $\lambda(u, w) \ge \min(\lambda(u, v), \lambda(v, w))$, where $\lambda$ is the minimum cut value. Deduce that among the $\binom{n}{2}$ values of $\lambda$ there are at most $n - 1$ different ones.

25. ★ Take the star $K_{1,3}$ with unit capacities, and the three commodities that join each pair of leaves. Find the maximum total [multicommodity flow](/multi-commodity-flow-problem/) and the least [multicut](/multicut-problem/), and show that they differ.
