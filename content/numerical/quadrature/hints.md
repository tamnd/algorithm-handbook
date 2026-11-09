1. $M = 0.685714$, $T = 0.708333$ and $S = 0.694444$, against $\log 2 = 0.693147$. The errors $Q - I$ are $-7.4 \times 10^{-3}$, $+1.52 \times 10^{-2}$ and $+1.30 \times 10^{-3}$: the midpoint error is about half the trapezoidal one, with the opposite sign. Both $\tfrac13(2M + T)$ and the four-panel Simpson rule give $0.693254$.

2. The rule is exact for $1, x, x^2$ and gives $-\tfrac49$ for $x^3$, whose integral is $0$, so $d = 2$. With two nodes and one of them fixed at an endpoint, this is the two-point Gauss-Radau rule.

4. The trapezoidal error scales like $m^{-2}$, so $m = 10\sqrt{400} = 200$. The Simpson error scales like $m^{-4}$, so $m \ge 10 \cdot 400^{1/4} \approx 44.7$, and $m$ must be even: $46$.

5. $\sigma^2 = \tfrac15 - \tfrac19 = \tfrac{4}{45}$. For $N = 100$ the error is $\sigma/10 \approx 0.0298$, and $N = \sigma^2/10^{-6} \approx 88{,}900$ points give $10^{-3}$.

8. Sorted, the points are $0, \tfrac14, \tfrac12$, and the one-dimensional formula gives $D_3^* = \tfrac16 + \tfrac13 = \tfrac12$. The variation of $x^2$ on $[0, 1]$ is $1$, so the bound is $\tfrac12$; the average is $\tfrac{5}{48}$ and the actual error is $\tfrac13 - \tfrac{5}{48} = \tfrac{11}{48} \approx 0.229$.

9. On $[0, 1]$ with one panel, the errors on $1, x, x^2, x^3$ are $0$ and the error on $x^4$ is $\tfrac15 - \tfrac16 = \tfrac{1}{30}$. On $\int_1^2 dx/x$ the rule gives $0.692708$, off by $-4.4 \times 10^{-4}$, three times better than Simpson's $+1.3 \times 10^{-3}$ from the same values.

13. Orthogonality to $1$ and $x$ under $w = x$ gives $\pi_2 = x^2 - \tfrac65 x + \tfrac{3}{10}$, with zeros $(6 \mp \sqrt6)/10$. The weights are $(9 \mp \sqrt6)/36$, and $E(x \cdot x^4) = \int_0^1 x\,\pi_2^2 = \tfrac{1}{600}$.

14. Rationalize the two terms: $\frac{2 + \sqrt2}{4(3 - \sqrt2)} + \frac{2 - \sqrt2}{4(3 + \sqrt2)} = \frac{4}{7}$. Use $\alpha_k = 2k + 1$ and $\beta_k = k^2$. The errors are about $3.0 \times 10^{-3}$, $1.3 \times 10^{-4}$, $1.4 \times 10^{-6}$ and $2.0 \times 10^{-9}$: roughly like $e^{-4\sqrt n}$, not geometric, because $1/(1 + x)$ has a pole at $x = -1$.

17. For $s = 3$ there are 25 points against $5^3 = 125$, and the rule is still exact for total degree 5. For $s = 10$ there are 221 points against $5^{10} = 9{,}765{,}625$.

20. If $a$ is a node, $p(x) = (x - a)\prod_{i \ge 2}(x - x_i)^2$ has degree $2n - 1$, is nonnegative on $[a, b]$ and vanishes at every node, so $Q(p) = 0 < \int p\,w$. With both ends prescribed, use $(x - a)(b - x)\prod_{i=2}^{n-1}(x - x_i)^2$, of degree $2n - 2$.

21. $x^{2n} - \pi_n^2$ has degree at most $2n - 1$, so the rule integrates it exactly, and $Q_n(\pi_n^2) = 0$ because every node is a zero of $\pi_n$. For $n = 4$ the value is $\tfrac{128}{11025} \approx 0.01161$.

22. The rule sums the Fourier series at $m$ equally spaced points, so $T_m = 2\pi\sum_{\ell} c_{\ell m}$ (aliasing). Sum the geometric series over $\ell \ne 0$. The errors are $3.76 \times 10^{-2}$, $1.93 \times 10^{-4}$ and $5.12 \times 10^{-9}$.

23. Carry the weights of the four trapezoidal rules through the extrapolation. The result is $\tfrac{1}{22680}(868, 4096, 1408, 4096, 1744, 4096, 1408, 4096, 868)$, all positive, with degree 7. The 9-point Newton-Cotes rule has degree 9 and weights $\tfrac{1}{28350}(989, 5888, -928, 10496, -4540, \ldots)$, negative at $\tfrac28$, $\tfrac12$ and $\tfrac68$.
