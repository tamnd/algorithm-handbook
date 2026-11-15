1. ◦ Decide which of these graphs are Laman graphs (generically minimally rigid in the plane): (a) $K_4$; (b) $K_4$ minus one edge; (c) two triangles that share one vertex; (d) $K_{3,3}$; (e) the wheel made of a 4-cycle and a hub joined to its four vertices. For each graph that fails, say whether it has too many edges somewhere or too few in total. Use [Laman's theorem](/laman-theorem/).

2. ◦ Use [Maxwell's counting rule](/maxwell-counting-rule/) in the form $m - (dn - D) = s - f$, where $s$ is the dimension of the self-stresses and $f$ the number of independent non-trivial infinitesimal motions. (a) A planar framework has 7 joints and 10 bars. Give a lower bound on $f$. (b) A planar framework with 8 joints and 14 bars has exactly one independent self-stress. Is it infinitesimally rigid? (c) A framework in space has 6 joints, 12 bars and no self-stress. Find $f$.

3. ◦ Take the six points with distance constraints $01, 02, 12, 34, 35, 45, 03, 04, 15$. Run [local propagation](/local-propagation-solving/) with the geometric rule "a point is ready when it has constraints to two placed points", starting once from each of the 9 constrained pairs. Which starting pairs place all six points, and which points does each of the others place?

4. ◦ By the criterion of Gauss and Wantzel in [ruler-and-compass constructibility](/ruler-and-compass-constructibility/), which of the regular $n$-gons with $n = 5, 7, 9, 15, 17, 18$ can be drawn with ruler and compass?

5. ◦ For a planar linkage of $N$ links, the fixed ground included, joined by $J$ pin joints, the count of freedoms is $M = 3(N - 1) - 2J$. Find $M$ for (a) the Watt six-bar linkage, with $N = 6$ and $J = 7$; (b) the five-bar loop, with $N = 5$ and $J = 5$; (c) a closed ring of $N$ links with $N$ pins. For which $N$ is the ring a structure, with $M = 0$?

6. ◦ Four rigid bodies in the plane, numbered 1 to 4, are joined by bars in general position. Use [Tay's theorem](/tay-theorem/) to decide rigidity for (a) three bars between each of the pairs $12$, $23$ and $34$; (b) four bars between 1 and 2, two between 2 and 3, and three between 3 and 4. For a rigid case, give three edge-disjoint spanning trees; for a flexible case, give the partition that fails.

7. ◦ A sketch has four points $a, b, c, d$ and five distances: $\lvert ab \rvert = 6$ and $\lvert ac \rvert = \lvert bc \rvert = \lvert ad \rvert = \lvert bd \rvert = 5$. Put $a = (0, 0)$ and $b = (6, 0)$. List the solutions given by the four sign vectors of the two triangles, as in the [root identification problem](/root-identification-problem/), and give $\lvert cd \rvert$ in each. What should a solver check before it returns one of them?

8. ◦ A 5-cycle with edge lengths $2, 3, 4, 5, 6$, in this order around the cycle, is to be placed on a line, an instance of the [distance geometry problem](/distance-geometry-problem/). Is there a placement? If so, give one with the first point at 0, and find how many placements there are up to congruence.

9. ◦ Use the [Cayley-Menger determinant](/cayley-menger-determinant/) of the squared distances. (a) Compute it for the triangle with sides 5, 5 and 6, and recover the area. (b) Show that the lengths 2, 3 and 6 give a determinant of the wrong sign, so that no triangle has them. (c) Compute it for the regular tetrahedron with edge 1, and find the volume.

10. ◦ Take the triangle with the vertices $p_0 = (0, 0)$, $p_1 = (1, 0)$ and $p_2 = (3, 0)$, on a line in the plane. (a) Write its [rigidity matrix](/rigidity-matrix/) and find its rank. (b) Give an infinitesimal motion that is not trivial. (c) Is the framework rigid? Explain why this does not contradict the [Asimow-Roth theorem](/asimow-roth-theorem/).

11. ◦ The [witness configuration method](/witness-configuration-method/) tests a Laman graph with 50 vertices in the plane at a placement whose coordinates are integers drawn uniformly from $\{1, \ldots, 10^4\}$. (a) What is the generic rank $r^*$ of the rigidity matrix, and what bound does the method give on the probability that the rank at the witness is smaller? (b) Which answer can be wrong, "rigid" or "flexible"? (c) How many independent witnesses bring the bound below $10^{-9}$?

12. • In [variational geometry](/variational-geometry/), fix $A = (0, 0)$ and $B = (4, 0)$ and solve for $C = (x, y)$ with $\lvert AC \rvert^2 = 25$ and $\lvert BC \rvert^2 = 9$ by [Newton's method for systems](/newton-method-for-systems/). (a) Find both exact solutions. (b) Show that the determinant of the Jacobian is $16y$. (c) Starting from $(3, 2)$, compute the first two iterates exactly. (d) Show that from every start with $y_0 > 0$ the iteration converges to the solution with $y > 0$, and say what happens when $y_0 = 0$.

13. • A box is placed against a corner of a fixture, in the setting of [assembly constraint solving](/assembly-constraint-solving/). In the box's own frame, which equals the world frame at the drawn pose, the bottom face is the plane $z = 0$. The mates are: the bottom face on the floor $z = 0$ (a plane-on-plane mate, weight 3); the points $p = (0, 1, 1)$ and $q = (0, 3, 1)$ of the box on the wall $x = 0$ (weight 1 each); the point $r = (1, 0, 1)$ on the wall $y = 0$ (weight 1). (a) Find the count $6 - \sum w$ and the rank of the linearized mate equations in the twist $(\omega, v)$ at the drawn pose. (b) Replace the last mate by the point $r' = (0, 5, 1)$ on the wall $x = 0$. Find the count, the rank, and the motion that is left.

14. • Run the [pebble game](/pebble-game-rigidity/) on the graph with vertices $0, \ldots, 5$ and edges $01, 12, 02, 23, 34, 24, 05, 45$. Give the number of independent edges, the number of non-trivial degrees of freedom, and the rigid components. Then find every edge whose addition makes the graph rigid.

15. • The triangular prism has triangles $012$ and $345$ and the edges $03, 14, 25$. Double the edge $03$ and split the resulting 10 edges into two edge-disjoint spanning trees. Which form of [Laman's theorem](/laman-theorem/) does this check, and how many such checks does the full test need?

16. • Decide which graphs are generically globally rigid in the plane, using the [Jackson-Jordán theorem](/jackson-jordan-theorem/): (a) $K_{3,3}$ plus one edge between two vertices of the same side; (b) the six-point graph of exercise 3 plus the edge $25$; (c) the same graph plus the edge $24$ instead; (d) the octahedron, $K_6$ minus a perfect matching.

17. • Draw the graph of exercise 16(b) at the points $p_0 = (0, 0)$, $p_1 = (6, 0)$, $p_2 = (3, -4)$, $p_3 = (-1, 5)$, $p_4 = (3, 6)$, $p_5 = (7, 4)$. Find, with exact rational coordinates, a second framework with the same 10 edge lengths that is not congruent to this one, and give one pair of points whose distance changes. Which of [Hendrickson's conditions](/hendrickson-global-rigidity-conditions/) does the graph fail?

18. • Run [Owen's decomposition](/owen-triconnected-decomposition/) on the seven points with constraints $01, 02, 12, 15, 25, 03, 04, 34, 36, 46, 56$. Give the separation pairs of the whole graph, the splits, the leaf triangles and the virtual edges, and say in which order the virtual lengths become known during the solve.

19. • Let $G$ be a Laman graph with $n \ge 3$ vertices. (a) Show that at least three vertices of $G$ have degree at most 3. (b) Show that if no vertex has degree 2, then at least six vertices have degree exactly 3, and give a graph where this is tight.

20. • Two rigid bodies in the plane are joined by three bars. Show that the framework is infinitesimally rigid if and only if the three bar lines neither pass through one common point nor are all parallel. For each bad case, describe the relative motion.

21. • Show that there are exactly 6 labeled Laman graphs on 4 vertices and exactly 100 on 5 vertices.

22. • Four points have the squared distances $\lvert 01 \rvert^2 = \lvert 02 \rvert^2 = \lvert 13 \rvert^2 = \lvert 23 \rvert^2 = 4$, $\lvert 12 \rvert^2 = 8$ and $\lvert 03 \rvert^2 = x$. As in the [distance geometry problem](/distance-geometry-problem/), form the Gram matrix $G_{ij} = \big(\lvert 0i \rvert^2 + \lvert 0j \rvert^2 - \lvert ij \rvert^2\big)/2$ for $i, j \in \{1, 2, 3\}$. (a) For $x = 8$, show that $G$ has rank 2 and factor it to get points in the plane. (b) For $x = 6$, show that the points exist in space but not in the plane, and find them. (c) For $x = 9$, show that they exist in no dimension. (d) For which $x$ do they exist in space? Compare with the sign of the Cayley-Menger determinant.

23. • Run the [Frontier vertex algorithm](/frontier-vertex-algorithm/) by hand, for points and distances in the plane, on the seven points with the constraints $01, 02, 12, 34, 35, 45, 03, 14, 26, 06, 56$. (a) Check that the graph is a Laman graph. (b) Give the clusters in an order in which the algorithm can find them, with the children of each. (c) Which point of the cluster on $\{0, 1, 2, 6\}$ leaves the simplified graph, and why? (d) Which step can the Fudos-Hoffmann reduction not make?

24. • A sketch has five points with $\lvert AB \rvert = \lvert BC \rvert = \lvert CD \rvert = 5$, $\lvert AC \rvert = 6$, $\lvert CE \rvert = 8$, $\lvert AE \rvert = 10$ and $\lvert DE \rvert = \sqrt{41}$. (a) Run [rule-based solving](/rule-based-constraint-solving/) with the Pair and Triangle rules, and list the merges. (b) Put $A = (0, 0)$ and $C = (6, 0)$, and find every placement. How many are there up to congruence?

25. ★ Show that for every placement of $K_4$ in the plane with no three points collinear, the self-stresses form a one-dimensional space and every coefficient of a nonzero stress is nonzero. Find the stress for the unit square $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$ with both diagonals, write down its [stress matrix](/equilibrium-stress-matrix/), and find its rank.

26. ★ Let $G$ be a Laman graph with $n \ge 4$ vertices that the [Fudos-Hoffmann reduction](/fudos-hoffmann-reduction/) reduces to one cluster. Show that $G$ has a separation pair. Conclude that a 3-connected Laman graph with $n \ge 4$, such as the prism or $K_{3,3}$, is not triangle-decomposable.

27. ★ Call a placement of a graph on the line generic when its coordinates are algebraically independent over $\mathbb{Q}$. Show that a graph with $n \ge 3$ vertices is generically globally rigid on the line if and only if it is 2-connected.

28. ★ Find the smallest triangle-free Laman graph, and show that it is unique up to relabeling.

29. ★ The [double banana](/double-banana-graph/) has two hinge vertices $a$ and $b$ and two bananas: a triangle $c_1 c_2 c_3$ with every $c_i$ joined to $a$ and $b$, and a triangle $d_1 d_2 d_3$ joined in the same way. (a) Show that it has $18 = 3n - 6$ edges and that every $k \ge 3$ of its vertices span at most $3k - 6$ edges. (b) Show that a generic placement in space has a non-trivial infinitesimal motion, and conclude that the rigidity matrix has rank 17 and one independent self-stress. (c) Show that this stress is nonzero on every edge, so that every edge is redundant although the framework flexes. (d) Which of Hendrickson's conditions fail, and why is the double banana not a counterexample to their sufficiency in space?

30. ★ (a) Show from Hendrickson's conditions that a graph with $n \ge 4$ vertices that is generically globally rigid in the plane has at least $2n - 2$ edges and minimum degree at least 3. (b) The wheel $W_n$ is a hub joined to every vertex of a cycle of $n - 1$ vertices. Show that $W_n$ is generically globally rigid in the plane for every $n \ge 4$, so that both bounds are tight. (c) How many independent self-stresses does a generic placement of $W_n$ have, and what rank does the stress matrix of a nonzero one have, by the [Gortler-Healy-Thurston theorem](/gortler-healy-thurston-theorem/)?
