2. The bases $\{x_1, x_2\}$, $\{x_1, x_3\}$, $\{x_2, x_4\}$ and $\{x_3, x_4\}$ give the basic feasible solutions $(3, 1, 0, 0)$, $(2, 0, 2, 0)$, $(0, 4, 0, 6)$ and $(0, 0, 4, 2)$, the corners $(3, 1)$, $(2, 0)$, $(0, 4)$ and $(0, 0)$. The bases $\{x_1, x_4\}$ and $\{x_2, x_3\}$ give $(4, 0, 0, -2)$ and $(0, -2, 6, 0)$, which are not feasible. The objective is 7, 4, 4 and 0 at the four corners, so the maximum is 7 at $(3, 1)$.

5. Only the rows with $d_p > 0$ count: $4/2 = 2$ and $3/3 = 1$. So $t = 1$, the third basic variable leaves, and $x_B$ becomes $(2, 7, 0)$. With $d = (-1, 0, -2)$ no basic variable falls, every $t \ge 0$ is feasible, and the method reports that the program is unbounded.

6. Three constraints are tight, one more than a point in the plane needs. All three slacks are zero, so a basis must hold $x_1$, $x_2$ and one of the slacks: there are three bases, and each of the three $3 \times 3$ matrices is nonsingular. Each has a basic variable equal to zero, which is what degenerate means.

7. The upper bound is $x \le 4 - y$ and the lower bounds are $x \ge 1 + y$ and $x \ge 0$. The pairs give $1 + y \le 4 - y$, that is $y \le 3/2$, and $y \le 4$. With $y \ge 0$ the projection is $[0, 3/2]$. At $y = 3/2$ the only choice is $x = 5/2$.

9. From $(0, 0)$ go along $(2, 1)$: the first row becomes $-t \le 1$, the second $0 \le 2$, and the objective is $5t$. The dual is $\min y_1 + 2y_2$ subject to $-y_1 + y_2 \ge 2$, $y_1 - 2y_2 \ge 1$, $y \ge 0$. Twice the first row plus the second gives $-y_1 \ge 5$, which no $y_1 \ge 0$ satisfies. The primal is unbounded and the dual infeasible.

11. At the origin $r = (-2, -1, 0, 0)$, so $x_1$ enters; the ratios are 4 and 2, and $x_4$ leaves. At $(2, 0)$ the reduced costs are $r_2 = -3$ and $r_4 = 2$; $x_2$ enters, and only $x_3$ gives a ratio, $2/2 = 1$. The method stops at $(3, 1)$ with value $-7$, multipliers $y = (-3/2, -1/2)$ and reduced costs $r_3 = 3/2$, $r_4 = 1/2$. Then $A^\top y \le c$ and $b^\top y = -6 - 1 = -7$.

12. The dual is $\min 4y_1 + 5y_2$ subject to $y_1 \ge 1$, $y_1 + y_2 \ge 2$, $y_1 + 2y_2 \ge 3$, $y \ge 0$, and $y = (1, 1)$ gives 9. The objective is the sum of the two rows, so no feasible $x$ does better than $4 + 5 = 9$. Both $y_i$ are positive, so an optimal $x$ is a feasible $x$ with both rows tight. These are the points $(t - 1,\ 5 - 2t,\ t)$ for $1 \le t \le 5/2$, a segment whose ends are the two given points.

13. Solve the two tight rows: $x_1 = (18 - b_1)/5$ and $x_2 = (3b_1 - 9)/5$. Both are nonnegative for $3 \le b_1 \le 18$, and the dual $y^* = (7/5, 1/5)$ does not depend on $b$, so the basis stays optimal there, with value $(7b_1 + 9)/5$. For $b_1 \ge 18$ the optimum stays at $(0, 9)$ with value 27, and the first constraint has shadow price 0.

16. Apply strong duality to $\min 0$ subject to $Ax = b$, $x \ge 0$. Its dual $\max b^\top y$ subject to $A^\top y \le 0$ is feasible with $y = 0$. If the dual had an optimum, so would the primal; so when the primal is infeasible the dual is unbounded, and some $y$ has $A^\top y \le 0$ and $b^\top y > 0$. Negate it. For the converse, a feasible $x$ would give $0 \le x^\top A^\top y = b^\top y < 0$.

18. The row minima are $-1$ and $-2$ and the column maxima are $3$ and $1$, so $\max \min = -1 < 1 = \min \max$. The row player plays $(3/7, 4/7)$, the column player $(2/7, 5/7)$, and the value is $1/7$: each strategy gives $1/7$ against both pure strategies of the other player.

19. The vertices are $(0, 0, 0)$, $(1, 0, 0)$, $(1, 80, 0)$, $(1, 80, 8200)$, $(1, 0, 9800)$ and $(0, 0, 10000)$: five pivots. At $(1, 80, 0)$ both $s_1$ (reduced cost $-100$) and $x_3$ (reduced cost $-1$) can enter; Bland's rule takes $x_3$ for its lower index, and so it skips the two vertices with $x_1 = 0$, $x_2 = 100$ that Dantzig's rule visits.

21. From the artificial basis the reduced costs of $x_1$ and $x_2$ are both $-3$. Enter $x_1$; the ratios are 1 and $3/2$, so $a_1$ leaves. At $x_1 = 1$, $a_2 = 1$ the multipliers are $y = (-2, 1)$, and every reduced cost is nonnegative, so the least sum is 1. The vector $y$ has $A^\top y = 0$ and $b^\top y = 1 > 0$, so no $x \ge 0$ has $Ax = b$.

22. If $P$ contains a line $\{x + td\}$, then $Ad = 0$, so $\operatorname{rank} A < n$, and every row tight at a point is orthogonal to $d$, so no point has $n$ independent tight rows. If $\operatorname{rank} A = n$, take $x \in P$ whose tight rows have the largest rank. If that rank is below $n$, take $d \ne 0$ orthogonal to them; some row has $a_i^\top d \ne 0$, so moving along $d$ or $-d$ makes a new row tight, and that row is not in the span of the old ones.

23. The volume ratio is $\frac{n}{n+1} \left(\frac{n^2}{n^2 - 1}\right)^{(n-1)/2}$. Use $1 + t < e^t$ for $t \ne 0$ on both factors: the first is less than $e^{-1/(n+1)}$ and the second less than $e^{(n-1)/(2(n^2-1))} = e^{1/(2(n+1))}$.

24. Fix $j$ and maximize $x_j$ over the optimal set $\{Ax = b,\ x \ge 0,\ c^\top x \le f^*\}$. If the maximum is positive, some optimal $x$ has $x_j > 0$. If it is 0, the dual of this program has a solution $(u, t)$ with $A^\top u + t c \ge e_j$, $t \ge 0$ and $b^\top u + t f^* = 0$; if $t > 0$ then $y = -u/t$ is dual optimal with a positive slack in column $j$, and if $t = 0$ then $y^* - u$ is, for any dual optimum $y^*$. Average the solutions found for all $j$: the optimal sets are convex, and a positive entry stays positive.

25. The set of $\lambda$ with $b + \lambda d$ in $\{Ax : x \ge 0\}$ is convex, so it is an interval, and there the primal is feasible and, by weak duality, bounded, so $z(\lambda)$ is finite. By strong duality $z(\lambda)$ is the maximum of $(b + \lambda d)^\top y$ over the fixed dual region, which has a vertex because $A^\top$ has rank $m$ (Exercise 22). So $z(\lambda)$ is the maximum of finitely many linear functions of $\lambda$, one per dual vertex.

26. The function is convex. Pair the lines; of a pair with equal slopes drop the lower one, and for the other pairs take the median $x_m$ of the crossing points. In $O(m)$ time find the lines that attain the maximum at $x_m$; their least and greatest slopes tell whether the optimum is at $x_m$, to its left or to its right. If it is to the left, then for each pair that crosses at or right of $x_m$ the line with the larger slope is below the other one on that side, so it can be dropped. About $m/4$ lines go each round, so $T(m) = T(3m/4) + O(m) = O(m)$.
