1. The width after $k$ halvings is $2^{-k}$, and $2^{-k} \le 2 \times 10^{-6}$ first holds at $k = 19$.

2. The iterates are $7/4$, $97/56$ and $18817/10864$, and the last is about $2.4 \times 10^{-9}$ above $\sqrt 3$.

5. $f(1) = f'(1) = 0$ and $f''(1) = 6$, so the multiplicity is 2 and the rate is $1/2$.

7. The rate is $\sin x^* \approx 0.674$, so each step gains $-\log_{10} 0.674 \approx 0.17$ digits: about six steps per digit.

8. The derivatives at $2$ are $4$, $1/4$ and $-1/2$. The first iteration moves away from $2$; the other two converge with rates $1/4$ and $1/2$, the last one alternating sides.

10. $1 - a x(2 - ax) = (1 - ax)^2$. Here $r_0 = 0.3$ and $r_k = 0.3^{2^k}$, so five steps suffice.

12. The simple root moves by $10^{-10}/|f'(1)| = 10^{-10}$. The double root splits into $1 \pm 10^{-5}$.

15. The sign sequences of $p, p', p'', p'''$ are $(+, -, 0, +)$ at $0$, with two changes, and $(+, +, +, +)$ at $2$. Since $p(1) = -1$, there are exactly two roots.

18. The step is $x - 3x = -2x$, so $|x_k| = 2^k|x_0|$. The derivative of $f$ is unbounded at the root.

19. Compute $2f'^2 - ff'' = m(m+1)x^{2m-2}$. Newton's rate is $(m-1)/m$: $1/2$ against $1/3$ for $m = 2$, and $0.9$ against $9/11 \approx 0.82$ for $m = 10$.

20. The floats in $[1, 2)$ are spaced $2^{-52}$ apart, so 52 halvings bring the width down to one ulp, and the next midpoint is not representable. The ends are $1.414213562373095$ and $1.4142135623730951$.

21. Here $L = 1/x_0$ and $\eta = |x_0^2 - 2|/(2x_0)$, so $h \le 1/2$ exactly when $x_0 \ge 1$. At $x_0 = 1$, $h = 1/2$ and $t^* = 1$: the root lies in $[0, 2]$.

22. $N'(x) = f(x)f''(x)/f'(x)^2$ and $f''(0) = 0$, so $N'(0) = 0$. By the chain rule the two-step map has derivative $N'(1)N'(0) = 0$: the cycle is superattracting.
