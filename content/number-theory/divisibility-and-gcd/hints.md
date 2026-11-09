1. $252 = 1 \cdot 198 + 54$, $198 = 3 \cdot 54 + 36$, $54 = 1 \cdot 36 + 18$, $36 = 2 \cdot 18 + 0$. The gcd is $18$, after four divisions. The quotients $1, 3, 1, 2$ are the continued fraction $252/198 = [1; 3, 1, 2]$.

3. $720 = 2^4 \cdot 3^2 \cdot 5$, so $d(720) = 5 \cdot 3 \cdot 2 = 30$ and $\sigma(720) = 31 \cdot 13 \cdot 6 = 2418$.

5. $157/68 = [2; 3, 4, 5]$, with convergents $2/1$, $7/3$, $30/13$ and $157/68$. For example $7 \cdot 1 - 2 \cdot 3 = 1$ and $30 \cdot 3 - 7 \cdot 13 = -1$.

9. $3/7 < 1$, go left to $1/2$; $3/7 < 1/2$, left to $1/3$; $3/7 > 1/3$, right to $2/5$; $3/7 > 2/5$, right to $3/7$. The path is $LLRR$. Since $3/7 = [0; 2, 3]$, the runs are $a_1 = 2$ moves left and $a_2 - 1 = 2$ moves right.

10. The answer is $120 = 2^3 \cdot 3 \cdot 5$. Write $16$ as a product of factors $e_i + 1$ in all ways ($16$, $8 \cdot 2$, $4 \cdot 4$, $4 \cdot 2 \cdot 2$, $2 \cdot 2 \cdot 2 \cdot 2$), give the largest exponent to the smallest prime, and compare $2^{15}$, $384$, $216$, $120$ and $210$.

12. If $a = qb + r$, then $2^a - 1 = 2^r (2^{qb} - 1) + (2^r - 1)$, and $2^b - 1$ divides $2^{qb} - 1$. So $(2^a - 1) \bmod (2^b - 1) = 2^r - 1$. The answer is $2^{\gcd(12, 18)} - 1 = 63$.

14. There are $\lfloor n/d \rfloor^2$ pairs with $d \mid a$ and $d \mid b$, and $\sum_{d \mid \gcd(a, b)} \mu(d)$ is $1$ when $\gcd(a, b) = 1$ and $0$ otherwise. Sum this over all pairs and swap the two sums. For $n = 10$ the nonzero terms are $100 - 25 - 9 - 4 + 1 - 1 + 1 = 63$, for $d = 1, 2, 3, 5, 6, 7, 10$.

15. $s = 10$, and $\sum_{a=1}^{10} \lfloor 100/a \rfloor = 100 + 50 + 33 + 25 + 20 + 16 + 14 + 12 + 11 + 10 = 291$. So $D(100) = 2 \cdot 291 - 100 = 482$, with ten divisions.

19. The quotient $(11 + 3i)/(1 + 8i)$ rounds to $1 - i$, with remainder $2 - 4i$. Then $(1 + 8i)/(2 - 4i) = -1.5 + i$; either rounding works, and with $-2 + i$ the remainder is $1 - 2i$. Then $(2 - 4i)/(1 - 2i) = 2$ exactly. The gcd is $1 - 2i$, up to the units $\pm 1, \pm i$, and its norm is $5$.

21. Use $F_{m+n} = F_m F_{n+1} + F_{m-1} F_n$ to show $\gcd(F_{m+n}, F_n) = \gcd(F_m, F_n)$, using that consecutive Fibonacci numbers are coprime. So the pair of indices follows Euclid's algorithm.

22. Every integer $N$ has a unique representation $N = ax + by$ with $0 \le x < b$. It has one with $y \ge 0$ too exactly when this $y$ is non-negative. For $N = ab - a - b$ the representation is $x = b - 1$, $y = -1$. The number of non-representable positive integers is $(a - 1)(b - 1)/2$, which is $30$ for $7$ and $11$; the largest is $59$.

23. Group $k$ by $d = \gcd(k, n)$: the $k \le n$ with $\gcd(k, n) = d$ are $k = dj$ with $\gcd(j, n/d) = 1$, and there are $\varphi(n/d)$ of them. For $n = 12$: $4 + 4 + 6 + 8 + 6 + 12 = 40$.

24. Use the norm $N(x + y\sqrt{-5}) = x^2 + 5y^2$, which is multiplicative. No element has norm $2$ or $3$, so $2$, $3$ and $1 \pm \sqrt{-5}$, of norms $4$, $9$ and $6$, are irreducible. The only units are $\pm 1$. Every Euclidean domain has unique factorization.

25. $C(n) = n^2 \sum_{d \le n} \mu(d)/d^2 + O(n \sum_{d \le n} 1/d)$, because $\lfloor n/d \rfloor^2$ differs from $n^2/d^2$ by at most $2n/d$. The error is $O(n \log n)$, and the tail of the series beyond $n$ is $O(1/n)$.
