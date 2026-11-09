1. ◦ The sorted array $A = [3, 8, 11, 15, 20, 26, 31, 40, 44, 52]$ is indexed from $0$. For the query $[12, 40]$ of [range search on a line](/one-dimensional-range-search/), give the index of the first key $\ge 12$, the index of the first key $> 40$, the count, and the keys reported.

2. ◦ Insert the keys $20, 10, 30, 5, 15, 25, 35, 12, 18$ in this order into an unbalanced binary search tree. Run the [range search](/bst-range-search/) for $[11, 26]$: which nodes does it enter, which keys does it report, and which nodes does it never touch?

3. ◦ Several exercises below use the ten points $P' = \{(1,7), (2,3), (3,9), (4,1), (5,6), (6,10), (7,4), (8,8), (9,2), (10,5)\}$. Let $D(x, y)$ be the number of points $p \in P'$ with $p_x \le x$ and $p_y \le y$. Compute $D(5,5)$, $D(7,6)$, $D(4,9)$ and $D(10,10)$, listing the points counted in each.

4. ◦ Answer the [three-sided query](/three-sided-range-query/) $[3, 8] \times (-\infty, 4]$ on $P'$. Which point is the lowest among those with $3 \le x \le 8$?

5. ◦ A [range tree](/range-tree/) on $16$ points in rank order has heap-numbered nodes, node $1$ covering ranks $[0, 16)$ and each node $[lo, hi)$ splitting into $[lo, mid)$ and $[mid, hi)$. Which canonical nodes cover the ranks $3$ to $12$, and how many are there?

6. ◦ Use the [lifting map](/paraboloid-lifting-map/) to write the disk with center $(4, 5)$ and squared radius $10$ as a condition $x^2 + y^2 \le \alpha x + \beta y + \gamma$, and use it to find the points of $P'$ in the closed disk, as in [circular range searching](/circular-range-searching/). Which point lies on the circle?

7. ◦ Under the logarithmic method of [decomposable searching problems](/decomposable-searching-problem/), blocks have sizes that are distinct powers of two. Which blocks exist after $22$ insertions? After the $23$rd? After the $24$th, and from which points is the new block built?

8. ◦ In the [epsilon-net theorem](/epsilon-net-theorem/) with VC dimension $d = 3$, $\varepsilon = 0.1$ and $\delta = 0.05$, evaluate the two terms of the bound on the sample size $m$ and give the smallest $m$ it allows.

9. • Count the points of $P'$ in the box $[3, 8] \times [2, 8]$ as a signed sum of four values of $D$, giving each value, and check the result by listing the points. This is the reduction of [orthogonal range counting](/orthogonal-range-counting/) to [dominance counting](/dominance-counting/).

10. • The $y$-coordinates of $P'$ in order of $x$ form the permutation $7, 3, 9, 1, 6, 10, 4, 8, 2, 5$. Count the pairs of points of $P'$ in which one point dominates the other, and use the count to find the number of inversions of the permutation.

11. • Answer three-sided queries on $P'$ sorted by $x$ by recursion with range minimum: find the lowest point in the index range; if it is above $c$, stop; otherwise report it and recurse on the two sides. For $[3, 8] \times (-\infty, 4]$ and for $[1, 10] \times (-\infty, 5]$, give the points in the order they are reported and the number of calls, counting calls on empty ranges. Show that a query reporting $k$ points always makes $2k + 1$ calls.

12. • Build the root of a [layered range tree](/layered-range-tree/) on $P'$: the array of all points sorted by $y$, and the array $\mathrm{left}[0..10]$ in which $\mathrm{left}[i]$ counts how many of the first $i$ entries go to the left child, which holds the points with $x \le 5$. For the $y$-range $[3, 8]$, the root positions are $s = 2$ to $t = 8$, half open. Which positions does the query use in each child, and which points are there?

13. • Solve the recurrence $Q(n) = 2 + 2 Q(n/4)$, $Q(1) = 1$ of the [kd-tree range search](/kd-tree-range-search/) exactly for $n = 4^j$, and evaluate it for $n = 64$ and $n = 4096$. Build a kd-tree on the $8 \times 8$ grid $\{1, \dots, 8\}^2$ by median splits, alternating $x$ and $y$ from the root down to single points, and count the nodes whose region meets the line $x = 3.25$.

14. • Run [offline counting](/offline-orthogonal-range-counting/) on $P'$ with the queries $Q_1 = [2, 7] \times [3, 8]$ and $Q_2 = [5, 10] \times [1, 6]$. For each query, give the number of inserted points with $y$ in range at its opening event and at its closing event, and the answer.

15. • Store the rectangles $R_1 = [0,4] \times [0,3]$, $R_2 = [2,6] \times [2,5]$, $R_3 = [3,8] \times [4,9]$, $R_4 = [5,7] \times [0,6]$ and $R_5 = [1,2] \times [6,8]$ for [point enclosure](/orthogonal-point-enclosure/). Which rectangles contain $q = (5, 4)$? Compute the four dominance counts $N_{aa}$, $N_{ab}$, $N_{ba}$, $N_{bb}$ of the counting reduction and check that they give the same number.

16. • Find the convex hull of $P'$. Decide with it whether the closed halfplanes $3x + y \le 8$ and $3x + y \le 9$ contain points of $P'$, as in [range emptiness](/range-emptiness-query/) for [halfspaces](/halfspace-range-searching/).

17. • In the language of [range spaces](/range-space/), how many distinct traces do closed halfplanes have on the six vertices of a regular hexagon, and how many do closed intervals have on six points of a line? Compare each with $\Phi_3(6)$ and $\Phi_2(6)$, the Sauer-Shelah bounds for VC dimensions $3$ and $2$.

18. • A set of $1000$ lines is in general position. Every simplex of a $(1/10)$-[cutting](/geometric-cutting/) is crossed by at most $100$ of them. Assuming every vertex of the arrangement lies in the interior of some simplex, give a lower bound on the number of simplices.

19. • Let the query be the lower median of a finite set of numbers, its $\lceil |S|/2 \rceil$-th smallest element. Give sets $A, B, A', B'$ with $|A| = |A'|$, $|B| = |B'|$, the same medians for $A$ and $A'$ and for $B$ and $B'$, but different medians for $A \cup B$ and $A' \cup B'$. Conclude that the median is not a decomposable searching problem, while counting is.

20. ★ For a range tree on $16$ leaves with the numbering of Exercise 5, find every range of ranks with the largest number of canonical nodes, and that number. For $n = 2^k$ leaves, what is the maximum, and why can it not reach $2k$?

21. ★ The points $1, 2, \dots, 20$ lie on a line, and the ranges are closed intervals. Find the smallest $\varepsilon$-net for $\varepsilon = 1/4$, so that every interval holding at least $5$ of the points contains a point of the net, and prove that no smaller net exists. Compare its size with the existence bound $\lceil (8d/\varepsilon) \log_2 (8d/\varepsilon) \rceil$ of the [epsilon-net theorem](/epsilon-net-theorem/).

22. ★ The ranges are closed halfplanes and the points are $P'$. With $\varepsilon = 1/2$, a heavy halfplane holds at least $5$ of the $10$ points. Show that no single point of $P'$ is an $\varepsilon$-net, and find every $\varepsilon$-net of size $2$.

23. ★ In the logarithmic method, the $i$-th insertion builds one new block from the new point and all smaller blocks. For $n = 2^k$ insertions into an empty structure, find the exact total size of all blocks built, and evaluate it for $n = 16$ and $n = 1024$.

24. ★ In a [partition tree](/partition-tree-query/) in the plane, suppose every node has $r$ children of exactly $1/r$ of its points, and a line crosses exactly $\sqrt{r}$ children. A triangle query opens up to $3\sqrt{r}$ children per node, so $V(n) \approx 3 \sqrt{r} \, V(n/r)$ and $V(n) = O(n^{e})$. Find $e$ as a function of $r$ and evaluate it for $r = 16$, $256$ and $4096$. How large must $r$ be for $e \le 0.55$?
