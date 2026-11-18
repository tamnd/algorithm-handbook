1. With $p = (1/2, 1/4, 1/6, 1/12)$: $H \approx 1.199$, $e^H \approx 3.32$ and the evenness is $0.865$. Then $\lambda = 25/72 \approx 0.347$, $1/\lambda = 2.88$, and the unbiased form is $(30 + 6 + 2 + 0)/132 = 19/66 \approx 0.288$.

2. The estimate is $50 \cdot 40/8 = 250$. Chapman's form is $51 \cdot 41/9 - 1 = 694/3 \approx 231$.

4. The threshold is $1 - 1/5 = 0.8$, so the coverage is $0.8/0.9 \approx 0.89$. For $R_0 = 12$ the threshold is $11/12$ and the coverage would be $1.02$: even vaccinating everyone does not stop spread, so a better vaccine or other measures are needed.

7. The fixed point is $1 - 1/r$ and the slope is $2 - r$. For $r = 2.5$ the point is $0.6$ with slope $-0.5$, stable. For $r = 3.2$ the point is $0.6875$ with slope $-1.2$, unstable.

10. The mean is $4/3$. The equation $f(s) = s$ is $3s^2 - 4s + 1 = 0$ with roots $1/3$ and 1, so $q = 1/3$. Two ancestors start independent lines, so the answer is $q^2 = 1/9$.

12. The equation is $\lambda^3 = \lambda/2 + 1/2$, which factors as $(\lambda - 1)(\lambda^2 + \lambda + 1/2) = 0$. The stable age distribution is proportional to $(1, P_1/\lambda, P_1 P_2/\lambda^2) = (1, 1/2, 1/4)$, that is $(4/7, 2/7, 1/7)$. The other two roots have modulus $\sqrt{1/2} \approx 0.71$.

15. With constant growth $I_t = G^t$, the equation gives $1 = R(G^{-1} + G^{-2})/2$. For $R = 2$ this is $G^2 = G + 1$, so $G = (1 + \sqrt 5)/2 \approx 1.618$. For $G = 1.2$, $R = 1/(0.5/1.2 + 0.5/1.44) \approx 1.309$.

19. The chance of no new case is $(1/2)^3 = 1/8$. Follow the chains as in the entry: the law of the final size on $0, 1, 2, 3$ is $1/8$, $3/32$, $3/16$ and $19/32$, with mean $9/4$.

21. Use [Jensen's inequality](/jensens-inequality/) with weights $p_i$ for the concave function $\ln$. On $x_i = p_i$ it gives $\ln \sum p_i^2 \ge \sum p_i \ln p_i$, that is $1/\lambda \le e^H$; on $x_i = 1/p_i$ it gives $H \le \ln S$. Equality holds when all $x_i$ are equal. For exercise 1: $2.88 \le 3.32 \le 4$.

22. With $k = 1/2$, squaring $q = (5 - 4q)^{-1/2}$ gives $4q^3 - 5q^2 + 1 = 0$, which is $(q - 1)(4q^2 - q - 1) = 0$. So $q = (1 + \sqrt{17})/8 \approx 0.640$, against $1/2$ for $k = 1$ and $0.203$ for Poisson offspring: more spread in the offspring makes early extinction more likely.

23. $\langle k^2 \rangle \ge \langle k \rangle^2$ because the variance is non-negative. With $P(k) \propto k^{-3}$, $\langle k \rangle / \langle k^2 \rangle = \sum k^{-2} / \sum k^{-1}$, which is about $0.315$, $0.220$ and $0.114$. The numerator tends to $\pi^2/6$ and the denominator grows like $\ln K$.

24. Infections by a case that has been infectious for time $u$ happen at rate $\beta e^{-\gamma u}$, which is $\beta/\gamma$ times the exponential density with rate $\gamma$. So $M(-r) = \frac{\sigma}{\sigma + r} \cdot \frac{\gamma}{\gamma + r}$. Here $R_0 = 3$, the growth rate solves $r^2 + 0.45r - 0.1 = 0$, so $r \approx 0.1631$, and $(1 + r/0.25)(1 + r/0.2) = 3$.

25. The trace is $-3$ and the determinant is $2$, so the reaction alone is stable. The conditions are $s = d - 4 > 0$ and $s^2 > 8d$, that is $d^2 - 16d + 16 > 0$, so $d > 8 + 4\sqrt 3 \approx 14.93$. At that $d$ the critical wavenumber squared is $s/(2d) = \sqrt{2/d} \approx 0.366$.
