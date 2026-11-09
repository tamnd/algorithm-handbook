1. ◦ Factor $N = 9991$ by [trial division](/trial-division/) with the divisors $2, 3, 5, 7, 9, \ldots$. How many divisions does it take? How many does [wheel factorization](/wheel-factorization/) modulo $30$ take, counting the divisions by $2$, $3$ and $5$?

2. ◦ Factor $N = 5959$ by [Fermat's method](/fermat-factorization/). List each trial value $x$ and $x^2 - N$.

3. ◦ Compute the fraction $\varphi(W)/W$ of trial divisors that a wheel keeps for $W = 30$, $210$ and $2310$. How much does each new prime in the wheel save, compared with the wheel before it?

4. ◦ Run [Pollard's rho](/pollard-rho/) on $N = 10403$ with $f(x) = x^2 + 1$, $x_0 = 2$ and Floyd's cycle detection. After how many steps does $\gcd(x_i - x_{2i}, N)$ first exceed 1, and what factor does it give?

5. ◦ Run [Pollard's $p - 1$ method](/pollard-p-minus-1/) on $N = 47053 = 211 \cdot 223$ with the base $2$ and $B = 7$, so $M = 420$. Which factor appears, and why only that one? Use the factorizations of $210$ and $222$.

6. ◦ List the $5$-[smooth](/smooth-number/) integers from $1$ to $30$. How many are there?

7. ◦ Use the [Dickman function](/dickman-function/) to estimate the fraction of integers up to $10^6$ that are $1000$-smooth. The true fraction is about $0.344$; why is the estimate low?

8. ◦ For $N = 4189$, the values $x^2 - N$ for $x = 67, 69, 74, 83$ are $300 = 2^2 \cdot 3 \cdot 5^2$, $572 = 2^2 \cdot 11 \cdot 13$, $1287 = 3^2 \cdot 11 \cdot 13$ and $2700 = 2^2 \cdot 3^3 \cdot 5^2$. Combine these [relations](/relation-collection/) into two different [congruences of squares](/congruence-of-squares/), and split $N$ with each.

9. ◦ Ignoring the $o(1)$ terms, compare $\ln L_N[1/2, 1]$, for the [quadratic sieve](/quadratic-sieve/), with $\ln L_N[1/3, (64/9)^{1/3}]$, for the [number field sieve](/general-number-field-sieve/), at $N = 10^{100}$ and $N = 10^{200}$. Near what size do they cross?

10. • Let $N = ab$ with odd $a < b$. Prove that if $b - a < 2\sqrt 2\, N^{1/4}$, Fermat's method succeeds at its first trial value $x = \lceil \sqrt N \rceil$. Why does this matter for choosing RSA primes?

11. • Run Pollard's $p - 1$ method with the base $2$ on $N = 69841 = 211 \cdot 331$, first with $B = 5$ ($M = 60$) and then with $B = 7$ ($M = 420$). Explain both results, given that $330 = 2 \cdot 3 \cdot 5 \cdot 11$.

12. • An RSA modulus $N = pq$ leaks $\varphi(N)$. Show how to recover $p$ and $q$ with one square root, and do it for $N = 10403$, $\varphi(N) = 10200$.

13. • For the quadratic sieve on $N = 4189$ with the primes up to $19$, which primes go into the [factor base](/factor-base/)? For each, give the residues of $x$ modulo $p$ at which $p$ divides $x^2 - N$.

14. • Run the block scan of the [Pollard-Strassen algorithm](/pollard-strassen/) on $N = 10403$, with $B = \lceil N^{1/4} \rceil$. Which block first has a product that shares a factor with $N$, what is that gcd, and how does the algorithm still find the least prime factor?

15. • The [special number field sieve](/special-number-field-sieve/) needs a polynomial $f$ with small coefficients and an integer $m$ with $f(m) \equiv 0 \pmod N$. Find a monic $f$ of degree $5$ and such an $m$ for $N = 2^{101} + 1$.

16. • Prove that $K + 1$ relations over a factor base of $K$ primes always contain a nonempty subset whose right sides multiply to a perfect square. Why does the method still collect a few more than $K + 1$ in practice?

17. • A 64-bit $N = pq$ has two primes near $2^{32}$. Estimate the expected number of steps of Pollard's rho, taking $\sqrt{\pi p/2}$ for the expected number of distinct values before a repeat modulo $p$. Compare with trial division by odd numbers.

18. • Let $N = 1524599 = 1009 \cdot 1511$. How many trial values does plain Fermat's method need? Show that Fermat's method on $24N$ succeeds at its first trial value, and use the result to split $N$. This is the idea of [Lehman's method](/lehman-factorization/).

19. ★ Every integer $n \le x$ has at most one prime factor above $\sqrt x$. Use this and Mertens' theorem, $\sum_{p \le y} 1/p = \ln \ln y + M + o(1)$, to prove that the fraction of integers up to $x$ that are not $\sqrt x$-smooth tends to $\ln 2$. Compare with $\rho(2)$.

20. ★ The congruence of squares method cannot split a prime power $p^k$. Give an algorithm that decides in time polynomial in $\lg N$ whether $N = b^k$ for some integers $b$ and $k \ge 2$, and bound its number of multiplications.

21. ★ Let $M = \operatorname{lcm}(1, 2, \ldots, B)$. Prove that $\ln M = \sum_{p^k \le B} \ln p$, and use the prime number theorem in the form $\sum_{p^k \le B} \ln p \sim B$ to show that the first stage of the $p - 1$ method needs about $B \lg e \approx 1.44 B$ squarings.

22. ★ Let $N = pq$ with primes $p < q$. Prove that for integers $u, v \ge 1$, $4uvN = (vp + uq)^2 - (vp - uq)^2$, and deduce that Fermat's method on $4uvN$ succeeds quickly when $q/p$ is close to $v/u$. Check it on $N = 1009 \cdot 1511$ with $u = 2$ and $v = 3$.
