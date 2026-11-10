1. ◦ Take $u = (2, 5, 3)$, $v = (2, 4, 3)$ and $w = (1, 6, 2)$, all objectives minimized. For each of the three pairs, say whether one vector weakly dominates, [dominates](/pareto-dominance/) or strictly dominates the other, or whether the two are incomparable.

2. ◦ Let $Y = \{(1, 9), (2, 7), (3, 8), (4, 4), (5, 5), (6, 3), (7, 6), (9, 2), (10, 1)\}$, both objectives minimized. Find the [Pareto front](/pareto-front/) $Y_N$, the [ideal point](/ideal-point/) and the [nadir point](/nadir-point/), and name a dominator of each dominated point.

3. ◦ For the front of exercise 2, which points are supported, that is, minimize $\lambda_1 y_1 + \lambda_2 y_2$ over $Y$ for some $\lambda > 0$? Which of those are extreme points of the convex hull? For the one supported point that is not extreme, give the weights for which it is optimal and the points it ties with.

4. ◦ Sort the eight images $P = (1, 9)$, $Q = (2, 6)$, $R = (3, 8)$, $S = (4, 4)$, $T = (5, 7)$, $U = (7, 2)$, $V = (8, 5)$, $W = (10, 1)$ into fronts by [non-dominated sorting](/non-dominated-sorting/). Give the front number and the Fonseca and Fleming rank of each point, as defined in [Pareto ranking](/pareto-ranking/). Which points have different values under the two rules?

5. ◦ Compute the [crowding distance](/crowding-distance/) of each point of the first front of exercise 4, scaling each objective by its range on that front. If the survival step of [NSGA-II](/nsga-ii/) must keep four of these points, which one goes?

6. ◦ Compute the [hypervolume](/hypervolume-indicator/) of $A = \{(1, 5), (2, 3), (4, 2), (5, 1)\}$ with the reference point $r = (6, 6)$, and the exclusive contribution of each point.

7. ◦ Let $A = \{(1, 5), (3, 3), (5, 1)\}$ and $B = \{(2, 4), (4, 2)\}$. Compute the additive [epsilon indicator](/epsilon-indicator/) $I_{\varepsilon+}(A, B)$ and $I_{\varepsilon+}(B, A)$. Does either set weakly dominate the other?

8. ◦ Let the reference set be $R = \{(0, 6), (3, 3), (6, 0)\}$ and $A = \{(1, 5), (5, 1)\}$. Compute [IGD](/igd-indicator/) and IGD+ of $A$.

9. ◦ On the set $Y$ of exercise 2, which point does the [epsilon-constraint](/epsilon-constraint-method/) problem "minimize $y_1$ subject to $y_2 \le 3$" return? Which point minimizes the [Tchebycheff](/weighted-tchebycheff-method/) function $\max(y_1, y_2)$, with weights $(1, 1)$ and the reference point $(0, 0)$?

10. • Show that the point $(9, 2)$ of exercise 2 minimizes no weighted sum with $\lambda > 0$. Then find weights $w$ for which it is the unique minimizer of $\max_i w_i y_i$ over $Y$, with the reference point $(0, 0)$, and give the value of the function there.

11. • In [NPGA](/npga/), a member with $k$ dominators in a population of $N$ is found dominated by a random comparison set of $t$ members with probability $1 - \binom{N-k}{t} / \binom{N}{t}$. Show that this is $t/N$ for $k = 1$. For $N = 10$, what is the least $t$ that catches a member with one dominator at least half the time?

12. • A [knapsack](/multi-objective-knapsack/) of capacity $8$ holds items of weights $2, 1, 5, 1$ with profit vectors $(3, 4)$, $(5, 3)$, $(1, 8)$, $(7, 1)$, both profits maximized. Find the Pareto front and the subset behind each point. Which points are unsupported? Give an epsilon-constraint problem that finds one of them.

13. • A graph has the arcs $su = (1, 5)$, $sv = (4, 1)$, $uv = (1, 2)$, $ut = (4, 3)$, $vt = (2, 3)$ and $st = (8, 6)$, with two costs to minimize. Find the Pareto front of the $s$-$t$ paths and the nondominated labels at $v$. Show that a method that keeps one label per vertex, whatever rule it uses to pick that label, loses a point of the front. See [multi-objective shortest path](/multi-objective-shortest-path/).

14. • The graph on the vertices $1, 2, 3, 4$ has the edges $\{1, 2\} = (2, 5)$, $\{1, 3\} = (4, 1)$, $\{2, 3\} = (1, 4)$, $\{2, 4\} = (6, 2)$ and $\{3, 4\} = (3, 3)$, with two weights to minimize. List the weight vectors of its eight spanning trees, the Pareto front, and the supported and unsupported points. See [multi-objective minimum spanning tree](/multi-objective-minimum-spanning-tree/).

15. • Let $Y = \{(2^k, 2^{6-k}) : k = 0, 1, \ldots, 6\}$. Find the size of the smallest $\varepsilon$-Pareto set of $Y$ in the multiplicative sense with $\varepsilon = 1$, that is, with the factor $2$ in each objective, and give one such set. See [approximate Pareto set](/approximate-pareto-set/).

16. • Prove that adding a point to a set $A$ leaves its hypervolume unchanged when some member of $A$ weakly dominates the new point, and increases it strictly when no member weakly dominates the new point and the new point strictly dominates the reference point.

17. • Show that for $p = 2$ the nadir point is $(f_1(x^2), f_2(x^1))$, where $x^1$ is a lexicographic minimizer of $(f_1, f_2)$ and $x^2$ of $(f_2, f_1)$. Then let $Y = \{(0, 2), (0, 5), (3, 0)\}$ and show that a payoff table built from a minimizer of $f_1$ that is not lexicographic can overestimate the nadir point.

18. • Write the non-dominated sort for two objectives in $O(N \log N)$ time: sort by $f_1$ with ties by $f_2$, keep the last $f_2$ value of each front, and place each point in the first front whose last value is larger than its own $f_2$, by binary search. Assume that no two points are equal. Why is the binary search valid, and why must equal points be excluded or handled apart? Run the method on the points of exercise 4.

19. • Run [Benson's algorithm](/benson-algorithm/) on "minimize $(x_1, x_2)$ over $x \ge 0$, $x_1 + x_2 \ge 4$, $x_1 + 3 x_2 \ge 6$". Give the vertices of the outer approximation, the value $z$ found for each vertex checked, and the cuts, round by round.

20. • For the problem of exercise 19, the anchor points are $(0, 4)$ and $(6, 0)$ and the ideal point is $(0, 0)$. Compute the points of [normal-boundary intersection](/normal-boundary-intersection/) for $\beta = (1, 0), (\tfrac34, \tfrac14), (\tfrac12, \tfrac12), (\tfrac14, \tfrac34), (0, 1)$, where $\beta_1$ weights the anchor that minimizes $f_1$. Does any of them hit the vertex $(3, 1)$?

21. ★ Let $N$ points in the plane have independent coordinates drawn from continuous distributions. Prove that the expected size of their Pareto front is the harmonic number $H_N$.

22. ★ Prove that it is NP-complete to decide whether a graph with two arc costs has an $s$-$t$ path of cost at most $(B_1, B_2)$, by a reduction from PARTITION.

23. ★ Let $X = \{x : A x \ge b\}$, and let $x^*$ be an efficient solution of the [multi-objective linear program](/multi-objective-linear-programming/) "minimize $C x$ over $X$". Use the linear program "maximize $\sum_i s_i$ subject to $C x + s = C x^*$, $A x \ge b$, $s \ge 0$" and its dual to prove that $x^*$ minimizes $\lambda^T C x$ over $X$ for some $\lambda$ with every $\lambda_i \ge 1$.

24. ★ Given $N$ mutually nondominated points in the plane, a reference point $r$ and an integer $k$, design an $O(k N^2)$ dynamic program that chooses $k$ of the points with the largest hypervolume.

25. ★ For $p = 2$, give an algorithm that computes $I_{\varepsilon+}(A, B)$ in $O((\lvert A \rvert + \lvert B \rvert) \log \lvert A \rvert)$ time, and prove it correct.
