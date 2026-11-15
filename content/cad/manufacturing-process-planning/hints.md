1. $\mathrm{BA} = 53.9 - 30 - 20 = 3.9$ mm, the neutral radius is $3.9/(\pi/2) = 2.4828$ mm, so $\delta = 0.4828$ mm and $K = 0.3219$. DIN 6935 with $r/s = 1.333$ gives $k = 0.65 + 0.5 \log_{10} 1.333 = 0.7125$, so $K = 0.3562$ and a blank of $53.98$ mm, 0.08 mm longer than the test.

2. The bend angle is $180 - 135 = 45$ degrees, $\theta = \pi/4$. Then $\mathrm{BA} = \tfrac{\pi}{4} \cdot 1.4 = 1.0996$, $\mathrm{OSSB} = 2 \tan 22.5^\circ = 0.8284$, $\mathrm{BD} = 0.5573$ and the blank is $60 - 0.5573 = 59.4427$ mm. Reading 135 degrees as the bend angle gives $\mathrm{BA} = 3.2987$, $\mathrm{BD} = 6.3582$ and a blank of $53.6418$ mm, almost 6 mm short.

4. $V = 640{,}000$ mm$^3$ and $A = 64{,}000 + 3{,}200 = 67{,}200$ mm$^2$, so $M = 9.524$ mm and $t = 2 \times 0.9524^2 = 1.81$ min. The long-bar value $M = 10$ mm gives $2.00$ min; the ends cool too, so the true modulus is smaller.

7. The approximation gives $f = \sqrt{8 \cdot 0.4 \cdot 0.004} = 0.1131$ mm. The exact arc height $r - \sqrt{r^2 - f^2/4} = 0.004$ gives $f^2/4 = r^2 - (r - 0.004)^2$, so $f = 0.1129$ mm. The two differ in the fourth decimal because $f \ll r$.

10. The face graph has a vertex per face and an edge per cube edge, so it is the octahedron, with 6 vertices and 12 edges. The kept bends must form a spanning tree of it, with 5 edges, so 5 edges are bends and 7 are cut.

11. Each bend has $\mathrm{BA} = \tfrac{\pi}{2} \cdot 1.4 = 2.1991$ and $\mathrm{OSSB} = 2$, so $\mathrm{BD} = 1.8009$. Along each direction there are two bends, so the blank is $140 - 2\,\mathrm{BD} = 136.3982$ by $100 - 2\,\mathrm{BD} = 96.3982$ mm. The base flat is $96 \times 56$ mm and each wall flat is 18 mm high; the corner squares have side $18 + 2.1991 = 20.1991$ mm.

13. The cost $c(V) = a/V + b V^p$ has one critical point, a minimum at $185.5$ m/min, so $c' < 0$ below it, and on $V \le 160$ the minimum is at the bound. There $t_m = 1.885$ min, $T = (397/160)^4 = 37.9$ min and the cost is $2.233$ dollars, 3 percent above the free optimum.

15. With all faces cooling, $V = 2.5 \times 10^6$ mm$^3$, $A = 165{,}000$ mm$^2$ and $M_c = 15.15$ mm, so $D_0 = 6 M_c = 90.91$ mm. The iteration $D_{k+1} = 6V/(165{,}000 - \pi D_k^2/4)$ gives $94.63$, $94.96$, $94.99$ mm, so $D = H = 95.0$ mm with $M_c = 15.83$ and $M_r = 19.00$ mm. The riser holds $6.73 \times 10^5$ mm$^3$ and gives $1.01 \times 10^5$; the plate needs $7.5 \times 10^4$, so the modulus decides. The neck modulus is $1.1 \times 15.83 = 17.4$ mm.

21. Each contact pushes with a clockwise moment of $\tfrac14$ about the center $(\tfrac12, \tfrac12)$, so none resists a clockwise turn, and that turn opens all four gaps. The weights $\lambda_i$ come out $\tfrac12, -\tfrac12, \tfrac12, -\tfrac12$, of mixed sign. With the last contact at $(0, \tfrac18)$ its moment is counterclockwise, and $\lambda = (-\tfrac18, -\tfrac12, -\tfrac18, -\tfrac12)$, all of one sign.

23. For $d = (1, 1, 1)$ the upper faces are $x = 1$, $y = 1$ and $z = 1$, and each meets two lower faces: one loop of 6 edges, a skew hexagon whose vertices alternate between the planes $x + y + z = 1$ and $x + y + z = 2$. Its projection along $d$ is a regular hexagon. For $d = (1, 1, 0)$ the upper faces are $x = 1$ and $y = 1$, plus the top and bottom under the second rule. Either way there is one loop of 6 edges, with two vertical edges and four horizontal ones, so it is not planar.

24. The octahedron is $K_{2,2,2}$, with Laplacian eigenvalues $0$, $4$ three times and $6$ twice, so it has $4^3 \cdot 6^2 / 6 = 384$ spanning trees. The cube and the octahedron are planar duals, and the complement of a spanning tree of a plane graph is a spanning tree of its dual: the 7 cut edges connect all 8 corners without a cycle. For the classes, a program that applies to the edge sets the 48 maps that permute and flip the coordinates finds 11 orbits.

25. A forced tool not loaded now must be loaded later, and different tools need different changes, so $\psi'$ is a lower bound. For a move with tool $t$ on bend $b$: if $t = \tau$ there is no cost, $F$ can only shrink and $\psi'$ does not grow. If $t \ne \tau$ the move pays $\textit{change}$, and $F(R \setminus \{b\}) \supseteq F(R) \setminus \{t\}$, because only $t$ can lose its forcing bend $b$, so $\psi'$ falls by at most 1. The maximum of consistent heuristics is consistent, and the flip and change parts of the cost are paid separately.

26. A turn by 90 degrees about a lattice point maps the lattice and the four clamp directions to themselves and keeps distances, so conditions 1 to 3 hold. It maps each wrench $(\nu, p \times \nu)$ to $(R\nu, p \times \nu)$, an invertible linear map, so positive spanning is kept. A fixture equal to its own turn needs the placed part to equal its turn, a symmetry of order 4 or, after two turns, of order 2. The triangle has neither, so its 56 fixtures fall into 14 classes of 4.

27. With $V = 1.728 \times 10^6$ mm$^3$ and $A = 86{,}400$ mm$^2$, the rule asks for $D(A - \pi D^2/4) \ge 6V = 1.037 \times 10^7$. The left side grows up to $D = 191$ mm, but $D \le 120$, where it is only $9.01 \times 10^6$. The iteration of the modulus method runs past 120 mm. A riser with $H = 2D$ has $M_r = 2D/9$, which is $26.7$ mm at $D = 120$ against $1.2\,M_c = 27.6$ mm, so it fails too. Use a side riser, an insulating sleeve, or a riser joined by a neck.

28. At a fixed $f$ the law reads $V T^n = C' f^{-a}$, a Taylor law with another constant, and Gilbert's formula does not contain $C$. With $t_m = K_0/(V f)$ and $V = C' f^{-a} T^{-n}$, the cost per part is $t_m (C_o + (C_o t_c + C_t)/T)$ with $t_m \propto f^{a - 1}$, which falls as $f$ grows when $a < 1$.
