1. ◦ Using [the equation of a line through a segment](/line-equation-from-segment/), find the line through $(2, -1)$ and $(5, 3)$ in canonical integer form: coefficients with greatest common divisor $1$ and $A > 0$.

2. ◦ Intersect the lines $2x + y - 7 = 0$ and $x - 3y + 7 = 0$ with the formulas of [line-line intersection](/line-line-intersection/). Then replace the second line by $4x + 2y + 1 = 0$ and say which case the determinants report.

3. ◦ Find the points where the circle of radius $5$ centered at the origin meets the line $x - y - 1 = 0$. What is the value of the discriminant $D = r^2 (A^2 + B^2) - e^2$ of [circle-line intersection](/circle-line-intersection/), where $e$ is the value of the left side of the line equation at the center?

4. ◦ The first circle has center $(0, 0)$ and radius $5$. For a second circle of radius $3$ centered at $(8, 0)$, at $(2, 0)$ and at $(4, 0)$, give the common points of the two circles and the number of their [common tangents](/common-tangents-two-circles/).

5. ◦ For each pair, say whether the segments meet and describe the intersection: (a) $(0,0)$–$(4,4)$ and $(0,4)$–$(4,0)$; (b) $(0,0)$–$(2,2)$ and $(3,3)$–$(5,5)$; (c) $(0,0)$–$(2,2)$ and $(1,1)$–$(3,3)$.

6. ◦ The [orthogonal sweep](/orthogonal-segment-intersection-sweep/) processes the events with equal $x$ in the order inserts, queries, deletes. Take the horizontal segment $(0,0)$–$(4,0)$ and the vertical segment $(0,-1)$–$(0,1)$. Which crossing is lost if the queries come before the inserts? Give a second vertical segment whose crossing is lost if the deletes come before the queries.

7. ◦ Apply the reduction of the [segment intersection lower bound](/segment-intersection-lower-bound/) to the numbers $3, 1, 4, 1, 5$. Which segments are built, which pair meets, and what does that say about the numbers?

8. ◦ Find the vertices of the [intersection of the half-planes](/half-plane-intersection/) $x \ge 0$, $y \ge 0$, $x + y \le 4$ and $x - y \le 2$, and its area. Which of the five half-planes is redundant if $y \le 5$ is added?

9. ◦ Four lines are in general position: no two are parallel and no three pass through one point. How many vertices, edges and faces does their [arrangement](/line-arrangement/) have, and how many of the faces are bounded?

10. • The circles with centers $(0,0)$ and $(6,0)$ and radii $2$ and $1$ have four common tangents. Find the external and internal centers of similarity, and the equations of the two internal tangents.

11. • Run the [Shamos-Hoey algorithm](/shamos-hoey-algorithm/) on $s_0 = (0,0)$–$(8,0)$, $s_1 = (1,3)$–$(7,3)$, $s_2 = (2,1)$–$(6,5)$ and $s_3 = (3,-1)$–$(5,2)$. At which event does it stop, and which pair does it report? Is that the crossing with the smallest $x$?

12. • Run the [Bentley-Ottmann algorithm](/bentley-ottmann-algorithm/) on the segments $a = (0,0)$–$(4,4)$, $b = (0,4)$–$(4,0)$ and $c = (0,2)$–$(4,2)$. How many events does it process, how many intersection points does it report, and how many intersecting pairs? Give the status order just before and just after the crossing.

13. • A set of $n$ segments has $n/2$ horizontal segments and $n/2$ vertical segments, and every horizontal one crosses every vertical one. Give $k$, and the running time of a pairwise test, of the Bentley-Ottmann sweep, and of the [orthogonal sweep](/orthogonal-segment-intersection-sweep/).

14. • The lower bound for [half-plane intersection](/half-plane-intersection/) uses the half-planes $y \ge 2 x_i x - x_i^2$ above the tangents of the parabola $y = x^2$. For $x_i = 3, -1, 2$, give the three half-planes, the order of their lines along the boundary of the intersection from left to right, and the two vertices.

15. • The square $[-2, 2]^2$ and the square $|x| + |y| \le 3$ are both convex polygons with four vertices. Find their [intersection](/convex-polygon-intersection/) and its area. What does this example show about the bound of $p + q$ vertices?

16. • Compute the area of the union of $R_1 = [0,3] \times [0,2]$, $R_2 = [1,4] \times [1,3]$ and $R_3 = [2,5] \times [0,1]$ with the sweep of [Klee's measure problem](/klee-measure-problem/): give the slabs between consecutive $x$-coordinates and the covered length of the sweep line in each.

17. • Let $P$ be the triangle $(0,0), (2,0), (0,2)$ and $Q$ the square $[3,4] \times [0,1]$. Compute the vertices of the Minkowski difference $P - Q = \{p - q\}$, the point of it nearest to the origin, and the distance between $P$ and $Q$, as [GJK](/gjk-algorithm/) would find them.

18. • Let $T$ be the triangle $(0,0), (4,0), (0,4)$ and $S$ the square $[3,4] \times [3,4]$. List the axes that the [separating axis theorem](/separating-axis-theorem/) tests, and the projections of $T$ and $S$ on each. Which axis separates them? What goes wrong if only the edge normals of $S$ are tested?

19. • Three of four lines pass through one point and the fourth line passes through none of their crossings and is parallel to none of them. Count the vertices, edges and faces of the [arrangement](/line-arrangement/) and check the counts against $E = n + \sum_v m_v$ and $F = 1 + n + \sum_v (m_v - 1)$, where $m_v$ is the number of lines through vertex $v$.

20. • In an arrangement of $n \ge 2$ lines with pairwise different slopes, how many faces are unbounded? Deduce the number of bounded faces when the lines are in general position.

21. ★ Can a finite set of half-planes have an empty intersection although every three of them have a point in common? Prove your answer.

22. ★ In the Bentley-Ottmann sweep, keep in the queue only the end point events and the crossing events of pairs that are currently adjacent in the status. Give a bound on the size of the queue, and explain why no crossing is lost when a pair stops being adjacent and its event is deleted.

23. ★ The problem 3SUM asks whether three distinct numbers of a set sum to $0$. Map each number $a$ to the point $(a, a^3)$. Show that for distinct $a$, $b$, $c$ the three points are collinear exactly when $a + b + c = 0$. What does this say about building a [line arrangement](/line-arrangement-construction/) in $o(n^2)$ time to find three collinear points?

24. ★ Give a set of $n$ axis-parallel rectangles whose union has $\Omega(n^2)$ vertices on its boundary. What does this say about computing the area of the union by first building its boundary, compared with the sweep of [Klee's measure problem](/klee-measure-problem/)?

25. ★ The red set has $n/2$ horizontal segments and the blue set $n/2$ vertical segments; no two segments of one color meet. Count the red-blue crossings in $O(n \log n)$ time even when there are $\Theta(n^2)$ of them, using a [Fenwick tree](/fenwick-tree/).
