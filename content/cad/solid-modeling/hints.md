1. $A \cap B$ is the segment $[1, 2] \times \{1\}$, and $A \cap^* B = \emptyset$. $A \cup B$ is already regular: a point of the open segment $(1, 2) \times \{1\}$ has $A$ below it and $B$ above it, so it is an interior point. $A - B$ is $A$ without that segment, which is not closed, and $A -^* B = A$. The regularization of $D$ is $A$; the dangling segment has no interior. All of these except $A \cap B$, $A - B$ and $D$ are r-sets, the empty set included.

3. $n = 26$ and $p = 48$: the full block has $3 \cdot 18 = 54$ face pairs, and the center cube is in 6 of them. The area is $156 - 96 = 60$, the outer area 54 plus the 6 faces of the cavity. The boundary has two shells.

4. $V = 24$, $E = 36$, $F = 14$ (six outer faces and four walls per hole). The top and bottom faces have three loops each, so $L = 18$ and $R = 4$. With $S = 1$ and $H = 2$, $24 - 36 + 14 - 4 = -2 = 2(1 - 2)$.

5. One MVFS, five MEV and four MEF: they give $V = 6$, $E = 9$, $F = 5$. In general MVFS gives one vertex and one face, each MEV one vertex and one edge, and each MEF one edge and one face, so the counts are $1$, $V - 1$ and $F - 1$, and they need $E = V + F - 2$, which is Euler's formula.

7. On $y = 1$: $A$ gives $[0, 4]$, $B$ gives $[1, 3]$, the difference $[0, 1] \cup [3, 4]$, $C$ gives $[7/2, 5]$, and $S$ gives $[0, 1] \cup [3, 5]$. On $y = 5/4$: $B$ gives $[2 - \sqrt{15}/4, 2 + \sqrt{15}/4] \approx [1.032, 2.968]$, and $S$ gives $[0, 2 - \sqrt{15}/4] \cup [2 + \sqrt{15}/4, 5]$.

10. The pocket gives 11 faces and 24 arcs: the 12 edges of the cube and the 4 rim edges are convex, and the 4 wall-to-wall and 4 wall-to-floor edges are concave. The six outer faces, the top included, have only convex arcs and are deleted; the four walls and the floor remain and match the pocket. The through hole gives 10 faces and 24 arcs, 20 convex and 4 concave; the four walls remain, joined in a cycle of concave arcs, and match the through hole.

13. With respect to $A$: out on $[-1, 0)$, on on $[0, 2]$, out on $(2, 4]$. With respect to $B$: out on $[-1, 1)$, on on $[1, 3]$, out on $(3, 4]$. On $(1, 2)$ both say on, and the labels cannot decide: the neighborhoods are the lower half disk from $A$ and the upper half disk from $B$, whose union is the full disk, so the piece is in. The result is out, on, in, on, out on $[-1, 0)$, $[0, 1]$, $(1, 2)$, $[2, 3]$, $(3, 4]$. At $(1, 1)$ the neighborhood is the lower half disk plus one quadrant, so the point is on.

14. $\kappa = 2$, so $h \le \sqrt{8 \cdot 10^{-3}/2} \approx 0.0632$ and the circumference $\pi$ needs 50 steps; 50 equal chords have the error $\frac12(1 - \cos(\pi/50)) \approx 0.000987$. For radius $0.01$, $\kappa = 100$, $h \approx 0.0089$ and 8 steps. A marching method that has no start point on the small circle never sees it.

15. At $x_0$, $F = (-1/50, -9/50)$, and one step gives $(32647/30215, 60561/60430, 81991/60430) \approx (1.0805, 1.0022, 1.3568)$. The largest residual then goes about $0.18$, $0.013$, $3 \cdot 10^{-5}$, $2 \cdot 10^{-10}$, $0$: it is squared at each step. At $(2, 0, 0)$ both gradients are multiples of $(1, 0, 0)$, so $JJ^{\mathsf T}$ is singular.

16. With the angle $\theta$ around the tube, $\theta = 0$ outside, the curvatures are $-1$ and $-\cos\theta/(3 + \cos\theta)$. The factor is $(1 + d)(1 + d\cos\theta/(3 + \cos\theta))$; it is positive everywhere exactly for $-1 < d < 2$, and $d = 2$ fails at the inner equator. The bound $\rho_{\min} = 1$ gives only $|d| < 1$: it ignores on which side the centers of curvature lie.

19. In floating point, $D(p, q, r) = 0$, $D(q, r, p) \approx -2.8 \cdot 10^{-17}$ and $D(r, p, q) = 0$. Exactly, the stored points turn clockwise and all three are negative, about $-1.9 \cdot 10^{-17}$. So two of the float answers say collinear, the third is right, and they do not agree with each other.

20. The volume is 2 and the center of mass is $(2/3, 2/3, 1/2)$. Integrate monomials over the triangle with $\int x^a y^b = a!\, b!\, 2^{a+b+2}/(a+b+2)!$. About the center, $J_{xx} = J_{yy} = 11/18$, $J_{zz} = 8/9$, $J_{xy} = 2/9$ and $J_{xz} = J_{yz} = 0$, with the convention $J_{xy} = -\int (x - c_x)(y - c_y)\,dV$.

23. For regular closed sets, $A \cup^* B = A \cup B$ and $A \cap^* B = \operatorname{cl}(\operatorname{int} A \cap \operatorname{int} B)$. Write $W = \operatorname{int} B \cup \operatorname{int} C$, so that $\operatorname{cl} W = B \cup C$, by regularity of $B$ and $C$. For an open $U$, $U \cap \operatorname{cl} W \subseteq \operatorname{cl}(U \cap W)$.

24. Square $\sqrt{x^2 + y^2} = 1 - x - y$; the condition $x + y \le 1$ picks the branch. It crosses the diagonal at $x = y = 1 - 1/\sqrt 2 \approx 0.293$, the distance curve at $1/\sqrt 2 \approx 0.707$, and $\max(x, y) = 1$ at $1$. Far from the corner all three approach the lines $x = 1$ and $y = 1$.

25. $V = 14$, $E = 23$, $F = 12$, so $V - E + F = 3$ with no rings, and $2(S - H)$ is even. Each boundary is a sphere with $\chi = 2$, and they meet in a segment with $\chi = 1$. Four faces meet at the shared edge.
