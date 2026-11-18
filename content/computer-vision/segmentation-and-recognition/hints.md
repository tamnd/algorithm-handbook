1. Continuous: the overlap is $2 \times 3 = 6$ and the union $16 + 16 - 6 = 26$, so IoU $= 3/13 \approx 0.231$. Inclusive: each box has $5 \times 5 = 25$ pixels, the overlap is $3 \times 4 = 12$ and the union 38, so IoU $= 6/19 \approx 0.316$. The same four numbers give different scores in the two forms.

2. Precision $1, 1/2, 2/3, 3/4, 3/5$ and recall $1/4, 1/4, 1/2, 3/4, 3/4$. The interpolated precision is 1 up to recall $1/4$, then $3/4$ up to recall $3/4$, then 0. All-point AP $= 1/4 + 1/4 \cdot 3/4 + 1/4 \cdot 3/4 = 5/8 = 0.625$. The 11-point AP is $(3 + 5 \cdot 0.75)/11 = 27/44 \approx 0.614$, and the 101-point AP is $(26 + 50 \cdot 0.75)/101 = 127/202 \approx 0.629$.

3. $\mathrm{IoU}_0 = 50/70 = 5/7$, $\mathrm{IoU}_1 = 20/40 = 1/2$ and $\mathrm{IoU}_2 = 5/15 = 1/3$. The mean is $65/126 \approx 0.516$, while the pixel accuracy is $75/100 = 0.75$. The small class 2 pulls the mean down.

6. $\mathrm{IoU}(B_1, B_2) = 1/3$, $\mathrm{IoU}(B_1, B_3) = 9/11 \approx 0.818$ and $\mathrm{IoU}(B_2, B_3) = 3/7 \approx 0.429$. Greedy NMS keeps $B_1$ (0.9) and $B_2$ (0.8) and removes $B_3$. Linear: $0.9$, $0.8 \cdot 2/3 \approx 0.533$, then $0.7 \cdot 2/11 \cdot 4/7 \approx 0.073$. Gaussian: $0.9$, $0.8\,e^{-2/9} \approx 0.641$, then $0.7\,e^{-(9/11)^2/0.5}\,e^{-(3/7)^2/0.5} \approx 0.127$. The order is $B_1, B_2, B_3$ in all three.

9. The weights are $0.7 \cdot 0.4$, $0.3 \cdot 0.4$, $0.7 \cdot 0.6$ and $0.3 \cdot 0.6$ for the four points, so the sample is $1.12 + 0.96 + 2.52 + 0.36 = 4.96$. Rounding gives the cell $(1, 3)$ and the value 6.

11. $\mathrm{IoU}(A, B) = \mathrm{IoU}(A, C) = 3/5$ and $\mathrm{IoU}(B, C) = 1/3$. With $A$ first, only $A$ is kept; with $B$ first, $B$ and $C$ are kept. Every dropped box overlaps a kept one too much, so the kept set is maximal. With scores $0.9, 0.8, 0.8$ for $A, B, C$, greedy keeps 0.9 while $\{B, C\}$ has 1.6.

14. The probabilities are harmonic: $x_2 = (2 \cdot 1 + x_3 + 0)/4$ and $x_3 = (1 + x_2 + 0)/4$. So $x_2 = 3/5$ and $x_3 = 2/5$: pixel 2 gets label $A$ and pixel 3 label $B$.

15. Link the source to each free pixel with its background cost and the pixel to the sink with its object cost; the seeds get infinite links. The four labelings of pixels 2 and 3 cost 6 (both object), 2.5 (object, background), 12 and 6.5, so the cut gives pixel 2 to the object and pixel 3 to the background, cutting $w_{23}$. After the new seed, pixel 3's region costs drop out and the cut costs 4 with pixel 2 still object, cutting $w_{34}$.

16. $D = (1, 0, 1, 1, 2, 5)$. The total cost of root position $x$ is $m(x) + D(x + 1)$, which gives $3, 2, 4, 3, 7$. The best is the root at 1 with cost 2, and the child at 1, where $f(1) + (2 - 1)^2 = 1$: one step left of its rest position.

19. With hard assignments $\gamma_t(k) \in \{0, 1\}$, $\sigma_k = 1$ and $w_k = 1/K$, the mean gradient is $\frac{\sqrt K}{n} \sum_{x_t \in \text{cell } k} (x_t - \mu_k)$, which is $\sqrt K/n$ times the VLAD block. The lengths are $KD = 8192$ and $2KD = 32768$.

23. The interpolated precision $p$ does not increase, and the all-point AP is $\int_0^1 p(r)\,dr$. Compare each strip $((j - 1)/10, j/10]$ with its two end values to get $(S - p_0)/10 \le A \le (S - p_{10})/10$ with $S = \sum_{j=0}^{10} p(j/10)$, then use $A_{11} = S/11$. One true positive at the top among $N$ objects gives $A = 1/N$ and $A_{11} = 1/11$. The COCO bound is $1/101$.

24. Write $d(A, B) = |A \triangle B|/|A \cup B|$. Split $A \cup B \cup C$ into its seven parts and show $d(A, C) \le d(A, B) + d(B, C)$ by comparing each part's count in the three ratios; Kosub (2019) gives two short proofs. The corollary is $1 - \mathrm{IoU}(g_1, g_2) \le (1 - a) + (1 - b)$.

25. Let $B(j)$ be the least cost of the first $j$ samples. Then $B(j) = \min_{i < j} \{B(i) + c(i, j) + \nu [i > 0]\}$, where $c(i, j)$ is the squared deviation from the mean of $g_{i+1}, \ldots, g_j$, found in $O(1)$ from prefix sums of $g$ and $g^2$. For $\nu = 2$ the best is $(0.5, 0.5, 0.5, 0.5, 5)$ with cost $1 + 2 = 3$; for $\nu = 1/2$ it is $u = g$ with two jumps and cost 1.

26. The probabilities solve the Dirichlet problem, so each free value is the weighted mean of its neighbors, and the maximum principle bounds them by the seed values. On the chain they are $2/3$, $4/9$ and $2/9$ at $a$, $b$ and $c$, so thresholding cuts the edge $a$-$b$ of weight 3, while the minimum cut is the edge $s$-$a$ of weight 2.

27. With $x = |\delta_x|/w$ and $y = |\delta_y|/w$, the overlap is $I = (1 - x)(1 - y) w^2$ and the union $2w^2 - I$, so IoU $\ge 1/2$ means $(1 - x)(1 - y) \ge 2/3$. The function $\log(1 - |x|) + \log(1 - |y|)$ is concave, so its upper level set is convex. One quadrant has area $\int_0^{1/3} \bigl(1 - \tfrac{2/3}{1 - x}\bigr)\,dx = \tfrac13 - \tfrac23 \ln\tfrac32$.
