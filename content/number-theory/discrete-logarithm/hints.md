1. The baby steps $5^0, \ldots, 5^6$ are $1, 5, 25, 31, 14, 23, 21$, and $5^{-7} \equiv 30$. The giant steps $35 \cdot 30^i$ are $35, 16, 10, 18, 23$; the last is in the table with $j = 5$, so $x = 4 \cdot 7 + 5 = 33$.

2. $\gcd(3, 30) = 3$, so there are $0$ or $3$ roots. The cube roots of $1$ are $1, 5, 25$, and $2^3 = 8$, so the roots are $2, 10, 19$. Since $\log_3 3 = 1$ is not divisible by $3$, the congruence $x^3 \equiv 3$ has no solution.

3. $\gcd(3, 100) = 1$, so $x \mapsto x^3$ is a bijection, inverted by raising to $3^{-1} \bmod 100 = 67$. The root is $10^{67} \bmod 101 = 91$.

5. Sixteen digits, each found with one exponentiation of at most $16$ squarings and a comparison with $\pm 1$: a few hundred multiplications in all. A prime with smooth $p - 1$ gives no security.

9. $g^{(p-1)/2} \equiv -1$ because $g$ has order $p - 1$. Here $35^{23} \equiv -1 \pmod{47}$, and indeed $x = 33$ is odd. In a group of prime order $q$ there is no small subgroup to project onto.

10. $x \equiv 2 \pmod 3$, since $23^{32} \equiv 5^{64} \pmod{97}$. The binary digits of $x \bmod 32$, from the lowest, are $1, 0, 1, 1, 0$, so $x \equiv 13 \pmod{32}$. Then $x = 77$.

11. From the first relation $\log 7 = 9$, then $\log 5 = 33 - 9 = 24$ and $\log 3 = 17 - 48 \equiv 69$. The last relation gives $2 \log 3 \equiv 38 \pmod{100}$, which has the two solutions $19$ and $69$, because $2$ is not invertible modulo $100$. Finally $\log 37 = 2 \cdot 69 + 24 - 6 \equiv 56$.

12. $3 + 5x \equiv 43 + x$, so $4x \equiv 40 \pmod{46}$, then $2x \equiv 20 \pmod{23}$ and $x \equiv 10 \pmod{23}$. The candidates are $10$ and $33$; since $5^{10} \equiv 12$, the answer is $33$.

15. The irreducibles of degree at most $2$ are $t$, $t + 1$ and $t^2 + t + 1$, so count the solutions of $a + b + 2c = 10$: $11 + 9 + 7 + 5 + 3 + 1 = 36$, or $36/1024 \approx 3.5\%$.

18. Each relation needs $u^{u}$ trials with $u \ln u \approx \frac{1}{2c} \sqrt{\ln p \ln \ln p}$, so about $B$ relations cost $L_p[1/2, c + 1/(2c) + c]$ with trial division, and the linear algebra $L_p[1/2, 2c]$. If a smoothness test is nearly free, the relations cost $L_p[1/2, c + 1/(2c)]$; at $c = 1/\sqrt 2$ both parts are $L_p[1/2, \sqrt 2]$.

19. Let $f(x) = x^3 + x$, so $f(-x) = -f(x)$. For $x \ne 0$, $f(x) \ne 0$, since $x^2 = -1$ has no solution, and exactly one of $f(x)$ and $-f(x)$ is a square. Each pair $\{x, -x\}$ gives two points, which with $(0, 0)$ and the point at infinity makes $p + 1$. Then $r \mid p^2 - 1$, while $r \nmid p - 1$ since $\gcd(p - 1, p + 1) = 2$.

20. Expand by the binomial theorem; the terms with $p^2$ vanish. Then $h^{p-1} = (g^{p-1})^x$, and both have the form $1 + ap$, so $x \equiv a_h / a_g \pmod p$. Here $3^6 \equiv 43 = 1 + 6 \cdot 7$ and $17^6 \equiv 22 = 1 + 3 \cdot 7 \pmod{49}$, so $x \equiv 3 \cdot 6^{-1} \equiv 4 \pmod 7$. Modulo $7$, $17 \equiv 3$, so $x \equiv 1 \pmod 6$, and $x = 25$.

21. Write $G \cong C_l \times C_{n/l}$. Given $g_l$ and $h_l$ of order $l$, simulate the algorithm on pairs: the first component uses the oracle of the group of order $l$, and the second you compute yourself, with $g = (g_l, \gamma)$ and $h = (h_l, \gamma^y)$ for a random $y$. The answer modulo $n$, reduced modulo $l$, is $\log h_l$. Shoup's bound for the group of order $l$ then gives $\Omega(\sqrt l)$.
