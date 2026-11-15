1. ◦ A closed triangle mesh of a torus, a [manifold mesh](/manifold-mesh/) of genus 1, has $V = 9$ vertices. Find $E$ and $F$ from $\chi = V - E + F$ and $3F = 2E$.

2. ◦ In a [corner table](/corner-table/), corners $3t$, $3t + 1$ and $3t + 2$ belong to triangle $t$. Give the triangle of corner 13 and the corners $\mathrm{next}(13)$ and $\mathrm{prev}(13)$. For a closed mesh with $m$ triangles, how many integers do the arrays $V$ and $O$ hold together?

3. ◦ Compute the [discrete Gaussian curvature](/discrete-gaussian-curvature/) $K = 2\pi - \Theta$ at a corner of a cube, where three right angles meet, and at a vertex where seven equilateral triangles meet. Then add up the angle defects of the regular icosahedron, five equilateral triangles at each of its 12 vertices, and compare with the [discrete Gauss-Bonnet theorem](/discrete-gauss-bonnet-theorem/).

4. ◦ Two tetrahedra share one vertex and nothing else. Give $V$, $E$, $F$ and $\chi$ of this mesh. Does every edge have two faces? Is the mesh a manifold mesh?

5. ◦ A hole in a mesh has a border loop of 7 vertices. A patch that uses only the loop vertices, as in [hole filling](/hole-filling/), has how many triangles and how many chords? How many such patches are there? How many triples $i < m < k$ does the dynamic program of [Liepa hole filling](/liepa-hole-filling/) examine?

6. ◦ Let $A = [0, 2]^3$ and $B = [1, 3] \times [1, 3] \times [0, 2]$. Give the volumes of the union, the intersection and the difference $A - B$ that [mesh Boolean operations](/mesh-boolean-operations/) must produce.

7. ◦ In the plane $z = 0$, let $A$ be the rectangle $[0, 2] \times [0, 1]$ and $B$ the square $[0, 1] \times [0, 1]$. Find the one-sided distances $h(A, B)$ and $h(B, A)$, the symmetric distance, and the mean distance from $A$ to $B$, the numbers that the [Metro mesh comparison](/metro-mesh-comparison/) estimates.

8. ◦ In [isotropic remeshing](/isotropic-remeshing/) with target length $L = 0.3$, give the split and collapse thresholds. Which of the edges of length $0.45$, $0.3$ and $0.2$ are split, which are collapse candidates, and how long are the halves of the split edge?

9. ◦ A [progressive mesh](/progressive-mesh/) starts from a tetrahedron and applies vertex splits until the mesh has 30 vertices. How many splits does it store, and what are $E$ and $F$ of the final mesh? [Edgebreaker](/edgebreaker/) then codes the final mesh, which has genus 0. How many symbols does it write, how many of them are C, and how many bits does the code C = 0, S = 100, R = 101, L = 110, E = 111 use? If the string has 3 symbols S, how many symbols E does it have?

10. ◦ A closed triangle mesh of genus 3 has $V = 12$ vertices. Find $E$ and $F$. A [cut graph](/cut-graph/) is built from a spanning tree $T$ of the vertices, a spanning tree $C$ of the dual graph that uses only edges not in $T$, and the leftover edges $X$. How many edges do $T$, $C$ and $X$ have? A reduced cut graph has $B$ vertices of degree at least 3 joined by $P$ paths; how large can $B$ and $P$ be? A quad mesh of the same genus, built along a [cross field](/cross-field/), has 4 vertices of valence 3, 6 of valence 6, and all its other irregular vertices of valence 5. How many have valence 5?

11. • [Vertex welding](/vertex-welding/) with tolerance $\varepsilon = 1$ runs on five points on a line, at $x = 0$, $0.6$, $1.2$, $1.8$ and $3$. Pairs within $\varepsilon$ are merged by a disjoint set structure. Which classes result, and what is the largest distance between two points of one class?

12. • A tetrahedron has the vertices $0 = (0, 0, 0)$, $1 = (1, 0, 0)$, $2 = (0, 1, 0)$, $3 = (0, 0, 1)$ and the faces $(0, 1, 2)$, $(0, 1, 3)$, $(1, 2, 3)$, $(0, 2, 3)$ as read from a file. Run [consistent mesh orientation](/consistent-mesh-orientation/) by breadth-first search from the first face, kept as it is. Then compute $W = \frac16 \sum \det[a\ b\ c]$ over the faces $(a, b, c)$ and give the final outward faces.

13. • Five vertices on a path have heights $z = (0, 0, 1, 0, 0)$; the two ends are fixed and each inner vertex has its two path neighbours. Apply two steps of [Laplacian smoothing](/laplacian-smoothing/) with $\lambda = \frac12$, updating all inner vertices at once from the old values.

14. • [Taubin smoothing](/taubin-smoothing/) uses $\lambda = \frac12$ and $\mu = -\frac35$. Find the pass band frequency $k_{PB}$, the gain $f(k) = (1 - \lambda k)(1 - \mu k)$ at $k = \frac12$ and at $k = 2$, and the largest gain on $[0, k_{PB}]$ with the frequency where it occurs.

15. • In a planar mesh, the edge from $(0, 0)$ to $(2, 0)$ has the two opposite vertices $(1, \frac12)$ and $(1, -\frac12)$. Compute its [cotangent Laplacian](/cotangent-laplacian/) weight $\frac12(\cot\alpha + \cot\beta)$ exactly, and check the sign against $\alpha + \beta$.

16. • A closed triangle mesh of genus 2 has 20 vertices, every one of valence 6 or 7. How many have valence 7? Use $\sum_i (6 - d_i) = 6\chi$ and say where this identity comes from.

17. • The boundary vertices $0, 1, 2$ of a disk mesh are pinned at $(0, 0)$, $(6, 0)$, $(0, 6)$. The inner vertices are 3 and 4, and the triangles are $(0, 1, 3)$, $(1, 4, 3)$, $(1, 2, 4)$, $(2, 0, 4)$, $(0, 3, 4)$. Compute the [Tutte embedding](/tutte-embedding/) with uniform weights and the ORIENT2D value of every triangle.

18. • A vertex $v_0$ at the origin has the four neighbours $(2, 0)$, $(0, 1)$, $(-2, 0)$, $(0, -1)$ in counterclockwise order. Compute [Floater's mean value coordinates](/floater-mean-value-coordinates/) $\lambda_i$ and check that $\sum_i \lambda_i v_i = v_0$.

19. • On the surface of a box with edges $1$, $1$ and $2$, find the length of the shortest path between two opposite corners by unfolding, as in the [discrete geodesic problem](/discrete-geodesic-problem/). Compare it with the shortest path along the edges.

20. • Let $T_1$ have the vertices $(0, 0, 0)$, $(2, 0, 0)$, $(0, 2, 0)$ and $T_2$ the vertices $(1, 2, -1)$, $(1, 4, -1)$, $(1, 3, 2)$. Each triangle has vertices on both sides of the plane of the other. Use the interval step of the [triangle-triangle intersection](/triangle-triangle-intersection/) test to decide whether they meet.

21. • A solid is the cube $[0, 3]^3$ with a hollow cavity $[1, 2]^3$, stored as two closed shells. Both shells were oriented with their normals pointing away from their own centres. What is $W$, the signed volume sum, and what should it be? Which shell has the wrong orientation, and why does flipping each component by the sign of its own volume not detect it?

22. • A toy form of [mixed-integer quadrangulation](/mixed-integer-quadrangulation/) has the energy $E(a, b) = (a - 0.6)^2 + (b - a - 0.7)^2$ with $a$ and $b$ required to be integers. Give the relaxed minimum, the result of greedy rounding (round first the variable closest to an integer, then solve again), the result of rounding both at once, and the best integer point.

23. • Take the open square pyramid with base corners $(\pm1, \pm1, 0)$, apex $(0, 0, 1)$ and the four side triangles. At the apex, compute the cotangent weights of the four side edges, the mixed area $A$, and the [discrete mean curvature](/discrete-mean-curvature/) normal $\mathbf K = \frac{1}{2A}\sum_j (\cot\alpha_j + \cot\beta_j)(x - x_j)$. Give $H = \frac12|\mathbf K|$, the angle defect divided by $A$, and the principal curvatures $k_{1,2} = H \pm \sqrt{\max(H^2 - K^G, 0)}$. Is the clamp at 0 used here, and what does the result say about the two estimates?

24. • The local step of [ARAP parameterization](/arap-parameterization/) replaces the $2 \times 2$ Jacobian $J$ of a triangle by the nearest rotation, with angle $\theta = \operatorname{atan2}(J_{21} - J_{12},\, J_{11} + J_{22})$. Find $\theta$ and the squared Frobenius distance $|J - R_\theta|^2$ for $J = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$, for $J = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ and for $J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. What goes wrong with the formula in the last case, and what does that triangle look like in the plane?

25. ★ Prove that a closed triangle mesh of genus 0 in which every vertex has valence at least 3 has at least four vertices of valence at most 5. Give a mesh where exactly four vertices have valence below 6.

26. ★ Prove that one step of Laplacian smoothing with uniform weights keeps $\sum_i d_i x_i$ on a closed mesh, where $d_i$ is the valence. Use it to find the point to which smoothing with $\lambda = \frac12$ moves the closed square pyramid with base $(0,0,0)$, $(2,0,0)$, $(2,2,0)$, $(0,2,0)$, apex $(1,1,3)$, and the base cut by the diagonal from the first to the third corner. Explain why the steps converge.

27. ★ Show that for $0 < \lambda < -\mu$ the Taubin gain $f(k) = (1 - \lambda k)(1 - \mu k)$ is at least 1 exactly on $[0, k_{PB}]$, and that its maximum there is $1 + (\lambda + \mu)^2 / (-4\lambda\mu)$.

28. ★ Remove the top and the bottom face of the unit cube, and keep the four side faces with outward normals. Compute the [generalized winding number](/generalized-winding-number/) at the centre $(\frac12, \frac12, \frac12)$ and at the centre of the missing bottom face, $(\frac12, \frac12, 0)$. Would a threshold at $\frac12$ call these points inside? A centred $1 \times 1$ square at distance $d$ subtends the solid angle $4 \arcsin\!\big(1 / (1 + 4d^2)\big)$.

29. ★ Run the planar form of [volumetric mesh repair](/volumetric-mesh-repair/) on three sides of the square $[1, 3]^2$, the segments $(1, 1) \to (3, 1)$, $(3, 1) \to (3, 3)$ and $(1, 3) \to (1, 1)$, on the grid $[0, 4]^2$ with $h = 1$ and grid points perturbed to $(i + \varepsilon, j + \varepsilon^2)$. Count the marked grid edges, find the odd cells, patch them along the shortest path of cells, and list the inside grid points. Compare the marks after patching with the marks of the closed square.

30. ★ Flatten the open pyramid of exercise 23 by [discrete conformal equivalence](/discrete-conformal-equivalence/), with $u = 0$ at the four base corners and a target angle sum $\Theta$ at the apex. Show that the apex scale factor is $u = \log\big(2 / (3(1 - \cos(\Theta/4)))\big)$, and that a solution exists exactly for $0 < \Theta < 4\pi$. Give $u$ and the new side length for $\Theta = 2\pi$. Then show that the first Newton step from $u = 0$ equals the apex value of [boundary first flattening](/boundary-first-flattening/) with $u_B = 0$, which solves $A_{II} u_I = -\Omega_I$ with the cotangent Laplacian of the input. Compute it and compare with the exact value. Why can the Newton iteration not end in a wrong minimum?
