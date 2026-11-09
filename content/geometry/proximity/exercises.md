1. ◦ Decide whether $\sqrt{8} + \sqrt{18} < 7$ with integer arithmetic only, by squaring twice as the entry on [Euclidean distance](/euclidean-distance/) does for sums of lengths.

2. ◦ Let $a = (0,0)$ and $b = (6,3)$. For each of $p = (1,7)$, $(8,1)$ and $(-3,1)$, compute the squared distance from $p$ to the [line](/point-to-line-distance/) through $a$ and $b$ and to the [segment](/point-to-segment-distance/) $ab$, and give the nearest point of the segment.

3. ◦ Let $A = \{(0,0), (2,0), (7,0)\}$ and $B = \{(1,0), (3,3)\}$. Compute the directed distances $h(A, B)$ and $h(B, A)$ and the [Hausdorff distance](/hausdorff-distance/) $H(A, B)$.

4. ◦ Six points lie on the $x$-axis at $x = 0, 1, 3, 6, 10, 15$. Draw the directed [nearest neighbor graph](/nearest-neighbor-graph/). Which point has the largest in-degree, how many edges has the undirected graph, and which pairs are mutual nearest neighbors? Is the undirected graph the minimum spanning tree?

5. ◦ Let $p = (0,0)$ and $q = (6,0)$. For each third point $r = (3,2)$, $(3,4)$ and $(3,6)$, taken alone with $p$ and $q$, decide whether $pq$ is an edge of the [Gabriel graph](/gabriel-graph/) and of the [relative neighborhood graph](/relative-neighborhood-graph/). Use the dot product test and the lune test with squared distances.

6. ◦ Let $S = \{(0,0), (5,1), (7,4), (4,8), (1,6), (3,3)\}$. Find the convex hull, the [farthest pair](/farthest-pair/) and its squared distance. Then find the point farthest from $(3,3)$ and check that its distance lies between half the diameter and the diameter.

7. ◦ Let $S = \{(0,0), (1,3), (2,2), (3,1), (4,4), (6,0), (2,6)\}$. Sort the other six points by slope around $(2,2)$ and read off the lines through $(2,2)$ that contain three or more points. Then list every such line of $S$, as the slope-sorting method for [collinear points](/collinear-points/) would.

8. ◦ (a) Compute the stretch bound $1/(1 - 2\sin(\pi/k))$ of the [Yao graph](/yao-graph/) for $k = 7$, $8$ and $12$ cones. (b) What is the smallest $k$ whose bound is at most 2, and at most $1.5$? (c) For which separation $s$ does the spanner of the [well-separated pair decomposition](/well-separated-pair-decomposition/) guarantee stretch 2, $1.5$ and $1.1$?

9. • Run the top level of [divide and conquer](/closest-pair-divide-and-conquer/) on $P = \{(0,0), (1,6), (2,2), (4,5), (5,3), (7,7), (8,0), (9,4)\}$. The left half is the four points with the smallest $x$, and the dividing line is $x = 5$, the $x$-coordinate of the first right point. Give the squared closest distances of the two halves, the strip in $y$ order, the number of distances the strip loop computes, and the answer.

10. • A k-d tree on seven points has root $(9,6)$, split on $x$. Its left child $(3,9)$, split on $y$, has children $(2,3)$ and $(5,12)$; its right child $(14,10)$, split on $y$, has children $(13,1)$ and $(11,14)$. Trace the [k-d tree search](/kd-tree-nearest-neighbor-search/) for $q = (8,14)$. Which nodes are visited, which subtrees are skipped, and what is returned?

11. • The [randomized grid algorithm](/randomized-closest-pair/) receives the points in the order $(0,0)$, $(12,9)$, $(5,1)$, $(20,3)$, $(6,4)$, $(14,8)$, $(19,0)$. Give $\delta^2$ after each insertion and the insertions that rebuild the grid. Which grid side $s$ with $s \le \delta < 2s$ is a valid choice at the end?

12. • Let $A$ be the segment from $(0,0)$ to $(6,0)$ and $B = \{(0,1), (3,1), (6,1)\}$. Compute $h(B, A)$, $h(A, B)$ and $H(A, B)$. Where on the segment is $h(A, B)$ attained?

13. • Map each number $a$ to the point $(a, a^3)$. Show that the slope between $(a, a^3)$ and $(b, b^3)$ is $a^2 + ab + b^2$, and that three distinct numbers give collinear points exactly when they sum to 0. Find all collinear triples for the numbers $-7, -2, 1, 3, 4, 6$, and the slope of each line.

14. • Let $C = \{(0,0), (2,6), (3,1), (4,7), (8,3), (9,7)\}$. Run [Kruskal's algorithm](/kruskal/) to find the [Euclidean minimum spanning tree](/euclidean-minimum-spanning-tree/): list the squared lengths it accepts and rejects, and give the total length. Check that every edge of the nearest neighbor graph of $C$ is in the tree.

15. • The six points of exercise 14 are in convex position, and their [Delaunay triangulation](/delaunay-triangulation/) has the six hull edges and the diagonals $(2,6)(3,1)$, $(3,1)(4,7)$ and $(4,7)(8,3)$. Find the relative neighborhood graph and the Gabriel graph. Which Gabriel edge is not an RNG edge, and which point lies in its lune? Which Delaunay edges are not Gabriel edges, and which point lies in each diametral disk? Give the edge counts along the [chain of proximity graphs](/proximity-graphs/).

16. • The points $(0,0)$, $(2,3)$, $(6,6)$, $(7,2)$, $(7,5)$ have the Delaunay triangles $\{(0,0), (7,2), (2,3)\}$, $\{(2,3), (7,5), (6,6)\}$ and $\{(2,3), (7,2), (7,5)\}$. Compute the [Urquhart graph](/urquhart-graph/) and the relative neighborhood graph. Which edge is in one and not the other, and why does the longest-edge rule miss it?

17. • For the triangle $(0,0)$, $(6,0)$, $(2,3)$, find for each side the values of $\beta \ge 1$ for which it is an edge of the lune-based [$\beta$-skeleton](/beta-skeleton/) with open regions. Use the test $\|r - p\|^2 < \beta\,(r - p) \cdot (q - p)$ and its mirror at $q$. How many edges has the skeleton for $\beta = 1$, $2$, $20$ and $30$?

18. • Build the Yao graph of the points of exercise 14 with $k = 4$ half-open quadrants $[0°, 90°)$, $[90°, 180°)$, $[180°, 270°)$ and $[270°, 360°)$. List the choices of each point, and count the edges. Does the graph contain the tree of exercise 14? Compute the stretch of the pair $(3,1)$, $(4,7)$, which is the largest of the graph.

19. • Build the fair split tree of the numbers $0, 1, 2, 4, 8$ on a line: the box of a node is the interval from its smallest to its largest number, $c$ is its midpoint, $r$ is half its length, and a split at the midpoint sends points on it to the left. Run FIND-PAIRS with $s = 2$. List the pairs, and check that they cover each of the 10 pairs of numbers exactly once.

20. • Red points are $(0,0)$, $(1,2)$, $(8,7)$ and blue points are $(4,1)$, $(9,3)$, $(3,8)$. Find the closest pair and the [bichromatic closest pair](/bichromatic-closest-pair/), and check with the dot product test that the bichromatic pair is a Gabriel edge of all six points. Then find the bichromatic closest pair of red numbers $1, 9, 14, 30$ and blue numbers $5, 17, 22, 40$ on a line.

21. • Let $S = \{(0,0), (3,1), (5,4), (1,5), (8,2)\}$ and $q = (3,3)$. Find the nearest neighbor of $q$ in $S$ and the set of [reverse nearest neighbors](/reverse-nearest-neighbor/) of $q$. Does the answer change between the rule with $\le$ and the strict rule?

22. ★ Let $P$ be the segment from $(0,0)$ to $(4,0)$, and let $Q$ be the polygonal curve through $(0,0)$, $(3,0)$, $(1,0)$, $(4,0)$. Find the Hausdorff distance, the weak [Fréchet distance](/frechet-distance/), the Fréchet distance and the discrete Fréchet distance of the vertex sequences, and prove the value of the Fréchet distance. How does the discrete distance change when $P$ gets extra vertices at $(1,0)$, $(2,0)$ and $(3,0)$?

23. ★ Show that the farthest pair of $n$ points in the plane takes $O(n)$ time under the $L_\infty$ distance $\max(|\Delta x|, |\Delta y|)$ and under the $L_1$ distance $|\Delta x| + |\Delta y|$. Then show that the largest extent of the points along the four directions at $0°$, $45°$, $90°$ and $135°$ is at least $\cos(\pi/8)$ times the Euclidean diameter. Apply all three methods to the set of exercise 6.

24. ★ In the randomized grid algorithm, call the insertion of the $k$-th point, $k \ge 3$, a rebuild when it lowers $\delta$. Show by looking backwards from the first $k$ points that a rebuild happens with probability at most $2/k$, so the expected number of rebuilds is at most $2 \ln n$. For the seven points of exercise 11 in random order, compute the bound $\sum_{k=3}^{7} 2/k$ and the exact probabilities of a rebuild at $k = 3$ and at $k = 7$.

25. ★ Allow ties in the nearest neighbor graph, so that a point counts as a nearest neighbor of $p$ whenever no other point is strictly closer to $p$. Show that if a point $o$ is a nearest neighbor of six other points, those six points form a regular hexagon centered at $o$. Conclude that among points with integer coordinates, no point is a nearest neighbor of six others.

26. ★ Given two sorted sets $A$ and $B$ of $m$ and $n$ numbers, compute $H(A, B)$ in $O(m + n)$ time. Run your method on $A = \{0, 3, 9, 10\}$ and $B = \{1, 6, 15\}$. For finite sets in the plane, how do you get $O((m + n) \log(m + n))$ time?
