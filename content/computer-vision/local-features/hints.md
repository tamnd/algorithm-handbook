1. A pixel is brighter when its value is at least 115 and darker when it is at most 85. Pixels 12 to 16 and 1 to 6 are brighter, an arc of 11 that wraps around, and no pixel is darker. So the pixel is a corner for $n = 9$ and not for $n = 12$. The quick test sees 130, 118, 105 and 121, three of them brighter, so it passes. The quick test is a necessary condition only for $n = 12$: an arc of 12 covers at least three of the four pixels, while an arc of 9 may cover only two, so for $n = 9$ the quick test would throw away true corners.

2. The ratios are $0.667$, $0.889$, $0.2$, $0.8$ and $0.857$. The first and third are kept. The fourth has the ratio exactly 0.8 and fails the strict test $d_1 < 0.8\, d_2$.

3. The bytes per descriptor are 512, 256, 32 and 64, so the totals are 1024, 512, 64 and 128 megabytes.

4. The window has $6 \times 12$ cells and $5 \times 11 = 55$ blocks of 36 values, so 1980 values. For $64 \times 128$ there are $7 \times 15 = 105$ blocks, so 3780.

5. An octave needs $s + 3 = 7$ Gaussian images and $s + 2 = 6$ DoG images, so that extrema can be found at $s$ levels with a level above and below. The factor is $k = 2^{1/4} \approx 1.1892$, and each candidate has $8 + 9 + 9 = 26$ neighbours.

7. The nearest neighbours of the rows are $b_0$, $b_1$ and $b_1$; those of the columns are $a_0$, $a_1$, $a_1$ and $a_2$. The mutual pairs are $(a_0, b_0)$ and $(a_1, b_1)$. For $a_2$ the ratio is $1.5/2 = 0.75 < 0.8$, but $b_1$ prefers $a_1$.

8. The values of $\lambda_{\min}$ are 0.1, 8, 0.1 and 0.1, and the Harris measures are $-3.0804$, $67.04$, $-3.01$ and $0.0164$. The first and third are edges (the third is an edge at $45°$, with eigenvalues 9.9 and 0.1), the second is a corner and the fourth is flat. The flat region has a small positive measure, as the corner has a large one, so a threshold on the size is needed.

10. $m_{10} = 70$ and $m_{01} = -20$, so $\theta = \operatorname{atan2}(-20, 70) \approx -15.95°$. With $v$ pointing down this is a turn upward in the picture, and the nearest bin is $-12°$.

11. The mapped points are $(10, 0)$, $(20, 10)$, $(30, 4)$, $(16, 16)$ and $(24, 14)$. The first four have a detection within 1.5 pixels, at the distances 1.118, 0, 1 and 1; the last has none. The repeatability is $4/5 = 0.8$.

15. Given $d_2$, the nearest point is uniform in the ball of radius $d_2$, so $P(d_1 < r d_2) = r^D$. For $r = 0.8$ the values are 0.8, 0.64, 0.4096, 0.1074 and 0.00079. In high dimension the two nearest wrong descriptors are almost equally far, so a false match almost never passes; a simulation in the plane (seed 38, 20000 runs, 200 points in a disk) gave 0.636 against 0.64.

16. The values for $g = 2, \ldots, 8$ are 2.2222, 1.125, 0.7, 0.3636, 0.8696, 2.4167 and 3.175. The minimum is at $g = 5$, where the area 22 changes from 16 to 24 over $g \pm 2$.

17. Take the pair with the smallest entry of the whole matrix. It is the smallest in its row and in its column. For only one mutual pair, take $D_{ij} = i + j$: every row and every column has its nearest neighbour at index 0, so $(a_0, b_0)$ is the only mutual pair.

18. Greedy takes the cost 1 and is then forced to take $M$, so it pays $1 + M$; the optimum takes the two entries 2 and pays 4. The ratio $(1 + M)/4$ has no bound as $M$ grows.
