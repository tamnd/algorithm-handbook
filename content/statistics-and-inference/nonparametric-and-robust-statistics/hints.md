1. $F_5(2) = 2/5$ and $F_5(4) = 4/5$. $D_5 = 1/6$, reached just below $x = 1$, where $F_5 = 0$ and $F = 1/6$, and at $x = 5$, where $F_5 = 1$ and $F = 5/6$. This is far below $0.5633$, so the test does not reject.

4. With $\alpha = 0.1$, $g = 1$: drop 1 and 50, and the mean of $2, \ldots, 8, 10$ is $45/8 = 5.625$. With $\alpha = 0.2$, $g = 2$: the mean of $3, \ldots, 8$ is $11/2$. The mean is $9.6$ and the median $5.5$. The breakdown point is $(g + 1)/n = 3/10$.

6. The ranks of $|d_i|$ are $3, 1, 6, 7, 4, 2, 8, 5$, so $W^+ = 3 + 6 + 7 + 2 + 8 + 5 = 31$ and $W^- = 5$. Ten of the 256 subsets of $\{1, \ldots, 8\}$ have sum at most 5, so the one-sided p-value is $10/256 = 5/128 \approx 0.039$ and the two-sided one is $5/64 \approx 0.078$.

7. $U = 2 + 3 + 4 = 9$ of $mn = 12$ pairs. Under the null, $U$ is the rank sum of $x$ minus 6 over the $\binom73 = 35$ equally likely rank sets, and its law is symmetric about 6. $P(U \le 3)$ counts $1, 1, 2, 3$ sets for $U = 0, 1, 2, 3$, so $P(U \ge 9) = 7/35 = 1/5$, and the two-sided p-value is $2/5$. The estimate of $P(X > Y)$ is $9/12 = 3/4$.

8. $d = -1, 1, -1, 1, 0$, $\sum d^2 = 4$ and $r_S = 1 - 24/120 = 4/5$. The permutations with $\sum d^2 \le 4$ are the identity, the four adjacent swaps and the three products of two disjoint adjacent swaps, so $p = 8/120 = 1/15 \approx 0.067$.

10. $k = \lceil 10 \cdot 0.8 \rceil = 8$, so $q = 2.5$, the 8th smallest residual, and the interval is $[7.5, 12.5]$. The coverage is exactly $8/10$. With $n_2 = 50$ and $\alpha = 0.01$, $k = \lceil 50.49 \rceil = 51 > n_2$, so $q = \infty$ and the interval is the whole line.

11. The median is 1 when at least two of the three draws are 1, in $3 \cdot 2 + 1 = 7$ of the 27 resamples, and 9 in another 7; it is 5 in the other 13. The mean is 5 and the variance $(7 \cdot 16 + 7 \cdot 16)/27 = 224/27 \approx 8.30$, a standard error of about $2.88$.

12. The observed difference is 4. Of the 20 splits, only $\{14, 11, 9\}$ and $\{14, 11, 8\}$ give A a sum of at least 33, so $p = 1/10$ one-sided; adding $\{5, 7, 8\}$ and $\{5, 7, 9\}$ gives $1/5$ two-sided. The observed split and its mirror image always count, so no data give a two-sided p-value below $2/20 = 0.1$. The Monte Carlo p-value is $96/1000 = 0.096$.

13. The groups hold the ranks $1, 2, 3$; $4, 5, 6$; $7, 8, 9$, so $H = \frac{12}{90} \cdot \frac{36 + 225 + 576}{3} - 30 = 36/5 = 7.2$, the largest possible value. Only the 6 ways to give these three blocks of ranks to the groups reach it, so the exact p-value is $6/1680 = 1/280 \approx 0.0036$. The chi-square value $e^{-3.6} \approx 0.027$ is almost eight times larger.

16. The sorted slopes are $1, 3/2, 2, 2, 2, 3, 6, 22/3, 21/2, 18$, so Theil-Sen gives $b = 5/2$, $a = -2$. The inner high medians are $2, 2, 3, 3, 21/2$, their low median is $b = 3$, and the residuals $y_i - 3x_i$ give $a = -3$. Least squares gives $y = -7.6 + 5.2x$, pulled up by the point $(5, 25)$.

19. Relative to the centre, the corners form two opposite pairs $\pm v$. A closed half-plane through the centre contains the centre and at least one corner of each pair, and only 3 points for a generic direction, so the depth of $(1, 1)$ is 3. For $c \ne (1, 1)$, take the half-plane $\{p : u \cdot (p - c) \ge 0\}$ with $u = c - (1, 1)$: it misses the centre, and $u \cdot (v - u) + u \cdot (-v - u) = -2|u|^2 < 0$, so it holds at most one corner of each pair. The point $(1, 1/2)$ has depth 1, from the normal $(1, -1)$. The maximum 3 equals $\lceil 5/2 \rceil$ and is above $\lceil 5/3 \rceil = 2$.

23. Sorted, the middle values are $x_{(5)} = 9$ and $x_{(6)} = 12$. Leaving out one of the five smallest values gives the median 12, and one of the five largest gives 9. So the jackknife variance is $\frac{9}{10} \cdot 10 \cdot (3/2)^2 = 81/4$ and the standard error is $4.5$. It depends only on the gap $x_{(6)} - x_{(5)}$: in general $\frac{n - 1}{4}(x_{(k+1)} - x_{(k)})^2$ for $n = 2k$, which is why it does not converge to the true variance.

24. Let $R$ and $R'$ be the rank sums of the two groups and $D = R - m(N + 1)/2$. Then $R + R' = N(N + 1)/2$ gives $R' - n(N + 1)/2 = -D$, and $U = R - m(m + 1)/2$ gives $U - mn/2 = D$. The mean-rank form of $H$ is $\frac{12}{N(N + 1)}\bigl(D^2/m + D^2/n\bigr) = \frac{12 D^2}{mn(N + 1)} = z^2$. In exercise 7, $R = 15$, $D = 3$ and $H = z^2 = 9/8$.

25. With no ties and exchangeability, the rank of the observed value among the $b + 1$ values is uniform, so $c$ is uniform on $\{0, \ldots, b\}$. Then $p \le \alpha$ exactly when $c \le \alpha(b + 1) - 1$, which has probability $\lfloor \alpha(b + 1) \rfloor / (b + 1) \le \alpha$. With $b = 19$ and $\alpha = 0.06$ this rejects only at $c = 0$, with probability $0.05$, while $c/b \le 0.06$ allows $c \le 1$ and rejects with probability $0.1$.

26. Given the training part, the calibration scores are independent with a continuous distribution function $F$, so the values $F(S_i)$ are independent uniforms, and $F(q)$ is the $k$-th smallest of $n_2$ uniforms, which is Beta$(k, n_2 + 1 - k)$. Here $k = \lceil 20 \cdot 0.9 \rceil = 18$: the mean is $0.9$, the standard deviation $\sqrt{36/(400 \cdot 21)} \approx 0.065$, and $P(F(q) < 0.8) = 0.8^{18}(19 - 18 \cdot 0.8) \approx 0.083$.

27. For $x_i < x_j$, the slope $(y_j - y_i)/(x_j - x_i)$ is below $t$ exactly when $y_j - t x_j < y_i - t x_i$. With $t = 2$ the sequence is $-1, -1, -2, -1, 15$: 2 inversions for the slopes $1$ and $3/2$, and 3 tied pairs for the three slopes equal to 2. Merge sort counts inversions in $O(n \log n)$ time, and the $r$-th smallest slope is below $t$ exactly when at least $r$ slopes are; apply this to the middle rank or ranks.

28. Under a shift $\theta$, the fraction of positive signs has mean $1 - F(-\theta) = 1/2 + \theta f(0) + o(\theta)$ and variance about $1/(4n)$, so its efficacy is $4f(0)^2$. The mean has mean $\theta$ and variance $\sigma^2/n$, so its efficacy is $1/\sigma^2$. The ratio is $4\sigma^2 f(0)^2$: $2/\pi \approx 0.637$ for the normal, $4 \cdot 2 \cdot (1/2)^2 = 2$ for the Laplace law and $4 \cdot (1/3) \cdot (1/2)^2 = 1/3$ for the uniform law.
