1. All four have degree $3$, so lex and grlex agree: $x^2z > xy^2 > xyz > y^3$. Grevlex first prefers the smaller power of $z$, then the smaller power of $y$: $xy^2 > y^3 > x^2z > xyz$. So $y^3$ passes both $x^2z$ and $xyz$, and $xy^2$ passes $x^2z$.

4. $S = y^2 f - x g = y^2z + xy$, with leading term $y^2z$. Neither $x^2y$ nor $xy^3$ divides $y^2z$ or $xy$, so the remainder is $S$ itself. Since it is not zero, $\{f, g\}$ is not a Gröbner basis.

5. In the first order the quotients are $xy - y + 1$ and $1$, and the remainder is $y^2 - y + 1$. In the other order the remainder is $y^2 + y + 1$. The two differ, so the set is not a Gröbner basis. From $(xy + y) - y(x - 1) = 2y$ the ideal is $\langle x - 1, y \rangle$, the point $(1, 0)$, and the normal form of $f$ is $f(1, 0) = 1$.

7. The first pseudo-remainder uses the multiplier $3^2 = 9$ and is $-8x - 8$, with primitive part $x + 1$. Then $g(-1) = 0$, so the next pseudo-remainder is $0$, and both inputs are primitive. The gcd is $x + 1$.

9. The solution modulo $77$ is $57$, and the symmetric representative is $57 - 77 = -20$. It works because $77 > 2 \cdot 30$, so only one integer in $[-30, 30]$ has these residues. Modulo $7$ alone, any of $-27, -20, -13, -6, 1, 8, 15, 22, 29$ would fit.

12. $\binom{2k}{k}$ has ratio $2(2k + 1)/(k + 1)$, $k^2 3^k$ has ratio $3(k + 1)^2/k^2$, and $1/(2k)!$ has ratio $1/((2k + 1)(2k + 2))$. For $3^k + 2^k$ the ratio is $3 - 2^k/(3^k + 2^k)$. It is not constant, and it tends to $3$ exponentially fast, which no rational function of $k$ other than a constant does.

14. $S(f_1, f_2) = y f_1 - x f_2$ reduces to $y^2 - 2y + 1$. The pair of $f_1$ and this new polynomial has coprime leading terms $x^2$ and $y^2$, and $S(f_2, f_3) = f_2$ reduces to zero. The reduced basis is $\{x^2 + y - 1, \; xy - x, \; (y - 1)^2\}$. The only zero is $(0, 1)$, and the standard monomials $1, x, y$ give dimension $3$, so the point has multiplicity $3$.

16. The leading terms $x^2$ and $y^2$ are coprime, so the product criterion settles the one pair. The standard monomials are $1, x, y, xy$. Walking through $1, y, y^2, y^3, y^4$ in lex gives normal forms $1, y, x, xy, y$, so $y^4 - y$ is the first relation, and $x$ has normal form $x = y^2$. The lex basis is $\{x - y^2, \; y^4 - y\}$.

20. $R(z) = \operatorname{res}_x(x^2 + x - 1, \; 1 - z(2x + 1)) = 1 - 5z^2$, since $2\alpha + 1 = \pm\sqrt{5}$ at the roots $\alpha$. For $c = \pm 1/\sqrt{5}$ the gcd is $2x + 1 \mp \sqrt{5}$, up to a constant. The integral is $\frac{1}{\sqrt{5}} \log \frac{2x + 1 - \sqrt{5}}{2x + 1 + \sqrt{5}}$.

22. The ansatz gives $a = 1$ and $2a + b = 0$, so the antidifference is $(k - 2)2^k$ and the sum is $(n - 2)2^n + 2$. Gosper's algorithm reduces the problem to a polynomial solution of a linear recurrence. Here the term ratio is $2(k + 1)/k$, and the polynomial part of the antidifference has degree $1$.

25. The values satisfy $v_{i+2} = 39 v_{i+1} - 324 v_i$, and $z^2 - 39z + 324$ has roots $12 = 2^2 \cdot 3$ and $27 = 3^3$. So the terms are $x^2y$ and $y^3$. The Vandermonde system $c_1 + c_2 = 8$, $12c_1 + 27c_2 = 171$ gives $f = 3x^2y + 5y^3$.

26. Key idea: among the monomials of the ideal with a given power of $x$, keep the one with the least power of $y$, and keep only those that no other monomial of the ideal divides. Dickson's lemma makes the list finite. Count the monomials outside column by column: for $a_i \le a < a_{i+1}$ the powers $y^0, \dots, y^{b_i - 1}$ lie outside. For $\langle x^2, xy, y^2 \rangle$ the sum is $1 \cdot 2 + 1 \cdot 1 = 3$.

27. Key idea: the powers $1, x_n, x_n^2, \dots$ are linearly dependent modulo $I$, so $I \cap K[x_n] \ne 0$. By the elimination theorem the basis elements in $K[x_n]$ form a Gröbner basis of this principal ideal. Their leading terms are powers of $x_n$, and in a reduced basis no leading term divides another, so there is exactly one.

28. Key idea: the leading terms $x_1^2, \dots, x_n^2$ are pairwise coprime, so every pair passes the product criterion. The zeros are $x_i = t^{2^{i-1}}$ with $t^{2^n} = t$, which gives $2^n$ distinct points, as many as the $2^n$ square-free standard monomials. Since $\gcd(2^{n-1}, 2^n - 1) = 1$, the value of $x_n$ is different at every zero. So the eliminant is $x_n^{2^n} - x_n$, and lex output can be exponentially larger than grevlex output.

29. Key idea: the roots are the primitive eighth roots of unity, and $x^4 + 1 = \Phi_8$ is irreducible. Modulo $2$ it is $(x + 1)^4$. For odd $p$, $8$ divides $p^2 - 1$, so $\mathbb{F}_{p^2}^\times$ contains the roots, and every irreducible factor modulo $p$ has degree at most $2$. Factors found modulo $p$ must then be combined, and the number of combinations can grow exponentially.

30. Key idea: for $f = 1/x - 1/x^2$, $b = 1/x$ works, and the integral is $e^x/x$. For $f = 1/x^2$, a pole of $b$ of order $e$ gives a pole of $b'$ of order $e + 1$ that nothing cancels. So $b$ has at most a simple pole at $0$: $b = c/x + p$ with $p$ a polynomial. Matching $x^{-2}$ gives $c = -1$, which leaves a term $-1/x$ that $p' + p$ cannot cancel.
