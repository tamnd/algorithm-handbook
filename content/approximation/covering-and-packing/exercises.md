1. ◦ Pack the list $0.4, 0.7, 0.3, 0.6, 0.2, 0.5, 0.3$ into unit bins by [next fit](/next-fit-bin-packing/), [first fit](/first-fit-bin-packing/), [best fit](/best-fit-bin-packing/) and [first fit decreasing](/first-fit-decreasing/). Give the bins each rule produces, and compare the counts with $\lceil S \rceil$, where $S$ is the total size.

2. ◦ Run first fit decreasing on $0.5, 0.4, 0.4, 0.3, 0.2, 0.2$. Find OPT, and check the result against both bounds $\frac32\text{OPT}$ and $\frac{11}{9}\text{OPT} + \frac69$. Which bound is met with equality?

3. ◦ An instance has three items of size $0.6$, three of size $0.45$ and two of size $0.3$. Compute $\lceil S \rceil$ and the number of items larger than $1/2$, the two [lower bounds](/bin-packing-lower-bound/). Then find OPT and explain why neither bound is reached.

4. ◦ Pack the rectangles (width, height) $(0.5, 0.6)$, $(0.4, 0.5)$, $(0.3, 0.5)$, $(0.6, 0.4)$, $(0.5, 0.3)$, $(0.4, 0.2)$ into a strip of width 1 by next fit decreasing height, as in [strip packing](/strip-packing/). Give the shelves and the height. Compare the height with the total area $A$ and with the bound $2A + h_{\max}$, and deduce an upper bound on the ratio for this instance.

5. ◦ The universe is $\{1, \dots, 6\}$ and the sets are $A = \{1, 2, 3, 4\}$ of cost 10, $B = \{4, 5, 6\}$ of cost 10, $C = \{1, 2, 5\}$ of cost 7 and $D = \{3, 6\}$ of cost 7. Run [greedy set cover](/greedy-set-cover/) and find the optimal cover. Compute $d$, the bound $H_d \cdot \text{OPT}$, and the [element frequency](/element-frequency/) $f$.

6. ◦ Vertex cover is set cover in which the sets are the stars of the vertices, so greedy set cover has ratio $H_\Delta$ on a graph of maximum degree $\Delta$. For which values of $\Delta$ is this bound better than the ratio 2 of the [maximal matching algorithm](/vertex-cover-2-approximation/)?

7. ◦ A star has a centre of weight 4 and five leaves of weight 1. Run the [primal-dual algorithm for weighted vertex cover](/primal-dual-weighted-vertex-cover/), taking the edges in the order of their leaves. Give the cover, its weight, the value of the dual and OPT. Which vertices of the cover are redundant?

8. ◦ Run [farthest-first traversal](/gonzalez-k-center/) on the points $0, 2, 3, 7, 13, 14$ of the line, starting from $0$, for $k = 2$ and for $k = 3$. In each case give the centres, the radius, the optimal radius and the ratio.

9. ◦ The Petersen graph has 10 vertices and 15 edges. Colour each vertex uniformly at random with one of three colours, and count the edges whose ends get different colours. What is the expected count, and what is the best count? Compare the ratio with the ratio $1/2$ of a random cut for [maximum cut](/maximum-cut/).

10. • Run the [primal-dual algorithm for set cover](/set-cover-primal-dual/) on the instance of exercise 5, raising the dual of the uncovered elements in the order $1, 2, \dots, 6$. Give the sets bought, the dual value and the bound $f \sum_e y_e$. Then find the LP optimum and show it is optimal with a dual solution, and run threshold rounding at $1/f$. Compare all costs with OPT.

11. • Run the greedy algorithm for [dominating set](/dominating-set/) on the $3 \times 3$ grid graph, breaking ties as you like. Then prove that the domination number of the grid is 3.

12. • Let $S_1 = \{1, 2, 3, 4, 5\}$, $S_2 = \{1, 2, 6, 7\}$, $S_3 = \{3, 4, 8, 9\}$ and $S_4 = \{5, 10\}$. Run [greedy maximum coverage](/greedy-max-coverage/) for $k = 2$ and $k = 3$, find the optimum in each case, and compare the result with the bound $(1 - (1 - 1/k)^k)\,\text{OPT}$.

13. • In budgeted [maximum coverage](/max-coverage/), each set has a cost and the chosen sets must have total cost at most a budget $B$. Show that the greedy rule that picks the set of largest new coverage per unit cost, while it fits, has no constant ratio. Suggest a simple change that removes your bad example.

14. • By the [Nemhauser-Wolsey-Fisher theorem](/nemhauser-wolsey-fisher-theorem/), greedy run for $\ell$ steps reaches $(1 - (1 - 1/k)^\ell)\,\text{OPT}$, where OPT is the best value of $k$ elements. For $k = 10$, find the least $\ell$ that guarantees $0.99\,\text{OPT}$. How many steps does the weaker bound $1 - e^{-\ell/k}$ ask for?

15. • A [covering integer program](/covering-integer-program/) asks for $\min x_1 + x_2 + x_3$ with $6x_1 + 5x_2 + 4x_3 \ge 10$ and $x \in \{0, 1\}^3$. Find OPT and the optimum of the natural LP. Write the knapsack cover inequalities for $S = \{1\}$ and $S = \{2, 3\}$, and show that adding them raises the LP optimum to OPT.

16. • In [set packing](/set-packing/) with sets of size at most $k$, any maximal packing has at least $\text{OPT}/k$ sets. Show that this bound is tight for every $k$: give an instance and an order in which greedy takes one set while OPT is $k$.

17. • For the cycle $C_5$, find the optimum of the LP relaxation of maximum [independent set](/independent-set/) and of [vertex cover](/vertex-cover/), and compare each with the integer optimum. Prove that your LP values are optimal.

18. • Derandomize the random cut for maximum cut by the [method of conditional expectations](/method-of-conditional-expectations/), placing the vertices one at a time. Show that the rule you get is the greedy rule, and conclude that greedy cuts at least half of the edge weight.

19. • In the $k$-diameter problem, the goal is to split the points into $k$ clusters so that the largest cluster diameter is as small as possible. Show that the clusters of farthest-first traversal, each point assigned to its nearest centre, have ratio 2 for this objective.

20. • In the [cutting stock problem](/cutting-stock-problem/), rolls have width 10 and the orders have widths 6, 4 and 3. List the maximal cutting patterns. With demands 3, 3 and 2, find the least number of rolls and prove it is optimal.

21. ★ Prove that every graph with $n$ vertices and no isolated vertex has a [dominating set](/dominating-set/) of at most $n/2$ vertices.

22. ★ Show that unweighted set cover with all sets of size at most 2 can be solved in polynomial time: if every element lies in a set and $\nu$ is the size of a [maximum matching](/maximum-matching/) among the 2-sets, then OPT $= n - \nu$, where $n$ is the number of elements.

23. ★ Prove that every vertex of the polytope $\{x : x_u + x_v \ge 1 \text{ for each edge } uv,\ 0 \le x \le 1\}$ has all coordinates in $\{0, \frac12, 1\}$.

24. ★ Prove that no online algorithm for bin packing has asymptotic ratio below $4/3$. Use a list of $n$ items of size $\frac12 - \varepsilon$ that may be followed by $n$ items of size $\frac12 + \varepsilon$.

25. ★ A [packing integer program](/packing-integer-program/) with 0/1 variables has $m$ constraints, and each item fits alone. Using a [basic feasible solution](/basic-feasible-solution/) of the LP, show that the better of the rounded-down LP solution and the best single item has value at least $\text{OPT}/(m + 1)$. What does this give for the [knapsack problem](/knapsack-problem/)?
