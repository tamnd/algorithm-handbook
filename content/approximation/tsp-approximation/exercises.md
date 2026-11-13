1. ◦ Four cities $A, B, C, D$ have the costs $AB = BC = CD = DA = BD = 1$ and $AC = 5$. Show that these costs break the triangle inequality, and list the three tours with their costs. Then find the least $M$ such that adding $M$ to every cost gives costs that obey the triangle inequality, as in [metric TSP](/metric-tsp/). Compare the ratio of the worst tour to the best tour before and after the change.

2. ◦ For a graph $G$ on $n$ vertices, give each pair cost 1 if it is an edge of $G$ and cost 2 if not. Explain why these costs obey the triangle inequality. Find OPT when $G$ is the complete bipartite graph $K_{2,3}$ and when $G$ is the star $K_{1,4}$.

3. ◦ Six cities have the costs below, which obey the triangle inequality.

   |  | $A$ | $B$ | $C$ | $D$ | $E$ | $F$ |
   |---|---|---|---|---|---|---|
   | $A$ | 0 | 6 | 14 | 9 | 7 | 18 |
   | $B$ | 6 | 0 | 17 | 4 | 8 | 15 |
   | $C$ | 14 | 17 | 0 | 16 | 9 | 15 |
   | $D$ | 9 | 4 | 16 | 0 | 8 | 11 |
   | $E$ | 7 | 8 | 9 | 8 | 0 | 12 |
   | $F$ | 18 | 15 | 15 | 11 | 12 | 0 |

   The tour $A\,B\,D\,F\,C\,E$ is the unique optimal tour; find its cost. Find a minimum spanning tree and its cost, and the [1-tree bound](/mst-lower-bound-for-tsp/) for each choice of the special vertex. Which special vertex gives the best bound, and how far is it from OPT?

4. ◦ Run the [nearest neighbour](/nearest-neighbor-tsp/) rule on the cities of Exercise 3, starting at $A$. Give the tour and its cost. Then repeat from each of the other five cities. Which starts give an optimal tour?

5. ◦ Run [nearest insertion](/nearest-insertion/) on the cities of Exercise 3, starting from the cycle that holds $A$ alone. At each step give the city added, its distance to the cycle and the increase in cost. Check that the distances add up to the cost of the minimum spanning tree.

6. ◦ Run the [greedy edge](/greedy-edge-heuristic/) rule on the cities of Exercise 3. List the edges in order of cost, say which are kept, and give the reason each rejected edge is rejected. What is the cost of the tour?

7. ◦ Build the [double-tree](/double-tree-algorithm/) tour of the cities of Exercise 3 as a [preorder walk](/mst-preorder-walk-tsp/) of the minimum spanning tree, rooted at $A$, with the children of each vertex in alphabetical order. Give the tour, its cost and the bound $2\,c(T)$.

8. ◦ Run [Christofides' algorithm](/christofides-algorithm/) on the cities of Exercise 3. Which vertices of the minimum spanning tree have odd degree, what matching is added, and what tour results?

9. ◦ Six points lie on a line at $0, 2, 3, 7, 8, 12$, with cost $|x - y|$. For the [bottleneck TSP](/bottleneck-tsp/), find $t_1$, the least threshold at which the cheap edges connect all points, $t_2$, the least threshold at which they form a biconnected graph, and OPT, the least possible longest edge of a tour. What does the [Parker-Rardin algorithm](/bottleneck-tsp-approximation/) guarantee here? Also find the least total cost of a tour.

10. • Run [cheapest insertion](/cheapest-insertion/) on the cities of Exercise 3, starting from $A$. Give the order in which the cities enter, the increase at each step and the final tour. Compare with the nearest insertion tour of Exercise 5.

11. • Run [farthest insertion](/farthest-insertion/) on the cities of Exercise 3, starting from $A$. Give the order of the cities, the increase at each step and the final tour.

12. • The nearest neighbour tour from $A$ in Exercise 4 is $A\,B\,D\,E\,C\,F$. Find every [2-opt](/two-opt/) move that shortens it, with its gain. Where does the best move lead?

13. • The tour $A\,B\,D\,F\,E\,C$ of Exercise 5 costs 56. Find an [Or-opt](/or-opt/) move of one city that shortens it, and the result. Which 2-opt move gives the same tour?

14. • For the cities of Exercise 3, take $A$ as the special vertex and the penalties $\pi_C = \pi_F = -7/2$, with $\pi = 0$ at the other cities. Compute $L(\pi)$, the [Held-Karp](/held-karp-bound/) value of a minimum 1-tree for the penalized costs $c_{uv} + \pi_u + \pi_v$ minus $2 \sum_v \pi_v$. What does the result tell you about the subtour LP of this instance?

15. • Christofides' algorithm is tight on the following family. Take $n$ odd, cities $0, 1, \ldots, n - 1$ on a path, cost 1 on the pairs $\{i, i + 1\}$, cost $1 + \varepsilon$ on the pairs $\{i, i + 2\}$, and shortest path costs elsewhere. For $n = 7$ and $\varepsilon = 0.1$, find the minimum spanning tree, the matching, ALG, OPT and the ratio. Then find the ratio for general $n$ and $\varepsilon$ and its limit.

16. • An [asymmetric TSP](/asymmetric-tsp/) instance has the costs below, where the row is the start of an arc and the column its end. The costs obey the directed triangle inequality.

| from \ to | $A$ | $B$ | $C$ | $D$ |
|---|---|---|---|---|
| $A$ | 0 | 1 | 7 | 8 |
| $B$ | 3 | 0 | 9 | 9 |
| $C$ | 4 | 5 | 0 | 1 |
| $D$ | 8 | 6 | 9 | 0 |

Run the repeated cycle cover algorithm, taking the alphabetically first city of each cycle as its representative. Give each cycle cover, the total cost of the arcs and the bound $\lfloor \log_2 n \rfloor \cdot \text{OPT}$. Shortcut the circuit $A\,B\,A\,C\,D\,C\,A$ to a tour, and compare with OPT and with the reverse of the optimal tour.

17. • Put $n$ cities $0, 1, \ldots, n - 1$ on a one-way ring road, so that the cost from $i$ to $j$ is $(j - i) \bmod n$. Show that these costs obey the directed triangle inequality. Find OPT and the cost of the same tour driven in the opposite direction. What does this say about solving an asymmetric instance by any method that ignores direction?

18. • [Karp's partitioning](/karp-partitioning-tsp/) on a $k \times k$ grid has the worst-case bound ALG $\le \text{OPT} + ((7 + \sqrt{2})k + \sqrt{2})L$ for points in a square of side $L$. Take $n = 10^6$ uniform random points in the unit square and the estimate $\text{OPT} \approx 0.7124\sqrt{n}$ from the [Euclidean TSP](/euclidean-tsp/) entry. What is the largest $k$ for which the bound promises a tour within 10 percent of OPT, and about how many points does each cell then hold?

19. • Points $P(1,1)$, $Q(6,1)$, $R(2,5)$, $S(5,6)$, $T(3,2)$ and $U(6,4)$ lie on an $8 \times 8$ grid with the Manhattan distance. Give each point the Z-order key whose binary digits, from the highest, are $y_2 x_2 y_1 x_1 y_0 x_0$, where $x_2 x_1 x_0$ and $y_2 y_1 y_0$ are the binary forms of the coordinates. Visit the points in the order of their keys, as a [space-filling curve](/space-filling-curve-tsp/) tour does, and find its cost. OPT is 22. What is the ratio?

20. • For a tour on $n = 10$ cities, count the 2-opt moves, that is, the pairs of tour edges that share no city. Count the sets of three tour edges no two of which share a city, and the [3-opt](/three-opt/) moves that are not 2-opt moves, given that each such set has four of them. Give the counts as formulas in $n$.

21. ★ Points lie on a line, with cost $|x - y|$. Prove that every 2-optimal tour is optimal, and find its cost.

22. ★ Points in the plane are the corners of a convex polygon, no three on a line, with the Euclidean distance. Prove that every 2-optimal tour visits them in the order around the polygon, so 2-opt always finds OPT on such inputs.

23. ★ With the costs 1 and 2 of Exercise 2, prove that OPT $= n$ if $G$ has a Hamiltonian cycle, and otherwise OPT $= n + p$, where $p$ is the least number of vertex-disjoint paths of $G$ that cover all vertices. Use this to find OPT for $K_{2,4}$.

24. ★ For points on a line with cost $|x - y|$, prove that the bottleneck values of Exercise 9 always satisfy $t_2 = \text{OPT} \le 2 t_1$. Give an instance with $\text{OPT} = 2 t_1$.

25. ★ Take the shortest path costs of the Petersen graph, so that its 15 edges cost 1 and the other pairs cost 2. Show that $x_e = 2/3$ on each edge of the graph, and 0 elsewhere, is a feasible point of the [subtour elimination LP](/subtour-elimination-lp/), and that the LP value is exactly 10. The Petersen graph has no Hamiltonian cycle; use this to find OPT and the ratio OPT/LP on this instance.
