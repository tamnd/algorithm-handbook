1. ◦ With the convention of the [cross-ratio](/cross-ratio/) entry, for which the points $0, 1, 2, 3$ on a line give $1/4$, compute the cross-ratio of $0, 2, 3, 6$. Map the four points by $x \mapsto x/(x + 1)$, a homography of the line, and check that the cross-ratio does not change.

2. ◦ Use the [RANSAC iteration bound](/ransac-iteration-bound/) with $p = 0.99$ to fill a table of $k$ for the sample sizes $s = 2, 3, 4, 5, 7, 8$ and the inlier ratios $w = 0.6$ and $w = 0.3$. Which models do the sizes 4, 5, 7 and 8 belong to?

3. ◦ Two cameras have $K = I$, $R = I$ and the second centre moved along the $x$ axis, so $F = [t]_\times$ with $t = (1, 0, 0)$. Write out the [epipolar](/epipolar-geometry/) constraint $x_2^{\mathsf T} F x_1 = 0$ for $x_1 = (x_1, y_1, 1)$ and $x_2 = (x_2, y_2, 1)$. What are the epipolar lines?

4. ◦ Give the degrees of freedom and the size of the minimal sample of a homography, a [fundamental matrix](/fundamental-matrix/), an [essential matrix](/essential-matrix/), a calibrated pose and a camera matrix $P$. Give also the degrees of freedom of the [trifocal tensor](/trifocal-tensor/).

5. ◦ A calibrated camera moves forward, $R = I$ and $t = (0, 0, 1)$. Write $E = [t]_\times R$ and give its singular values. Check the conditions of the [characterization](/essential-matrix-characterization/).

6. ◦ For the $F$ of Exercise 3 and the match $(0, 0) \leftrightarrow (5, 0.4)$, compute the [Sampson distance](/sampson-distance/) and compare it with the smallest total squared move of the two points that makes them satisfy the constraint.

7. ◦ Apply [Hartley normalization](/hartley-normalization/) to the points $(0, 0)$, $(4, 0)$, $(4, 3)$ and $(0, 3)$: give the centroid, the scale factor and the normalized points.

8. • Find the [homography](/homography/) that maps the unit square $(0, 0)$, $(1, 0)$, $(1, 1)$, $(0, 1)$ to the quadrilateral $(0, 0)$, $(2, 0)$, $(3/2, 3/2)$, $(0, 1)$, with $h_{33} = 1$. Where does the centre of the square go, and why is it the meeting point of the diagonals? Find the vanishing line, the image of the line at infinity.

9. • The bound of [RANSAC](/ransac/) assumes that the points of a sample are drawn with replacement. For $n = 20$ points with 10 inliers and samples of two distinct points, compute the exact probability that a sample is clean, the number of samples needed for $p = 0.99$, and the failure probability after the 17 samples that the usual bound gives.

10. • A point at depth 4 projects to $x_1 = (0.1, 0.2)$ in camera 1 and to $x_2 = (0.08, 0.16)$ in camera 2, with $R = I$ and $t = (0, 0, 1)$. The [decomposition of $E$](/essential-matrix-decomposition/) gives four candidates: $R \in \{I, \operatorname{diag}(-1, -1, 1)\}$ and $\pm t$. Triangulate the point under each candidate, give its depths in both cameras, and apply the [cheirality](/cheirality/) test.

11. • Cameras $P_1 = [I \mid 0]$ and $P_2 = [I \mid (-1, 0, 0)]$ see $X = (1, 0.4, 4)$. Compute $x_1$ and $x_2$. With the noisy $x_2 = (0.01, 0.1)$, triangulate by the [midpoint method](/midpoint-triangulation/) and by the [linear method](/linear-triangulation/), and compare with the depth $1/d$ from the disparity $d$.

12. • A pose must be found with [RANSAC](/ransac/) from matches with 40 percent inliers. Compare the number of samples for $p = 0.99$ with [P3P](/p3p/) samples of 3 points (plus one point to choose among the solutions, which does not change the count), with samples of 4 points and with DLT samples of 6 points.

13. • A camera with $f = 1000$ pixels and the principal point at the origin pans by $5°$, so that a ray at the angle $\alpha$ from the axis is seen afterwards at $\alpha + 5°$. Using the rotation homography of [image stitching](/image-stitching/), where do the points $x = 0$ and $x = 500$ of the first image go?

14. • Two models have the residuals $(0.1, 0.2, 0.3, 0.9, 5, 6)$ and $(0.6, 0.7, 0.8, 0.9, 0.95, 7)$. With the threshold $T = 1$, which one does RANSAC choose by counting inliers, and which one does [MSAC](/msac/) choose with the cost $\sum \min(r^2, T^2)$?

15. • In [preemptive RANSAC](/preemptive-ransac/) with $M = 400$ hypotheses, blocks of $B = 50$ and enough observations, follow Algorithm 1: the first observation scores all $M$, and observation $i \ge 2$ scores $f(i) = \lfloor M 2^{-\lfloor i/B \rfloor} \rfloor$ hypotheses until $f(i) \le 1$. Count the observations used and the scorings, and compare with the bound $2BM$.

16. • Show that $k = \log(1 - p)/\log(1 - w^s)$ is close to $\ln(1/(1 - p))/w^s$ when $w^s$ is small. Compare $1/w^s$ with $k$ for $(w, s) = (0.5, 4)$ and $(0.5, 7)$.

17. • For $t = (1, 2, 2)$ and $R = I$, check by hand that $E = [t]_\times$ satisfies $2EE^{\mathsf T}E - \operatorname{tr}(EE^{\mathsf T})E = 0$, and find its singular values.

18. ★ The [seven-point algorithm](/seven-point-algorithm/) looks for $\alpha$ with $\det(\alpha F_1 + (1 - \alpha) F_2) = 0$. Take $F_1 = \operatorname{diag}(1, 2, 3)$ and $F_2 = \operatorname{diag}(3, 2, 1)$. Find the roots and explain why the cubic has only two. What does this say about writing the pencil as $\lambda F_1 + \mu F_2$?

19. ★ Show that if all scene points lie on one plane, the matches satisfy $x_2 \sim H x_1$, and every $F = [v]_\times H$ satisfies $x_2^{\mathsf T} F x_1 = 0$. Conclude that the $n \times 9$ matrix of the [eight-point algorithm](/eight-point-algorithm/) has rank at most 6, and check it with a short program on 12 random points with exact rational arithmetic.

20. ★ Count the degrees of freedom of the fundamental matrix in a second way: two cameras have $2 \cdot 11$ parameters, and the [projective reconstruction theorem](/projective-reconstruction-theorem/) says which of them the matches cannot see.

21. ★ Show that the two rotations $R$ and $R'$ of the [decomposition of $E$](/essential-matrix-decomposition/) satisfy $R' = R_t R$, where $R_t = 2tt^{\mathsf T}/\|t\|^2 - I$ is the half turn about the baseline. Use it to explain why a point in front of both cameras for $(R, t)$ is behind at least one camera for $(R', t)$.
