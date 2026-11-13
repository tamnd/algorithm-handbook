1. ◦ The cube $[0,2]^3$ has 12 triangles with outward normals. With [back-face culling](/back-face-culling/), a face with a vertex $v_0$ and normal $n$ is kept when $n \cdot (E - v_0) > 0$. How many triangles are kept for the eyes $E = (3,3,3)$, $(1,-4,1)$, $(-1,5,1)$ and $(2,1,1)$? Say what the rule does in the last case, where the eye lies in the plane of a face.

2. ◦ Use the frustum of the example in [frustum culling](/frustum-culling/): left $x - z \ge 0$, right $-x - z \ge 0$, bottom $y - z \ge 0$, top $-y - z \ge 0$, near $-z - 1 \ge 0$ and far $z + 10 \ge 0$. Classify the box $[1,3] \times [0,1] \times [-3,-2]$ against each plane with its p-vertex and n-vertex. Is the box dropped, and does it meet the frustum?

3. ◦ One pixel receives five fragments, at depths 3, 1, 4, 2 and 5 in drawing order, where a smaller depth is nearer. How many are shaded with a late depth test, with the [early depth test](/early-depth-test/), and with a depth prepass? What is the expected number shaded with the early test if the five fragments come in a uniformly random order?

4. ◦ On one scanline of 8 pixels with centers at $i + \frac12$, two triangles cover $[0, 8)$. Triangle A, with the smaller index, has depth $z = x + 1$, and triangle B has $z = 8 - x$; a smaller $z$ is nearer. Run the span step of the [Watkins scanline algorithm](/watkins-scanline-algorithm/): where does it split the span, which pixels go to each triangle, and how many pieces does it pop? Compare with the number of depth tests of a [z-buffer](/z-buffer/).

5. ◦ The L-shaped room has the vertices $(0,0)$, $(6,0)$, $(6,2)$, $(2,2)$, $(2,6)$ and $(0,6)$. Find the [visibility polygon](/visibility-polygon/) of $q = (5,1)$ and its area. Which points of the room see all of it?

6. ◦ A [terrain](/terrain-visibility/) profile has the eye at $(0, 2)$ and the heights 1, 3, 2, 5, 3, 7 at $x = 1, \ldots, 6$. With one scan outward that keeps the largest slope seen so far, find the visible vertices. How high must a mast at $x = 8$ be for its top to be seen?

7. ◦ The eye ray to a visible point $P$ crosses, in order, the front face of shadow volume 1, the front face of volume 2 and the back face of volume 1, and beyond $P$ it crosses the back face of volume 2. Give the z-pass and z-fail counts of the [shadow volume algorithm](/shadow-volume-algorithm/), and say whether $P$ is in shadow. Then the eye moves inside a third volume, and the ray leaves that volume before $P$. Which count is still right?

8. ◦ An orthogonal polygon has $r = 7$ reflex vertices. How many vertices does it have? Compare the bound of the [orthogonal art gallery theorem](/orthogonal-art-gallery-theorem/) with the bound of [Chvátal's theorem](/chvatal-art-gallery-theorem/).

9. ◦ The visible set is $V = \{A, C, D\}$. Classify each kept set as exact, conservative, aggressive or approximate, in the sense of [visibility culling](/visibility-culling/): $\{A, B, C, D\}$, $\{A, C\}$, $\{A, B, C\}$ and $\{A, C, D\}$.

10. ◦ A unit cube with triangulated faces is lit by a point light at $(3, 2, 5)$. Count the [silhouette edges](/silhouette-edge/) seen from the light and the triangles of the closed shadow volume: near cap, sides and far cap.

11. • In the plane, build a 2D BSP tree from the segments $s_1$ from $(2,0)$ to $(2,4)$, $s_2$ from $(0,3)$ to $(4,3)$ and $s_3$ from $(3,0)$ to $(4,2)$, inserted in this order, with the side function $x - 2$ for $s_1$ and $y - 3$ for $s_2$. How many fragments are there? Give the far-to-near order of [BSP tree visibility](/bsp-tree-visibility/) for the eyes $(5,4)$ and $(0,0)$.

12. • A $4 \times 4$ depth buffer, with a smaller depth nearer, has the rows 1 1 2 9, then 1 1 3 2, then 4 4 1 1, then 4 5 1 1, from top to bottom. Build the max pyramid of the [hierarchical z-buffer](/hierarchical-z-buffer/). An object is hidden over a rectangle when its least depth is at least the stored maximum there. Answer the queries: least depth 6 over the left half; least depth 3 over the top right $2 \times 2$ block; least depth 9.5 over the same block. Count the pyramid cells read.

13. • Four unit cells $(0,0)$, $(1,0)$, $(2,0)$ and $(2,1)$, where cell $(i,j)$ is $[i, i+1] \times [j, j+1]$, are joined by a door on $x = 1$ with $y \in [0.4, 0.6]$, a door on $x = 2$ with $y \in [0, 1]$, and a door on $y = 1$ with $x \in [2, 3]$. The eye is at $(\frac12, \frac12)$ and sees the cone between the directions $(1,-1)$ and $(1,1)$. Run [portal culling](/portal-culling/) with exact cones. Which cells are reached? Repeat with the first door widened to $y \in [0.3, 0.7]$.

14. • A room is the rectangle $[0,6] \times [0,2]$ with an alcove $[0,1] \times [2,6]$ on top. The edge $e$ runs from $a = (2,0)$ to $b = (6,0)$. Find the [weak visibility polygon](/weak-visibility-polygon/) $V(e)$ and the region $V(a) \cap V(b)$, with their areas. If $e$ is a light, give the areas of the umbra, the penumbra and the fully lit part.

15. • In the plane, a light is the segment from $(-2,3)$ to $(2,3)$, an occluder is the segment from $(-1,1)$ to $(1,1)$, and the ground is $y = 0$. For the ground point $(p, 0)$, find the light points that it does not see. Give the umbra, the penumbra and the visible fraction of the light, as in [shadow determination](/shadow-determination/). Compare with a point light at $(0,3)$.

16. • A unit cube is seen from an eye outside it that lies in no plane of a face. Show that the silhouette has 4 edges when exactly one coordinate of the eye is outside $[0,1]$, and 6 edges otherwise.

17. • Use the depth map $d(z) = \frac{f}{f-n}(1 - \frac{n}{z})$ of [z-fighting](/z-fighting/), stored as an integer with 24 bits, with $f = 1000$. Estimate the depth step $\Delta z$ at $z = 500$ for $n = 0.1$ and for $n = 1$. Can a decal 0.01 in front of a wall at $z = 500$ be resolved? Estimate $\Delta z$ there for reversed depth in a 32-bit float, and find the distance below which half of the integer depth values lie.

18. • Prove that an orthogonal polygon with $n$ vertices has $r = (n - 4)/2$ reflex vertices, from the sum of its interior angles. Deduce that $\lfloor n/4 \rfloor = \lfloor r/2 \rfloor + 1$.

19. • An $8 \times 4$ screen, with a smaller depth nearer, holds a wall L over columns 0 to 3 at depth 2 and a wall R over columns 4 to 7 at depth 3. A box at depths 5 to 6 covers columns 2 to 5 of rows 1 and 2. Show that neither wall alone hides the box but the two together do, as in [occlusion culling](/occlusion-culling/). Give the [occlusion query](/occlusion-query/) count if R has a gap in column 5. Why does a positive count not prove that the object in the box is visible?

20. • In the reduction of [minimum guard NP-hardness](/minimum-guard-np-hardness/), take the formula $(u_1 \lor u_2 \lor \bar u_3) \land (\bar u_1 \lor u_3 \lor u_4) \land (\bar u_2 \lor \bar u_4 \lor u_3)$. Compute $K$, choose a satisfying assignment, and list the guards. Explain why any $K$ vertex guards put exactly one guard in each pair $\{t, f\}$ and $\{T, F\}$.

21. • A frame has $10^6$ pixels. Of them, 99% have one opaque layer and 1% have 8 transparent layers. Count the fragments. How many passes does [depth peeling](/depth-peeling/) need, and how many fragment tests in all? How many fragments does the [A-buffer](/a-buffer/) store? About how many passes does dual peeling need?

22. • A convex hexagon has 14 triangulations. For each, find the least number of fans that cover it, where a fan is a set of triangles that share a vertex. Relate the answer to the fan proof of Chvátal's theorem.

23. ★ Show that the plane version of [hidden-surface removal](/hidden-surface-removal/), with the visible pieces listed from left to right, needs $\Omega(n \log n)$ time in the algebraic decision tree model. Use the tangent lines $y = -2 x_i t + x_i^2$ of the parabola $y = -t^2$, clipped to segments, in place of the short horizontal segments of the entry.

24. ★ Five rooms lie in a row: room $i$ is $[i, i+1] \times [0, 4]$ for $i = 0, \ldots, 4$. The doors are on $x = 1$ with $y \in [0,1]$, on $x = 2$ with $y \in [1,2]$, on $x = 3$ with $y \in [2,3]$, and on $x = 4$ with $y \in [0, b]$. For which $b$ does the first room belong to the [potentially visible set](/potentially-visible-set/) of the last, with a line of sight through the interiors of all four doors?

25. ★ Show that a mesh with $F$ faces, seen in an orthographic view from a uniformly random direction, has exactly $F/2$ front faces in expectation. For a perspective eye uniform on a sphere of radius $R$ about the origin, show that a face whose plane is at signed distance $h_f \in [-R, R]$ from the origin is a front face with probability $(1 - h_f/R)/2$. Apply both to the cube $[-1,1]^3$ with 12 triangles and $R = 2$.

26. ★ In a simple polygon, show that the points that see every point of an edge from $a$ to $b$ are exactly $V(a) \cap V(b)$. Give a counterexample in a polygon with one hole.

27. ★ The terrain profile has the vertices $(0,0)$, then $(2i - 1, 0)$ and $(2i, i^2)$ for $i = 1, \ldots, k$, and the eye is at $(0,0)$. Show that the visible part of the profile has $k$ pieces, and find the visible part of the ascent from $(3,0)$ to $(4,4)$. Show that one left-to-right scan finds all pieces in $O(n)$ time for $n$ vertices, and compare with terrain visibility on a TIN, where the output can have $\Theta(n^2)$ size.
