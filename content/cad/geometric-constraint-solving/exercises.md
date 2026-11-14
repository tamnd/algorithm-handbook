1. ◦ Decide which of these graphs are Laman graphs (generically minimally rigid in the plane): (a) $K_4$; (b) $K_4$ minus one edge; (c) two triangles that share one vertex; (d) $K_{3,3}$; (e) the wheel made of a 4-cycle and a hub joined to its four vertices. For each graph that fails, say whether it has too many edges somewhere or too few in total. Use [Laman's theorem](/laman-theorem/).

2. ◦ Use [Maxwell's counting rule](/maxwell-counting-rule/) in the form $m - (dn - D) = s - f$, where $s$ is the dimension of the self-stresses and $f$ the number of independent non-trivial infinitesimal motions. (a) A planar framework has 7 joints and 10 bars. Give a lower bound on $f$. (b) A planar framework with 8 joints and 14 bars has exactly one independent self-stress. Is it infinitesimally rigid? (c) A framework in space has 6 joints, 12 bars and no self-stress. Find $f$.

3. ◦ Take the six points with distance constraints $01, 02, 12, 34, 35, 45, 03, 04, 15$. Run [local propagation](/local-propagation-solving/) with the geometric rule "a point is ready when it has constraints to two placed points", starting once from each of the 9 constrained pairs. Which starting pairs place all six points, and which points does each of the others place?

4. ◦ By the criterion of Gauss and Wantzel in [ruler-and-compass constructibility](/ruler-and-compass-constructibility/), which of the regular $n$-gons with $n = 5, 7, 9, 15, 17, 18$ can be drawn with ruler and compass?

5. ◦ For a planar linkage of $N$ links, the fixed ground included, joined by $J$ pin joints, the count of freedoms is $M = 3(N - 1) - 2J$. Find $M$ for (a) the Watt six-bar linkage, with $N = 6$ and $J = 7$; (b) the five-bar loop, with $N = 5$ and $J = 5$; (c) a closed ring of $N$ links with $N$ pins. For which $N$ is the ring a structure, with $M = 0$?

6. ◦ Four rigid bodies in the plane, numbered 1 to 4, are joined by bars in general position. Use [Tay's theorem](/tay-theorem/) to decide rigidity for (a) three bars between each of the pairs $12$, $23$ and $34$; (b) four bars between 1 and 2, two between 2 and 3, and three between 3 and 4. For a rigid case, give three edge-disjoint spanning trees; for a flexible case, give the partition that fails.

7. ◦ A sketch has four points $a, b, c, d$ and five distances: $\lvert ab \rvert = 6$ and $\lvert ac \rvert = \lvert bc \rvert = \lvert ad \rvert = \lvert bd \rvert = 5$. Put $a = (0, 0)$ and $b = (6, 0)$. List the solutions given by the four sign vectors of the two triangles, as in the [root identification problem](/root-identification-problem/), and give $\lvert cd \rvert$ in each. What should a solver check before it returns one of them?

8. ◦ A 5-cycle with edge lengths $2, 3, 4, 5, 6$, in this order around the cycle, is to be placed on a line. Is there a placement? If so, give one with the first point at 0, and find how many placements there are up to congruence.

9. • In [variational geometry](/variational-geometry/), fix $A = (0, 0)$ and $B = (4, 0)$ and solve for $C = (x, y)$ with $\lvert AC \rvert^2 = 25$ and $\lvert BC \rvert^2 = 9$ by [Newton's method for systems](/newton-method-for-systems/). (a) Find both exact solutions. (b) Show that the determinant of the Jacobian is $16y$. (c) Starting from $(3, 2)$, compute the first two iterates exactly. (d) Show that from every start with $y_0 > 0$ the iteration converges to the solution with $y > 0$, and say what happens when $y_0 = 0$.

10. • A box is placed against a corner of a fixture, in the setting of [assembly constraint solving](/assembly-constraint-solving/). In the box's own frame, which equals the world frame at the drawn pose, the bottom face is the plane $z = 0$. The mates are: the bottom face on the floor $z = 0$ (a plane-on-plane mate, weight 3); the points $p = (0, 1, 1)$ and $q = (0, 3, 1)$ of the box on the wall $x = 0$ (weight 1 each); the point $r = (1, 0, 1)$ on the wall $y = 0$ (weight 1). (a) Find the count $6 - \sum w$ and the rank of the linearized mate equations in the twist $(\omega, v)$ at the drawn pose. (b) Replace the last mate by the point $r' = (0, 5, 1)$ on the wall $x = 0$. Find the count, the rank, and the motion that is left.

11. • Run the [pebble game](/pebble-game-rigidity/) on the graph with vertices $0, \ldots, 5$ and edges $01, 12, 02, 23, 34, 24, 05, 45$. Give the number of independent edges, the number of non-trivial degrees of freedom, and the rigid components. Then find every edge whose addition makes the graph rigid.

12. • The triangular prism has triangles $012$ and $345$ and the edges $03, 14, 25$. Double the edge $03$ and split the resulting 10 edges into two edge-disjoint spanning trees. Which form of [Laman's theorem](/laman-theorem/) does this check, and how many such checks does the full test need?

13. • Decide which graphs are generically globally rigid in the plane, using the [Jackson-Jordán theorem](/jackson-jordan-theorem/): (a) $K_{3,3}$ plus one edge between two vertices of the same side; (b) the six-point graph of exercise 3 plus the edge $25$; (c) the same graph plus the edge $24$ instead; (d) the octahedron, $K_6$ minus a perfect matching.

14. • Draw the graph of exercise 13(b) at the points $p_0 = (0, 0)$, $p_1 = (6, 0)$, $p_2 = (3, -4)$, $p_3 = (-1, 5)$, $p_4 = (3, 6)$, $p_5 = (7, 4)$. Find, with exact rational coordinates, a second framework with the same 10 edge lengths that is not congruent to this one, and give one pair of points whose distance changes.

15. • Run [Owen's decomposition](/owen-triconnected-decomposition/) on the seven points with constraints $01, 02, 12, 15, 25, 03, 04, 34, 36, 46, 56$. Give the separation pairs of the whole graph, the splits, the leaf triangles and the virtual edges, and say in which order the virtual lengths become known during the solve.

16. • Let $G$ be a Laman graph with $n \ge 3$ vertices. (a) Show that at least three vertices of $G$ have degree at most 3. (b) Show that if no vertex has degree 2, then at least six vertices have degree exactly 3, and give a graph where this is tight.

17. • Two rigid bodies in the plane are joined by three bars. Show that the framework is infinitesimally rigid if and only if the three bar lines neither pass through one common point nor are all parallel. For each bad case, describe the relative motion.

18. • Show that there are exactly 6 labeled Laman graphs on 4 vertices and exactly 100 on 5 vertices.

19. ★ Show that for every placement of $K_4$ in the plane with no three points collinear, the self-stresses form a one-dimensional space and every coefficient of a nonzero stress is nonzero. Find the stress for the unit square $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$ with both diagonals, write down its stress matrix, and find its rank.

20. ★ Let $G$ be a Laman graph with $n \ge 4$ vertices that the [Fudos-Hoffmann reduction](/fudos-hoffmann-reduction/) reduces to one cluster. Show that $G$ has a separation pair. Conclude that a 3-connected Laman graph with $n \ge 4$, such as the prism or $K_{3,3}$, is not triangle-decomposable.

21. ★ Call a placement of a graph on the line generic when its coordinates are algebraically independent over $\mathbb{Q}$. Show that a graph with $n \ge 3$ vertices is generically globally rigid on the line if and only if it is 2-connected.

22. ★ Find the smallest triangle-free Laman graph, and show that it is unique up to relabeling.
