1. Subtract twice the first row from the second and the first row from the third; the echelon form has rows $(1, 2, 3)$, $(0, -2, -2)$, $(0, 0, 0)$. The rank is $2$, and the nullspace is spanned by $(-1, -1, 1)$. Rank plus nullity is $2 + 1 = 3$, the number of columns.

4. The first column has a zero on top, so the first two rows are swapped. Elimination then gives the diagonal $1, 1, 2$ and the solution $(x, y, z) = (1, 2, 3)$. One swap changes the sign, so the determinant is $-(1 \cdot 1 \cdot 2) = -2$.

5. $L$ has rows $(1, 0, 0)$, $(2, 1, 0)$, $(4, 3, 1)$ and $U$ has rows $(2, 1, 1)$, $(0, 1, 1)$, $(0, 0, 2)$, so $\det A = 4$. Forward substitution gives $y = (4, 2, 2)$, and back substitution gives $x = (1, 1, 1)$.

6. The determinant is $13 \equiv 6$, and $6^{-1} \equiv 6 \pmod 7$. The inverse has rows $(2, 1)$ and $(2, 4)$; the product with $A$ has rows $(8, 7)$ and $(14, 22)$, which is the identity modulo $7$.

10. The characteristic polynomial is $x^2 - 3x + 1$, so $A^{-1} = 3I - A$, with rows $(1, -1)$ and $(-1, 2)$. Modulo $x^2 - 3x + 1$, $x^5 \equiv 55x - 21$, so $A^5$ has rows $(89, 55)$ and $(55, 34)$: Fibonacci numbers.

12. Expanding an $n \times n$ determinant multiplies each of $n$ entries by a minor of order $n - 1$. Dividing the recurrence by $n!$ gives $M(n)/n! = M(n-1)/(n-1)! + 1/(n-1)!$, which sums to the formula. $M(10) = 6\,235\,300$, close to $(e - 1) \cdot 10!$, while elimination needs $625$ field operations of all kinds.

15. The squared row norms are $54$, $132$ and $69$, so $H = \sqrt{491\,832} \approx 701.3$, and $11 \cdot 13 \cdot 17 = 2431 > 2H$. The residues are $7$, $3$ and $5$; they combine to $2317$, whose symmetric residue is $2317 - 2431 = -114$.

16. Each row has norm less than $\sqrt{100} \cdot 2^{20}$, so $\log_2 H < 100 (20 + \log_2 10) \approx 2332.2$. The product of $k$ primes larger than $2^{30}$ exceeds $2^{30k}$, and $30k \ge 2333.2$ first holds at $k = 78$.

19. Subtract four times the first equation from the second: $-3y - 6z = c - 24$. For $c = 15$ this is $y + 2z = 3$, and the solutions are $(1, 1, 1) + t(1, -2, 1)$ for $t \in \mathbb{Z}$; the vector $(1, -2, 1)$ is primitive, so it spans the integer kernel. For $c = 16$, $y + 2z = 8/3$ has no integer solution; $y = (-4/3, 1/3)$ gives $yA = (0, -1, -2)$ and $y \cdot (6, 16) = -8/3$.

23. After the first step $f = (1/3, -1/6)$, $g = (-1/6, 1/3)$, $x = (1, 1/2)$ and $d = 3/4$. After the second, $f = (1/3, -1/6, 0)$, $g = (0, -1/6, 1/3)$ and $x = (1, 0, 1)$. Here $t_k = t_{k-1}/2$ for $k \ge 1$, so $\varepsilon_f$ is half the second entry of $T_2 f = e_1$, which is $0$.

24. Unimodular operations do not change the gcd of the $k \times k$ minors, by the Cauchy-Binet formula, and for a diagonal matrix in Smith form that gcd is $d_1 \cdots d_k$. For the given matrix the entries have gcd $1$, the $2 \times 2$ minors include $-3$ and $2$, so their gcd is $1$, and the determinant is $-3$. The Smith form is $\operatorname{diag}(1, 1, 3)$ and $\mathbb{Z}^3 / L \cong \mathbb{Z}/3\mathbb{Z}$.

25. A minor that is nonzero modulo $p$ is nonzero over $\mathbb{Z}$. Fix one nonzero $r \times r$ minor $m$, where $r$ is the rank over $\mathbb{Q}$; the rank drops only if $p$ divides $m$. By the Hadamard bound $|m| < 2^{2332.2}$, and $k$ distinct primes above $2^{30}$ dividing $m$ force $2^{30k} < |m|$.

26. Cramer's rule gives $x_j = \det A_j / \det A$. Bound $|\det A|$ by the product of the column norms, and $|\det A_j|$ by the same product with one column replaced by $\|b\|$; this is line L2 of DIXON. If $u/v \equiv u'/v' \pmod{p^k}$, then $p^k$ divides $uv' - u'v$, and $|uv' - u'v| \le 2ND < p^k$.

27. $H = UA$ with $\det U = \pm 1$, and $H$ is triangular with positive diagonal. For the second fact, write $d e_i = (d e_i A^{-1}) A$ with $d = |\det A|$; the row vector $d e_i A^{-1}$ is $\pm$ a row of the adjugate, so it is integral.

28. Induction on $k$. If the division-free entries after step $k - 1$ are $c_{k-1}$ times the Bareiss entries, the next division-free entry is $c_{k-1}^2$ times the Bareiss numerator, which is $q_{k-1}$ times the Bareiss entry. So $c_k = c_{k-1}^2 q_{k-1}$ with $c_1 = 1$, and the exponent of $q_j$ doubles at each later step.
