1. ◦ The square $[0,2]^2$ is cut by its two diagonals, which meet at $(1,1)$. As a [planar subdivision](/planar-subdivision/), how many vertices, edges, faces and connected components does it have? Check the counts against $V - E + F = 1 + C$.

2. ◦ Build the [slab method](/slab-method-point-location/) structure for the subdivision of Exercise 1. How many slabs are there between $x = 0$ and $x = 2$, which edges does each slab list hold, and in which face is the query point $(1/2, 1)$?

3. ◦ Locate the points $(3, 2)$ and $(5, 1)$ in the square $(0,0), (4,0), (4,4), (0,4)$ by the wedge method of [point location in a convex polygon](/convex-polygon-point-location/), with the center $c = (2, 2)$. Which wedge does each point fall in, and what does the final orientation test return?

4. ◦ By the lower bound of [planar point location](/planar-point-location/), how many orientation tests does any method need in the worst case for the subdivision of Exercise 1, counting vertices, edges and faces as possible answers?

5. ◦ How many trapezoids does the [trapezoidal map](/trapezoidal-map/) of the three edges of the triangle $(0,0), (6,1), (2,5)$ have? Describe each of them.

6. • Take $n/2$ long segments from $(0, i)$ to $(2n, i)$ for $i = 1, \ldots, n/2$, and $n/2$ short segments from $(2j - 1, 0)$ to $(2j, 0)$ for $j = 1, \ldots, n/2$. Give a lower bound on the total length of the slab lists of the slab method. How many insertions and deletions does the sweep of [Sarnak and Tarjan](/sarnak-tarjan-point-location/) make on the same input?

7. • A triangulation of a triangle has $N = 10$ vertices. How many triangles and edges does it have? Show that at least four of its seven inner vertices have degree at most $8$, so that [Kirkpatrick's method](/kirkpatrick-point-location/) can remove one of them in the first round.

8. • The points $(i, 0)$ and $(i, 1)$ for $i = 0, \ldots, m$ are triangulated by the vertical edges and the diagonals from $(i, 0)$ to $(i + 1, 1)$. How many steps does the straight [triangle walk](/triangle-walk-point-location/) from $(1/4, 1/2)$ to $(m - 1/4, 1/2)$ take? What does this say about the worst case of a walk?

9. • The segment $s_i$ goes from $(-i, i)$ to $(i, i)$, for $i = 1, \ldots, n$. Insert them into a [trapezoidal map](/trapezoidal-map/) in the order $s_1, s_2, \ldots, s_n$, and then, in a fresh map, in the order $s_n, \ldots, s_1$. How many inner nodes of the search structure does the query $(0, n + 1)$ visit in each case?

10. • Show that the subdivision of Exercise 1 is a [monotone subdivision](/monotone-subdivision/). Number the four triangles in the order bottom, left, right, top, and give the five separating chains. How many edge entries do the chains hold in total, for how many edges?

11. • Kirkpatrick's analysis gives at most $\log_{18/17}(n - 3) + 1$ levels. How many levels does this bound allow for $n = 1000$, and how many triangle tests can a query make? Compare with $\lceil \log_2 1000 \rceil$.

12. • A structure for [vertical ray shooting](/vertical-ray-shooting/) returns the edge directly above a query point $q$, or none. With the subdivision in a [doubly connected edge list](/doubly-connected-edge-list/), how do you report the face that contains $q$ in $O(1)$ more time? What is the answer when no edge is above $q$?

13. ★ All $m$ query points are known before the first answer is needed. Answer them all in $O((n + m) \log (n + m))$ time and $O(n + m)$ space, with an ordinary balanced search tree and no persistence.

14. ★ Redo the counting of Kirkpatrick's method with the degree bound $10$ in place of $8$. At least what fraction of the inner vertices have degree at most $10$, and by what factor does each round shrink $N - 3$ at least? Is the bound better or worse than $17/18$?

15. ★ The [trapezoidal map](/trapezoidal-map/) entry states that the longest search path over all query points exceeds $3 \lambda \ln(n + 1)$ with probability at most $2/(n + 1)^{\lambda \ln 1.25 - 3}$. Find an integer $\lambda$ for which this probability is at most $1/2$ for every $n \ge 3$. If, as in [Seidel's algorithm](/seidel-point-location/), the structure is rebuilt with a new random order until its longest search path is at most $3 \lambda \ln(n + 1)$, what is the expected number of builds?
