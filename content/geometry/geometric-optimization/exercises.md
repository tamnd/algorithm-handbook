1. ◦ Find the [minimum enclosing circle](/minimum-enclosing-circle/) of the five points $(0,0)$, $(8,0)$, $(4,6)$, $(1,3)$, $(7,2)$: its center, its radius and the points on its boundary. Then add the point $(4,-3)$. What is the new circle, and how many points fix it?

2. ◦ In the analysis of [Welzl's algorithm](/welzls-algorithm/), the expected number of containment tests per point is at most $c_\delta$, where $c_0 = 0$ and $c_j = 1 + j\,c_{j-1}$. Compute $c_4$, the constant for balls in $\mathbb{R}^3$, and $c_5$, the constant for ellipses in the plane, where $\delta = d(d+3)/2 = 5$. Check both values against $\lfloor (e-1)\,\delta! \rfloor$.

3. ◦ List the [antipodal pairs](/antipodal-pairs/) of the convex pentagon $(0,0)$, $(4,0)$, $(4,2)$, $(2,4)$, $(0,4)$. How many are there, and how does the count agree with $n + t$, where $t$ is the number of pairs of parallel edges?

4. ◦ Find the [Fermat point](/fermat-point/) and the least sum of distances to the corners for the triangle $(0,0)$, $(2,0)$, $(1,5)$. Then do the same for the triangle $(0,0)$, $(6,0)$, $(-3,1)$.

5. ◦ Use Kuhn's test from the [geometric median](/geometric-median/) entry to decide whether the data point $(1,2)$ is the geometric median of $(0,0)$, $(4,0)$, $(0,4)$, $(1,2)$. Then replace $(1,2)$ by $(3,3)$ and decide again. Where is the median of the second set, and what is its sum of distances?

6. ◦ (a) For the terminals $(1,4)$, $(5,0)$, $(3,7)$, give a [rectilinear Steiner minimal tree](/rectilinear-steiner-tree-problem/) and a rectilinear minimum spanning tree, with their lengths. (b) In the star graph with a center and five leaves, every edge of length 1, take the five leaves as terminals. Compute $\mathrm{MST}$ and $\mathrm{SMT}$ in the shortest path metric, and compare their ratio with the bound $n/(2(n-1))$ of the [Steiner ratio](/steiner-ratio/) entry.

7. ◦ Find the largest block of zeros in the $4 \times 6$ matrix with rows `100100`, `000010`, `001000`, `000001`, by the row-by-row histogram method of the [largest empty rectangle](/largest-empty-rectangle/) entry. Give the histogram of each row and the area of the block.

8. ◦ Run the [Bădoiu–Clarkson algorithm](/badoiu-clarkson-algorithm/) on the points $(0,0)$, $(6,0)$, $(0,8)$, with $c_1 = (0,0)$ and $c_{i+1} = c_i + (q_i - c_i)/(i+1)$, where $q_i$ is the point farthest from $c_i$. Give $c_1, \ldots, c_4$ and the squared radius $\max_p |p - c_i|^2$ at each. Does the radius shrink at every step? Check the bound $|c_i - c^*|^2 \le r^{*2}/i$.

9. ◦ Bound the [Heilbronn](/heilbronn-triangle-problem/) value $\Delta(7)$ from below with Erdős's parabola $(x, x^2 \bmod 7)$, $0 \le x < 7$, scaled into the unit square, and from above with the strip argument. Give the smallest triangle area of the parabola set in grid units.

10. ◦ An obstacle is the triangle $(2,-1)$, $(6,-1)$, $(4,3)$, and $s = (0,0)$, $t = (8,0)$. Which corners does $s$ see? List the edges of the [visibility graph](/visibility-graph/) on $s$, $t$ and the three corners, and find a shortest path from $s$ to $t$ and its length.

11. • Take the five points of exercise 1 in a uniformly random order. In Welzl's algorithm the last point causes a recursive call exactly when it lies outside the minimum enclosing circle of the other four. For which of the five points is that so, and what is the probability of a recursive call at the last step? Compare it with the bound $3/n$ from backwards analysis.

12. • For the convex pentagon $P = (1,5)$, $(5,1)$, $(5,7)$, $(3,8)$, $(2,7)$, compute the [diameter](/polygon-diameter/), the [width](/polygon-width/) and the [minimum-area enclosing rectangle](/minimum-area-enclosing-rectangle/), with the corners of the rectangle. Is the rectangle flush with the edge that gives the width? Check the bound $A^* \le 2\,\mathrm{area}(P)$.

13. • Find a [minimum-area enclosing triangle](/minimum-area-enclosing-triangle/) of the rectangle $[0,4] \times [0,2]$ and its area. Use the bound $A^* \le 2\,\mathrm{area}(K)$ of Gross, which every parallelogram attains, to show that no smaller triangle exists, and check that the midpoint of each side of your triangle touches the rectangle.

14. • Find the [Euclidean Steiner minimal tree](/euclidean-steiner-tree-problem/) of the corners $(0,0)$, $(2,0)$, $(2,1)$, $(0,1)$ of a $2 \times 1$ rectangle: its Steiner points, its length and its ratio to the minimum spanning tree. Explain why the full topology that pairs $(0,0)$ with $(2,0)$ and $(0,1)$ with $(2,1)$ cannot be realized.

15. • Run one step of [Weiszfeld's algorithm](/weiszfelds-algorithm/) for the points $(0,0)$, $(4,0)$, $(0,3)$, starting at their centroid. Give the new point and the sum of distances before and after. What is the exact least sum of distances, and why can you get it without iterating?

16. • Let $H$ be $n$ points in the plane and let $w(G)$ be the half perimeter of the axis-parallel bounding box of $G$, with $w(\emptyset) = -\infty$. Show that $(H, w)$ is an [LP-type problem](/lp-type-problem/) of combinatorial dimension 4. For $n = 10\,000$, give the sample size $r = \lceil \delta \sqrt{n} \rceil$ of [Clarkson's algorithm](/clarksons-algorithm/), the bound on the expected number of violators from the sampling lemma, and an upper bound on the probability that a sample has more than $2\sqrt{n}$ violators.

17. • Find the center and the area of the [minimum volume enclosing ellipse](/minimum-volume-enclosing-ellipsoid/) of the parallelogram $(0,0)$, $(4,0)$, $(5,2)$, $(1,2)$, and of the triangle $(0,0)$, $(6,0)$, $(0,2)$. Use an affine map from the square $(\pm 1, \pm 1)$, whose ellipse is the circle of radius $\sqrt{2}$, and the triangle example of the entry.

18. • Run the first step of [Khachiyan's algorithm](/khachiyans-algorithm/) on the five points $(\pm 1, \pm 1)$ and $(0,0)$ with equal weights $u_i = 1/5$. Here $q_i = (a_i, 1)$, $\Lambda = \sum_i u_i q_i q_i^{\mathsf T}$, $w_i = q_i^{\mathsf T} \Lambda^{-1} q_i$, $\kappa = \max_i w_i$ and $\beta = (\kappa - d - 1)/((d+1)(\kappa - 1))$. Give $\Lambda$, all $w_i$, the weighted mean of the $w_i$, $\kappa$, $\beta$ and the new weights. Where do the weights tend, and what is the final ellipse?

19. • In the polygon $(0,0)$, $(12,0)$, $(12,5)$, $(8,5)$, $(8,2)$, $(4,2)$, $(4,5)$, $(0,5)$, find the [shortest path](/euclidean-shortest-path/) from $s = (1,4)$ to $t = (11,4)$, its length and its number of links. Then find a [minimum link path](/minimum-link-path/) and its length. Why is the link distance not 1?

20. • In the box $[0,8] \times [0,6]$ with the points $(2,2)$, $(5,4)$, $(6,1)$, $(3,5)$, run the sweep of the [largest empty rectangle](/largest-empty-rectangle/) entry from the left support $(2,2)$ and list the rectangles it records with their areas. The set has 18 maximal empty rectangles; which one is the largest?

21. • Find the [minimum enclosing ball](/minimum-enclosing-ball/) of the four points $(1,1,1)$, $(1,-1,-1)$, $(-1,1,-1)$, $(-1,-1,1)$, and of the eight corners of the cube $\{-1,1\}^3$. Compare each radius with Jung's bounds $D/2 \le r^* \le D\sqrt{d/(2(d+1))}$, where $D$ is the diameter.

22. • Show that the three collinear points $(0,0)$, $(1,0)$, $(2,0)$ have no [minimum-width annulus](/minimum-width-annulus/): the infimum of the widths is 0, but every annulus that holds the points has positive width. Use the centers $(1, R)$ for large $R$.

23. ★ Prove that for any three terminals in the plane with the $L_1$ metric, the rectilinear minimum spanning tree is at most $4/3$ times the rectilinear Steiner minimal tree. Give three terminals with integer coordinates that attain $4/3$. Why does this not contradict the ratio $3/2$ of the plus shape?

24. ★ Let $K$ be a convex polygon of diameter $D$, attained by the points $a$ and $b$. Prove that the rectangle with two sides parallel to $ab$ that encloses $K$ has area at most $2\,\mathrm{area}(K)$, so the [minimum-area enclosing rectangle](/minimum-area-enclosing-rectangle/) satisfies $A^* \le 2\,\mathrm{area}(K)$. Then prove that every triangle has $A^* = 2\,\mathrm{area}(K)$ exactly.

25. ★ Prove Jung's bound in the plane: the [minimum enclosing circle](/minimum-enclosing-circle/) of a set of diameter $D$ has radius at most $D/\sqrt{3}$, with equality for the corners of an equilateral triangle. Use the two cases for the points on the circle.

26. ★ Let $H$ be $n$ distinct numbers, and let $w(G) = -\min G$, so that a number violates $R$ when it is smaller than every element of $R$; this is an LP-type problem with $\delta = 1$. For a uniformly random $r$-subset $R$, prove that the expected number of violators is exactly $(n - r)/(r + 1)$, which is the bound of the sampling lemma with equality.

27. ★ The minimum-area annulus minimizes $\pi(R^2 - r^2)$ instead of $R - r$. Show that it is a linear program in the four variables $c_x$, $c_y$, $R^2 - |c|^2$ and $r^2 - |c|^2$. Solve it for the six points $(\pm 5, 0)$, $(0, \pm 5)$, $(3,0)$, $(0,3)$, prove that the answer is optimal, and compare it with the minimum-width annulus of the same points, centered at $(-1,-1)$ with width $\sqrt{37} - \sqrt{17}$.
