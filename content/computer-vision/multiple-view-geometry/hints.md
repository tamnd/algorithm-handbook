1. The cross-ratio of $0, 2, 3, 6$ is $(2 \cdot 3)/(3 \cdot 4) = 1/2$. The images are $0, 2/3, 3/4, 6/7$, and the same formula gives $(2/3)(3/28) / ((3/4)(4/21)) = 1/2$.

2. For $w = 0.6$ the values are 11, 19, 34, 57, 163 and 272; for $w = 0.3$ they are 49, 169, 567, 1893, 21055 and 70188. The sizes 4, 5, 7 and 8 belong to the homography, the five-point $E$, the seven-point $F$ and the eight-point $F$.

6. $x_2^{\mathsf T} F x_1 = y_1 - y_2 = -0.4$. The first two entries of $F x_1$ and of $F^{\mathsf T} x_2$ are $(0, -1)$ and $(0, 1)$, so the Sampson distance is $0.16/2 = 0.08$ in squares, or 0.2828. Moving each $y$ by 0.2 toward the other costs $0.04 + 0.04 = 0.08$, so here the approximation is exact, since the constraint is linear in the coordinates.

8. $H$ has the rows $(6/5, 0, 0)$, $(0, 6/5, 0)$ and $(-2/5, 1/5, 1)$. The centre goes to $(2/3, 2/3)$; a homography maps lines to lines, so the meeting point of the diagonals goes to the meeting point of their images. The points at infinity $(1, 0, 0)$ and $(0, 1, 0)$ go to $(3, 0, -1)$ and $(0, 6, 1)$, and the line through them is $(2, -1, 6)$, that is $2x - y + 6 = 0$.

9. $q = (10/20)(9/19) = 9/38 \approx 0.2368$, smaller than $w^2 = 0.25$, so $k = \lceil \ln 0.01/\ln(29/38) \rceil = 18$ instead of 17. After 17 samples the failure probability is $(29/38)^{17} = 0.0101$ instead of $0.75^{17} = 0.0075$.

10. The depths in the two cameras are $(4, 5)$ for $(I, t)$, $(-4, -5)$ for $(I, -t)$, $(-0.444, 0.556)$ for $(\operatorname{diag}(-1, -1, 1), t)$ and $(0.444, -0.556)$ for $(\operatorname{diag}(-1, -1, 1), -t)$. Only $(I, t)$ puts the point in front of both cameras.

13. $H = K R K^{-1}$ maps $x$ to $f \tan(\arctan(x/f) + 5°)$ on the horizontal line through the principal point. So $0 \mapsto 87.49$ and $500 \mapsto 614.36$: the shift grows toward the edge of the image.

15. The scorings are $400 + 48 \cdot 400 + 50 \cdot (200 + 100 + 50 + 25 + 12 + 6 + 3) = 39400$ over 399 observations; at $i = 400$, $f(i) = 1$ and the run stops. The bound $2BM$ is 40000.

18. The pencil is $\operatorname{diag}(3 - 2\alpha, 2, 1 + 2\alpha)$, with determinant $2(3 - 2\alpha)(1 + 2\alpha)$, a quadratic. Its roots $\alpha = 3/2$ and $\alpha = -1/2$ give $\operatorname{diag}(0, 2, 4)$ and $\operatorname{diag}(4, 2, 0)$. The coefficient of $\alpha^3$ is $\det(F_1 - F_2) = 0$, so the third solution is at infinity, $F_1 - F_2 = \operatorname{diag}(-2, 0, 2)$, which is also singular. With $\lambda F_1 + \mu F_2$ the cubic is homogeneous and keeps all three roots.

19. On a plane, $x_2^{\mathsf T} [v]_\times H x_1 = x_2^{\mathsf T} [v]_\times x_2$ up to scale, which is 0. The matrices $[v]_\times H$ form a space of dimension 3, all in the null space of the $n \times 9$ matrix, so its rank is at most 6. A program with exact fractions (seed 7, 12 points) gives rank 6 for planar points and 8 for points in general position.

20. The theorem says the matches fix the pair of cameras up to a projective map of space, which has 15 degrees of freedom. So $F$ has $22 - 15 = 7$.

21. $[t]_\times R_t = -[t]_\times$, because $[t]_\times t = 0$, so $[t]_\times R_t R = -E$, which is $E$ up to scale. The half turn about the baseline maps the ray of camera 2 to its mirror image, so a point in front of both cameras for $(R, t)$ is reconstructed for $(R', t)$ in front of one camera and behind the other.
