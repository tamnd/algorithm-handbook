1. ◦ An 8-bit image ($L - 1 = 255$) must reach a [PSNR](/psnr/) of 40 dB against its reference. What mean squared error does that allow, and what is the root mean squared error in codes?

2. ◦ A $4 \times 4$ image with $L = 8$ levels has eight pixels of level 1, four of level 4, two of level 6 and two of level 7. Compute the map $T[k] = \lfloor (2(L-1)c_k + N)/(2N) \rfloor$ of [histogram equalization](/histogram-equalization/), where $c_k$ is the cumulative count and $N = 16$, and the histogram of the output. Which entry of $T$ is a tie, and how is it rounded?

3. ◦ The histogram $h = (3, 1, 2, 4)$ has $L = 4$ levels, and a threshold $t$ puts the levels $\le t$ in class 0. Compute the between-class variance $\omega_0\omega_1(\mu_0 - \mu_1)^2$ for $t = 0, 1, 2$ as fractions, and give the threshold of [Otsu's method](/otsu-thresholding/).

4. ◦ For the histogram $h = (4, 0, 2, 0, 3, 1)$, the thresholds $t = 2$ and $t = 3$ give the same between-class variance. Explain why without computing it, and say which of the two a scan that keeps a threshold only on a strict increase returns. What happens in general on a run of empty bins?

5. ◦ A constant gray of $0.6$ is dithered by [ordered dithering](/ordered-dithering/) with the thresholds $(m + \tfrac12)/n^2$ of the Bayer matrices $M_2 = \begin{pmatrix} 0 & 2 \\ 3 & 1 \end{pmatrix}$ and $M_4$. How many pixels of each tile turn on for $n = 2$ and for $n = 4$, and what mean gray does each pattern show?

6. ◦ Compute the gradient $(g_x, g_y)$ at the center of the $3 \times 3$ patch with rows $(0, 0, 0)$, $(0, 0, 90)$, $(0, 90, 90)$, with $g_x$ the right column minus the left and $g_y$ the bottom row minus the top, weighted $[1, 1, 1]$ for [Prewitt](/prewitt-operator/), $[1, 2, 1]$ for [Sobel](/sobel-operator/) and $[3, 10, 3]$ for [Scharr](/scharr-operator/). Give the angle $\operatorname{atan2}(g_y, g_x)$ for each. Then do the same for the patch with rows $(0, 0, 0)$, $(0, 0, 0)$, $(0, 90, 90)$.

7. ◦ Build the [Gaussian pyramid](/gaussian-pyramid/) of a $100 \times 60$ image with sizes rounded up, $W_{l+1} = \lceil W_l/2 \rceil$, down to $1 \times 1$. List the level sizes and the total number of samples $S$, and compare $S$ with $\tfrac43 WH$.

8. ◦ The [Hough transform](/hough-transform/) runs on a $640 \times 480$ image with $T = 180$ angles $\theta_k = k\pi/T$, distance bins of width 1 from $-D$ to $D$, and $D = \lceil \sqrt{(W-1)^2 + (H-1)^2} \rceil$. How many cells does the accumulator have? In which distance bin does the edge point $(3, 4)$ vote at $\theta = \pi/4$?

9. ◦ For the [Harris detector](/harris-corner-detector/) with $k = 0.04$, compute $R = \lambda_1\lambda_2 - k(\lambda_1 + \lambda_2)^2$ for the eigenvalue pairs $(100, 1)$, $(100, 10)$ and $(50, 50)$, and say which have $R > 0$, the sign the detector reads as a corner, and which have $R < 0$, as along an edge.

10. ◦ One step of the [Lucas-Kanade method](/lucas-kanade-method/) on a window gives $G = \sum \nabla I\,\nabla I^{\mathsf T} = \begin{pmatrix} 20 & 5 \\ 5 & 10 \end{pmatrix}$ and $b = -\sum \nabla I\, I_t = (30, 5)$. Solve $G d = b$ for the shift $d = (u, v)$. What would make $G$ singular?

11. • Dither a $4 \times 4$ image of constant gray $\tfrac14$ to black and white with [Floyd-Steinberg dithering](/floyd-steinberg-dithering/) in raster order, ties going to the higher level. Which pixels turn on? The input holds $16 \cdot \tfrac14 = 4$ units of gray; where did the rest go?

12. • Run [hysteresis thresholding](/hysteresis-thresholding/) with $t_\ell = 4$ and $t_h = 8$ on the strengths with rows $(1, 2, 9, 3, 0)$, $(0, 5, 1, 4, 1)$, $(0, 1, 0, 1, 5)$, $(6, 0, 0, 0, 4)$, $(5, 4, 0, 8, 0)$, once with 8-connectivity and once with 4-connectivity. List the kept pixels as $(x, y)$. Which weak pixels are dropped in both cases?

13. • Run two-pass [connected component labeling](/connected-component-labeling/) on the binary image with rows `11011001`, `01010011`, `01110110`, `10000100`, scanning the west and north neighbors for 4-connectivity and also the north-west and north-east ones for 8-connectivity. How many provisional labels does the first pass make, how many unions merge two sets, and how many components are there, for each connectivity?

14. • The energies of a $4 \times 4$ image have rows $(3, 1, 4, 1)$, $(5, 9, 2, 6)$, $(5, 3, 5, 8)$, $(9, 7, 9, 3)$. Fill the table of [seam carving](/seam-carving/) for 8-connected vertical seams, and find the seam of least energy with ties going to the leftmost column. Is the seam of least energy unique?

15. • The binary $7 \times 6$ image has rows `0000000`, `0111100`, `0111100`, `0111111`, `0111100`, `0000000`, and pixels outside it are background. Compute its [erosion](/morphological-erosion/) and its [opening](/morphological-opening/) by the $3 \times 3$ square. How many pixels does each have, and which part of the shape does the opening remove?

16. • Compute the one-dimensional distance transform $D(p) = \min_q \big((p - q)^2 + f(q)\big)$ of $f = (0, 5, 1, 9, 9, 2, \infty, 0)$, the step that the [Felzenszwalb-Huttenlocher transform](/felzenszwalb-distance-transform/) runs on each column and row. Which samples $q$ are on the lower envelope?

17. • A single feature pixel sits at the origin. Give the [chamfer distance](/chamfer-distance/) to the offsets $(4, 1)$, $(5, 2)$, $(3, 3)$ and $(7, 3)$ as the least total weight of a path of mask steps, once for the 3-4 mask (divide by 3) and once for the 5-7-11 mask (steps $(1, 0)$, $(1, 1)$, $(2, 1)$ and their symmetric copies, divide by 5). Compare both with the Euclidean distance.

18. • Let $f = (1, 2, 0, 0)$ and $g = (0, 1, 2, 0)$, a circular shift of $f$ by one sample. Compute the DFT of $f$, the cross-power spectrum normalized to unit magnitude, and its inverse, as in [phase correlation](/phase-correlation/). Compare with the plain circular cross-correlation of $f$ and $g$.

19. • A binary rectangle 4 pixels wide and 2 pixels high has its pixel centers at integer points. Compute its [central moments](/image-moments/) $\mu_{20}$, $\mu_{02}$ and $\mu_{11}$, the first Hu invariant $\varphi_1 = \eta_{20} + \eta_{02}$ with $\eta_{pq} = \mu_{pq}/\mu_{00}^{1 + (p+q)/2}$, and the ratio $\sqrt{\mu_{20}/\mu_{02}}$. Why is that ratio not 2?

20. • In [Felzenszwalb-Huttenlocher segmentation](/felzenszwalb-segmentation/), a component $C$ merges with its neighbor across an edge of weight $w$ when $w \le \min(\mathrm{Int}(C_1) + k/|C_1|, \mathrm{Int}(C_2) + k/|C_2|)$. Show that for $k = 0$ and nonnegative weights the result is exactly the connected components of the graph of zero-weight edges.

21. • Compute the [normalized cross-correlation](/normalized-cross-correlation/) of the template $t = (1, 2, 3)$ with the windows $(2, 4, 6)$, $(5, 4, 3)$, $(1, 3, 2)$, $(11, 12, 13)$ and $(7, 7, 7.0001)$. What does the last one show about nearly flat windows?

22. • A detector of the [Viola-Jones](/viola-jones-detector/) kind and a [Canny detector](/canny-edge-detector/) both come with a proof about what they compute. Say, for each, which part of the output is fixed by the algorithm and which depends on parameters that are tuned or learned, and how the quality of the result is judged.

23. ★ A $1 \times (a + b)$ image has $a$ pixels of value 0 followed by $b$ pixels of value 1. Find the minimizer of $\tfrac12\lVert u - f \rVert^2 + \lambda \sum_x |u_{x+1} - u_x|$, the energy of [total variation denoising](/total-variation-denoising/) on one row, for every $\lambda > 0$. Check your answer for $a = 2$, $b = 3$ with $\lambda = 0.6$ and $\lambda = 1.5$.

24. ★ An [integral image](/integral-image/) of an $8192 \times 8192$ image with 8-bit pixels is stored in unsigned 32-bit words that wrap modulo $2^{32}$. How many bits would exact entries need? Show that the four-read rectangle sum is still correct for every rectangle whose true sum is below $2^{32}$, and find the largest $s$ such that every $s \times s$ square is safe. How many bits does the table of $f^2$ of a $4096 \times 4096$ 8-bit image need?

25. ★ Find the exact number of samples $S$ of the [Gaussian pyramid](/gaussian-pyramid/) of a $2^a \times 2^b$ image with $a \ge b$, sizes halved down to $1 \times 1$. Show that $S \le \tfrac43 WH$ holds only when $a = b$, and check the formula on $4 \times 1$ and $1024 \times 512$.

26. ★ In phase correlation, a bin where the cross-power spectrum is zero has no phase and is set to 0. Take $f = (1, 1, 0, 0)$ and $g = (0, 1, 1, 0)$ and compute the result. Then show in general that for a circular shift by $d$ of an $N$-sample signal with $z$ zero bins, the value at $d$ is $(N - z)/N$, every other value has magnitude at most $z/N$, and the peak is still at $d$ when $z < N/2$.

27. ★ Let $\gamma$ be an [opening](/morphological-opening/) and $\varphi$ a [closing](/morphological-closing/), on the whole plane so that the border plays no part. Using only that both are increasing and idempotent, that $\gamma$ is anti-extensive ($\gamma(f) \le f$) and that $\varphi$ is extensive, prove that the [alternating filter](/morphological-filtering/) $\varphi\gamma$ is idempotent. Why can the same pair, computed on a bounded image with background outside, fail to be idempotent?
