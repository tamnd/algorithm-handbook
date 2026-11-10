1. $S = 3$. Next fit uses 4 bins, $[0.4]$, $[0.7, 0.3]$, $[0.6, 0.2]$, $[0.5, 0.3]$. First fit uses 4, $[0.4, 0.3, 0.2]$, $[0.7, 0.3]$, $[0.6]$, $[0.5]$. Best fit uses 3, $[0.4, 0.6]$, $[0.7, 0.3]$, $[0.2, 0.5, 0.3]$, and so does first fit decreasing. Since $\lceil S \rceil = 3$, best fit and first fit decreasing are optimal.

3. $\lceil S \rceil = \lceil 3.75 \rceil = 4$, and three items exceed $1/2$. A bin with a $0.6$ item has room only for a $0.3$ item, so the three $0.45$ items share no bin with a $0.6$ item, and they do not fit in one bin. So OPT $= 3 + 2 = 5$.

5. Greedy takes $C$ (cost $7/3$ per element), then $D$ ($7/2$), then $A$ or $B$ (10 for one element), for a total of 24. OPT is $A$ and $B$, cost 20. Here $d = 4$, $H_4 = 25/12$ and the bound is about $41.7$; $f = 2$.

7. Leaves 1, 2 and 3 go tight one by one, leaving the centre with residual weight 1; the fourth edge makes leaf 4 and the centre tight together. The cover is the centre and four leaves, of weight 8; the dual is 4, and OPT is 4. All four leaves are redundant, and the ratio 2 is reached.

8. For $k = 2$ the centres are $0$ and $14$ and the radius is 7; OPT is 4, with centres 3 and 13, so the ratio is $7/4$. For $k = 3$ the third centre is 7 and the radius is 3; OPT is 2, since the gaps split the points into four groups and two of them must share a centre. The ratio is $3/2$.

10. The algorithm buys $C$ ($y_1 = 7$), then $A$ ($y_3 = 3$), then $D$ ($y_6 = 4$), for cost 24, dual 14 and bound 28; reverse delete removes nothing. The LP optimum is 17, at $x = \frac12$ on every set, and the dual with $y = 7$ on element 1, $y = 3$ on element 4 and $y = 7$ on element 6 is feasible with value 17. Threshold rounding takes all four sets, cost $34 = 2 \cdot \text{LP}^*$.

13. Take a set $X$ of cost 1 covering 2 elements and a set $Y$ of cost $B$ covering $B$ other elements, with budget $B \ge 3$. Greedy takes $X$ first, and then $Y$ no longer fits, so greedy covers 2 elements against $B$. Taking the better of the greedy answer and the best single set that fits removes the example.

15. OPT is 2. The LP sets $x_1 = 1$ and $x_2 = \frac45$, value $\frac95$. For a set $S$ already taken, the inequality is $\sum_{i \notin S} \min(a_i, D_S)\, x_i \ge D_S$, where $D_S$ is the demand left. $S = \{1\}$ gives $x_2 + x_3 \ge 1$, and $S = \{2, 3\}$ gives $x_1 \ge 1$.

21. Take a spanning tree of each component and colour it properly with two colours. Each vertex has a tree neighbour of the other colour, so each colour class dominates its component. Take the smaller class in each component.

22. View the 2-sets as edges. In a minimum cover the chosen edges contain no path of three edges, since the middle one could be dropped, so they form a forest of stars. One edge from each star is a matching, and counting elements shows that it has $n - \text{OPT}$ edges. Conversely, a matching of size $\nu$ plus one set for each unmatched element is a cover.

23. If a vertex $x$ of the polytope has a coordinate outside $\{0, \frac12, 1\}$, let $V^+$ be the vertices with $\frac12 < x_v < 1$ and $V^-$ those with $0 < x_v < \frac12$. Add $\varepsilon$ on $V^+$ and subtract it on $V^-$, then do the opposite. Both points are feasible for small $\varepsilon$, and $x$ is their midpoint.

24. After the small items an algorithm has $b$ bins, and OPT is $n/2$ at this point, so the ratio is at least $2b/n$. If the large items follow, each of them needs a bin with no other large item and at most one small item, so the algorithm ends with at least $2n - b$ bins against OPT $= n$. The larger of $2b/n$ and $(2n - b)/n$ is at least $\frac43$.

25. A basic optimum has at most $m$ fractional coordinates, since only $m$ constraints besides the bounds $0 \le x_j \le 1$ can be tight with fractional values. Rounding them down loses at most $m$ times the best single item. For knapsack, $m = 1$ gives ratio 2.
