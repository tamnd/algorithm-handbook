1. The virtual condition of a pin is $d_M + t = 20.00 + 0.05 = 20.05$ mm. The zone grows by the departure from maximum material: $0.05$ mm at 20.00, $0.10$ mm at 19.95 and $0.15$ mm at 19.90.

4. The point $(3, 4)$ is at distance $5 - 4 = 1$ outside and has algebraic distance $9 + 16 - 16 = 9 = 1 \cdot (1 + 8)$. The point $(0, 3)$ is at distance $-1$ inside and has algebraic distance $-7 = (-1)(-1 + 8)$. In the sum of squares the outside point weighs $81/49 \approx 1.65$ times as much, although both are at distance 1.

5. The sagitta is $50 - \sqrt{2475} \approx 0.2506$ mm. The best plane is parallel to the chord at half the sagitta, so its largest distance is about $0.1253$ mm: no plane fits with $\varepsilon = 0.1$, while with $\varepsilon = 0.2$ both a plane and the cylinder are valid.

6. A cone has $1$, the rotation about its axis. Two planes at a right angle have $1$, the translation along their common line. A box corner has $0$. A hemisphere with its base has $1$, the rotation about the axis through the center normal to the base.

8. $6 = 110_2$ gives $\varphi_2(6) = 0.011_2 = 3/8$, so the point is $(3/8, 3/8)$, or $(15, 6)$ mm. $11 = 1011_2$ gives $\varphi_2(11) = 0.1101_2 = 13/16$, so the point is $(11/16, 13/16)$, or $(27.5, 13)$ mm.

10. The hull has two parallel edges of slope $\frac12$: the lower one from $(0, 0)$ to $(4, 2)$ through $(2, 1)$, and the upper one from $(1, 2)$ to $(3, 3)$. Their distance is $1.5 / \sqrt{1.25} = 3/\sqrt 5 \approx 1.3416$, the minimum zone. The least-squares line passes through the centroid $(2, 1.6)$ with slope about $0.6292$, the main axis of the scatter matrix with $S_{xx} = 10$, $S_{xy} = 5$, $S_{yy} = 5.2$; its residuals span a zone of width about $1.5977$, which is $19\%$ wider.

11. An edge-edge pair sets it: the edge from $(0, 0, 0)$ to $(4, 4, 1)$ and the edge from $(0, 4, 1)$ to $(2, 1, 2)$. Their cross product is the normal $(7, -2, -20)$, the dot products of the five points with it lie in $[-28, 0]$, and the flatness is $28/\sqrt{453} \approx 1.3156$. Check that every face-vertex pair of the hull gives a larger width.

14. The nearest neighbor tour is $B, E, C, A, D$ with no ties, of length $2\sqrt 2 + \sqrt 5 + 3 + 4\sqrt 2 + 4 \approx 17.721$. The shortest tour is $B, A, C, E, D$ or its reverse, of length $\sqrt 2 + \sqrt{10} + 3 + \sqrt 5 + 2\sqrt 2 + 4 \approx 16.641$.

16. Let $F_k(b)$ be the least cost of the first $k$ dimensions within a budget of $b$ steps. The cheapest choice is $(0.04, 0.03, 0.03)$ at cost $5 + 4 + 4 = 13$, and the next best cost $14$. Of the $27$ choices, $15$ are feasible.

18. $h_0 = 5\sqrt 2 \approx 7.0711$. The sensitivities are $\partial h/\partial r = 1/\sin 45° = \sqrt 2$ and $\partial h/\partial \alpha = -r\cos(\alpha/2)/(2\sin^2(\alpha/2)) \approx -3.5355$ per radian, or $-0.0617$ per degree. The worst case is $0.0141 + 0.0309 \approx 0.0450$ mm and the RSS value $0.0339$ mm. The corners give $-0.0447$ and $+0.0453$ mm, so the linear model is close here because the tolerances are small.

20. Line A alone fits exactly at angle $0$, and line B alone fits exactly at angle $\arctan 0.1 \approx 5.71°$. The joint fit uses the pooled scatter matrix $\begin{pmatrix} 16 & 0.8 \\ 0.8 & 0.08 \end{pmatrix}$ of both sets, each centered on its own centroid. Its smallest eigenvalue, about $0.0399$, is the total squared error; the direction is at about $2.87°$, and the lines are $1.2 \cos 2.87° \approx 1.1985$ apart.

22. Write $i$ with $m$ bits. The condition $i/N \in [a/2^j, (a+1)/2^j)$ fixes the top $j$ bits of $i$ to the bits of $a$. The condition on $\varphi_2(i)$ fixes its first $m - j$ binary digits, which are the low $m - j$ bits of $i$ in reverse order. Together they fix all $m$ bits, so exactly one $i$ qualifies.

23. Growing by $t$ adds $Pt + \pi t^2$ (Steiner). Shrinking moves each edge in by $t$; the inner polygon has the same angles, and the area lost is $Pt$ minus the overlap at the corners, $t^2 \cot(\theta_i/2)$ at each. The rectangle gives $60 + 0.01\pi - 0.04 \approx 59.991$. The triangle has $P = 30$ and three angles of $60°$, so the area is $6 + 0.01\pi - 0.03\sqrt 3 \approx 5.9795$.

24. The Lagrange condition is $a_i b e^{-b T_i} = \lambda$ for every $i$, so every cost term equals $\lambda / b$. Take logarithms and use $\sum T_i = T$ to find $T_i$. The result is $T = (0.06848, 0.04076, 0.04076)$ mm, every cost term equals $0.13030$, and the total is $0.39091$, against $6 e^{-2.5} \approx 0.49251$ for equal tolerances.

26. The mean lies at least $(\max - \min)/n$ from each extreme, so the largest deviation from the mean is at most $(1 - 1/n)(\max - \min)$. The midrange leaves exactly $(\max - \min)/2$. For $(0, \dots, 0, R)$ the mean leaves $R(1 - 1/n)$ and the midrange $R/2$.
