1. ◦ A knapsack has capacity $W = 10$ and four items with weights $w = (4, 6, 3, 5)$ and values $v = (20, 18, 15, 10)$. Run the [greedy fractional knapsack](/greedy-fractional-knapsack/) and give the fractional optimum and the critical item. Then find the 0-1 optimum, and the value of the repaired greedy that returns the better of the greedy prefix and the best single item.

2. ◦ Fill in the table of [knapsack dynamic programming](/knapsack-dynamic-programming/) for capacity $W = 6$ and the items $(w, v) = (3, 4), (4, 5), (2, 3)$, taken in this order. Give each row $V[i][0..6]$, the optimal value and an optimal set.

3. ◦ (a) How many different tours does a symmetric [traveling salesman problem](/traveling-salesman-problem/) on 12 cities have? (b) What is $n^2 2^n$ for $n = 12$? (c) A [large neighborhood search](/large-neighborhood-search/) for a 40-city tour removes 6 cities in each move. How many different sets of 6 cities could it remove, and how many if, as in the measured example of the entry, it always removes one city together with its 5 nearest neighbors?

4. ◦ Five cities lie on a line at $0, 3, -1, 7, -6$, with $c(x, y) = |x - y|$. Run the [nearest neighbor heuristic](/nearest-neighbor-heuristic/) from the city at 0, and give the tour and its cost. What is the optimal tour cost? Then run the heuristic from each of the other four cities.

5. ◦ In an uncapacitated [facility location problem](/facility-location-problem/) on a line, facilities $A$, $B$, $C$ sit at $0$, $4$, $10$ with opening costs $6$, $2$, $5$, and clients sit at $1, 2, 5, 9, 11$. Each client is served by its nearest open facility at cost equal to the distance. Give the total cost of each of the seven nonempty sets of open facilities, and the optimum.

6. ◦ A depot is at $(0, 0)$, with Manhattan distances, and four customers with demand 1 each are at $1 = (3, 0)$, $2 = (4, 1)$, $3 = (0, 3)$ and $4 = (1, 4)$. List the six savings of [Clarke-Wright](/clarke-wright-savings/). Run the method with truck capacity $Q = 2$ and with $Q = 4$, and give the routes and their total cost in each case.

7. ◦ Take the cycle $1, 2, 3, 4, 5, 6, 1$ with unit edge weights, and the bisection $A = \{1, 3, 5\}$, $B = \{2, 4, 6\}$. Give its cut and the values $D(v)$ of [Kernighan-Lin](/kernighan-lin/). What is the gain of swapping 1 with 2, and of swapping 1 with 4? What is the cut after the better swap?

8. ◦ The coverage function $f(S) = |\bigcup_{T \in S} T|$ is [submodular](/submodular-function/). Take $T_1 = \{1, 2, 3, 4\}$, $T_2 = \{1, 2, 5\}$, $T_3 = \{3, 4, 6\}$ and the limit $|S| \le 2$. What does greedy choose, and what is the optimum? Compare the ratio with $1 - 1/e$.

9. ◦ Four towns 1, 2, 3, 4 have six links: $a$, $b$, $c$ all join 1 and 2 and are red, blue and green; $d = 34$, $e = 23$ and $f = 14$ are all yellow. Find a largest forest that uses each color at most once, as a [matroid intersection](/matroid-intersection/) of a graphic and a partition matroid. Give the rank of each matroid alone, and a set $U$ that proves your answer by the [matroid intersection theorem](/matroid-intersection-theorem/).

10. ◦ In [competitive facility location](/competitive-facility-location/), take the path $a - b - c - d$ with values $2, 3, 3, 2$. What total can Player 2 guarantee, and which first move of Player 1 holds Player 2 to it? Then take five sites with no edges and values $5, 4, 3, 2, 1$.

11. • Apply [Lagrangian relaxation](/lagrangian-relaxation/) to the capacity constraint of the knapsack of exercise 1. Show that the relaxed problem has value $L(\lambda) = \lambda W + \sum_i \max(0, v_i - \lambda w_i)$ for $\lambda \ge 0$, and that this is an upper bound on the 0-1 optimum. Find the $\lambda$ that minimizes it and the minimum value. Why must the minimum equal the fractional optimum?

12. • Four cities have the distances $d_{12} = 2$, $d_{13} = 9$, $d_{14} = 10$, $d_{23} = 6$, $d_{24} = 4$, $d_{34} = 8$. Run the [Held-Karp algorithm](/held-karp-algorithm/) from city 1: give the values $C(S, j)$ for $|S| = 1, 2, 3$ and the optimal tour.

13. • A *1-tree* on the cities of exercise 12 is a spanning tree on cities 2, 3, 4 plus the two cheapest edges at city 1. Every tour is a 1-tree, so the cheapest 1-tree is a lower bound. With multipliers $\pi_v$, replace each $d_{uv}$ by $d_{uv} + \pi_u + \pi_v$ and subtract $2 \sum_v \pi_v$ from the cheapest 1-tree; this is the Lagrangian bound for the degree constraints. Compute the bound for $\pi = 0$ and for $\pi = (0, 1, 0, -1)$. Is the second bound tight?

14. • Solve the 0-1 knapsack with $W = 9$ and items $(w, v) = (3, 4), (4, 5), (2, 3), (5, 7)$ by meet in the middle, as in the [knapsack problem](/knapsack-problem/) entry: split the items into $\{1, 2\}$ and $\{3, 4\}$, list the (weight, value) pairs of each half, and combine them. Give the optimum and every optimal set.

15. • The depot is at $(0, 0)$ with Manhattan distances, $Q = 2$, and four customers with demand 1 are at $1 = (5, 5)$, $2 = (4, 4)$, $3 = (5, -1)$ and $4 = (-1, 5)$. Run [Clarke-Wright savings](/clarke-wright-savings/) and find the optimal routes. Explain the failure in terms of a greedy matching.

16. • A hypergraph has vertices $a, b, c, d, e$ and nets $\{a, b, c\}$, $\{c, d\}$, $\{d, e\}$, $\{a, e\}$, $\{b, d, e\}$. The partition is $\{a, b\} \mid \{c, d, e\}$. Count the cut nets, and compute the gain of every vertex by the rule of [Fiduccia-Mattheyses](/fiduccia-mattheyses/). Check the gain of the vertex with the largest gain by moving it and counting the cut again.

17. • The Laplacian of the cycle $C_n$ has eigenvalues $2 - 2\cos(2\pi k / n)$ for $k = 0, \ldots, n - 1$. Evaluate the spectral lower bound $n \lambda_2 / 4$ of the [graph partitioning problem](/graph-partitioning-problem/) for $C_4$ and $C_8$, and compare with the minimum bisection of each. What happens to the bound as $n \to \infty$?

18. • Run one round of the [matroid intersection algorithm](/matroid-intersection-algorithm/) on bipartite matching. The graph has $L = \{u_1, u_2\}$, $R = \{v_1, v_2\}$ and edges $p = u_1 v_1$, $q = u_1 v_2$, $r = u_2 v_1$; $M_1$ allows one edge at each vertex of $L$, $M_2$ one at each vertex of $R$. Start from $I = \{p\}$. Give $X_1$, $X_2$, the arcs of the exchange graph, the shortest path and the new set.

19. • In a [quadratic assignment problem](/quadratic-assignment-problem/), facilities $A$, $B$, $C$ have flows $f_{AB} = 4$, $f_{BC} = 1$, $f_{AC} = 2$ in both directions, and the locations are the points 0, 1, 3 on a line. The objective counts every ordered pair. Give the cost of all six assignments. Then run pairwise exchange with best improvement from the assignment $(A, B, C) \mapsto (0, 3, 1)$. Does it reach the optimum?

20. • Show that the Lovász extension $\hat f(x) = \int_0^1 f(\{e : x_e \ge \theta\}) \, d\theta$ of the cut function of a graph with edge weights $w$ is $\hat f(x) = \sum_{uv \in E} w_{uv} |x_u - x_v|$. Check that it is convex, as Lovász's theorem in the [submodular function](/submodular-function/) entry requires.

21. • Give a family of 0-1 knapsack instances, with three items that each fit alone, on which the repaired greedy of exercise 1 returns a value whose ratio to the optimum tends to $1/2$.

22. • A bipartite graph is $d$-regular with $d \ge 1$. Use the matroid intersection theorem, with the two partition matroids of bipartite matching, to show that it has a perfect matching. (Bound $r_1(U)$ and $r_2(E \setminus U)$ below by $|U|/d$ and $|E \setminus U|/d$.)

23. ★ Let $f$ be monotone, submodular and normalized, and let greedy pick $k$ elements, each with the largest marginal gain. Prove that $f(S_k) \ge \bigl(1 - (1 - 1/k)^k\bigr) f(S^*)$ for an optimal $S^*$ with $|S^*| \le k$, and deduce the bound $1 - 1/e$. Then give a weighted coverage instance with $k = 2$ on which the ratio of greedy tends to $3/4$, however greedy breaks ties.

24. ★ Let $G$ be a graph with edge weights $w \ge 0$ and let $m_v$ be a real number for each vertex. Show how to minimize $f(S) = \mathrm{cut}(S) + \sum_{v \in S} m_v$ over all $S \subseteq V$ with one [minimum $s$-$t$ cut](/min-cut-problem/), and give the constant that relates the two values. Apply it to the path $1 - 2 - 3$ with $w_{12} = 2$, $w_{23} = 1$ and $m = (-3, 1, -1)$.

25. ★ For the instance of exercise 5, dualize the constraints that each client is served exactly once with multipliers $v_j$, as in [Lagrangian relaxation](/lagrangian-relaxation/). Show that $L(v) = \sum_j v_j + \sum_i \min\bigl(0, f_i - \sum_j \max(0, v_j - c_{ij})\bigr)$, where $f_i$ is the opening cost and $c_{ij}$ the service cost. Find multipliers with $L(v) = 15$, which proves the optimum of exercise 5.

26. ★ Prove that in a directed graph with root $r$, a set of $|V| - 1$ arcs is a spanning [arborescence](/arborescence/) rooted at $r$ if and only if it is a forest in the underlying undirected graph and has at most one arc into each vertex and none into $r$. Then take vertices $r, a, b, c$ and arcs $r \to a$, $b \to c$, $c \to b$, $b \to a$. Every vertex other than $r$ has an entering arc and the underlying graph is connected. Show that there is no arborescence, with a certificate $U$ from the matroid intersection theorem.

27. ★ Show that minimum bisection, which is NP-hard on general graphs, can be solved in $O(n^2)$ time on a tree with $n$ vertices, $n$ even. Give the dynamic program and the argument for the running time.
