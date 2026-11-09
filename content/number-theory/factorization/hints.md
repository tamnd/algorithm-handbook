1. $9991 = 97 \cdot 103$. Plain trial division makes $49$ divisions: by $2$ and by the $48$ odd numbers from $3$ to $97$. The wheel makes $28$: by $2$, $3$, $5$ and by the $25$ numbers from $7$ to $97$ coprime to $30$.

2. $\lceil \sqrt{5959} \rceil = 78$: $78^2 - N = 125$, $79^2 - N = 282$, $80^2 - N = 441 = 21^2$. So $5959 = (80 - 21)(80 + 21) = 59 \cdot 101$.

3. $8/30 \approx 0.267$, $48/210 \approx 0.229$, $480/2310 \approx 0.208$. Adding the prime $p$ multiplies the fraction by $1 - 1/p$: a saving of $1/7$ and then $1/11$, while the wheel grows from $8$ to $48$ to $480$ entries.

5. $210 = 2 \cdot 3 \cdot 5 \cdot 7$ divides $420$, so $2^{420} \equiv 1 \pmod{211}$. But $222 = 2 \cdot 3 \cdot 37$, and the order of $2$ modulo $223$ divides $222$ without dividing $420$, since $2^6 \not\equiv 1$. So the gcd is $211$.

8. $300 \cdot 2700 = 900^2$ and $67 \cdot 83 \equiv 1372$, so $1372^2 \equiv 900^2$ and $\gcd(1372 - 900, 4189) = \gcd(472, 4189) = 59$. Also $572 \cdot 1287 = 858^2$ and $69 \cdot 74 \equiv 917$, so $\gcd(917 - 858, 4189) = 59$. So $4189 = 59 \cdot 71$.

10. The first success is at $x = (a + b)/2$, and $x - \sqrt N = (\sqrt b - \sqrt a)^2 / 2 = (b - a)^2 / \big(2(\sqrt a + \sqrt b)^2\big) \le (b - a)^2 / (8\sqrt N)$, since $(\sqrt a + \sqrt b)^2 \ge 4\sqrt N$. If this is below 1, then $x = \lceil \sqrt N \rceil$. RSA primes must therefore not be too close together.

11. With $B = 5$ the gcd is $331$: the order of $2$ modulo $331$ is $30$, which divides $60$; what matters is the order of the base, not $p - 1$. With $B = 7$ both $211$ and $331$ divide $2^{420} - 1$, and the gcd is $N$. Take gcds more often, or back up to the last prime power and add them one at a time.

12. $p + q = N - \varphi(N) + 1$ and $pq = N$, so $p$ and $q$ are the roots of $t^2 - (p + q)t + N$. Here $p + q = 204$, the discriminant is $204^2 - 4 \cdot 10403 = 4$, and $p, q = 101, 103$.

14. $B = 11$. The tenth block, $100, \ldots, 110$, is the first whose product shares a factor with $N$, and the gcd is $N$ itself, since it contains both $101$ and $103$. A scan of the block, one gcd per element, finds $101$ first.

18. $\lceil \sqrt N \rceil = 1235$ and the factors give $x = (1009 + 1511)/2 = 1260$, so $26$ trial values. For $24N$: $\lceil \sqrt{24N} \rceil = 6049$ and $6049^2 - 24N = 25 = 5^2$, so $24N = 6044 \cdot 6054$, and $\gcd(6044, N) = 1511$.

19. The integers up to $x$ with a prime factor $p > \sqrt x$ number $\sum_{\sqrt x < p \le x} \lfloor x/p \rfloor = x \sum_{\sqrt x < p \le x} 1/p + O(\pi(x))$, with no double counting. By Mertens the sum is $\ln \ln x - \ln \ln \sqrt x + o(1) = \ln 2 + o(1)$. So the smooth fraction tends to $1 - \ln 2 = \rho(2)$.

20. Only prime $k \le \lg N$ need checking. For each, find $b = \lfloor N^{1/k} \rfloor$ by binary search on $[1, 2^{\lceil \lg N / k \rceil}]$, computing $b^k$ by repeated squaring and stopping once it exceeds $N$. That is $O(\lg N)$ candidates, each $O(\lg N / k)$ search steps of $O(\lg k)$ multiplications, so $O((\lg N)^2 \lg \lg N)$ multiplications in all.

21. The exponent of $p$ in $M$ is the largest $k$ with $p^k \le B$, so $\ln M$ adds $\ln p$ once for each prime power $p^k \le B$. Hence $\ln M \sim B$, and computing $a^M$ takes about $\lg M = \ln M / \ln 2 \approx 1.44 B$ squarings.

22. Expand both squares. Fermat's method on $4uvN$ starts at $\lceil 2\sqrt{uvN} \rceil$ and succeeds at $x = vp + uq$, and $x - 2\sqrt{uvN} = (\sqrt{vp} - \sqrt{uq})^2 \approx (vp - uq)^2 / (4\sqrt{uvN})$. This is below 1, so the first trial value works, when $|vp - uq| < 2(uvN)^{1/4}$, which holds when $q/p$ is close to $v/u$. With $u = 2$, $v = 3$: $x = 3027 + 3022 = 6049$ and $vp - uq = 5$.
