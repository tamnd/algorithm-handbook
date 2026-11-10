1. The LP optimum is $(1, \tfrac15, 1)$ with value 21, and the integer optimum is 19 at $(1, 0, 1)$. The only minimal cover is $\{1, 2\}$: the set $\{2, 3\}$ weighs exactly 8, so it is not a cover. The cut $x_1 + x_2 \le 1$ has the value $\tfrac65$ at the LP optimum. With the cut, the LP value drops to 19, the integer optimum.

3. $A_1$ is an interval matrix and $A_4$ is the incidence matrix of a directed 3-cycle, so both are TU. $\det A_2 = 2$, and with $b = (1, 1, 1)$ the point $(\tfrac12, \tfrac12, \tfrac12)$ is a vertex. $\det A_3 = 2$, and with $b = (0, 1)$ the point $(\tfrac12, \tfrac12)$ is a vertex.

5. The point with every coordinate $\tfrac12$ is feasible with value $\tfrac52$. Adding the five edge constraints gives $2\sum_v x_v \ge 5$, so $\tfrac52$ is optimal. A cover of an odd cycle needs at least $\lceil 5/2 \rceil = 3$ vertices, and 3 suffice. The gap is at least $\tfrac65$.

10. For $a$, $q^- = 0.3 \cdot 10 = 3$ and $q^+ = 0.7 \cdot 2 = 1.4$. For $b$, $q^- = q^+ = 2$. With $\mu = 1/6$, $a$ scores $\tfrac56 \cdot 1.4 + \tfrac16 \cdot 3 = \tfrac53$ and $b$ scores 2, so $b$ wins. With the product, $a$ scores 4.2 and $b$ scores 4, so $a$ wins.

11. With $f_0 = \tfrac14$, the fractional cut is $0.75 s_1 + 0.5 s_2 \ge 0.25$, that is $3s_1 + 2s_2 \ge 1$. The mixed-integer cut takes the coefficients $\min\{f_j / f_0,\ (1 - f_j)/(1 - f_0)\}$ and reads $\tfrac13 s_1 + \tfrac23 s_2 \ge 1$; with the same right side, each of its coefficients is smaller. It is tight at $(s_1, s_2) = (1, 1)$, where $x_1 = 1$, and at $(3, 0)$, where $x_1 = 0$. If $s_2$ is continuous, its coefficient becomes $\bar a_2 / f_0 = 2$.

12. The inverse of the basis gives $x_1 + \tfrac23 s_1 - \tfrac13 s_2 = \tfrac43$. Here $f_0 = \tfrac13$ and both fractional parts are $\tfrac23$, so the fractional cut is $\tfrac23(s_1 + s_2) \ge \tfrac13$ and the mixed-integer cut is $\tfrac12(s_1 + s_2) \ge 1$. Since $s_1 + s_2 = 8 - 3x_1 - 3x_2$, they read $x_1 + x_2 \le \tfrac52$ and $x_1 + x_2 \le 2$. The hull is $\{x \ge 0 : x_1 + x_2 \le 2\}$, which is cut out by one rank-one cut, so the rank is 1.

15. The minimal covers are $\{1, 2\}$, $\{1, 3, 4\}$ and $\{2, 3, 4\}$. The point has weight $6 + 2 + 2 = 10$ and violates $x_1 + x_3 + x_4 \le 2$, since $\sum_{j \in C} (1 - x^*_j) = \tfrac56 < 1$. With $x_1 = 1$ the capacity left is 4, and only one of items 2, 3, 4 fits, so $\alpha_1 = 2 - 1 = 1$. The lifted cut $x_1 + x_2 + x_3 + x_4 \le 2$ has the value $\tfrac{13}{6}$ at $x^*$, so it cuts it off too.

16. With $x_j$ workers starting in hour $j$, the rows are $x_1 \ge 2$, $x_1 + x_2 \ge 3$, $x_1 + x_2 + x_3 \ge 4$, $x_2 + x_3 \ge 3$ and $x_3 \ge 2$. Each column has consecutive ones, so the matrix is TU. Adding the rows of hours 2 and 5 gives $x_1 + x_2 + x_3 \ge 5$, and $x = (2, 1, 2)$ attains it.

18. Fill a table $R[0..b]$ with $R[0]$ true and $R[v]$ true when $R[v - a_j]$ is true for some $a_j \le v$. For $(4, 7)$ the values with no solution are 1, 2, 3, 5, 6, 9, 10, 13 and 17. The time is polynomial in $b$, not in its number of bits, so the algorithm is pseudo-polynomial.

19. The dual of the subproblem is $\max\{2u - 2yv : u - v \le 1,\ u \le 4,\ u, v \ge 0\}$, with vertices $(0, 0)$, $(1, 0)$ and $(4, 3)$. At $y = 0$ the subproblem costs 8 with the dual solution $(4, 3)$. The cut is $\eta \ge 8 - 6y$ and the upper bound is 8. The master then picks $y = 1$, $\eta = 2$, with lower bound 5. At $y = 1$ the subproblem costs 2, so the upper bound is 5 as well. The optimum is $y = 1$, $x = (2, 0)$, with value 5.

21. If the graph is bipartite, use the sufficient condition for two nonzeros per column, with the two sides of the graph as the two classes. If it is not, it has an odd cycle. The rows of its vertices and the columns of its edges form a square submatrix with determinant $\pm 2$.

22. Every $k \times k$ minor of $A'$ equals, up to sign, an $m \times m$ minor of $[I \;\, A']$: add the identity columns of the rows it does not use. The $m \times m$ minors of $B^{-1}[I \;\, A]$ are those of $[I \;\, A]$ divided by $\det B = a_{rs} = \pm 1$, and those are minors of $A$ up to sign.

23. Let $s = \mathbf{1}^T A_R$ and $Q = \{x \in [0,1]^R : \lfloor s/2 \rfloor \le x^T A_R \le \lceil s/2 \rceil\}$. The matrix of $Q$ is TU and $Q$ contains $\tfrac12 \mathbf{1}$, so $Q$ has an integral vertex $\bar x$. Put the rows with $\bar x_i = 1$ into $R_1$. The signed column sums are $2\bar x^T A_R - s$, which lie in $\{-1, 0, 1\}$.

24. First, a vertex has $x_v \le 1$: if $x_v > 1$, no tight constraint contains $x_v$. Let $V^+ = \{v : 0 < x_v < \tfrac12\}$ and $V^- = \{v : \tfrac12 < x_v < 1\}$. If either is nonempty, add $\varepsilon$ on $V^+$ and subtract it on $V^-$, or the reverse. A tight edge with one end in $V^+$ has its other end in $V^-$, so both points stay feasible for small $\varepsilon$, and $x$ is their midpoint. For the approximation, take the vertices with $x_v \ge \tfrac12$ at an optimal vertex: the cover costs at most twice the LP value.

25. If $ax + by = ab - a - b$ with $x, y \ge 0$, then $a(x + 1) + b(y + 1) = ab$. So $b$ divides $x + 1$ and $a$ divides $y + 1$, and the left side is at least $2ab$. For $\beta > ab - a - b$, take the integer solution with $0 \le x \le b - 1$; then $by = \beta - ax > -b$, so $y \ge 0$. For $(5, 7)$ the answer is 23.
