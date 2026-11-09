1. ◦ Order the monomials $x^2z$, $xy^2$, $y^3$ and $xyz$ with $x > y > z$ in lex, in grlex and in grevlex. Which pairs change places between the orders? See [monomial ordering](/monomial-ordering/).

2. ◦ Draw the [expression tree](/expression-tree/) and the [expression DAG](/expression-dag/) of $(x + y)(x + y) + (x + y)$ and count the nodes of each. Then let $e_0 = x$ and $e_{k+1} = e_k \cdot e_k$, and give the node counts of $e_k$ as a tree and as a DAG.

3. ◦ How many monomials of total degree at most $10$ are there in $10$ variables? A polynomial in these variables has degree at most $10$ in each variable and $50$ terms. Compare the number of values needed by dense interpolation, by [Zippel's method](/zippel-sparse-interpolation/), and by [Ben-Or and Tiwari](/ben-or-tiwari-algorithm/) with the term bound $T = 50$.

4. ◦ In grevlex with $x > y > z$, compute the [S-polynomial](/s-polynomial/) of $f = x^2y + z$ and $g = xy^3 - y$. Does it reduce to zero modulo $\{f, g\}$? What does that say about $\{f, g\}$?

5. ◦ Divide $f = x^2y^2 + xy + x$ by $(xy + y, \; x - 1)$ in lex with $x > y$ using the [multivariate division algorithm](/multivariate-division-algorithm/). Give the quotients and the remainder. Then divide by the same two polynomials in the other order. Find the reduced Gröbner basis of the ideal they generate over $\mathbb{Q}$, and the normal form of $f$.

6. ◦ Write the [Sylvester matrix](/sylvester-matrix/) of $f = x^2 - x + 3$ and $g = 2x + 1$ and compute its determinant. Check the answer against $\operatorname{lc}(g)^{\deg f} f(-1/2)$.

7. ◦ Run the [primitive PRS](/primitive-prs/) on $f = x^3 + x^2 - x - 1$ and $g = 3x^2 + 2x - 1$. Give each pseudo-remainder, its primitive part, and the gcd.

8. ◦ Compute $\gcd(x^2 - 1, \; x^2 + 2x + 1)$ by the [heuristic gcd](/heuristic-gcd/) with the evaluation point $\xi = 10$. Check that $\xi$ is large enough for the method.

9. ◦ A [modular method](/modular-methods/) for the determinant of an integer matrix knows that $|\det A| \le 30$, and finds $\det A \equiv 1 \pmod 7$ and $\det A \equiv 2 \pmod{11}$. Find $\det A$. Would the prime $7$ alone have been enough?

10. ◦ Compute $\int dx/(x^3 + x^2)$ by [partial fractions](/partial-fraction-decomposition/). Which part of the answer is rational and which is logarithmic?

11. ◦ Build the [Macaulay matrix](/macaulay-matrix/) of $f_1 = x^2 + y$ and $f_2 = xy - 1$ in degree $D = 3$, with rows $m f_i$ for monomials $m$ of degree at most $1$. Give its size and rank. Show that its row space contains a polynomial whose leading monomial in grevlex is divisible by neither $x^2$ nor $xy$.

12. ◦ Which of these are [hypergeometric terms](/hypergeometric-term/) in $k$: $\binom{2k}{k}$, $k^2 3^k$, $1/(2k)!$, $3^k + 2^k$? Give the term ratio where there is one.

13. ◦ Show that $x^2 + y$, $x - 1$ and $y - 1$ have no common zero over $\mathbb{C}$. Write $1$ as a combination of them, as the [Nullstellensatz](/hilbert-nullstellensatz/) promises.

14. • Run [Buchberger's algorithm](/buchberger-algorithm/) on $x^2 + y - 1$ and $xy - x$ in lex with $x > y$. Which pairs can the product criterion skip? Give the reduced Gröbner basis, the common zeros, and the dimension of the quotient ring as a vector space.

15. • Solve $x^2 + y^2 = 5$, $xy = 2$ by computing a lex Gröbner basis with $x > y$ and using the [elimination theorem](/elimination-theorem/).

16. • Show that $x^2 - y$ and $y^2 - x$ already form a grevlex Gröbner basis. List the standard monomials. Then run [FGLM](/fglm-algorithm/) by hand to get the lex basis with $x > y$.

17. • Run Buchberger's algorithm on $x^3 - 1$ and $x^2 - 1$ in $\mathbb{Q}[x]$. Then show that for any two polynomials in one variable it returns the monic gcd, and explain why each S-polynomial step is a step of Euclid's algorithm.

18. • Factor $x^4 + 4$ over $\mathbb{Z}$ by [Kronecker's method](/kronecker-factorization-method/) with the points $0, 1, -1$. At most how many triples of divisors must be tried for a quadratic factor?

19. • Let $f, g \in \mathbb{Z}[x]$ and let $p$ be a prime that divides neither leading coefficient. Prove that $\deg \gcd(f \bmod p, \, g \bmod p) \ge \deg \gcd(f, g)$. Give an example where the inequality is strict.

20. • Compute $\int dx/(x^2 + x - 1)$ with the [Rothstein-Trager](/rothstein-trager/) resultant. Give $R(z)$, its roots, and the logarithmic part, and check the answer by differentiating.

21. • Use the [Horowitz-Ostrogradsky](/horowitz-ostrogradsky/) method on $\int dx/(x^2 + 1)^2$. Give $D^-$, $D^*$, the polynomials $B$ and $C$, and the integral.

22. • Find an antidifference of $k\,2^k$ by trying $(ak + b)2^k$, and use it to sum $\sum_{k=0}^{n-1} k\,2^k$. Why does [Gosper's algorithm](/gosper-algorithm/) look for a solution of this shape?

23. • For $I = \langle x^2y, xy^2 \rangle \subseteq K[x, y]$, give the Hilbert function and the [Hilbert series](/hilbert-series/). Write $I$ as an intersection of primary ideals and say which component is embedded.

24. • Describe the [cylindrical algebraic decomposition](/cylindrical-algebraic-decomposition/) of $\mathbb{R}^2$ for $y^2 - x^3 + x$, projecting onto $x$. Count the cells, the cells on the curve, and the two-dimensional cells.

25. • A polynomial $f \in \mathbb{Z}[x, y]$ has at most $2$ terms. Its values at $(2^i, 3^i)$ for $i = 0, 1, 2, 3$ are $8, 171, 4077, 103599$. Recover $f$ with the Ben-Or–Tiwari algorithm.

26. ★ Prove that every monomial ideal in $K[x, y]$ has a unique minimal set of monomial generators $x^{a_1}y^{b_1}, \dots, x^{a_r}y^{b_r}$ with $a_1 < \dots < a_r$ and $b_1 > \dots > b_r$. When $a_1 = 0$ and $b_r = 0$, show that the number of monomials outside the ideal is $\sum_{i=1}^{r-1} (a_{i+1} - a_i)\, b_i$.

27. ★ Let $I \subseteq K[x_1, \dots, x_n]$ have a quotient of finite dimension. Prove that the reduced lex Gröbner basis with $x_1 > \dots > x_n$ contains exactly one polynomial in $K[x_n]$ alone.

28. ★ Let $I$ be generated by $x_i^2 - x_{i+1}$ for $1 \le i < n$ and $x_n^2 - x_1$. Show that these generators are a grevlex Gröbner basis, and that the lex basis contains a polynomial in $x_n$ of degree $2^n$. What does this say about the cost of going from grevlex to lex?

29. ★ Prove that $x^4 + 1$ is irreducible over $\mathbb{Z}$ but factors modulo every prime. What does this mean for [polynomial factorization](/polynomial-factorization/) by factoring modulo a prime and then combining the factors?

30. ★ By [Liouville's theorem](/liouville-theorem/), for $f, g \in \mathbb{C}(x)$ with $g$ not constant, $\int f e^g$ is elementary exactly when $b' + g'b = f$ has a solution $b \in \mathbb{C}(x)$. Use this to show that $\int e^x (1/x - 1/x^2)\,dx$ is elementary and $\int e^x/x^2\,dx$ is not.
