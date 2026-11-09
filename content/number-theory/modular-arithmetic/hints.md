1. $3^{200} \equiv 9$. Fermat gives $3^{12} \equiv 1$ and $200 \equiv 8 \pmod{12}$; the order of $3$ is in fact $3$, since $3^3 = 27 \equiv 1$, and $200 \equiv 2 \pmod 3$. In binary $200 = 11001000_2$: seven squarings and two multiplications by $3$.

3. $\gcd(14, 100) = 2$ divides $30$, so there are two solutions. Divide by $2$: $7x \equiv 15 \pmod{50}$, and $7^{-1} \equiv 43 \pmod{50}$, so $x \equiv 45 \pmod{50}$. The solutions are $45$ and $95$.

6. The order of $2$ is $10$, so $2$ is a primitive root. The primitive roots are $2, 6, 7, 8$, the powers $2^k$ with $\gcd(k, 10) = 1$; there are $\varphi(10) = 4$.

8. $1000 = 2626_7$ and $300 = 606_7$, written with the high digit first as $(2, 6, 2, 6)$ and $(0, 6, 0, 6)$. The product is $\binom20 \binom66 \binom20 \binom66 = 1$.

10. The inverses are $6, 4, 9, 8$. Prefix products modulo $11$: $2, 6, 30 \equiv 8, 56 \equiv 1$. The full product is $1$, its own inverse.

11. $n' = 95$, $\tilde 5 = 640 \bmod 97 = 58$, $\tilde 7 = 23$. $T = 58 \cdot 23 = 1334$, $m = (T \bmod 128) \cdot n' \bmod 128 = 10$, and $(T + 10 \cdot 97)/128 = 18$, which is $35 \cdot 128 \bmod 97$.

13. $40 = 5 \cdot 2^3$, so $q = 5$, $s = 3$. Start with $M = 3$, $c = 3^5 \equiv 38$, $t = 5^5 \equiv 9$, $R = 5^3 \equiv 2$. The first pass finds that $t$ has order $4$ and gives $M = 2$, $c = 9$, $t = 40$, $R = 35$; the second gives $M = 1$, $c = 40$, $t = 1$, $R = 28$. And $28^2 = 784 \equiv 5 \pmod{41}$.

16. $x \equiv 21 \pmod{24}$. Two congruences $x \equiv a \pmod m$ and $x \equiv b \pmod n$ are compatible exactly when $\gcd(m, n) \mid a - b$, and then the solution is unique modulo $\operatorname{lcm}(m, n)$. In the second system $2 - 5$ is odd.

18. Eight: $1, 29, 34, 41, 64, 71, 76, 104$. Modulo each of $3, 5, 7$ the equation has the two roots $\pm 1$, and the theorem combines them in $2^3$ ways.

20. $\mu = 19$, and the smallest such $x$ is $13$ itself: $\lfloor 13 \cdot 19 / 256 \rfloor = 0$, so the estimate is $13$. The estimated quotient can be too small because $\mu$ is rounded down.

21. $2730 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 13$, and $p - 1$ divides $12$ for each of these primes. So $n^{13} \equiv n \pmod p$ for each, by Fermat's theorem in the form $n^p \equiv n$ applied repeatedly.

22. Induction on $k$: $a^2 \equiv 1 \pmod 8$ for odd $a$, and if $a^{2^{k-2}} = 1 + 2^k t$ then squaring gives $1 + 2^{k+1} t + 2^{2k} t^2$. So every order divides $2^{k-2} < \varphi(2^k) = 2^{k-1}$.

23. Pair each element with its inverse; only the elements with $x = x^{-1}$ remain. The elements of order dividing $2$ form a subgroup, a vector space over $\mathbb{F}_2$ of size $2^r$, and its product is the identity unless $r = 1$. Modulo a prime the group is cyclic, so $-1$ is the only element of order 2. Modulo $15$ the product is $1$.

24. For $a \ne 0$, $\left(\frac{a(a+1)}{p}\right) = \left(\frac{a^2(1 + a^{-1})}{p}\right) = \left(\frac{1 + a^{-1}}{p}\right)$. As $a$ runs over the nonzero residues, $1 + a^{-1}$ runs over all residues except $1$, and the symbols of all residues sum to $0$.

26. Pick a random $x$ and give $x^2 \bmod n$ to the box. It has four square roots $\pm x$, $\pm y$, and the box cannot know which $x$ you chose. With probability $1/2$ the answer $y$ is not $\pm x$, and then $\gcd(x - y, n)$ is $p$ or $q$.
