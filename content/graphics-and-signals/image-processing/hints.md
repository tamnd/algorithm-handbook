1. Solve $40 = 10\log_{10}(255^2/\mathrm{MSE})$: $\mathrm{MSE} = 65025/10^4 = 6.5025$, so the root mean squared error is $2.55$ codes.

2. The cumulative counts are $c = (0, 8, 8, 8, 12, 12, 14, 16)$, and $T = (0, 4, 4, 4, 5, 5, 6, 7)$. At level 1, $(L-1)c_1/N = 3.5$ is a tie, and the formula rounds it up to 4. The output has 8 pixels at level 4, 4 at level 5, 2 at level 6 and 2 at level 7: the levels 0 to 3 stay empty, so the output is not flat.

3. With $N = 10$ and pixel sum 17: for $t = 0$, $0.3 \cdot 0.7 \cdot (17/7)^2 = 867/700 \approx 1.239$; for $t = 1$, $0.4 \cdot 0.6 \cdot (8/3 - 1/4)^2 = 841/600 \approx 1.402$; for $t = 2$, $0.6 \cdot 0.4 \cdot (3 - 5/6)^2 = 169/150 \approx 1.127$. Otsu's threshold is $t = 1$.

7. The levels are $100 \times 60$, $50 \times 30$, $25 \times 15$, $13 \times 8$, $7 \times 4$, $4 \times 2$, $2 \times 1$ and $1 \times 1$, eight in all, with $S = 6000 + 1500 + 375 + 104 + 28 + 8 + 2 + 1 = 8018$. That is 18 more than $\tfrac43 WH = 8000$, because $\lceil 25/2 \rceil$ and $\lceil 15/2 \rceil$ round up.

10. $\det G = 175$, $u = (10 \cdot 30 - 5 \cdot 5)/175 = 11/7$ and $v = (20 \cdot 5 - 5 \cdot 30)/175 = -2/7$. $G$ is singular when all the gradients of the window are parallel or zero: a flat window, or one straight edge, the aperture problem.

12. With 8-connectivity the kept pixels are $(2, 0)$, $(1, 1)$, $(3, 1)$, $(4, 2)$, $(4, 3)$ and $(3, 4)$. With 4-connectivity only the two strong pixels $(2, 0)$ and $(3, 4)$ stay, because every weak pixel near them touches them only at a corner. The weak pixels $(0, 3)$, $(0, 4)$ and $(1, 4)$ are dropped in both cases: their component has no strong pixel.

13. With 4-connectivity: 6 provisional labels, 3 merging unions, 3 components. With 8-connectivity: 3 labels, 1 merging union, 2 components. In both cases the number of merging unions is the number of labels minus the number of components.

14. The table has rows $(3, 1, 4, 1)$, $(6, 10, 3, 7)$, $(11, 6, 8, 11)$, $(15, 13, 15, 11)$. The bottom minimum is 11 in column 3; tracing back gives columns 2, 2 and then a tie between columns 1 and 3 in row 0, broken to column 1. The seam is $(1, 2, 2, 3)$ with energy $1 + 2 + 5 + 3 = 11$. It is not unique: $(3, 2, 2, 3)$ also costs 11.

16. $D = (0, 1, 1, 2, 3, 2, 1, 0)$. Only the parabolas of $q = 0, 2, 5, 7$ are on the lower envelope; those of $q = 1, 3, 4$ lie above it everywhere, and $q = 6$ has $f = \infty$.

20. Edges are scanned by weight, so all zero-weight edges come first. Every merge among them is by a zero edge, so every component has $\mathrm{Int} = 0$, and a zero edge between two components passes $0 \le \min(0, 0)$. Once the positive edges start, every component still has $\mathrm{Int} = 0$ and $k/|C| = 0$, so $w > 0$ fails the test and nothing more merges.

23. Try pieces that are flat on each side. If $\lambda(1/a + 1/b) < 1$, then $u = \lambda/a$ on the zeros and $u = 1 - \lambda/b$ on the ones; otherwise $u$ is the constant $b/(a + b)$. To prove it, write the optimality condition $(u_j - f_j) + \lambda(p_{j-1} - p_j) = 0$ with $p_0 = p_{a+b} = 0$, $|p_j| \le 1$, and $p_j = \operatorname{sign}(u_{j+1} - u_j)$ where the difference is not zero. In the first case $p_j$ climbs by $1/a$ to exactly 1 at the step and falls by $1/b$ to 0; in the second its largest value is $ab/((a + b)\lambda) \le 1$. For $a = 2$, $b = 3$: $\lambda = 0.6$ gives $(0.3, 0.3, 0.8, 0.8, 0.8)$ and $\lambda = 1.5$ gives $0.6$ everywhere.

24. The largest entry is $255 \cdot 2^{26}$, which needs 34 bits. With wrapping words every entry is the true value modulo $2^{32}$, so the four-read sum is the true rectangle sum modulo $2^{32}$, which is the sum itself when it lies in $[0, 2^{32})$. Since $2^{32} - 1 = 255 \cdot 16843009$, a square is safe when $s^2 \le 16843009$, so $s = 4104$. The $f^2$ table needs $\lceil \log_2(65025 \cdot 2^{24} + 1) \rceil = 40$ bits.

25. The first $b + 1$ levels are $2^{a-l} \times 2^{b-l}$ and hold $(4WH - 2^{a-b})/3$ samples; then come $a - b$ levels of height 1 with $2^{a-b} - 1$ samples. So $S = (4WH + 2 \cdot 2^{a-b} - 3)/3$, which is at most $\tfrac43 WH$ only when $2^{a-b+1} \le 3$, that is $a = b$. For $4 \times 1$, $S = 7$; for $1024 \times 512$, $S = 699051$, a third of a sample above $\tfrac43 WH$.

26. $\hat f = (2, 1 - i, 0, 1 + i)$, and the result is $(\tfrac14, \tfrac34, \tfrac14, -\tfrac14)$. In general the cross-power spectrum of a circular shift is $|\hat f_k|^2$ times a phase factor, so it is zero exactly at the $z$ bins where $\hat f_k = 0$. The inverse is the delta at $d$ minus $\frac1N$ times a sum of $z$ unit complex numbers: at $d$ that sum is $z$, elsewhere its magnitude is at most $z$.

27. From $\gamma \le \mathrm{id}$ and $\varphi$ increasing, $\varphi\gamma\varphi\gamma \le \varphi\varphi\gamma = \varphi\gamma$. From $\varphi \ge \mathrm{id}$ and $\gamma$ increasing, $\gamma\varphi\gamma \ge \gamma\gamma = \gamma$, so $\varphi\gamma\varphi\gamma \ge \varphi\gamma$. On a bounded image with background outside, the erosion inside the closing removes foreground at the border, so the computed closing is not extensive. With the cross $\{(0,0), (\pm1, 0), (0, \pm1)\}$, the $3 \times 3$ image with rows `011`, `111`, `010` goes to the center pixel alone, and a second application empties it.
