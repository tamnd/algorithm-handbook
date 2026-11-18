1. ◦ The 16 pixels of the circle around a pixel with $I_p = 100$ have, in order from pixel 1 to pixel 16, the values 130, 128, 125, 120, 118, 117, 90, 100, 105, 96, 98, 119, 121, 124, 140, 135. With $t = 15$, apply the [FAST](/fast-corner-detector/) segment test for $n = 9$ and for $n = 12$. Does the pixel pass the quick test on pixels 1, 5, 9 and 13? What does this say about using that quick test for $n = 9$?

2. ◦ Five features have the nearest and second nearest distances $(d_1, d_2)$ equal to $(0.20, 0.30)$, $(0.40, 0.45)$, $(0.10, 0.50)$, $(0.36, 0.45)$ and $(0.60, 0.70)$. Which matches does [Lowe's ratio test](/lowe-ratio-test/) keep with the threshold 0.8? Take care with the fourth.

3. ◦ A map of a city holds $2 \times 10^6$ features. How many megabytes (of $2^{20}$ bytes) do the descriptors take for SIFT with 128 single precision numbers, for [SURF](/surf/) with 64, for [ORB](/orb-features/) with 256 bits and for [BRISK](/brisk-features/) with 512 bits?

4. ◦ Count the values of the [HOG](/histogram-of-oriented-gradients/) descriptor of a $48 \times 96$ window with cells of $8 \times 8$ pixels, blocks of $2 \times 2$ cells with a stride of one cell and 9 orientation bins. Check your method on the $64 \times 128$ window, which gives 3780.

5. ◦ The [DoG detector](/difference-of-gaussians-detector/) uses $s = 4$ intervals per octave. How many Gaussian images and how many DoG images does one octave need, what is the factor $k$ between adjacent scales, and with how many neighbours is each candidate compared?

6. ◦ Two SIFT histograms are $x = (1, 3, 0, 0)$ and $y = (0, 1, 1, 2)$. Compute their [RootSIFT](/rootsift/) vectors, the Hellinger kernel $H(x, y)$ and the squared Euclidean distance of the RootSIFT vectors, and check that it equals $2 - 2H$.

7. • Three features of image $A$ and four of image $B$ have the descriptor distances given by the rows $(2, 5, 7, 4)$, $(3, 1, 6, 8)$ and $(9, 1.5, 5, 2)$, where row $i$ belongs to $a_i$ and column $j$ to $b_j$, counting from 0. Find the [mutual nearest neighbor](/mutual-nearest-neighbor-matching/) pairs. Show that $a_2$ passes the ratio test with threshold 0.8 and is still not in a mutual pair.

8. • For the structure tensors with entries $(S_{xx}, S_{xy}, S_{yy})$ equal to $(10, 0, 0.1)$, $(10, 0, 8)$, $(5, 4.9, 5)$ and $(0.2, 0, 0.1)$, compute the [Shi-Tomasi](/shi-tomasi-corner-detector/) score $\lambda_{\min}$ and the Harris measure $\det M - 0.04 (\operatorname{tr} M)^2$. Say which tensors come from an edge, a corner and a flat region, and why the sign of the Harris measure alone does not separate a flat region from a corner.

9. • For [local binary patterns](/local-binary-patterns/) with $P = 6$ neighbours, count the uniform codes (at most two changes between 0 and 1 around the circle), the labels of the u2 mapping, the labels of the riu2 mapping, and the rotation invariant codes. Compare with the values 59, 10 and 36 for $P = 8$.

10. • A $3 \times 3$ patch has the rows $(0, 10, 20)$, $(0, 10, 40)$ and $(0, 0, 10)$ for $v = -1, 0, 1$, and the columns are $u = -1, 0, 1$, with $u$ to the right and $v$ down. Compute the moments $m_{10}$ and $m_{01}$ and the angle of the intensity centroid used by [ORB](/orb-features/), and the bin of $12°$ into which ORB puts it.

11. • Image 2 is image 1 scaled by 2 and moved by $(10, 0)$. A detector finds $(0, 0)$, $(5, 5)$, $(10, 2)$, $(3, 8)$ and $(7, 7)$ in image 1, and $(11, 0.5)$, $(20, 10)$, $(30, 3)$, $(16, 15)$, $(25, 25)$ and $(40, 40)$ in image 2. With the tolerance $\varepsilon = 1.5$ pixels, compute the [repeatability](/detector-repeatability/) as the number of repeated points over $\min(n_1, n_2)$.

12. • Show that when every intensity $I$ is replaced by $255 - I$, every bit of a [BRIEF](/brief-descriptor/) descriptor flips except where the two intensities of a test are equal. What does this mean for matching a scene against its photographic negative, and for a dark object on a light background against a light object on a dark one?

13. • [SURF](/surf/) filters of side $L = 9, 15, 21, 27$ form its first octave. Give the scale $\sigma$ of each one, and count the integral image lookups needed for one box sum and for the filter $D_{xy}$ made of four boxes. Why does the cost not depend on $L$?

14. • Two images have 4000 features each. Count the operations of brute-force matching for 128 single precision numbers (multiply-adds) and for 256-bit descriptors (population counts of 64-bit words). Write a short program that does both on random data and compare the times on your computer.

15. ★ Model the distances from a query to the wrong descriptors as the points of a Poisson process of constant density in $D$ dimensions, so that the number within distance $d$ grows as $d^D$. Show that the ratio $d_1/d_2$ of the two nearest satisfies $P(d_1/d_2 < r) = r^D$. Evaluate it for $r = 0.8$ and $D = 1, 2, 4, 10, 32$, and explain what this says about the [ratio test](/lowe-ratio-test/) for false matches in high dimension.

16. ★ The dark extremal regions of one nested chain have the areas $0, 4, 9, 16, 20, 22, 23, 24, 40, 80, 150$ at the levels $g = 0, \ldots, 10$. With $\Delta = 2$, compute the stability $q(g) = (a(g + \Delta) - a(g - \Delta))/a(g)$ of [MSER](/maximally-stable-extremal-regions/) for $g = 2, \ldots, 8$ and find the maximally stable level.

17. ★ Prove that for any two nonempty sets of descriptors with a finite distance matrix, at least one [mutual nearest neighbor](/mutual-nearest-neighbor-matching/) pair exists. Give an example with many features on each side and only one mutual pair.

18. ★ Greedy matching takes the cheapest pair, removes its row and column, and repeats. For the cost matrix $\begin{pmatrix} 1 & 2 \\ 2 & M \end{pmatrix}$ with $M > 3$, compare its total cost with the optimum that the [Hungarian algorithm](/hungarian-algorithm/) finds, as used in [shape context](/shape-context/) matching. How bad can the ratio be?
