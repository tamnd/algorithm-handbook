1. The primes $2, 3, 5, 7$ have passes, clearing $49$, $31$, $16$ and $8$ flags: $104$ clear operations. The flag of $90$ is cleared three times, by $2$, $3$ and $5$. There are only $74$ composites up to $100$, so $30$ clears repeat work; this waste is the factor $\log \log n$.

3. At $i = 15$, $\mathrm{lp}(15) = 3$: the prime $2$ writes $30$, and $3 \cdot 15 = 45 > 40$ stops the loop. The number $36 = 2 \cdot 18$ is written at $i = 18$. There are $27$ writes, one for each composite up to $40$.

5. Count the pairs $(e, f)$ with $ef \le 16$: those with $e \le 4$ and those with $f \le 4$, minus the $4^2$ counted twice. The sum is $2(16 + 8 + 5 + 4) - 16 = 50$.

6. $30 - \lfloor 30/4 \rfloor - \lfloor 30/9 \rfloor - \lfloor 30/25 \rfloor = 30 - 7 - 3 - 1 = 19$. The other $11$ are $4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28$.

7. $\phi(50, 1) = 25$, $\phi(50, 2) = 25 - \phi(16, 1) = 17$, $\phi(50, 3) = 17 - \phi(10, 2) = 14$, $\phi(50, 4) = 14 - \phi(7, 3) = 12$. So $\pi(50) = 12 + 4 - 1 = 15$.

9. $221 = 4 \cdot 5^2 + 11^2 = 4 \cdot 7^2 + 5^2$: two solutions, so $221 = 13 \cdot 17$ is composite. $229 = 4 \cdot 1^2 + 15^2$ is the only solution, so $229$ is prime.

10. For fixed $i$, $j$ runs from $i$ to $(k - i)/(2i + 1)$, with $k \approx n/2$, and $i$ runs up to about $\sqrt{k/2}$. The count is about $\sum_i k/(2i + 1) \approx (k/2) \ln \sqrt k$, or $(n/8) \ln n$. The crossed-out $x = i + j(2i + 1)$ are the odd multiples $(2i + 1)(2j + 1)$ of $2i + 1$ from $(2i + 1)^2$ on, so restricting $i$ to odd primes $q = 2i + 1$ costs $\sum_{q \le \sqrt n} k/q = \Theta(n \log \log n)$.

12. Group the pairs by $g = \gcd(a, b)$ and apply Möbius inversion to $\lfloor n/g \rfloor^2$. For the second form, count the pairs with $a < b$ by $b$, the same number with $a > b$, and the pair $(1, 1)$. For $n = 10$: $100 - 25 - 9 - 4 + 1 - 1 + 1 = 63$, and $2 \cdot 32 - 1 = 63$.

14. The $78498$ primes up to $10^6$. About $10^6 \cdot 2.89 \approx 2.9 \cdot 10^6$ clear operations, plus one start offset per base prime. About $10^6 / \ln 10^{12} \approx 36000$ primes.

16. $a = \pi(5) = 3$ and $\phi(200, 3) = 54$. The primes $7, 11, 13$ give $P_2 = (9 - 4 + 1) + (7 - 5 + 1) + (6 - 6 + 1) = 10$, so $\pi(200) = 54 + 3 - 1 - 10 = 46$. A product of three primes above $5$ is at least $7^3 = 343 > 200$.

19. For $k < r$, $x/k - x/(k + 1) = x/(k(k + 1)) \ge 1$, so the values for $k \le r$ are distinct, and all except perhaps the last exceed $r$. The values for $k > r$ are at most $r$ and include every $v \le r$. The two sets overlap exactly when $\lfloor x/r \rfloor = r$, that is, when $x < r(r + 1)$. For $x = 50$: $r = 7$, $56 > 50$, and there are $13$ values.

20. For $p \le x^{1/4}$ each step touches at most $2\sqrt x$ values, and there are $O(x^{1/4} / \log x)$ such primes. For $p > x^{1/4}$, $p^2 > \sqrt x$, so only the values $\lfloor x/k \rfloor$ with $k \le x/p^2$ are touched, and $\sum_{p > x^{1/4}} x/p^2 = O(x^{3/4} / \log x)$ by the prime number theorem.

21. Three prime factors above $x^{1/3}$ would multiply to more than $x$. The products $pq$ number $\sum_{x^{1/3} < p \le \sqrt x} (\pi(x/p) - \pi(p) + 1)$. With $p = x^s$ the main part is $\frac{x}{\ln x} \int_{1/3}^{1/2} \frac{ds}{s(1 - s)} = \ln 2 \cdot \frac{x}{\ln x}$, and the primes add $x / \ln x$. Buchstab gives $\omega(3)\, x / \ln x^{1/3} = 3\omega(3)\, x / \ln x = (1 + \ln 2)\, x / \ln x$, the same.

22. $\sum_{p \le x} 1/p = \pi_2(x)/x + \int_2^x \pi_2(t)\, dt / t^2$ over twin primes. The integrand is $O\big((\log \log t)^2 / (t \log^2 t)\big)$; with $t = e^u$ this becomes $O\big((\log u)^2 / u^2\big)\, du$, which is integrable.

23. Write $p = a^2 + b^2$; this is unique up to order and signs. Since $p$ is odd, exactly one of $a, b$ is even, say $a = 2x$, so $p = 4x^2 + b^2$ with $x, |b| > 0$, and no other choice is possible.

24. $\lfloor n/d \rfloor^2 = n^2/d^2 + O(n/d)$, so $\sum_{d \le n} \mu(d) \lfloor n/d \rfloor^2 = n^2 \sum_{d \le n} \mu(d)/d^2 + O(n \log n)$, and the tail $\sum_{d > n} 1/d^2$ is $O(1/n)$. Halve the result as in Exercise 12.
