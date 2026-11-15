1. With maximal smoothness the count is $n + p = 13$ per direction, so $13$, $169$ and $2197$. The $C^0$ space has $pn + 1 = 31$ per direction, so $31$, $961$ and $29791$.

3. Each abscissa is the mean of three consecutive inner knots: $0, \tfrac13, 1, 2, \tfrac83, 3$. There are six, one per function. The first and the last carry the boundary conditions, and the equation is imposed at the other four.

5. The relative change is $(\ell/L)(A/A' - 1) = \tfrac{1}{50} \cdot 3 = 6\%$, and the defeatured model is the stiffer one. The stress in the groove is $P/A' = 4P/A$, four times the value of the defeatured model, and this factor does not depend on $\ell$.

6. The midline runs from $x = 0.8$ to $x = 39.2$, half a thickness short of each free edge. The offset is $d = s/2 = 0.1$, so each center lies $d^2/(2t) = s^2/(8t) = 0.003125$ from the midline, and the reported thickness is $t + d^2/t = 1.60625$.

8. The $3 \times 3$ grid has $V_b = 12$ and $V_+ = 4$, so $64 = 8^2$, the tensor product of $C^1$ cubic splines with three elements. Splitting the center cell adds one crossing vertex; its four edge midpoints are T-junctions and do not count, so $4(12 + 5) = 68$. Splitting a corner cell adds one crossing vertex and two boundary vertices, so $4(14 + 5) = 76$.

9. On $[0, 1]$ the rows are $N_0 = (1, 0, 0, 0)$, $N_1 = (0, 1, 0, 0)$, $N_2 = (0, 0, 1, \tfrac12)$ and $N_3 = (0, 0, 0, \tfrac12)$. On $[1, 2]$ they are $N_2 = (\tfrac12, 0, 0, 0)$, $N_3 = (\tfrac12, 1, 0, 0)$, $N_4 = (0, 0, 1, 0)$ and $N_5 = (0, 0, 0, 1)$. Only $N_2$ and $N_3$ cross $u = 1$. For $N_2$ the values and the first derivatives match there, $\tfrac12$ and $-\tfrac32$ on both sides, but the second derivatives are $-9$ and $3$, so the space is $C^1$ at $u = 1$, as a knot of multiplicity 2 in degree 3 predicts.

13. The kept level-0 functions have the knots $(0, 1, 2, 3)$, $(1, 2, 3, 4)$, $(2, 3, 4, 4)$ and $(3, 4, 4, 4)$, and the kept level-1 functions those with support in $[0, 2]$: $(0, 0, 0, \tfrac12)$, $(0, 0, \tfrac12, 1)$, $(0, \tfrac12, 1, \tfrac32)$ and $(\tfrac12, 1, \tfrac32, 2)$. The sums are $\tfrac{41}{32}$ at $\tfrac34$ and $\tfrac{51}{32}$ at $\tfrac54$. The two-scale relation gives the coefficients $\tfrac14, \tfrac34, \tfrac34, \tfrac14$; the first two belong to kept functions, so the truncated function is $\tfrac34 N_{(1, \frac32, 2, \frac52)} + \tfrac14 N_{(\frac32, 2, \frac52, 3)}$, with value $\tfrac{3}{32}$ at $\tfrac54$.

14. The points are $0, \tfrac16, \tfrac12, \tfrac56, 1$. At $\tfrac12$ the row is $(0, -9, 18, -9, 0)$, which is $-(1, -2, 1)/h^2$ with $h = \tfrac13$. The solution is $(0, \tfrac1{12}, \tfrac5{36}, \tfrac1{12}, 0)$. The exact solution $x(1 - x)/2$ is a quadratic, so it lies in the space and satisfies every row, and the matrix is nonsingular.

16. On each element the error of the interpolant is $s(h - s)$, and $\int_0^h s^2 (h - s)^2 \, ds = h^5/30$. Summed over $1/h$ elements this gives the error $h^2/\sqrt{30}$, a factor $\sqrt6$ above the best approximation. Both are of order $h^2 = h^{p+1}$.

19. Here $g(\tfrac12) = (1 + a)/2$ is the minimum, so the map is valid for $a > -1$. In degree 3 the coefficients are $(1, b, b, 1)$ with $b = (1 + 2a)/3$, positive for $a > -\tfrac12$. One de Casteljau step gives $(1, (2 + a)/3, (1 + a)/2, (1 + a)/2)$ on the left half and the mirror image on the right, positive exactly for $a > -1$: one subdivision certifies every valid map of this family.

20. With $\phi_1 = x$ and $\phi_2 = x^2$, the stiffness matrix is $\begin{pmatrix} (1 + \alpha)/2 & (1 + 3\alpha)/4 \\ (1 + 3\alpha)/4 & (1 + 7\alpha)/6 \end{pmatrix}$ and the load vector is $(\tfrac18, \tfrac1{24})$. Its determinant is $(1 + 14\alpha + \alpha^2)/48$, which is where the denominator comes from. Compare $c_1/2 + c_2/4$ with the exact $u(\tfrac12) = \tfrac18$.

21. By symmetry the weights are $(w_1, w_2, w_3, w_2, w_1)$. The B-spline two places to the left meets only the point $\tfrac12$, with value $\tfrac18$, so $w_1 = \tfrac1{15}$. The next one gives $\tfrac34 w_1 + \tfrac12 w_2 + \tfrac18 w_3 = \tfrac{13}{60}$ and $B_i$ itself gives $\tfrac14 w_1 + w_2 + \tfrac34 w_3 = \tfrac{11}{20}$. So $w_2 = \tfrac7{30}$ and $w_3 = \tfrac25$, and the sum is 1.

22. The Greville points are $0, \tfrac12, 1, \tfrac32, 2$, and on each element the three nonzero functions are Bernstein polynomials with second derivatives $(2, -4, 2)$. With the right-hand derivative, the row at $1$ equals the row at $\tfrac32$; with the left-hand one, it equals the row at $\tfrac12$. Either way two rows coincide and the rank is 4.
