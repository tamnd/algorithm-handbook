1. ◦ Solve the [LP relaxation](/lp-relaxation/) of $\max\, 12x_1 + 10x_2 + 7x_3$ subject to $4x_1 + 5x_2 + 3x_3 \le 8$, $x \in \{0, 1\}^3$, and find the integer optimum. List every minimal cover of the row, and check that its [cover inequality](/cover-inequality/) cuts off the LP optimum. What is the LP value once the cut is added?

2. ◦ A binary $z$ must force $4x_1 - x_2 \le 2$ when $z = 1$, with $0 \le x_1 \le 3$ and $0 \le x_2 \le 5$. Write the [big-M constraint](/big-m-formulation/) and find the smallest valid $M$. Give a point of the box that $M = 9$ wrongly cuts off when $z = 0$.

3. ◦ Which of these matrices are [totally unimodular](/total-unimodularity/): $A_1 = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}$, $A_2 = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$, $A_3 = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ and $A_4 = \begin{pmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix}$? For each one that is not, give an integral $b$ for which $\{x : Ax \le b,\ x \ge 0\}$ has a fractional vertex.

4. ◦ Solve $\max\, x_1 + x_2$ subject to $2x_1 + x_2 \le 4$, $x_1 + 2x_2 \le 4$, $x \ge 0$ as a linear program. Find multipliers $u \ge 0$ whose [Chvátal-Gomory cut](/chvatal-gomory-cut/) cuts off the LP optimum, and the integer optimum.

5. ◦ Find the optimal value of the LP relaxation of [vertex cover](/vertex-cover/) on the cycle $C_5$, with a proof that no smaller value is possible, and the integer optimum. What lower bound does this give on the [integrality gap](/integrality-gap/) of the relaxation?

6. ◦ A maximization solver has an incumbent of value 95 and a best bound of 100. What is the relative gap? At another node the LP value is 40 and the incumbent is 37. A variable $x_j \ge 0$, integer, is nonbasic at 0 with reduced cost 4. Can $x_j$ be fixed to 0 in the subtree? What if the reduced cost is 2?

7. ◦ Show that $4x + 6y = 9$ has no integer solution in two ways: by a divisibility argument, and by a Chvátal-Gomory proof that derives $0 \le -1$ from the two inequalities $4x + 6y \le 9$ and $-4x - 6y \le -9$. Does $4x + 6y = 10$ have a solution with $x, y \ge 0$?

8. ◦ The incumbent of a 0-1 program is $\bar x = (1, 0, 1, 1, 0)$. Write the [local branching](/local-branching/) function $\Delta(x, \bar x)$ as a linear expression in $x$. How many binary points satisfy $\Delta(x, \bar x) \le 1$? And $\Delta(x, \bar x) \le 2$?

9. ◦ The incumbent of a 0-1 program is $(1, 0, 1, 0, 1, 1)$ and the current LP solution is $(1, 0.4, 1, 0, 0.7, 1)$. Which variables does [RINS](/relaxation-induced-neighborhood-search/) fix, and to what values? How many binary points does the sub-MIP have at most?

10. ◦ Two candidates for [pseudocost branching](/pseudocost-branching/) have these data. Candidate $a$ has fractional part $0.3$ and pseudocosts $\Psi^- = 10$, $\Psi^+ = 2$. Candidate $b$ has fractional part $0.5$ and $\Psi^- = \Psi^+ = 4$. Compute the estimated gains $q^-$ and $q^+$ of each, and the winner under the score $(1 - \mu)\min + \mu \max$ with $\mu = 1/6$ and under the product score.

11. • A row of the optimal tableau of a pure integer program is $x_1 + 0.75 s_1 + 0.5 s_2 = 2.25$, with nonbasic $s_1, s_2 \ge 0$ integer. Write Gomory's fractional cut and the [Gomory mixed-integer cut](/gomory-mixed-integer-cut/), and show that the second dominates the first. Find two integer points with $x_1 \ge 0$ at which the mixed-integer cut is tight. How does the cut change if $s_2$ is continuous?

12. • Return to the program of Exercise 4 and add slacks $s_1, s_2$. Write the optimal tableau row of $x_1$. Derive Gomory's fractional cut and the Gomory mixed-integer cut from this row, and write both in terms of $x_1, x_2$. Find the integer hull and the Chvátal rank of the LP polyhedron.

13. • An interval matrix is a 0-1 matrix whose ones in each column are consecutive. Prove with Ghouila-Houri's characterization in [total unimodularity](/total-unimodularity/) that every interval matrix is TU.

14. • Write an integer $y$ with $0 \le y \le 20$ with binary variables. How many are needed, and what extra constraint keeps $y \le 20$? Show that $w \le x_1$, $w \le x_2$, $w \ge x_1 + x_2 - 1$, $w \ge 0$ force $w = x_1 x_2$ for binary $x_1, x_2$, and give a point of their LP relaxation where $w \ne x_1 x_2$. Linearize $w = x_1 y$ for binary $x_1$ and the integer $y$ above.

15. • For the knapsack row $6x_1 + 5x_2 + 4x_3 + 3x_4 \le 10$ over $\{0,1\}^4$, list all minimal covers. Show that $x^* = (1, 0, \tfrac12, \tfrac23)$ satisfies the row and find the cover inequality it violates. Then lift $x_1$ into the cover inequality of $\{2, 3, 4\}$, and say whether the lifted inequality also cuts off $x^*$.

16. • A shop is open five hours, and each worker works three consecutive hours, starting in hour 1, 2 or 3. The hours need at least 2, 3, 4, 3 and 2 workers. Write the integer program that minimizes the number of workers. Use the [Hoffman-Kruskal theorem](/hoffman-kruskal-theorem/) to explain why its LP relaxation has an integral optimum, then find the optimum and prove it optimal with a combination of two constraints.

17. • Let $T_t = \operatorname{conv}\{(0, 0), (0, 1), (t, \tfrac12)\}$ for an integer $t \ge 1$. Find all integer points of $T_t$ and the LP maximum of $x_1$. Show that LP-based branch and bound that branches on a fractional variable solves $\max\{x_1 : x \in T_t \cap \mathbb{Z}^2\}$ with three nodes, for every $t$, and compare with the number of rounds that [Gomory's algorithm](/gomory-cutting-plane-algorithm/) needs.

18. • Give a dynamic program that decides in $O(nb)$ time whether $a_1 x_1 + \dots + a_n x_n = b$ has a solution in nonnegative integers, for positive integers $a_j$ and $b$. Run it by hand for $(a_1, a_2) = (4, 7)$ and list every $b \le 20$ with no solution. Is your algorithm polynomial in the input size?

19. • Apply [Benders decomposition](/benders-decomposition/) to $\min\, 3y + x_1 + 4x_2$ subject to $x_1 + x_2 \ge 2$, $x_1 \le 2y$, $x \ge 0$, $y \in \{0, 1\}$, with $\eta \ge 0$ as the starting bound on the subproblem cost. Start from $y = 0$. Write the dual of the subproblem, the cut of each iteration, and the lower and upper bounds, until they meet.

20. • Find all minimal covers of $x_1 + x_2 + \dots + x_{2k} \le k$ over $\{0,1\}^{2k}$, and count them for $k = 3$. Show that every one of their cover inequalities is implied by the row and the bounds $0 \le x \le 1$, and explain why.

21. ★ Prove that the vertex-edge incidence matrix of an undirected graph is totally unimodular if and only if the graph is bipartite.

22. ★ Let $A \in \mathbb{Z}^{m \times n}$ be TU and let $a_{rs} \ne 0$. A simplex pivot on $a_{rs}$ multiplies $[I \;\, A]$ on the left by $B^{-1}$, where $B$ is $I$ with column $r$ replaced by column $s$ of $A$. Swap columns $r$ and $m + s$ of $B^{-1}[I \;\, A]$, so that it reads $[I \;\, A']$. Prove that $A'$ is TU.

23. ★ Prove the "only if" half of Ghouila-Houri's characterization: if $A$ is TU, every set $R$ of rows splits into $R_1$ and $R_2$ with $\sum_{i \in R_1} a_{ij} - \sum_{i \in R_2} a_{ij} \in \{0, \pm 1\}$ for every column $j$.

24. ★ Prove that every vertex of $\{x \in \mathbb{R}^V : x_u + x_v \ge 1 \text{ for all } uv \in E,\ x \ge 0\}$ has all its coordinates in $\{0, \tfrac12, 1\}$, for every graph $G = (V, E)$. Use it to give a 2-approximation for [vertex cover](/vertex-cover/).

25. ★ Let $a, b \ge 2$ be coprime integers. Prove that $ab - a - b$ is the largest integer $\beta$ for which $ax + by = \beta$ has no solution in nonnegative integers. What is it for $(a, b) = (5, 7)$?
