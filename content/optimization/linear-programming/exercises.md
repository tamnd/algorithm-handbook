1. ◦ Convert to the equality [standard form](/lp-standard-form/) $\min c^\top x$, $Ax = b$, $x \ge 0$: maximize $x_1 - 2x_2$ subject to $x_1 + x_2 \ge 2$, $x_1 - x_2 \le 3$, $x_1 \ge 0$ and $x_2$ free. Name each new variable and say why it is there.

2. ◦ Add [slack variables](/slack-variables/) $x_3, x_4$ to the constraints $x_1 + x_2 \le 4$, $x_1 - x_2 \le 2$, $x \ge 0$. List all six basic solutions of the system $x_1 + x_2 + x_3 = 4$, $x_1 - x_2 + x_4 = 2$, say which are [basic feasible solutions](/basic-feasible-solution/), and match those with the corners of the region in the $(x_1, x_2)$ plane. Then find the maximum of $2x_1 + x_2$ by checking the corners.

3. ◦ Write the [dual](/dual-linear-program/) of: maximize $2x_1 + 3x_2$ subject to $x_1 + 2x_2 \le 8$, $3x_1 + x_2 \le 9$, $x \ge 0$. Check that $x = (2, 3)$ and $y = (7/5, 1/5)$ are feasible and have the same objective value. What does [weak duality](/weak-duality/) let you conclude?

4. ◦ Show that the system $x_1 + x_2 \le 2$, $x_1 - x_2 \ge 3$, $x_2 \ge 0$ has no solution by giving nonnegative multipliers of its three rows, written in the form $a^\top x \le \beta$, whose sum reads $0 \le -1$. This is the certificate of [Farkas' lemma](/farkas-lemma/).

5. ◦ In one step of the [simplex method](/simplex-method/) the basic variables are $x_B = (4, 6, 3)$, and the entering column gives $d = (2, -1, 3)$, so that $x_B$ becomes $x_B - t d$ when the entering variable is $t$. Apply the [ratio test](/ratio-test/): what is the step $t$, which basic variable leaves, and what is the new $x_B$? What does the method report if instead $d = (-1, 0, -2)$?

6. ◦ The region $x_1 + x_2 \le 2$, $x_1 \le 1$, $x_2 \le 1$, $x \ge 0$ has a corner at $(1, 1)$. Add slacks $s_1, s_2, s_3$. How many constraints are tight at $(1, 1)$, and how many different bases have $(1, 1)$ as their basic solution? Why is the point [degenerate](/lp-degeneracy/)?

7. ◦ Use [Fourier-Motzkin elimination](/fourier-motzkin-elimination/) to remove $x$ from the system $x + y \le 4$, $x - y \ge 1$, $x \ge 0$, $y \ge 0$. Which inequalities in $y$ remain, and what is the projection of the region onto the $y$-axis? Give a point of the region with the largest $y$.

8. ◦ For the program of Exercise 3 the optimal dual is $y^* = (7/5, 1/5)$. Use the [shadow price](/shadow-price/) of the first constraint to predict the optimum when its right-hand side rises from 8 to 9. Then solve the new program and check the prediction.

9. ◦ Show that maximizing $2x_1 + x_2$ subject to $-x_1 + x_2 \le 1$, $x_1 - 2x_2 \le 2$, $x \ge 0$ is unbounded, by giving a feasible point and a direction along which the objective grows for ever. Write the dual and show directly that it is infeasible. Which case of [LP duality](/lp-duality/) is this?

10. ◦ The $d$-dimensional cube $[0, 1]^d$ is a polytope with $2d$ facets. What bound does the [Hirsch conjecture](/hirsch-conjecture/) give for the diameter of its graph, and what is the diameter? Is the bound tight here?

11. • Run the simplex method with [Dantzig's rule](/dantzig-pivot-rule/) on: minimize $-2x_1 - x_2$ subject to $x_1 + x_2 + x_3 = 4$, $x_1 - x_2 + x_4 = 2$, $x \ge 0$, from the basis $\{x_3, x_4\}$. At each step give the basis, the point, the [reduced costs](/reduced-cost/) and the ratios. Give the final multipliers $y$ and check that they prove optimality.

12. • Maximize $x_1 + 2x_2 + 3x_3$ subject to $x_1 + x_2 + x_3 \le 4$, $x_2 + 2x_3 \le 5$, $x \ge 0$. Show that $y = (1, 1)$ is an optimal dual solution, and use [complementary slackness](/complementary-slackness/) to show that $(0, 3, 1)$ and $(3/2, 0, 5/2)$ are both optimal. Describe the set of all optimal solutions.

13. • For the program of Exercise 3, let the first right-hand side be $b_1$ in place of 8. For which values of $b_1$ does the basis of the optimum $(2, 3)$ stay optimal? Give the optimal value as a function of $b_1$ on that range, and say what happens for larger $b_1$ ([sensitivity analysis](/lp-sensitivity-analysis/)).

14. • Fourier-Motzkin elimination of one variable from $m$ inequalities, half of which bound it from above and half from below, gives $m^2/4$ new inequalities. Show that if this happens at every step, then after $k$ eliminations there are $4(m/4)^{2^k}$ inequalities.

15. • Take the dual of the equality-form dual $\max b^\top y$ subject to $A^\top y \le c$, $y$ free, by the general rule of the [dual linear program](/dual-linear-program/) page, and show that you get back $\min c^\top x$ subject to $Ax = b$, $x \ge 0$.

16. • Assume [strong duality](/strong-duality/), proved by the [simplex method](/simplex-method/) and not from Farkas' lemma. Derive this form of Farkas' lemma: the system $Ax = b$, $x \ge 0$ has no solution if and only if some $y$ has $A^\top y \ge 0$ and $b^\top y < 0$.

17. • A directed graph has the arcs $s \to a$ of length 1, $s \to b$ of length 4, $a \to b$ of length 2, $a \to t$ of length 6 and $b \to t$ of length 3. Write the [shortest path linear program](/shortest-paths-lp-formulation/) with one distance variable per vertex, give its optimal solution, and give an optimal solution of its dual. Check complementary slackness: on which arcs does the dual put flow, and which constraints are tight?

18. • In a zero-sum game the row player gets $3$, $-1$ in row 1 and $-2$, $1$ in row 2 against columns 1 and 2. Show that the game has no saddle point. Write the row player's problem as a linear program and its dual as the column player's problem, and solve both. What is the value of the game?

19. • Run the simplex method with [Bland's rule](/bland-rule/) on the three-variable [Klee-Minty cube](/klee-minty-cube/): minimize $-100x_1 - 10x_2 - x_3$ subject to $x_1 \le 1$, $20x_1 + x_2 \le 100$, $200x_1 + 20x_2 + x_3 \le 10000$, $x \ge 0$, with slacks $s_1, s_2, s_3$ and the index order $x_1, x_2, x_3, s_1, s_2, s_3$. Start from the slack basis. List the vertices it visits. How many pivots does it make, against 7 for Dantzig's rule?

20. • Show that a polyhedron $\{x \in \mathbb{R}^n : Ax \le b\}$ with $m$ rows has at most $\binom{m}{n}$ vertices. Compare the bound with the number of vertices of the cube $[0, 1]^3$.

21. • Run phase one of the [two-phase method](/two-phase-simplex-method/) on $x_1 + x_2 = 1$, $2x_1 + 2x_2 = 3$, $x \ge 0$, with artificial variables $a_1, a_2$. Show that the least sum of the artificials is 1, and read a Farkas certificate of infeasibility from the final multipliers.

22. ★ Prove that a nonempty polyhedron $P = \{x \in \mathbb{R}^n : Ax \le b\}$ has a vertex if and only if it contains no line, and that both hold if and only if $A$ has rank $n$.

23. ★ The [ellipsoid method](/ellipsoid-method/) replaces half of the unit ball in $\mathbb{R}^n$, $n \ge 2$, by an ellipsoid with one semi-axis $n/(n+1)$ and $n - 1$ semi-axes $n/\sqrt{n^2 - 1}$. Prove that its volume is less than $e^{-1/(2(n+1))}$ times the volume of the ball.

24. ★ Let $\min c^\top x$, $Ax = b$, $x \ge 0$ and its dual have optimal solutions. Prove that there are optimal $x^*$ and $y^*$ such that for every $j$ exactly one of $x^*_j$ and $c_j - A_j^\top y^*$ is zero. (This is the theorem of Goldman and Tucker on strict complementarity.)

25. ★ Let $A$ have rank $m$ and let $\{y : A^\top y \le c\}$ be nonempty. Prove that the optimal value $z(\lambda)$ of $\min c^\top x$ subject to $Ax = b + \lambda d$, $x \ge 0$ is finite on an interval of $\lambda$, possibly empty or unbounded, and is a convex piecewise linear function there ([parametric linear programming](/parametric-linear-programming/)).

26. ★ Give an $O(m)$ algorithm that minimizes $\max_i (a_i x + b_i)$ over $x \in \mathbb{R}$, or reports that it is unbounded below, for $m$ given lines, without sorting. This is a linear program in two variables, and the method is the first step of [Megiddo's algorithm](/megiddo-fixed-dimension-lp/). Use [prune and search](/prune-and-search/) and the [median of medians](/median-of-medians/).
