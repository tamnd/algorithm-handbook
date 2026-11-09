1. $p(x) = x^2 + x + 1$.

4. The bound is $h^2/8 = 0.00125$. An error below $10^{-6}$ needs $h \le \sqrt{8 \times 10^{-6}}$, that is 1111 intervals.

5. $T_2 = 2x^2 - 1$, $T_3 = 4x^3 - 3x$ and $T_4 = 8x^4 - 8x^2 + 1$; both sides equal $-1/2$.

7. $2.75$ and $2.9375$.

8. The result is $0.7$, with error $0.0069$ against $0.14$ for $s_2$.

11. $\max|x(x - 0.5)(x - 1)| = \sqrt3/36 \approx 0.0481$, so the bound is $e\sqrt3/216 \approx 0.0218$; the actual maximum error is about $0.0144$.

13. The equation $M_0 + 4M_1 + M_2 = 6(y_0 - 2y_1 + y_2)$ with $M_0 = M_2 = 0$ gives $M_1 = -3$, and $s(1/2) = 11/16$.

14. The $L^2$ best line is $x - 1/6$, with maximum error $1/6$. The minimax line is $x - 1/8$, with error $1/8$ attained with alternating signs at $0$, $1/2$ and $1$.

17. $x^3 = (3T_1 + T_3)/4$. Drop $T_3/4$ to get $3x/4$, with error $|T_3|/4 \le 1/4$, which equioscillates at four points.

19. The extrema are at $\cos(k\pi/n)$, $k = 0, \dots, n$. The difference $2^{1-n}T_n$ is monic and equioscillates at $n + 1$ points. For $n = 4$ the answer is $x^2 - 1/8$, with error $1/8$.

20. The result is $1/(2(k+1))$: Aitken only halves the error, because the error is not close to geometric.

21. Let $g = s + e$ with $e$ zero at the knots. Integrate $\int s''e''$ by parts on each interval; the boundary terms vanish by $s''(a) = s''(b) = 0$, and the rest vanishes because $s'''$ is constant on each piece. Then $\int g''^2 = \int s''^2 + \int e''^2$.

22. $\rho = 2 + \sqrt3 \approx 3.732$, so about $15\ln 10/\ln\rho \approx 26$. The errors are near $10^{-6}$ for $n = 10$, $2.4 \times 10^{-12}$ for $n = 20$ and $1.4 \times 10^{-15}$ for $n = 26$.
