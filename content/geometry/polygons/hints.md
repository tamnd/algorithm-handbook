3. Twice the signed area is $(b - a) \times (c - a) = 14$, so the triangle is counterclockwise. The coordinates are $\lambda_a = \operatorname{orient}(p, b, c)/14 = 6/14 = 3/7$, $\lambda_b = \operatorname{orient}(a, p, c)/14 = 3/14$ and $\lambda_c = \operatorname{orient}(a, b, p)/14 = 5/14$. All three are positive and they sum to 1, so $p$ is inside.

4. (a) The shoelace sum is 26, so the area is 13. (b) At the lowest vertex $v_0$, $\operatorname{orient}(v_4, v_0, v_1) = 21 > 0$, so the polygon is counterclockwise. (c) $\operatorname{orient}(v_2, v_3, v_4) = -6$, so $v_3$ is reflex. (d) The edge vectors have gcds 1, 1, 1, 2, 1, so $B = 6$ and $I = 13 - 3 + 1 = 11$.

5. From $(2,2)$ the ray crosses only $v_1 v_2$, at $x = 14/3$: one crossing, inside. From $(3,4)$ the ray passes through $v_2 = (4,4)$, the upper end of both $v_1 v_2$ and $v_2 v_3$. The half-open rule counts an edge only when $y$ lies in $[y_{\min}, y_{\max})$, so neither edge counts, and $v_4 v_0$ is crossed at $x = 1/5$, to the left. There are no crossings and the point is outside, which is right because the boundary touches the ray at $v_2$ without crossing it.

9. Each pass around the square adds one full turn and one crossing, and each pass adds 8 to the shoelace sum. For the stars, count how many edges a ray from the center crosses; each crosses it in the same direction.

11. Removing a diagonal is allowed when the merged angle at both endpoints stays at most $180°$. At $v_3$ the fan angles are $45°, 90°, 90°, 45°$ in the order $v_4, v_5, v_0, v_1, v_2$.

15. The edge directions of $-Q$ are $(2,-2), (0,2), (-2,0)$; merge them with the four edge directions of $P$, starting from the sum of the lowest vertices. $P$ and $Q$ meet exactly when the origin lies in $P \oplus (-Q)$, and the distance between them is the distance from the origin to $P \oplus (-Q)$.

17. The new arguments are $y = 11$, giving $f(3, 2, 3, 2)$. Both sums count the lattice points under the same segment, once by columns and once by rows.

18. The points on $d$ strictly between its ends are boundary points of $P_1$ and $P_2$ but interior points of $P$, and the two ends of $d$ are counted on both boundaries. Then add $A_1 = I_1 + B_1/2 - 1$ and $A_2 = I_2 + B_2/2 - 1$.

19. The edges of $-P$ are the edges of $P$ turned by $180°$, so the merged edge sequence is the edge sequence of $P$ followed by its negation. An edge of $P$ and an edge of $-P$ merge into one only when they point the same way, that is, when the two edges of $P$ are parallel.

20. The triangle $0, v_i, v_{i+1}$ has signed area $\frac{1}{2}(v_i \times v_{i+1})$ and centroid $(v_i + v_{i+1})/3$. Sum the area-weighted centroids and divide by $A$; triangles with negative area cancel the parts outside the polygon.

21. Sum over $y$ from 0 to 25: the count is $\sum_{y=0}^{25} (\lfloor (100 - 4y)/3 \rfloor + 1)$. Shift the numerator so that the slope term is nonnegative, for example by summing over $j = 25 - y$, which gives $26 + f(26, 3, 4, 0)$.
