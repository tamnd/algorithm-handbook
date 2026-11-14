1. ◦ A printer uses layers of thickness $t = 0.1$ mm. A facet of the part has the normal $(3, 0, 4)$, and the build axis is $z$. Find the cusp height that the [staircase effect](/staircase-effect/) leaves on this facet, and the cusp height when each layer is cut at its middle height instead of at its bottom.

2. ◦ Slice the octahedron $|x| + |y| + |z| \le 1$, as 8 triangles, with the rule of [slicing for additive manufacturing](/slicing-for-additive-manufacturing/) that a vertex at the height of the plane counts as above it. Which triangles does the plane $z = 0$ cut, and what is the contour? What do the planes $z = -1$ and $z = \tfrac12$ give? Give the area inside each contour.

3. ◦ Run greedy [adaptive slicing](/adaptive-slicing/) with the allowed thicknesses $0.1, 0.2, 0.3$ and the cusp bound $c = 0.1$ on a part that spans $0 \le z \le 1.8$. Below $z = 1.2$ all its side facets are vertical. Above $z = 1.2$ every side facet has $|\cos \theta| = \tfrac12$, and the top face is horizontal at $z = 1.8$. List the layer boundaries, and compare the number of layers with uniform layers of $0.1$.

4. ◦ An [infill pattern](/infill-pattern/) uses extrusion width $w = 0.4$ mm and line spacing $s = 4$ mm. Give the infill density of parallel lines and of a square grid. What spacing gives a grid of density 25%? What is the density of a honeycomb with edge $a = 2$ mm, by the entry's approximation?

5. ◦ The design surface has the contact point $p = (0, 0, 0)$ and the unit normal $n = (0, \tfrac35, \tfrac45)$, and the tool axis is $a = (0, 0, 1)$. Give the [cutter location data](/cutter-location-data/): the centre and the tip of a ball cutter of radius 5, the tip of a flat cutter of radius 5, and the tip of a torus cutter with $R = 5$ and corner radius $r_c = 1$.

6. ◦ A ball cutter of radius $r = 3$ mm cuts a plane with passes $w = 2$ mm apart. Find the exact [scallop height](/scallop-height/) and the approximation $w^2/(8r)$. Which stepover gives a scallop of 0.01 mm, by the approximation and exactly?

7. ◦ Compute the [inverse tool offset](/inverse-tool-offset/) for a ball cutter of radius 2 on a grid of spacing 1. The part is a floor at height 0 with a single pin of height 1 at the grid point $(0, 0)$. Give the tip height $Z$ at the grid points at distance 0, 1, $\sqrt2$ and 2 from the pin. How many grid offsets does the footprint of the tool cover?

8. ◦ A ray of a [dexel representation](/dexel-representation/) holds the intervals $I = [0, 3] \cup [5, 9]$ of material. A tool covers $J = [2, 6] \cup [8, 10]$ on the same ray. Give $I \setminus J$, $I \cup J$ and $I \cap J$ as sorted interval lists.

9. ◦ A gap is $G = A - B - C - D$ with nominal value 0.15 mm. The parts $B$, $C$, $D$ have tolerances $\pm 0.03$, $\pm 0.04$ and $\pm 0.12$ mm, and $A$ is exact. Give $T_{\mathrm{WC}}$ and $T_{\mathrm{RSS}}$ from [tolerance stack-up](/tolerance-stack-up/), and the range of the gap under each model. Under which model does the whole range stay positive?

10. ◦ Find the [no-fit polygon](/no-fit-polygon/) of the fixed triangle $A$ with corners $(0, 0), (4, 0), (0, 4)$ and the moving square $B = [0, 2]^2$, whose reference point is the origin. Give its vertices and its area, and compare its number of edges with the bound $n + m$.

11. • Use the facet test of [support structure generation](/support-structure-generation/) with the overhang angle $\alpha = 45°$: a facet needs support when $n_z < 0$ and $n_z^2 > \cos^2\!\alpha\, \|n\|^2$. Which of the facet normals $(0, 3, -4)$ and $(0, 4, -3)$ need support? Then use the layer view with $t = 0.25$ mm: the layer below is the square $[0, 20]^2$ and the layer above is $[0, 20] \times [0, 20.6]$. Find the region that needs support and its area.

12. • A part is the floor $y \le 0$ with a wall $x \ge 3$ that rises to $y = 4$ (work in the plane of the profile). A ball of radius 5 touches the floor at $p = (0, 0)$. Show that the local test of [gouge detection](/gouge-detection/) passes, but the ball gouges the wall. How far must the ball move straight up to clear the wall? What is the largest radius of a ball that touches the floor at $p$ without a gouge?

13. • A rectangular [pocket](/pocket-machining/) of $8 \times 6$ is cleared with a tool of radius $r = 1$. Give the region of tool centres, the uncut area, the area of the opening, and the lower bound on the path length of the toolpath planning entry. Then give the lengths of the [contour-parallel](/contour-parallel-toolpath/) offset loops of the boundary at distances 1 and 2, the distance at which the offset collapses, and what it collapses to. How many arcs does the medial axis of the rectangle have?

14. • A pocket has a convex corner of angle $60°$, cleared by contour-parallel loops with tool radius $r = 2$. The first loop runs at distance $r$ from the walls and the next at $r + s$. For which stepovers $s$ is there no island of uncut material at the corner? For $s = 3.5$, which points of the bisector of the corner, at what distances from the corner, stay uncut between the first two loops?

15. • An [iso-scallop toolpath](/iso-scallop-toolpath/) uses a ball of radius $r = 4$ mm and the scallop bound $h = 0.01$ mm. To first order, find the pass spacing on a plane, across a convex cylinder of radius 12 mm and across a concave cylinder of radius 12 mm. Then an [iso-planar toolpath](/iso-planar-toolpath/) on the plane $z = \tfrac43 x$ must keep the surface spacing found for the plane. What spacing of the drive planes, measured along $x$, does it need?

16. • A triangle with corners $(0, 0), (2, 0), (0, 2)$ moves in a straight line by the vector $(3, 1)$. Give the [swept volume](/swept-volume/) as a polygon, its area, and check the area as the area of the triangle plus the length of the move times the width of the triangle across the move. Does the number of vertices meet the bound $n + 2$?

17. • A [z-map](/z-map-model/) has grid spacing 1 and all heights 5. A ball cutter of radius 2 on a shank moves its centre in a straight line from $(0, 0, 4)$ to $(6, 0, 1)$. Find the new heights at the grid points $(0, 0)$, $(2, 0)$, $(6, 0)$, $(7, 0)$ and $(2, 1)$. Explain why the height at $(2, 0)$ is lower than the bottom of the ball when the ball is right above that point.

18. • Three faces of a part have the outward normals $(1, 0, 0)$, $(0, 1, 0)$ and $(-1, -1, 1)$. Find a direction $d$ with $d \cdot n > 0$ for all three, so that one [accessibility cone](/accessibility-cone/) contains them all. Show that no such direction exists when a fourth face with normal $(0, 0, -1)$ is added.

19. • A part is a cube, and a probe must reach every face along a direction $d$ with $d \cdot n \ge 0$ and $d \ne 0$ for each face it reaches. Show that no single direction reaches all six faces, and give two directions that together reach all of them.

20. • A cube $[0, 2]^3$ has a blind square hole $0.5 < y, z < 1.5$ drilled from the face $x = 0$ to the depth $x = 1$. Using the model of [mold parting directions](/mold-parting-direction/) with two halves that move in opposite directions and any parting surface, find every direction $d$ that works.

21. • Two parts in a stack have equal standard deviation $\sigma$ and correlation $\rho$. Find the variance of $G = X_1 - X_2$ and of $G = X_1 + X_2$. At $\rho = 1$, compare both with the value that the root sum of squares assumes.

22. • Run [bottom-left fill](/bottom-left-fill/), with holes allowed, on a strip of width 6. The rectangles (width, height) come in the order $(3, 2), (4, 1), (2, 3), (6, 1), (1, 2)$. Give the position of each, the height used, and decide whether the height is optimal. What height results if the rule never places a piece in a hole?

23. • In [topology optimization](/topology-optimization/), prove that adding material never increases compliance: if $K \preceq K'$ as positive definite stiffness matrices, then $f^{\mathsf T} K'^{-1} f \le f^{\mathsf T} K^{-1} f$. Use the form $c = \max_u (2 f^{\mathsf T} u - u^{\mathsf T} K u)$.

24. ★ Find the least build height of a regular tetrahedron of edge 1 over all [build orientations](/build-orientation/), and a direction that achieves it. Compare it with the height when the tetrahedron stands on a face.

25. ★ A slot has half-width 2 and depth 3, in a cross-section of a part. A ball cutter of radius 1 on a shank of radius 1 touches the middle of the slot floor. How far can the tool axis tilt from the vertical, in the plane of the cross-section, before the shank hits the slot? Compare with the cone of rays from the contact point that leave the slot. Use the fact in the [accessibility cone](/accessibility-cone/) entry that a ball tool reaches a point when its centre is ray-accessible from the part grown by $r$.

26. ★ The square $[-1, 1]^2$ rotates about its centre from $0°$ to $45°$. Find the area of its [swept volume](/swept-volume/).

27. ★ Three parts are in a chain with $|a_i| = 1$, and part $i$ costs $c_i / T_i$ when its tolerance is $T_i$. Under the worst case constraint $\sum T_i \le T$, derive the cheapest $T_i$, and compute them and the cost for $c = (1, 4, 9)$ and $T = 0.6$. Then solve the same problem under the RSS constraint $\sqrt{\sum T_i^2} \le T$, and compute the $T_i$ and the cost for $c = (1, 8, 27)$ and $T = 0.6$.

28. ★ Let $A$ be the U-shaped polygon with corners $(0, 0), (3, 0), (3, 2), (2, 2), (2, 1), (1, 1), (1, 2), (0, 2)$, and $B = [0, 1]^2$ with its reference point at the origin. Show that the translation $t = (1, 1)$ is a feasible placement whose interior does not meet the interior of $A$, yet $t$ lies in the interior of the [no-fit polygon](/no-fit-polygon/) $A \oplus (-B)$. Find all feasible $t = (1 + u, 1 + v)$ with $|u|, |v| < \tfrac12$.

29. ★ Two springs in series carry a load $f$. Spring $i$ has the stiffness $k_i x_i^p$, where $x_i > 0$ is its amount of material, $k = (1, 4)$, and $x_1 + x_2 \le 3$. The compliance is $c = f^2 (1/(k_1 x_1^p) + 1/(k_2 x_2^p))$. For $p = 1$, find the optimal $x$ and check the optimality condition of the [SIMP method](/simp-method/), equal sensitivities $-\partial c / \partial x_i$. Then find the optimum for general $p$ and for $p = 3$, and say whether this problem is convex.
