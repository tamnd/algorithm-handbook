3. The event times are 3, 4, 6 and 9, with $n_j = 8, 7, 5, 3$ and $d_j = 1, 1, 1, 2$. Yes: a censored time tied with an event time is still at risk at that time, so $n = 7$ at $t = 4$. $\hat S = 7/8,\ 3/4,\ 3/5,\ 1/5$, and $\hat S = 1/5$ from 9 until the last time 12. The median is 9, the first time at which $\hat S \le 1/2$.

4. $\hat H = 1/8,\ 15/56,\ 131/280,\ 953/840$ at 3, 4, 6 and 9, so $\hat H(9) \approx 1.1345$ and $\exp(-\hat H(9)) \approx 0.322$, against $\hat S(9) = 0.2$. Since $1 - x \le e^{-x}$ for every $x$, each Kaplan-Meier factor $1 - d_j/n_j$ is at most $e^{-d_j/n_j}$, and so is their product.

5. $\sum d_j/(n_j(n_j - d_j)) = 1/56 + 1/42 + 1/20 = 11/120$ up to $t = 6$, so the variance is $(3/5)^2 \cdot 11/120 = 33/1000$ and the standard error is $0.182$. The plain interval is $(0.244, 0.956)$. For the log-log interval, $\hat\tau = 0.182/(0.6\,|\log 0.6|) = 0.593$, and $(0.6^{\exp(1.96\hat\tau)}, 0.6^{\exp(-1.96\hat\tau)}) = (0.195, 0.852)$. Both are asymptotic intervals, and with eight subjects they are rough.

6. $E_A = 3 \cdot 10/16 = 15/8$, so $O_A - E_A = 1/8$. $V = 3 \cdot 13 \cdot 10 \cdot 6/(16^2 \cdot 15) = 39/64 \approx 0.609$.

7. A pair is comparable when the earlier time is an event, so the subject censored at 4 is never the earlier one. The comparable pairs are $(2,4^+), (2,5), (2,6), (2,9^+), (5,6), (5,9^+), (6,9^+)$: seven pairs. Only $(2, 5)$ is discordant, since $0.7 < 0.8$, so $C = 6/7 \approx 0.857$.

9. The marginal ratio is $r(1 + \theta H_0)/(1 + \theta r H_0) = 3 \cdot 2/(1 + 3) = 1.5$, half of the conditional ratio. Kendall's $\tau = \theta/(\theta + 2) = 0.2$.

13. The event times are 1, 2, 3, 4, 7, 8, 9, with $(n_j, n_{Aj}, d_j, d_{Aj}) = (10,5,1,0), (9,5,1,1), (8,4,2,0), (6,4,1,1), (3,2,1,1), (2,1,1,0), (1,1,1,1)$. Then $O_A = 4$, $E_A = 44/9 \approx 4.889$, $V = 1837/1134 \approx 1.620$, $X^2 \approx 0.488$ and $p \approx 0.48$. The data give no evidence against equal hazards. The p-value is not the probability that the hazards are equal, and a large p-value with ten subjects is not evidence that they are; the $\chi^2_1$ law is also only an approximation here.

15. The event times 1, 3, 6, 8 have risk sets with $x$-means $3/5, 3/4, 1/2, 1$, so $U(0) = (0 - 3/5) + (1 - 3/4) + (0 - 1/2) + 0 = -17/20$ and $I(0) = 6/25 + 3/16 + 1/4 + 0 = 271/400$. The Newton step gives $\beta_1 = -340/271 \approx -1.2546$, and the iteration converges to $\hat\beta \approx -1.2271$, a hazard ratio of about $0.29$ with standard error about $1.25$. $U(0)^2/I(0) \approx 1.066$: with one event at each time, $I(0)$ equals the hypergeometric variance and $U(0) = O_1 - E_1$.

18. The rows are $t = 1, 3, 5, 7$ with $n = 8, 6, 4, 2$. $\hat F_1 = 1/8,\ 13/48,\ 13/48,\ 47/96$, $\hat F_2 = 0,\ 7/48,\ 7/24,\ 7/24$ and $\hat S = 7/8,\ 7/12,\ 7/16,\ 7/32$, which sum to 1 at every row. One minus Kaplan-Meier for cause 1 is $1/8,\ 13/48,\ 13/48,\ 61/96$. Both change only at cause-1 event times, and they agree until a cause-2 event has happened strictly before a cause-1 event time: at $t = 7$ the cumulative incidence uses $\hat S(7-) = 7/16$ and the other uses $35/48$.

20. The innermost intervals are $(2, 3]$, $(4, 5]$ and $(6, 7]$, with masses $s_1, s_2, s_3$, and the likelihood is $s_1(s_1 + s_2)(s_2 + s_3)s_3$. Writing $u = s_1 + s_2 = 1 - s_3$, it is $s_1(1 - s_1)\,u(1 - u)$ with $s_1 \le u$, which is largest at $s_1 = u = 1/2$. So $\hat s = (1/2, 0, 1/2)$ with likelihood $1/16$: the NPMLE puts no mass in the middle. The gradient ratios $\frac14\sum_i \alpha_{ij}/P_i$ are all equal to 1, so the Kuhn-Tucker conditions hold.

23. With no censoring, $O_1 = |G_1|$. At the $k$-th event time there are $n - k + 1$ subjects at risk and one event, so $E_1 = \sum_k n_{1k}/(n - k + 1)$. A subject of group 1 at rank $i$ is at risk at the event times $k = 1, \ldots, i$, so it contributes $\sum_{k \le i} 1/(n - k + 1)$ to $E_1$ and 1 to $O_1$.

24. Take $T^\ast$ and $C^\ast$ independent with hazards $g_1$ and $g_0$. The hazard of $Y$ is $g_1 + g_0$, so $P(Y > t) = \exp(-\int_0^t (g_1 + g_0))$, and the same holds for $Y^\ast = \min(T^\ast, C^\ast)$ by independence. The subdensity of $(Y, \delta = 1)$ at $t$ is $g_1(t)P(Y \ge t)$, and that of $(Y^\ast, \delta^\ast = 1)$ is $g_1(t)P(Y^\ast \ge t)$, the same; likewise for $\delta = 0$. So no test based on $(Y, \delta)$ alone can detect dependent censoring.

25. Sort by time in decreasing order and process one time value at a time. For a value $y$, first insert the censored subjects at $y$ into a Fenwick tree indexed by score rank, then, for each event at $y$, query the number of inserted subjects with a smaller score, an equal score and a larger score (concordant, tied, discordant), and only then insert the events at $y$. Each subject costs $O(\log n)$ for one insertion and at most one query, after an $O(n \log n)$ sort.

26. $F_1(t \mid 0) = \frac12(1 - e^{-2t})$ and $F_1(t \mid 1) = \frac13(1 - e^{-3t})$, so $\tilde h_1(t \mid 0) = 2e^{-2t}/(1 + e^{-2t})$ and $\tilde h_1(t \mid 1) = 3e^{-3t}/(2 + e^{-3t})$. Their ratio is $3e^{-t}(1 + e^{-2t})/(2(2 + e^{-3t}))$, which is 1 at $t = 0$ and about $0.31$ at $t = 1$, and tends to 0. The limits are $F_1(\infty \mid 0) = 1/2$ and $F_1(\infty \mid 1) = 1/3$: more cause-2 events leave fewer subjects to have a cause-1 event.

27. By symmetry $s_1 = s_3 = a$ and $s_2 = b = 1 - 2a$ after every step. The update gives $b' = \frac14\bigl(b/(a + b) + b/(b + a)\bigr) = \frac12\, b/(a + b)$, and $a + b = (1 + b)/2$, so $b' = b/(1 + b)$. If $b = 1/m$ then $b' = 1/(m + 1)$, and the start $b = 1/3$ gives $1/(k + 3)$.
