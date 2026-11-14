1. ◦ In the plane, let $A = [0, 2] \times [0, 1]$, $B = [1, 3] \times [1, 2]$, and let $D$ be $A$ together with the segment from $(2, 1/2)$ to $(3, 1/2)$. Compute $A \cap B$, $A \cap^* B$, $A \cup B$, $A - B$, $A -^* B$ and the regularization $\operatorname{cl}(\operatorname{int} D)$ with the [regularized set operations](/regularized-set-operations/). Which of these sets are [r-sets](/r-set/)? Is a point of the segment $(1, 2) \times \{1\}$ an interior point of $A \cup B$?

2. ◦ In [function representation](/function-representation/), a solid is $\{x : f(x) \ge 0\}$. On the line, take $f_1(x) = -x$ and $f_2(x) = x$. Which sets do $\min(f_1, f_2) \ge 0$ and $\max(f_1, f_2) \ge 0$ describe? Which of them is regular, and what does the regularization $\operatorname{cl}\{f > 0\}$ give for each?

3. ◦ A [voxel model](/spatial-occupancy-enumeration/) is the $3 \times 3 \times 3$ block of unit cubes with the center cube removed. Count the cubes $n$ and the pairs $p$ of cubes that share a face, and compute the surface area as $6n - 2p$. How many shells does the boundary have?

4. ◦ A block has two square through holes side by side, each with four planar walls. Count $V$, $E$, $F$, the loops $L$, the rings $R = L - F$, the shells $S$ and the holes $H$, and check the [Euler-Poincaré formula](/euler-poincare-formula/) $V - E + F - R = 2(S - H)$.

5. ◦ Build a triangular prism with [Euler operators](/euler-operators/). How many MVFS, MEV and MEF operations do you need? For any solid of genus 0 with one shell and no rings, show that the counts are $1$, $V - 1$ and $F - 1$.

6. ◦ In the [winged-edge data structure](/winged-edge-data-structure/), the topology takes $8E + V + F$ references. Compute this for a tetrahedron, a cube and a triangular prism.

7. ◦ Let $A = [0, 4] \times [0, 2]$, $B$ the disk of radius 1 about $(2, 1)$ and $C = [7/2, 5] \times [1/2, 3/2]$, and let $S = (A -^* B) \cup^* C$. With [CSG ray casting](/csg-ray-casting/), give the intervals of the lines $y = 1$ and $y = 5/4$ that lie in $S$, leaf by leaf and node by node.

8. ◦ Grow the box $[0, 1] \times [0, 2] \times [0, 3]$ by a ball of radius $r = 1$ with [solid offsetting](/solid-offsetting/). Give the exact volume of the result. Then shrink the box by $r = 1/4$, and say for which $r$ the shrunk box is empty.

9. ◦ Sort these into predicates and constructions, the distinction of the [geometric robustness problem](/geometric-robustness-problem/): the [orientation test](/orientation-test/), the intersection point of two lines, the [in-circle test](/in-circle-test/), the circumcenter of a triangle, whether a point lies inside a polygon, the area of a polygon. Which of them can give a wrong answer of a different kind from the others when computed in floating point?

10. ◦ Build the [attributed adjacency graph](/attributed-adjacency-graph/) of the cube $[0, 4]^3$ with the blind pocket $[1, 3] \times [1, 3] \times [2, 4]$ cut from its top. Count the faces, the convex arcs and the concave arcs, list the faces that the method of Joshi and Chang deletes, and name the template that the remaining component matches. Do the same for the square through hole $[1, 3] \times [1, 3] \times [0, 4]$.

11. • The planes $x, y, z \in \{0, 1, 2\}$ bound the notched cube $[0, 2]^3 -^* [1, 2]^3$. Into how many open cells do the nine planes cut space, and how many of them lie in the solid? Write the solid as a union of cells, each an intersection of six half-spaces, and count the leaves. Then find a CSG formula in which each of the nine half-spaces appears once, as in [B-rep to CSG conversion](/brep-to-csg-conversion/).

12. • Let $A = [0, 2] \times [0, 2] \times [0, 1]$ and $B = [0, 1] \times [0, 1] \times [0, 2]$. After [boundary evaluation](/boundary-evaluation/) with coplanar faces merged, give $V$, $E$ and $F$ of $A \cup^* B$, check $V - E + F = 2$, and give its area and volume. Which faces are not convex?

13. • Let $A = [0, 2] \times [0, 1]$ and $B = [1, 3] \times [1, 2]$. With [set membership classification](/set-membership-classification/), split the segment from $(-1, 1)$ to $(4, 1)$ into its parts in, on and out of $A \cup^* B$. Give the classification with respect to each of $A$ and $B$ first, and say where the labels alone are not enough and neighborhoods are needed. Is the point $(1, 1)$ in or on?

14. • The unit sphere and the plane $z = \sqrt 3 / 2$ meet in a circle of radius $1/2$. A [marching](/marching-surface-intersection/) method with equal steps $h$ along it has chord error about $h^2 \kappa / 8$. Find the largest $h$ for a chord error of $10^{-3}$, the number of steps around the circle, and the exact chord error of that many equal chords. What step and how many steps trace a circle of radius $0.01$ to the same chord error, and what happens if no start point lies on it?

15. • Viviani's curve is the intersection of $x^2 + y^2 + z^2 = 4$ and $(x - 1)^2 + y^2 = 1$. Start at $x_0 = (1.1, 0.9, 1.4)$ and make one corrector step $x \leftarrow x - J^{\mathsf T}(JJ^{\mathsf T})^{-1}F(x)$ of the least-length Newton method, with exact fractions. Then iterate in floating point until both residuals are below $10^{-12}$, and say how the residuals fall. Why does the method fail at the double point $(2, 0, 0)$?

16. • Take the torus with axis radius $R = 3$ and tube radius $r = 1$, with the outward normal. Give its principal curvatures in the sign convention of [offset surfaces](/offset-surface/), and find all $d$ for which the area factor $(1 - d\kappa_1)(1 - d\kappa_2)$ is positive at every point. Compare the answer with the bound $|d| < \rho_{\min}$.

17. • Round the equilateral triangle with inradius 1 by $r = 1/2$, that is, shrink it by $r$ and grow the result by $r$. How much area does it lose? Show that rounding any convex polygon with interior angles $\theta_i$ by a small enough $r$ loses $r^2(\sum_i \cot(\theta_i / 2) - \pi)$, and that filleting a convex polygon changes nothing.

18. • Two planes meet along a line, and the air between them is a wedge of angle $60°$. A [rolling ball](/rolling-ball-blend/) of radius 1 fills the concave edge. How far from the edge are the spine and the two contact lines? Through what angle does the blend arc turn, and how much material does the fillet add per unit length of edge?

19. • In double precision, the points $p = (0.1, 0.4)$, $q = (0.3, 1.0)$, $r = (0.6, 1.9)$ lie on $y = 3x + 0.1$ as decimals, but not as stored. Evaluate $D(p, q, r) = (q_x - p_x)(r_y - p_y) - (q_y - p_y)(r_x - p_x)$ and its cyclic shifts $D(q, r, p)$ and $D(r, p, q)$ in floating point, and then exactly on the stored values with fractions. What does each say, and which answers are wrong?

20. • Compute the volume, the center of mass and the inertia tensor about the center of mass of the wedge $\{x, y \ge 0, x + y \le 2, 0 \le z \le 1\}$ of unit density, as in [mass properties of solids](/mass-properties-of-solids/). Use exact fractions.

21. • Find the area of the union of the rectangles $[0, 3] \times [0, 2]$, $[1, 4] \times [1, 3]$ and $[2, 5] \times [0, 1]$ in two ways: by inclusion and exclusion, and by a sweep over $x$ that keeps the union of $y$ intervals, the 2D case of [Klee's measure problem](/klee-measure-problem/).

22. • Estimate the volume of the notched cube $[0, 2]^3 -^* [1, 2]^3$ by [Monte Carlo integration](/monte-carlo-integration/) with uniform points in $[0, 2]^3$. What is the standard deviation of one sample of the estimator $8 \cdot [\text{hit}]$? How many points give a standard error of $0.1\%$ of the volume? Run it once and report the estimate.

23. ★ Prove that the regular closed subsets of $\mathbb{R}^3$ satisfy $A \cap^* (B \cup^* C) = (A \cap^* B) \cup^* (A \cap^* C)$. Which step uses that $B$ and $C$ are regular?

24. ★ In function representation, the union with $\alpha = 0$ of the half-planes $x \ge 0$ and $y \ge 0$ is $f = x + y + \sqrt{x^2 + y^2}$. Show that the level set $f = 1$ is a branch of the hyperbola $(x - 1)(y - 1) = 1/2$. Where does it cross the diagonal $x = y$, and where does the curve of points at distance 1 from the complement of the union cross it? Answer the same for $\max(x, y) = 1$.

25. ★ Two unit cubes share one edge and nothing else. Count $V$, $E$ and $F$ of the union, show that no values of $S$ and $H$ satisfy the Euler-Poincaré formula, and explain the count with $\chi(A \cup B) = \chi(A) + \chi(B) - \chi(A \cap B)$ applied to the two boundary surfaces. Which data structure can store this solid, and why can the winged edge not?

26. ★ Among convex $n$-gons, show that the regular $n$-gon loses the least area under rounding by a small $r$, using the formula of exercise 17. Give the loss for $n = 3, 4, 6, 8$ and its limit as $n \to \infty$.

27. ★ Generalize the volume of the grown box to a convex polyhedron $P$: show that $P$ grown by $r$ has volume $V + A r + \frac{r^2}{2}\sum_e \ell_e (\pi - \beta_e) + \frac43 \pi r^3$, where $\ell_e$ is the length and $\beta_e$ the dihedral angle of edge $e$. Compute it for the regular tetrahedron of edge 1 and $r = 1$, and check it by sampling points.
