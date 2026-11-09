1. The running values are $2, 1, 2, 5, 5$, so $f(2) = 5$. The first four are the coefficients of the quotient $2x^3 + x^2 + 2x + 5$. Four multiplications and four additions.

2. $p_0 = 10$, $p_2 = -3$ and $p_1 = 5 \cdot 4 = 20$, so the middle coefficient is $p_1 - p_0 - p_2 = 13$ and the product is $10 + 13x - 3x^2$. The school method uses $9$ multiplications and $4$ additions.

3. $q = x^2 + 2x - 1$ and $r = x$. Indeed $(x^2 + 2x - 1)(x^2 + x - 1) = x^4 + 3x^3 - 3x + 1$, and adding $x$ gives $f$.

4. By the remainder theorem the first two remainders are $f(-1) = 6$ and $f(1) = 0$, so $x - 1$ divides $f$. The third is $ax + b$ with $a + b = 0$ and $-a + b = 6$, that is, $-3x + 3$.

6. Both $f(x)$ and $f(-x) = x^4 + x^3 - 7x^2 - x + 6$ have two sign changes, so $f$ has $0$ or $2$ positive roots and $0$ or $2$ negative roots. In fact $f = (x - 1)(x + 1)(x - 3)(x + 2)$, with two of each.

8. $f' = 3(x - 1)(x + 1)$ and $\gcd(f, f') = x - 1$, so $f$ is not square-free. $f = (x + 2)(x - 1)^2$, with $a_1 = x + 2$ and $a_2 = x - 1$.

10. Estrin's scheme uses $9$ multiplications and $7$ additions, with a critical path of $6$ operations; Horner's rule uses $7$ of each, $14$ operations in a chain. For the matrix, Horner's rule uses $15$ products (or $14$, if $a_{15} X$ is counted as scalar). Paterson-Stockmeyer with $k = 4$ computes $X^2, X^3, X^4$ and joins four blocks with three giant steps: $6$ products.

11. Write $f = (x - u) q + f(u)$ and differentiate: $f' = q + (x - u) q'$, so $f'(u) = q(u)$. Horner's rule gives $f(u)$ and $q$ with $2n$ operations, and evaluating $q$, of degree $n - 1$, takes $2n - 2$ more.

12. $\operatorname{rev}(f) = 1 + 3x - 2x^3 + x^4$ and $\operatorname{rev}(g) = 1 + x - x^2$, whose inverse modulo $x^3$ is $1 - x + 2x^2$. Then $\operatorname{rev}(q) \equiv (1 + 3x)(1 - x + 2x^2) \equiv 1 + 2x - x^2 \pmod{x^3}$, so $q = x^2 + 2x - 1$ and $r = f - qg = x$.

13. The iterates are $1$, $1 + 2x$, $1 + 2x + 3x^2 + 4x^3$ and $\sum_{k=0}^{7} (k + 1) x^k$. The coefficient of $x^k$ in $1/(1 - x)^2$ is $k + 1$.

15. $Q(x) Q(-x) = (1 - 3x^2)^2 - 4x^2 = 1 - 10x^2 + 9x^4$, so the new denominator is $1 - 10y + 9y^2$. The even-indexed and the odd-indexed terms each satisfy the recurrence it encodes, which is $a_{n+4} = 10 a_{n+2} - 9 a_n$. The sequence $0, 1, 2, 7, 20, 61, 182$ fits: $10 \cdot 20 - 9 \cdot 2 = 182$.

16. For $a > b$, $x^a - 1 = x^{a-b}(x^b - 1) + (x^{a-b} - 1)$, so the remainder of $x^a - 1$ by $x^b - 1$ is $x^{a \bmod b} - 1$. The polynomial algorithm then follows the integer one on the exponents, and $\gcd(x^{12} - 1, x^{18} - 1) = x^6 - 1$. The quotient $(x^n - 1)/(x - 1) = 1 + x + \cdots + x^{n-1}$ has $n$ terms.

17. $f' = \sum i a_i x^{i-1}$ is zero exactly when $a_i = 0$ for every $i$ not divisible by $p$, that is, $f = \sum_j a_{pj} x^{pj}$. Since $c^p = c$ in $\mathbb{F}_p$ and $(u + v)^p = u^p + v^p$, this is $(\sum_j a_{pj} x^j)^p$. Over $\mathbb{F}_3$, $f' = 3x^2 = 0$, so $\gcd(f, f') = f$; and $x^3 - 1 = (x - 1)^3$.

19. $f$ divides $x^7 - 1$, so $x^7 \equiv 1$ and $x^{64} = x^{63} x \equiv x \pmod f$. The gcd with $x^4 - x = x(x + 1)(x^2 + x + 1)$ is $1$, since $f(0) = f(1) = 1$ and $f \equiv 1 \pmod{x^2 + x + 1}$. For $n = 6$ Rabin's test also checks the prime $r = 2$: $x^8 \equiv x \pmod f$, so $\gcd(f, x^8 - x) = f \ne 1$. Without this check, a product of factors whose degrees divide $n$ would pass. In fact $f = (x^3 + x + 1)(x^3 + x^2 + 1)$.

21. For $p = 3$, $x^3 \equiv -x$, so $Q = \operatorname{diag}(1, -1)$ and $Q - I$ has a null space of dimension $1$: $x^2 + 1$ is irreducible over $\mathbb{F}_3$. For $p = 5$, $x^5 \equiv x$, so $Q = I$ and the dimension is $2$: two factors, $(x - 2)(x + 2)$.

23. The sequence is $x^3 - 2x - 1$, $3x^2 - 2$, $\tfrac43 x + 1$, $\tfrac{5}{16}$. The sign changes are $3$ at $-\infty$ and $0$ at $+\infty$, so there are three real roots, and $1$ at $0$ and $0$ at $2$, so one lies in $(0, 2]$. The roots are $-1$ and $(1 \pm \sqrt5)/2$, and only $(1 + \sqrt5)/2$ is positive.

24. If $g$ is monic irreducible of degree $d \mid n$, then $\mathbb{F}_q[x]/(g)$ is a field with $q^d$ elements, so $x^{q^d} \equiv x$ and hence $x^{q^n} \equiv x \pmod g$. Conversely, if $g \mid x^{q^n} - x$, every element of $\mathbb{F}_q[x]/(g)$ satisfies $y^{q^n} = y$, which forces $d \mid n$. The polynomial is square-free because its derivative is $-1$. Comparing degrees and applying Möbius inversion gives $N_n = \frac1n \sum_{d \mid n} \mu(d) q^{n/d}$, and $N_6 = (64 - 8 - 4 + 2)/6 = 9$.

25. By the Chinese remainder theorem, $a$ corresponds to the pair $(u, v) = (a(r_1), a(r_2))$, uniform over the $p^2 - p$ pairs with $u \ne v$, because $a$ is constant exactly when $u = v$. Line L6 splits $h$ when exactly one of $u, v$ is zero: $2(p - 1)$ pairs. Otherwise line L9 splits it when exactly one of $u, v$ is a square: $(p - 1)^2/2$ pairs. The total is $(p - 1)(p + 3)/2$ out of $p(p - 1)$, which is $(p + 3)/(2p)$, and $5/7$ for $p = 7$.

26. With $f' = n x^{n-1}$ and roots $\alpha_i$, $\operatorname{Res}(f, f') = \prod_i n \alpha_i^{n-1} = n^n (\prod_i \alpha_i)^{n-1} = n^n ((-1)^n a)^{n-1} = n^n a^{n-1}$, since $n(n - 1)$ is even. Multiply by $(-1)^{n(n-1)/2}$. For $n = 2$ this is $-4a$, which is $b^2 - 4ac$ for $x^2 + a$.

27. For monic $f$, $\operatorname{Res}(f, f') = \prod_i f'(\alpha_i) = \prod_i \prod_{j \ne i} (\alpha_i - \alpha_j)$. Pairing the factors for $(i, j)$ and $(j, i)$ gives $-(\alpha_i - \alpha_j)^2$ for each of the $n(n-1)/2$ pairs, and the sign cancels. The roots of $gh$ are those of $g$ and of $h$; the pairs within $g$, within $h$, and across give the three factors, the last being $\prod (\alpha_i - \beta_j)^2 = \operatorname{Res}(g, h)^2$. For $g = x$, $h = x - 1$: $1 = 1 \cdot 1 \cdot (-1)^2$.

28. If $\alpha$ is a root, so is $\alpha + c$ for every $c \in \mathbb{F}_p$, since $(\alpha + c)^p - (\alpha + c) = \alpha^p - \alpha$. So the roots are $\alpha + c$. A monic factor of degree $d$ with $0 < d < p$ has $-(d\alpha + s)$ as its coefficient of $x^{d-1}$, with $s \in \mathbb{F}_p$; $d$ is a unit, so $\alpha \in \mathbb{F}_p$, and then $\alpha^p - \alpha = 0 \ne a$. Example: $x^5 - x - 1$.
