1. ◦ Use the [counting theorem](/triangulation-counting-theorem/) and its consequences. (a) How many triangles and diagonals has a triangulation of a simple polygon with 12 vertices? (b) A polygon has 20 vertices in all, on its outer boundary and on 2 holes. How many triangles and diagonals has a triangulation? (c) How many triangles and edges has a triangulation of the five points $(0,0), (2,0), (4,0), (4,4), (0,4)$?

2. ◦ Let $t_m$ be the number of triangulations of a convex polygon with $m$ vertices, with $t_2 = 1$. The edge $v_0 v_{m-1}$ lies in exactly one triangle $v_0 v_k v_{m-1}$, so $t_m = \sum_{k=1}^{m-2} t_{k+1} t_{m-k}$. Compute $t_3, \ldots, t_7$ and compare them with the [Catalan count](/catalan-triangulation-theorem/).

3. ◦ The pentagon $v_0 = (0,0)$, $v_1 = (4,0)$, $v_2 = (4,4)$, $v_3 = (2,1)$, $v_4 = (0,4)$ is simple and counterclockwise. Which of its vertices are [ears](/ear/)? List all its diagonals and all its triangulations.

4. ◦ Label the vertices of a convex hexagon $v_0, \ldots, v_5$, and let $F_i$ be the fan triangulation whose diagonals all end at $v_i$. What is the [flip distance](/flip-distance/) from $F_0$ to $F_3$, and from $F_0$ to $F_1$? Give a shortest sequence of flips in each case.

5. ◦ The rectangle $(0,0), (4,0), (4,2), (0,2)$ has two triangulations. What is the smallest angle in each, and which one does the [max-min angle](/max-min-angle-triangulation/) rule choose?

6. ◦ In each quadrilateral $abcd$ below, the diagonal $ac$ splits it into two triangles. Can $ac$ be [flipped](/edge-flip/)? (a) $a = (0,0)$, $b = (4,0)$, $c = (1,1)$, $d = (0,4)$. (b) $a = (0,0)$, $b = (4,0)$, $c = (2,2)$, $d = (0,4)$.

7. ◦ [Seidel's algorithm](/seidel-polygon-triangulation/) takes $O(n \log^* n)$ expected time and [Tarjan and Van Wyk's](/tarjan-van-wyk-triangulation/) $O(n \log \log n)$. For $n = 2^{65536}$, compute $\log_2 n$, $\log_2 \log_2 n$ and $\log^* n$.

8. • In a triangulation of a simple polygon, let $t_i$ be the number of nodes of degree $i$ in the [dual tree](/triangulation-dual-tree/). Show that $t_1 = t_3 + 2$. A triangulated 10-gon has exactly three ears. How many of its triangles have exactly one polygon edge, and how many have none?

9. • The points $a = (0,0)$, $b = (5,1)$, $c = (6,6)$, $d = (1,5)$ form a convex quadrilateral. Find the smallest angle of the triangulation with diagonal $ac$ and of the one with diagonal $bd$. Which diagonal does the max-min angle rule keep, and which one does the [greedy triangulation](/greedy-triangulation/) choose?

10. • Every triangulation of a convex pentagon is a fan of two diagonals from one vertex. For the pentagon $(0,0), (4,0), (5,3), (2,5), (-1,3)$, find the triangulation of least total diagonal length, as the [dynamic program](/polygon-triangulation-dp/) would.

11. • Take the counterclockwise hexagon $A = (0,0)$, $B = (3,2)$, $C = (6,0)$, $D = (6,10)$, $E = (3,8)$, $F = (0,10)$. Classify each vertex as start, split, end, merge or regular for a top to bottom sweep, and give the diagonals that the [monotone partition](/monotone-polygon-partition/) sweep adds. Into how many triangles is the polygon then cut?

12. • The interval dynamic program for a convex polygon with $n$ vertices tries each triangle $v_i v_k v_j$ with $i < k < j$ exactly once. How many triangles does it try for $n = 20$? How many pairs $(i, j)$ with $j - i \ge 2$ does its table hold?

13. • A square with a triangular hole has 7 vertices. Join the hole to the outer square by one bridge, as in [triangulating a polygon with holes](/polygon-with-holes-triangulation/). How many vertices has the vertex list of the resulting polygon, how many triangles does ear clipping produce from it, and how many diagonals, including the bridge, does the triangulation have?

14. • How many vertices and edges has the [flip graph](/flip-graph/) of a convex pentagon, and of a convex hexagon? Which graph is the first one?

15. • A cube can be cut into tetrahedra whose corners are corners of the cube. Show that both 5 and 6 tetrahedra are possible, and give the volumes of the 5 pieces for the unit cube. Why does this show that the [counting theorem](/triangulation-counting-theorem/) has no direct analog for a [tetrahedralization](/tetrahedralization/)?

16. • A square with a square hole, 8 vertices in all, is triangulated after adding 3 [Steiner points](/steiner-points/) inside the region and 2 on the outer edges. How many triangles does the triangulation have? Check the answer by adding up angles.

17. ★ A triangle of a convex polygon triangulation is *internal* if none of its sides is a polygon edge. Show that the triangulations of a convex $n$-gon with no internal triangle are exactly those whose dual tree is a path, and that there are $n \cdot 2^{n-5}$ of them for $n \ge 5$. How many are there for $n = 8$?

18. ★ In a convex hexagon $v_0, \ldots, v_5$, let $T_1$ have the diagonals $v_0 v_2, v_2 v_4, v_4 v_0$ and $T_2$ the diagonals $v_1 v_3, v_3 v_5, v_5 v_1$. Show that the flip distance from $T_1$ to $T_2$ is exactly 4.

19. ★ Show that any triangulation of a convex polygon with $n$ vertices can be turned into the fan $F_0$ by at most $n - 3$ flips, each of which raises the degree of $v_0$. Conclude that the flip graph has diameter at most $2n - 6$.

20. ★ In a strictly convex quadrilateral $abcd$, show that the diagonal $ac$ gives a larger smallest angle than $bd$ if and only if $\angle abc + \angle cda < \pi$, that is, if $d$ lies outside the circle through $a$, $b$ and $c$. Check the rule on exercise 9.
