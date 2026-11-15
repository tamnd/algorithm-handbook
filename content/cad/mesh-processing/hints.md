1. A torus has $\chi = 0$. With $F = \frac23 E$ the formula gives $9 - E + \frac23 E = 0$, so $E = 27$ and $F = 18$.

2. Corner 13 is in triangle $\lfloor 13/3 \rfloor = 4$, with $\mathrm{next}(13) = 14$ and $\mathrm{prev}(13) = 12$. Each array has one entry per corner, so together they hold $6m$ integers.

3. The cube corner has $K = 2\pi - \frac{3\pi}{2} = \frac{\pi}{2}$, and eight corners give $4\pi$. Seven equilateral triangles give $K = 2\pi - \frac{7\pi}{3} = -\frac{\pi}{3}$, a saddle. The icosahedron has $K = 2\pi - \frac{5\pi}{3} = \frac{\pi}{3}$ at each vertex and $12 \cdot \frac{\pi}{3} = 4\pi = 2\pi\chi$ in total, with $\chi = 2$.

5. A triangulation of an $n$-gon with no new vertices has $n - 2 = 5$ triangles and $n - 3 = 4$ chords. There are $C_5 = 42$ patches, and the program examines $\binom{7}{3} = 35$ triples.

7. The point $(2, y)$ is at distance 1 from $B$, so $h(A, B) = 1$, while $B \subset A$ gives $h(B, A) = 0$ and $H = 1$. The distance is $x - 1$ on the right half, so the mean is $\frac12 \int_1^2 (x - 1)\,dx = \frac14$.

8. Split above $\frac43 L = 0.4$ and collapse below $\frac45 L = 0.24$. The edge of $0.45$ is split into halves of $0.225$, the edge of $0.3$ is left alone, and the edge of $0.2$ is a collapse candidate. The halves of $0.225$ are also below $0.24$, so the collapse step looks at them too; what stops a collapse from making long edges is the guard that no new edge may exceed $0.4$.

9. Each split adds one vertex, two faces and three edges, so 26 splits give $V = 30$, $F = 4 + 52 = 56$ and $E = 6 + 78 = 84$, with $V - E + F = 2$. With $t = 56$ the string has $t - 1 = 55$ symbols, of which $V - 3 = 27$ are C. The other 28 take 3 bits each, so the code has $27 + 84 = 111 = 2t - 1$ bits. Since $n_E = n_S + 1$, there are 4 symbols E.

10. $\chi = -4$, and $3F = 2E$ with $V - E + F = -4$ give $E = 48$ and $F = 32$. $T$ has $V - 1 = 11$ edges and $C$ has $F - 1 = 31$, so $X$ has $48 - 11 - 31 = 6 = 2g$. A reduced cut graph has $B \le 4g - 2 = 10$ and $P \le 6g - 3 = 15$. The indices $(4 - k)/4$ sum to $\chi$: $4 \cdot \frac14 + 6 \cdot (-\frac12) - \frac14 n_5 = -4$, so $n_5 = 8$.

12. The edge $\{0, 1\}$ runs $0 \to 1$ in the first two faces, so the second is flipped; continuing gives $(0, 1, 2)$, $(0, 3, 1)$, $(1, 3, 2)$, $(0, 2, 3)$. Faces through vertex 0, the origin, have determinant 0, and $(1, 3, 2)$ has $-1$, so $W = -\frac16 < 0$ and all four faces are reversed: $(0, 2, 1)$, $(0, 1, 3)$, $(1, 2, 3)$, $(0, 3, 2)$, with $W = \frac16$, the volume.

14. $k_{PB} = 2 - \frac53 = \frac13$. The gains are $f(\frac12) = \frac34 \cdot \frac{13}{10} = \frac{39}{40}$ and $f(2) = 0$. The parabola has its vertex at $k = (\lambda + \mu)/(2\lambda\mu) = \frac16$, where $f = \frac{121}{120}$.

16. Here $\chi = -2$, so $\sum (6 - d_i) = -12$, and each valence-7 vertex contributes $-1$: twelve of them. The identity comes from $\sum_i d_i = 2E$, $3F = 2E$ and $V - E + F = \chi$, which give $\sum_i d_i = 6V - 6\chi$.

17. The rows are $3x_3 - x_4 = x_0 + x_1$ and $4x_4 - x_3 = x_0 + x_1 + x_2$, which give $x_3 = (\frac{30}{11}, \frac{6}{11})$ and $x_4 = (\frac{24}{11}, \frac{18}{11})$. The ORIENT2D values are $\frac{36}{11}$, $\frac{36}{11}$, $\frac{144}{11}$, $\frac{144}{11}$, $\frac{36}{11}$; they are positive and sum to 36, twice the area of the boundary triangle.

21. Each shell counts its own volume, so $W = 27 + 1 = 28$, but the hollow solid has volume $27 - 1 = 26$. The inner shell is wrong: its normals must point into the cavity, out of the material. A rule that makes each shell's volume positive cannot see this, because the right orientation of an inner shell has negative volume; nesting has to be found, for example with a winding number of a point of the inner shell with respect to the outer one.

22. The relaxed minimum is $a = 0.6$, $b = 1.3$ with $E = 0$. The variable $b$ is $0.3$ from an integer and $a$ is $0.4$, so $b = 1$ first; then $a = 0.45$, rounded to 0, gives $E(0, 1) = 0.45$. Rounding both at once gives $(1, 1)$ with $E = 0.65$. The best integer point is $(1, 2)$ with $E = 0.25$.

23. Each base angle of a side triangle has cosine $1/\sqrt3$ and cotangent $1/\sqrt2$, and all angles are acute. Each side edge has weight sum $\sqrt2$, so $\sum_j(\cot\alpha_j + \cot\beta_j)(x - x_j) = (0, 0, 4\sqrt2)$. The Voronoi area is $4 \cdot \frac18(3 \cdot \frac{1}{\sqrt2} + 3 \cdot \frac{1}{\sqrt2}) = \frac{3}{\sqrt2}$, so $\mathbf K = (0, 0, \frac43)$ and $H = \frac23$. The apex angles are $\arccos\frac13 = 70.53°$, the defect is $2\pi - 4\arccos\frac13 = 1.3593$ and $K^G = 0.6408 > H^2 = 0.4444$. The clamp sets the root to 0, so $k_1 = k_2 = \frac23$: the two estimates disagree by much more than rounding at this coarse vertex.

24. For $\operatorname{diag}(2, 1)$, $\theta = 0$ and the distance is 1. The second matrix is $\sqrt2$ times the rotation by $45°$, so $\theta = 45°$ and the distance is $2(\sqrt2 - 1)^2 = 6 - 4\sqrt2 \approx 0.343$. For $\operatorname{diag}(1, -1)$ both arguments of atan2 are 0: $|J - R_\theta|^2 = |J|^2 + 2 - 2\operatorname{tr}(R_\theta^{\mathsf T} J) = 4$ for every $\theta$, so no rotation is nearest. The determinant is $-1$: the triangle is mirrored, a flipped triangle of the map.

25. With $\chi = 2$, $\sum (6 - d_i) = 12$. Each term is at most 3, because $d_i \ge 3$, so at least four terms are positive. The tetrahedron has exactly four vertices, all of valence 3, and the sum is $4 \cdot 3 = 12$.

26. The new position is $(1 - \lambda)x_i + \frac{\lambda}{d_i}\sum_{j \sim i} x_j$; multiplied by $d_i$ and summed, the neighbour sums give each $x_j$ exactly $d_j$ times. The valences are 4, 3, 4, 3 at the base corners and 4 at the apex, so the limit is $\frac{1}{18}\sum d_i x_i = (1, 1, \frac23)$. The step matrix $(1 - \lambda)I + \lambda D^{-1}A$ has eigenvalues in $[1 - 2\lambda, 1]$, with 1 simple on a connected mesh, so for $\lambda = \frac12$ every other mode decays.

27. $f(0) = 1$ and $f$ is a parabola that opens downward, since $\lambda\mu < 0$. The roots of $f(k) = 1$ are $k = 0$ and $k = -(\lambda + \mu)/(\lambda\mu) = 1/\lambda + 1/\mu$. The vertex is halfway, at $k^* = (\lambda + \mu)/(2\lambda\mu)$, and substitution gives the maximum.

28. Each missing face subtends $4\arcsin(\frac12) = \frac{2\pi}{3}$ from the centre, so the sides give $4\pi - \frac{4\pi}{3}$ and $w = \frac23$. From the centre of the bottom, the open half space above sees the sides and the missing top, which subtends $4\arcsin(\frac15)$ at distance 1, so $w = (2\pi - 4\arcsin\frac15)/(4\pi) \approx 0.436$. A threshold at $\frac12$ calls the centre inside and the point in the hole outside.

29. The sides mark 6 edges: two vertical edges under $y = 1$, and two horizontal edges at $x = 3$ and two at $x = 1$. The odd cells are $(0, 2)$ and $(2, 2)$, the cells at the free ends. The path along the row $y \in [2, 3]$ toggles the vertical edges at $x = 1 + \varepsilon$ and $2 + \varepsilon$, giving 8 marks and no odd cell. The inside points are $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$. The two toggled edges are exactly the edges that the missing side $(3, 3) \to (1, 3)$ would cross, so the patched marks equal those of the closed square.

30. Only the side edges change, to $s = \sqrt3\, e^{u/2}$, and the apex angle of a side triangle is $2\arcsin(1/s)$. Setting $4 \cdot 2\arcsin(1/s) = \Theta$ gives $s^2 = 1/\sin^2(\Theta/8) = 2/(1 - \cos(\Theta/4))$, and $s^2 = 3e^u$ gives the formula. The triangle inequality needs $s > 1$, that is an apex angle in $(0, \pi)$, so $0 < \Theta < 4\pi$. For $\Theta = 2\pi$, $u = \log\frac23 \approx -0.4055$ and $s = \sqrt2$: the square with the apex at its centre. At $u = 0$ the gradient is $g = 2\pi - 4\arccos\frac13 = 1.3593$ and the Hessian is $4/\sqrt2 = 2\sqrt2$, so the Newton step is $-0.4806$; BFF solves the same equation $2\sqrt2\, u = -\Omega$ once. The energy is convex, so every critical point is the global minimum, and the line search keeps it decreasing.
