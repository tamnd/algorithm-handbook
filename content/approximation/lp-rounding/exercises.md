1. ◦ The complete graph $K_4$ has vertex weights $1, 2, 3, 4$. Show that $x_v = \frac12$ for every vertex is an optimal solution of the weighted vertex cover LP, using a dual solution of the same value. Then apply [LP rounding for vertex cover](/lp-rounding-vertex-cover/) and find OPT. Compare the rounded cost with $2\,\text{LP}^*$ and with OPT.

2. ◦ A [randomized approximation algorithm](/randomized-approximation-algorithm/) for a minimization problem returns a solution of expected cost at most $2\,\text{OPT}$. Use [Markov's inequality](/markov-inequality/) to bound the probability that one run costs at most $3\,\text{OPT}$. How many independent runs, keeping the cheapest answer, make the probability of failing to reach $3\,\text{OPT}$ at most $1/100$?

3. ◦ A graph has a vertex $c$ joined to three leaves $\ell_1, \ell_2, \ell_3$ and to the vertex $t_1$ of a triangle $t_1 t_2 t_3$; all weights are 1. Find the optimal solution of the vertex cover LP and show that it is unique. Use the persistency theorem of [half-integrality](/half-integrality/) to fix some vertices, and find OPT by solving what is left.

4. ◦ In [LP rounding for set cover](/lp-rounding-set-cover/), an element lies in three sets with LP values $\frac12, \frac14, \frac14$. Find the probability that one round misses it. How many rounds make the probability of missing it at most $1/1000$? How many would the general bound $e^{-t}$ ask for?

5. ◦ A formula on $x_1, x_2, x_3$ has all eight clauses with three literals, one for each choice of signs. Show that every assignment satisfies exactly 7 clauses. What does this say about the ratio $7/8$ of the [random assignment](/random-assignment-max-3-sat/)?

6. ◦ In an LP solution of facility location, client $j$ is served by four facilities in fractions $0.4, 0.3, 0.2, 0.1$ at distances $1, 2, 4, 10$. Compute $C_j$. Apply the [filtering](/filtering-technique/) rule with $\varepsilon = \frac13$: which facilities stay, what fraction of $j$ survives, and what are the scaled fractions? Compare the surviving fraction with the guarantee $\varepsilon / (1 + \varepsilon)$. Repeat for $\varepsilon = 1$.

7. ◦ Run the [Bar-Yehuda-Even algorithm](/bar-yehuda-even-vertex-cover/) on the path $a - b - c - d$ with weights $2, 3, 3, 2$, taking the edges in the order $ab, bc, cd$. Give the cover, its weight, and the sum of the amounts subtracted. Find OPT and the ratio on this input.

8. ◦ On the 4-cycle $a_1 b_1 a_2 b_2$, the bipartite matching LP has the solution $x_e = \frac12$ on all four edges. Round each edge independently, keeping it with probability $\frac12$. What is the probability that the result is a perfect matching? What is it under [dependent rounding](/dependent-rounding/)?

9. ◦ The [randomized rounding](/randomized-rounding/) analysis for routing gives congestion at most $\frac{4 \ln m}{\ln \ln m} \max(C^*, 1)$ with probability at least $1 - 1/m$, and $C^* + 3\sqrt{C^* \ln m}$ when $C^* \ge 9 \ln m$. For a network with $m = 10^6$ edges, compute the first factor. For $C^* = 200$, check that the second bound applies and compute it.

10. • Points $a, b, c, d, e$ have costs $2, 2, 3, 3, 1$, and a cheapest set of points must meet each of the sets $\{a, b, c\}$, $\{b, d\}$, $\{c, d, e\}$, $\{a, e\}$, $\{a, c, d\}$. The LP optimum is $x = (\frac12, \frac12, 0, \frac12, \frac12)$. Find the frequency $f$, $\text{LP}^*$, and the best threshold $\min_i \max_{j \in T_i} x_j$ of [threshold rounding](/threshold-rounding/). What does the rounding take, and how does its cost compare with $f \cdot \text{LP}^*$, with the bound from the best threshold, and with OPT? Prove that $x$ is optimal with a dual solution.

11. • The analysis of [LP rounding for set cover](/lp-rounding-set-cover/) with $t$ rounds bounds the expected cost by $(t + n e^{-t})\,\text{LP}^*$. For which real $t$ is this bound smallest, and what is its value there? For $n = 150$, compare the integer choices $t = 5$ and $t = \lceil \ln n \rceil = 6$.

12. • The formula has the clauses $x_3 \lor \lnot x_2$, $\lnot x_1 \lor x_3$, $x_1$, $x_2$ and $\lnot x_1 \lor \lnot x_2 \lor \lnot x_3$. Show that $y_1 = y_2 = y_3 = \frac23$ is optimal for the MAX-SAT LP and find $\text{LP}^*$. Compute the expected number of satisfied clauses under LP rounding and under a fair random assignment, and find OPT. Check the result of [LP rounding for MAX-SAT](/max-sat-lp-rounding/) against $\frac34 \text{LP}^*$.

13. • Derandomize the LP rounding of exercise 12 by the [method of conditional expectations](/method-of-conditional-expectations/), fixing $x_1$, then $x_2$, then $x_3$, and breaking ties toward true. Give the conditional expectations at each step and the final assignment.

14. • The universe is $\{1, \dots, 6\}$, with sets $A = \{1, 2, 3\}$ and $B = \{4, 5, 6\}$ of cost 15 and $C = \{1, 2, 4, 5\}$ of cost 18. Run greedy set cover and record the price of each element. Find the smallest $\gamma$ for which the prices divided by $\gamma$ form a feasible dual, and compare it with $H_4$. Use [dual fitting](/dual-fitting/) to show that the greedy cost is $\gamma \cdot \text{LP}^*$ here, and find $\text{LP}^*$ and OPT.

15. • Facilities $A$ and $B$ stand at points 3 and 4 of a line, with opening costs 3 and 2. Clients stand at $0, 1, 2, 5$, and the distance is the service cost. Run the [Jain-Vazirani algorithm](/jain-vazirani-facility-location/): give the times at which the facilities open, the values $\alpha_j$, the facilities kept in phase 2, and the cost. Compare the cost with $\sum_j \alpha_j$, with OPT and with the bound $C + 3F \le 3 \sum_j \alpha_j$.

16. • Two machines and three jobs have times $p_{1j} = (4, 2, 2)$ and $p_{2j} = (1, 1, 2)$ and costs $c_{1j} = (1, 1, 1)$ and $c_{2j} = (2, 2, 1)$, with target $T = 4$. An optimal LP solution is $x_{11} = x_{21} = \frac12$, $x_{12} = 1$, $x_{23} = 1$. Run the [Shmoys-Tardos algorithm](/shmoys-tardos-gap/): give the slots, the jobs joined to each, a minimum cost matching, and the loads. Compare the cost with the LP value and the loads with $2T$. What is the least cost of an assignment with all loads at most $T$?

17. • A bin packing instance has two items of size $0.6$ and three of size $0.4$. Write the [configuration LP](/configuration-lp/), with one variable for each way to fill a bin. Find $\text{LP}^*$ and prove it optimal with a dual solution, and check that every configuration satisfies the dual constraint. Compare $\text{LP}^*$ with the total size and with OPT.

18. • Maximum coverage with $k = 2$ has the sets $S_1 = \{a, f\}$, $S_2 = \{c, e, f\}$, $S_3 = \{a, b, c\}$, $S_4 = \{b, d, e\}$. The LP optimum is $x = (\frac12, \frac12, \frac12, \frac12)$. Compute $L(x)$ and the expected coverage $F(x)$, and check $F(x) \ge \frac34 L(x)$. Run [pipage rounding](/pipage-rounding/), moving first along $e_1 - e_2$ and then along $e_3 - e_4$; give $F$ at the ends of each move and the final two sets. Find OPT.

19. • In the graphic matroid of a triangle with edges $e_1, e_2, e_3$, the bases are the three pairs of edges, and $x = (\frac23, \frac23, \frac23)$ is in the base polytope. Show that only one distribution over the bases has these marginals. What does [swap rounding](/swap-rounding/) output, whatever the order of its merges? Check negative correlation for $e_1$ and $e_2$.

20. • The threshold rounding for the [prize-collecting Steiner tree](/prize-collecting-steiner-tree/) pays at most $(\gamma / \alpha) \sum_e c_e x_e$ for the tree and at most $\frac{1}{1 - \alpha} \sum_v \pi_v (1 - y_v)$ for the penalties, where $\gamma = 2$ is the factor of the Steiner tree step. For a general $\gamma \ge 1$, find the best threshold $\alpha$ and the ratio it gives. What do you get when the graph is a tree, so that $\gamma = 1$?

21. ★ A cycle has $k \ge 3$ terminals $t_1, \dots, t_k$ joined in order by edges of cost 2, and a hub $h$ is joined to every terminal by an edge of cost $1 + \varepsilon$, with $0 < \varepsilon < 1 - 2/k$. All terminals must be connected. Run the [Goemans-Williamson algorithm](/goemans-williamson-steiner-forest/) and give its forest, its cost and its dual. Find OPT and the LP optimum. Show that the cost is exactly $(2 - 2/k)\,\text{LP}^*$ and that the ratio to OPT tends to $2 - 2/k$ as $\varepsilon \to 0$.

22. ★ The [Shmoys-Tardos-Aardal algorithm](/shmoys-tardos-aardal-facility-location/) with level $\alpha$ costs at most $F_{\text{LP}}/\alpha + 3 C_{\text{LP}}/(1 - \alpha)$. Suppose $F_{\text{LP}} = C_{\text{LP}}$. Which $\alpha$ minimizes the bound, and what ratio to $\text{LP}^*$ does it give? Compare with $\alpha = \frac14$.

23. ★ In [LP rounding for MAX-SAT](/max-sat-lp-rounding/), set $x_i$ true with probability $g(y_i) = 1 - 4^{-y_i}$ in place of $y_i$. Show that $1 - 4^{-y} \le g(y) \le 4^{y - 1}$ on $[0, 1]$, and use these two bounds to prove that every clause is satisfied with probability at least $\frac34 z_j$. What ratio does this one rounding give, without the random assignment?

24. ★ The [half-integrality](/half-integrality/) entry solves the vertex cover LP through the bipartite double cover $H$, which has vertices $v'$ and $v''$ for each $v$ and edges $u'v''$ and $v'u''$ for each edge $uv$, with $\text{LP}^* = \tau_w(H)/2$. For $K_4$ with weights $1, 2, 3, 4$, find $\tau_w(H)$ and every minimum weight cover of $H$. Which LP solution do they give, and does it agree with exercise 1?

25. ★ Choose $k$ vertices of $K_n$ to cover as many edges as possible, with $n$ even and $k = n/2$. This is maximum coverage with the vertices as sets, and each edge lies in $q = 2$ sets. Find the LP optimum and OPT, and show that their ratio tends to $\frac34 = 1 - (1 - \frac12)^2$. What does this say about the bound of [pipage rounding](/pipage-rounding/) for $q = 2$?
