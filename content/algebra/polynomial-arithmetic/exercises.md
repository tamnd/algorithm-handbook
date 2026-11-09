1. ◦ Evaluate $f = 2x^4 - 3x^3 + x - 5$ at $x = 2$ by [Horner's rule](/horner-rule/). List the running values, and read off the quotient of $f$ by $x - 2$. How many multiplications and additions did you use?

2. ◦ Multiply $(2 + 3x)(5 - x)$ with Karatsuba's three products $p_0 = a_0 b_0$, $p_2 = a_1 b_1$ and $p_1 = (a_0 + a_1)(b_0 + b_1)$. Then count the coefficient multiplications and additions that the school method of [polynomial multiplication](/polynomial-multiplication/) uses for two polynomials with three coefficients each.

3. ◦ Divide $f = x^4 + 3x^3 - 2x + 1$ by $g = x^2 + x - 1$ over $\mathbb{Q}$ by [long division](/polynomial-long-division/). Give the quotient and the remainder, and check that $f = qg + r$.

4. ◦ Without dividing, find the remainder of $x^{100} - 3x + 2$ when divided by $x + 1$, by $x - 1$ and by $x^2 - 1$. Which of the three divides it?

5. ◦ The roots of $x^3 - 6x^2 + 11x - 6$ are $r_1, r_2, r_3$. Use [Vieta's formulas](/vieta-formulas/), without finding the roots, to compute $r_1 + r_2 + r_3$, $r_1 r_2 r_3$, $r_1^2 + r_2^2 + r_3^2$ and $1/r_1 + 1/r_2 + 1/r_3$.

6. ◦ What does [Descartes' rule of signs](/descartes-rule-of-signs/) say about the number of positive roots and of negative roots of $f = x^4 - x^3 - 7x^2 + x + 6$? Check your answer by factoring $f$.

7. ◦ Decide which of these are irreducible over $\mathbb{Q}$: $x^4 + 10x + 5$ and $x^3 + 6x^2 + 12x + 8$. Then find the content and the primitive part of $6x^3 + 4x^2 - 10$, and factor it over $\mathbb{Z}$.

8. ◦ Compute $\gcd(f, f')$ for $f = x^3 - 3x + 2$ over $\mathbb{Q}$. Is $f$ [square-free](/square-free-polynomial/)? Give its square-free factorization $f = a_1 a_2^2$.

9. ◦ Use the [extended Euclidean algorithm](/polynomial-extended-euclidean-algorithm/) to find the inverse of $x + 1$ modulo $x^2 + 1$, first over $\mathbb{Q}$ and then over $\mathbb{F}_3$.

10. ◦ A polynomial of degree $7$ is evaluated by [Estrin's scheme](/estrin-scheme/). How many multiplications and additions does it use, and how long is its critical path, compared with Horner's rule? A polynomial of degree $15$ with scalar coefficients is evaluated at a square matrix: how many matrix products does Horner's rule use, and how many the [Paterson-Stockmeyer algorithm](/paterson-stockmeyer-algorithm/) with blocks of $4$ coefficients?

11. • Let $q$ be the quotient of $f$ by $x - u$ that Horner's rule produces. Prove that $f'(u) = q(u)$. Conclude that $f(u)$ and $f'(u)$ can be computed together with $4n - 2$ ring operations for $\deg f = n \ge 1$.

12. • Redo the division of $x^4 + 3x^3 - 2x + 1$ by $x^2 + x - 1$ in the manner of [fast polynomial division](/fast-polynomial-division/): reverse both polynomials, invert the reversed divisor modulo $x^3$, multiply, and reverse back.

13. • Compute the inverse of $f = (1 - x)^2 = 1 - 2x + x^2$ modulo $x^8$ by [Newton iteration](/newton-power-series-inversion/) $g \leftarrow g(2 - fg)$ from $g = 1$, at precisions $1, 2, 4, 8$. Show each iterate, and say what the coefficients are.

14. • Build the [subproduct tree](/subproduct-tree/) for the points $1, -1, 2, -2$, and evaluate $f = x^3 + 2x + 1$ at all four points by remainders down the tree, as in [fast multipoint evaluation](/fast-multipoint-evaluation/).

15. • The sequence $a_n = 2a_{n-1} + 3a_{n-2}$ has a generating function $P(x)/(1 - 2x - 3x^2)$. Do one step of the [Bostan-Mori algorithm](/bostan-mori-algorithm/) on the denominator, and conclude that $a_{n+4} = 10 a_{n+2} - 9 a_n$ for every such sequence. Check it on $a_0 = 0$, $a_1 = 1$.

16. • Prove that $\gcd(x^a - 1, x^b - 1) = x^{\gcd(a, b)} - 1$ over any field, by following the [polynomial Euclidean algorithm](/polynomial-euclidean-algorithm/). What is $\gcd(x^{12} - 1, x^{18} - 1)$? Use $x^n - 1$ and $x - 1$ to show that dividing two polynomials with two terms each can give a quotient with $n$ terms.

17. • Over $\mathbb{F}_p$, prove that $f' = 0$ exactly when $f = h^p$ for some polynomial $h$. Use this to explain why the test $\gcd(f, f') = 1$ fails for $f = x^3 - 1$ over $\mathbb{F}_3$, and factor that $f$.

18. • The polynomial $x^{16} - x$ over $\mathbb{F}_2$ is the product of all monic irreducible polynomials of degree $1$, $2$ and $4$. Use its degree to count the irreducible quartics over $\mathbb{F}_2$, and list them.

19. • Over $\mathbb{F}_2$, let $f = x^6 + x^5 + x^4 + x^3 + x^2 + x + 1$. Show that $f$ divides $x^{64} - x$ and that $\gcd(f, x^4 - x) = 1$, yet $f$ is reducible. Which check of [Rabin's test](/rabin-irreducibility-test/) rejects $f$, and why is it needed? (Hint: $(x + 1) f = x^7 + 1$.)

20. • Run [distinct-degree factorization](/distinct-degree-factorization/) by hand on $f = x^5 + x^4 + 1$ over $\mathbb{F}_2$, which is square-free. Give the parts $g_1$, $g_2$, $g_3$.

21. • Let $f = x^2 + 1$. Write down the Berlekamp matrix $Q$ of $v \mapsto v^p \bmod f$ in the basis $1, x$ for $p = 3$ and for $p = 5$, and find the dimension of the null space of $Q - I$ in each case. What does [Berlekamp's algorithm](/berlekamp-factorization/) conclude?

22. • Modulo $7$, $x^2 - 2 \equiv (x - 3)(x + 3)$. Lift this factorization to one modulo $49$, as [Hensel lifting](/hensel-lifting/) does, and check it.

23. • Compute the [Sturm sequence](/sturm-sequence/) of $f = x^3 - 2x - 1$. Use [Sturm's theorem](/sturm-theorem/) to find the number of real roots of $f$, and the number in $(0, 2]$. Check against the factorization $f = (x + 1)(x^2 - x - 1)$.

24. ★ Prove that over $\mathbb{F}_q$, $x^{q^n} - x$ is the product of all monic irreducible polynomials whose degree divides $n$. Deduce that the number $N_n$ of monic irreducible polynomials of degree $n$ satisfies $\sum_{d \mid n} d N_d = q^n$, give a formula for $N_n$, and compute $N_6$ for $q = 2$.

25. ★ Let $h = (x - r_1)(x - r_2)$ over $\mathbb{F}_p$ with $p$ odd and $r_1 \ne r_2$, and run one pass of lines L5 to L9 of [equal-degree factorization](/equal-degree-factorization/) with $d = 1$. Show that the pass splits $h$ with probability exactly $(p + 3)/(2p)$. What is it for $p = 7$?

26. ★ Using the definition of the [discriminant](/discriminant/) through the [resultant](/resultant/), prove that $\operatorname{disc}(x^n + a) = (-1)^{n(n-1)/2} n^n a^{n-1}$ over $\mathbb{Q}$, for $n \ge 2$. Check it against $b^2 - 4ac$ for $n = 2$.

27. ★ For monic $g$ and $h$ over a field, prove that $\operatorname{disc}(gh) = \operatorname{disc}(g) \operatorname{disc}(h) \operatorname{Res}(g, h)^2$. Start by showing that a monic $f$ with roots $\alpha_1, \ldots, \alpha_n$ has $\operatorname{disc}(f) = \prod_{i < j} (\alpha_i - \alpha_j)^2$. Check the formula on $g = x$, $h = x - 1$.

28. ★ Let $p$ be a prime and $a \in \mathbb{F}_p$ nonzero. Prove that $x^p - x - a$ is irreducible over $\mathbb{F}_p$. (If $\alpha$ is a root in an extension field, find the other roots, and look at the coefficient of $x^{d-1}$ in a monic factor of degree $d$.) Give an irreducible polynomial of degree $5$ over $\mathbb{F}_5$.
