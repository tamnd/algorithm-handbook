1. Write $x = b_0 + 2b_1$ and use $b_i = (I - Z_i)/2$. Then $N = 1.5\,II - 0.5\,IZ - ZI$, with no $ZZ$ term, and $\lambda = 1.5$.

2. Drop $3\,II$: it only adds a global phase, but sampling it would raise $\lambda$ from 4 to 7 and waste $3/7$ of the steps. Then $\lambda = 4$, the probabilities of $ZZ$, $XI$ and $IX$ are $1/2$, $1/8$ and $3/8$, $N = \lceil 2 \cdot 16 \cdot 0.25/10^{-3}\rceil = 8000$, and each sampled term, with the sign of its coefficient, acts for time $\lambda t/N = 2.5 \cdot 10^{-4}$.

6. $\frac12(XZXI + YZYI)$. The $Z$ sits on qubit 2, between the two modes, and the strings act as the identity on qubit 0, which is the rightmost symbol.

7. The excited population is $\frac12e^{-t} = \frac18$ and the coherence is $\frac12e^{-t/2} = \frac14$, so $\rho = \begin{pmatrix} 7/8 & 1/4 \\ 1/4 & 1/8 \end{pmatrix}$ and $\mathrm{Tr}\,\rho^2 = 49/64 + 1/64 + 2/16 = 29/32$.

10. $Z_jZ_{j+1}$ fails to commute only with $X_j$ and $X_{j+1}$, and each such commutator has norm $2h$. There are $2n$ such pairs, so $\|[A, B]\| \le 4hn$. With $4hn = 40$, $r = \lceil 25 \cdot 40/0.02\rceil = 50{,}000$ steps.

11. With $\lambda = L\Lambda$ the counts are about $L^2(L-1)\Lambda^2t^2/(2\epsilon)$ and $2L^2\Lambda^2t^2/\epsilon$, with ratio $(L-1)/4$. They are equal at $L = 5$, and qDRIFT asks for fewer from $L = 6$ on. Half the diamond distance between two unitary channels is at most the spectral distance, so Lloyd's guarantee is at least as strong at the same $\epsilon$. Both are counts that suffice by a bound, not the counts that are needed.

13. The eigenvalues of $H$ are $\pm 1$, so the walk has the eigenvalues $e^{\pm i\arccos(1/1.4)} = e^{\pm 0.7752i}$ and $e^{\pm i\arccos(-1/1.4)} = e^{\pm 2.3664i}$. Two eigenvalues of $H$ fill all four dimensions, so there is no $\pm 1$ part. The phase $0.7752$ gives $E = 1.4\cos 0.7752 = 1$.

15. $XI$ and $IX$ anticommute with $ZZ$, so $H^2 = 3\,II + 2\,XX$, $\langle H^2\rangle = 5$, $\langle H\rangle = -2$ and $\sigma^2 = 1$. The spectrum is $-\sqrt5, -1, 1, \sqrt5$, so $b = E_1 = -1$ and Temple gives $E_0 \ge -2 - 1/1 = -3$. Together: $-3 \le E_0 \le -2$.

20. In the symmetric composition the even orders cancel, and the $x^3$ terms of the five factors add up to $(4p^3 + (1 - 4p)^3)x^3E_3$. Setting this to zero gives $1 - 4p = -4^{1/3}p$, so $p = 1/(4 - 4^{1/3}) \approx 0.41449$ and the middle step is $1 - 4p \approx -0.65796$. In general $1 - 4p = -4^{1/3}p$ has the sign opposite to $p$.

21. $C_q$ is the Lagrange basis polynomial for the nodes $u_q = k_q^{-2}$, evaluated at $u = 0$. Interpolating $u^j$ for $j < m$ is exact, so $\sum_q C_qu_q^j = 0^j$. For $k = (1, 2, 4)$ the weights are $1/45$, $-4/9$ and $64/45$, and $s = 85/45 = 17/9 \approx 1.889$.

22. Sum the series in floating point, or bound the tail by its first term times $e^{6Jt}$, and bisect on $t$. The bound reaches $10^{-3}$ at $t \approx 2.79$ for $d = 50$ and $t \approx 5.87$ for $d = 100$, so $d/t \approx 17.9$ and $17.0$, falling toward $6e \approx 16.3$. The XX front moves at $2J$, about eight times slower than the bound allows.

23. The bound asks for $r = \lceil 8\sqrt{1.12 \cdot 10^4}\rceil = 847$ steps, $4r + 1 = 3389$ exponentials. The true error first drops below $10^{-4}$ at $r = 401$, which is $1605$ exponentials, about half.

24. If $m$ of the $N$ samples pick $ZI$, the circuit differs from the exact one by $e^{-i\varphi(ZI - IZ)}$ with $\varphi = (2m/N - 1)t$, whose overlap on $|{+}{+}\rangle$ is $\cos^2\varphi$. For $N = 100$, $1 - F = 0.0195$. Since $\varphi$ has variance $t^2/N$, $1 - F \approx 2t^2/N$.
