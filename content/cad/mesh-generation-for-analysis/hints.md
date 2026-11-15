1. The hypotenuse is 5, so $R = 5/2$; the shortest edge is 3, so $\rho = 5/6$. The smallest angle is opposite the edge 3, $\theta_{\min} = \arcsin(3/5) \approx 36.87°$, and $1/(2 \cdot 3/5) = 5/6$. With $A = 6$ and $\sum \ell_i^2 = 50$, the mean ratio is $24\sqrt3/50 \approx 0.831$. The inradius is $2A/(3+4+5) = 1$, so the radius ratio is $2/2.5 = 0.8$.

4. The total after $k$ layers is $d_k = h_1 (r^k - 1)/(r - 1) = 0.004\,(1.25^k - 1)$. It is $0.0426$ after 11 layers and $0.0542$ after 12, so 12 layers are needed.

5. A hex mesh has $6H = 2I + B$, so $B$ is even, and 7 is odd. Split one more face into two quads, or the same face into three, to make $B$ even. For a ball, the theorem of Thurston and Mitchell then gives a topological hex mesh with that boundary, and Eppstein's construction gives one with $O(B)$ hexes.

9. $40 \cdot 12 = 480$ hexes and $52 \cdot 13 = 676$ nodes. From $4 \cdot 40 = 2E_{\mathrm{int}} + 22$ the source has $69$ interior edges and $91$ edges in all, and $52 - 91 + 40 = 1$. The boundary has $40 + 40 + 22 \cdot 12 = 344$ quads. Inside there are $40 \cdot 11 = 440$ quads between layers and $69 \cdot 12 = 828$ quads swept from interior edges, $1268$ in all, and $6 \cdot 480 = 2 \cdot 1268 + 344$.

10. The Hessian is $\operatorname{diag}(8, 2)$, so $M = \operatorname{diag}(50, 12.5)$, with lengths $1/\sqrt{50} \approx 0.141$ in $x$ and $1/\sqrt{12.5} \approx 0.283$ in $y$. A unit equilateral triangle in the metric has area $(\sqrt3/4)/\sqrt{\det M} = \sqrt3/100$, about 58 triangles. The isotropic mesh must use the smaller length everywhere, $M = 50 I$, about 115 triangles: twice as many, $\sqrt{8/2} = 2$.

11. The diagonal from $(0,0)$ to $(3,1)$ gives $\frac32 \cdot \frac{20}{12} + 3 \cdot \frac{14}{12} = \frac{17}{2}$; the other diagonal gives $\frac{19}{2}$. The point $(0,2)$ lies outside the circle through the other three, so the first diagonal is Delaunay, and its smallest angle is $18.43°$ against $15.26°$.

12. In the first case each new tetrahedron has volume $\tfrac19$, and $3 \cdot \tfrac19 = \tfrac16 + \tfrac16$. In the second case the segment $de$ meets $z = 0$ at $(\tfrac76, \tfrac76, 0)$, outside $abc$, so the signed volumes are $\tfrac{7}{18}$, $-\tfrac49$, $\tfrac{7}{18}$. They still add up to $\tfrac13$, but $bcde$ is inverted and the three overlap.

15. Count angles: $\pi T = \pi(B - 2) + 2\pi V_i$. A perfect matching pairs the triangles, so $T$ must be even, which happens exactly when $B$ is even. The pentagon fan has $T = 5$ and no perfect matching. An even $T$ is not enough: a triangle with three ears has $T = 4$ and a star as its dual graph.

17. On the flat triangle, $p = 1 - y/\varepsilon$, so $\nabla(u - p) = (2x, 1/\varepsilon)$, which is at least $1/\varepsilon$ while the diameter stays 2. On the right triangle, $p = x$ and $\nabla(u - p) = (2x - 1, 0)$, of length at most 1 for every $\varepsilon$.

21. Put $s = h_0 + Lr$. The integral $\int_0^1 2\pi r\,dr/(h_0 + Lr)^2$ equals $\frac{2\pi}{L^2}\left(\ln\frac{h_0 + L}{h_0} + \frac{h_0}{h_0 + L} - 1\right)$. With $L = \tfrac12$ it is $74.2$, $131.2$ and $188.9$, or about $171$, $303$ and $436$ triangles, while a uniform mesh needs $7.3 \cdot 10^4$, $7.3 \cdot 10^6$ and $7.3 \cdot 10^8$. In three dimensions $\int 4\pi r^2\,dr/(h_0 + Lr)^3$ is also $\frac{4\pi}{L^3}\ln(1/h_0) + O(1)$.

23. Each interpolant is the piecewise linear function whose graph is the lifted triangulation, and $f_I \ge f$ because $f$ is convex, so the difference of the errors is $\int (f_{I,1} - f_{I,2})$, the volume between the two graphs, which together bound the lifted tetrahedron. Its volume is $\frac16|\det| = 1 = \frac{19}{2} - \frac{17}{2}$. The Delaunay triangulation is the lower hull of the lifted points, so its graph lies below.

24. The centre is $(\tfrac12, \tfrac12, \tfrac t2)$, so $R = \sqrt{1/2 + t^2/4}$, the shortest edge is 1, $\rho = R$ and $V = t/6$. The faces at the edge from $(0,0,0)$ to $(1,0,0)$ lie in $z = 0$ and in the plane through $(0,1,t)$, so the dihedral angle there is $\arctan t$. For $t = 0.1$: $\rho \approx 0.709$, $V = \tfrac{1}{60}$, angle $5.71°$; the smallest dihedral angle is $5.68°$ and the largest $171.95°$.

25. The kernel is the open triangle with corners $(0,0)$, $(-2,-2)$, $(2,-2)$. The areas are $2(y+2)$, $2(2-x)$, $x - y$, $-x - y$ and $2(x+2)$. By symmetry $x = 0$, and $2y + 4 = -y$ gives $p = (0, -\tfrac43)$ with smallest area $\tfrac43$. The average of the five ring vertices is the reflex corner $(0,0)$ itself, where two triangles have zero area.
