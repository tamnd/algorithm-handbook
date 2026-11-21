1. The row player's best responses are T against L, M against C and B against R. The column player's are L against T, C against M and L against B. The cells where the two best responses meet are (T, L) and (M, C), so these are the two pure equilibria. (B, R) is not one: against B the column player gets 2 from L and only 1 from R.

2. T is worse than M against R, and B is worse than M against L, so neither pure strategy dominates M. The mix gives $5p$ against L and $2(1 - p)$ against R. Both beat 1 when $p > 1/5$ and $p < 1/2$, so the answer is $1/5 < p < 1/2$.

3. Check the four cells: at each, one player gains by a switch. In the mixed equilibrium the inspector makes the worker indifferent: with $q$ the probability of Inspect, $1 = -q + 2(1 - q)$, so $q = 1/3$. The worker makes the inspector indifferent: with $p$ the probability of Work, $-p + (1 - p) = -2(1 - p)$, so $p = 3/4$. The worker gets 1 and the inspector gets $-1/2$.

4. Neither. A row player told F knows that the column player is told O or F with probability $1/2$ each, so F gives $1/2$ and O gives 1: the row player disobeys, and the distribution is not a correlated equilibrium. It is not coarse correlated either: it gives the row player $3/4$, and always playing O gives 1.

5. $3 \cdot 2 \cdot 2 = 12$ pure strategies. A mixed strategy is a distribution on 12 points, so it needs 11 numbers. A behaviour strategy needs $2 + 1 + 1 = 4$.

6. The row player gets $0.6 \cdot 0.5 + 0.4 \cdot 0.5 = 1/2$, and both pure strategies also give $1/2$, so the row player gains 0. The column player gets $1/2$ now and $0.6$ from tails, so it gains $1/10$. Hence $\varepsilon = 1/10$.

7. Each player has a table of $2 \cdot 2 \cdot 2 = 8$ numbers, so the graphical game needs $8 \cdot 20 = 160$. The normal form gives each of the 20 players a payoff at each of $2^{20}$ profiles: $20 \cdot 2^{20} = 20{,}971{,}520$ numbers.

8. Grim trigger needs $R/(1 - \delta) \ge T + \delta P/(1 - \delta)$, that is $4 \ge 6 - 5\delta$, so $\delta \ge 2/5$. Against tit for tat, the best deviations are to defect for ever, which needs $\delta \ge (T - R)/(T - P) = 2/5$, and to alternate D and C, which needs $\delta \ge (T - R)/(R - S) = 1/2$. So tit for tat is a best reply to itself for $\delta \ge 1/2$.

9. With rows and columns (Hawk, Dove), the row payoffs are $\begin{pmatrix} -1 & 4 \\ 0 & 2 \end{pmatrix}$. The mix with hawk share $p$ makes hawks and doves equal when $-p + 4(1 - p) = 2(1 - p)$, so $p = 2/3$, and both earn $2/3$ against it.

17. At the start, check each row and column against each other pure one: every pair has a column or row where the order flips. B is dominated by any mix $q\,\mathrm{T} + (1 - q)\,\mathrm{M}$ with $0 < q < 1$, and after B goes, L is dominated by $q\,\mathrm{C} + (1 - q)\,\mathrm{R}$ for $1/2 < q < 1$. Then T dominates M and R dominates C, leaving (T, R) with payoffs (3, 2).

21. If $(x, y)$ is an equilibrium, $x^{\mathsf T} M y' \ge x^{\mathsf T} M y \ge x'^{\mathsf T} M y$ for all $x', y'$, which forces $x$ and $y$ to be optimal and the payoff to be the value $v$. Conversely, optimal $x$ and $y$ give $v \le x^{\mathsf T} M y \le v$. Each set is the set of optimal solutions of a linear program, so it is a polytope.

22. For uniform $x$ and any $y$, $u(x, y) = c/3$, so the first ESS condition holds with equality against every mutant. Write the payoff matrix as $cI$ plus an antisymmetric matrix; then $u(y, y) = c \lvert y \rvert^2$, and $\lvert y \rvert^2 > 1/3$ for $y \ne x$. The second condition $u(x, y) > u(y, y)$ holds for every mutant exactly when $c < 0$.

23. Let the CE put weights $\alpha, \beta, \gamma, \delta$ on the four cells. Each of the four incentive constraints says that one weight times a positive number is at least another weight times a positive number, and the four constraints chain around the cycle of best responses. Going round the chain gives equality in each, which fixes the ratios of the weights, and these ratios are those of the product of the mixed equilibrium.

24. Let $T_i(a, b)$ be true when players $1, \ldots, i$ can play actions with $a_{i-1} = a$ and $a_i = b$ such that players $1, \ldots, i - 1$ are all playing best responses. To extend to $i + 1$, check for each $(a, b, c)$ whether $b$ is a best response of player $i$ to $(a, c)$; there are $k^3$ triples per step. Keep back pointers to recover an equilibrium.
