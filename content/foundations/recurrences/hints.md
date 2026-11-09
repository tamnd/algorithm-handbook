1. (a) $w = 3$ and $n^2 = O(n^{3-\varepsilon})$: case 1, $\Theta(n^3)$. (b) $w = 0$ and $f = \Theta(n^0)$: case 2, $\Theta(\log n)$. (c) $w = \lg 3 \approx 1.585$, $f = n^2$ is polynomially larger and $3(n/2)^2 = \frac34 n^2$: case 3, $\Theta(n^2)$. (d) $w = 2$, case 2 with $k = 1$: $\Theta(n^2 \lg^2 n)$. (e) $w = \log_9 3 = \frac12$, case 2: $\Theta(\sqrt n \lg n)$.

2. $n^0 = 1$, $n^1$, $n^{\lg 3} \approx n^{1.585}$ and $n^{\lg 7} \approx n^{2.807}$.

3. $C(0) = C(1) = 1$ and $C(n) = 1 + C(n-1) + C(n-2)$. The sequence $C(n) + 1$ satisfies the Fibonacci recurrence with initial values $2 = 2F_1$ and $2 = 2F_2$. $C(10) = 2 \cdot 89 - 1 = 177$.

4. Each of the $k$ levels above the leaves costs $n$, and the $n$ leaves cost $n$: $T(n) = n \log_3 n + n$.

5. The roots of $x^2 - x - 6$ are $3$ and $-2$, and the initial values give $a_n = 2 \cdot 3^n - (-2)^n$. At $n = 2$: $8 + 6 = 14 = 18 - 4$.

6. $x^2 - 4x + 4 = (x - 2)^2$, so $a_n = (A + Bn)2^n$, and the initial values give $a_n = (n + 1)2^n$. A root of multiplicity $m$ contributes a polynomial of degree $m - 1$ times $r^n$.

7. $F_9 F_{11} - F_{10}^2 = 34 \cdot 89 - 55^2 = 3026 - 3025 = 1$. Since $|\psi| < 1$, $|\psi^n/\sqrt5| < 1/2$. $\log_{10} F_{100} \approx 100 \log_{10}\varphi - \log_{10}\sqrt5 \approx 20.55$, so 21 digits.

8. $n^2$ and $n \lg n$ are smooth. $2^n$, $n^{\lg n}$ and $n!$ are not: the ratios $f(2n)/f(n)$ are $2^n$, $2n^2$ and more than $n^n$.

9. $n/\lg n$ is smaller than $n$ but not polynomially smaller. Dividing by $2^k$ gives $T(2^k)/2^k = T(2^{k-1})/2^{k-1} + 1/k$, so $T(2^k) = 2^k H_k$ and $T(n) = \Theta(n \lg\lg n)$.

10. (a) $\frac12 + \frac13 + \frac16 = 1$, so $p = 1$ and the integral is $\ln x$: $\Theta(x \log x)$. (b) With $y = 2^{-p}$, $y + y^2 = 1$, so $y = 1/\varphi$ and $p = \lg\varphi \approx 0.694$. The integral is $\Theta(x^{1-p})$, so $T(x) = \Theta(x)$.

11. $T(2^k) = 3^{k+1} - 2^{k+1}$, that is $T(n) = 3n^{\lg 3} - 2n$.

12. Let $S(n) = T(n)/n$; then $S(n) = S(\sqrt n) + 1$, and with $m = \lg\lg n$ this is $S = m + 1$. So $T(n) = n(\lg\lg n + 1)$.

14. A good string ends in $b$ or $c$, after any good string of length $n - 1$, or in $a$ after $b$ or $c$. So $s_n = 2s_{n-1} + 2s_{n-2}$ with $s_0 = 1$, $s_1 = 3$, the roots are $1 \pm \sqrt3$, and $s_3 = 22$.

15. Level $i$ of the tree costs at most $(9/10)^i cn$, and the sum is at most $10cn$. With groups of three the fractions add up to 1, every level costs $cn$, and the bound is only $O(n \log n)$.

16. You need $\log_3 a < \lg 7$, that is $a < 3^{\lg 7} \approx 21.85$. So $a = 21$.

17. $b_n = \lg a_n$ satisfies $b_n = b_{n-1} + b_{n-2}$ with $b_0 = b_1 = 1$, so $b_n = F_{n+1}$ and $a_n = 2^{F_{n+1}}$.

18. $T(n) = \lg^* n$ exactly. The values where $\lg^*$ changes, $1, 2, 4, 16, 65536, \ldots$, are integers, so the ceiling never moves $\lg n$ across one of them.

20. On $n = b^K$, level $j$ costs $a^j (n/b^j)^w \lg^k(n/b^j) = n^w ((K - j)\lg b)^k$. Sum over $j$: for $k = -1$ the sum is a harmonic number $H_K$, and for $k < -1$ it converges.

21. You get $nF_n - (n-1)F_{n-1} = 2n - 1 + F_{n-1}$, so $F_n = F_{n-1} + 2 - 1/n$ and $F_n = 2n - H_n$. In the theorem $\omega(z) = 1$ and $\mathcal H = 1 - \int_0^1 z\,dz = \frac12$, so $F_n \sim 2n$. This is [quickselect](/quickselect/) looking for the smallest item, where the part that remains has a uniformly random size.

22. $F_{2n} = F_n(2F_{n+1} - F_n)$ and $F_{2n+1} = F_{n+1}^2 + F_n^2$; recurse on $\lfloor n/2 \rfloor$, as in [fast doubling](/fibonacci-fast-doubling/). $F_n$ has about $0.694n$ bits, so the last multiplications alone cost more than $n$.

23. $N_0 = 1$, $N_1 = 2$ and $N_h = N_{h-1} + N_{h-2} + 1$, so $N_h + 1$ is a Fibonacci sequence. Then use $F_m \ge \varphi^{m-2}$.

24. Induction on $k$: after one step the pair is $(b, a \bmod b)$ with $k - 1$ steps left, and $a \ge b + (a \bmod b)$. The pair $(F_{k+2}, F_{k+1})$ needs exactly $k$ steps; this is [Lamé's theorem](/lames-theorem/).
