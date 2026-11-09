1. With $n - k = 7$, the steps multiply by $8, 9, 10, 11, 12$ and divide by $1, 2, 3, 4, 5$, so $r$ runs $8, 36, 120, 330, 792$, and $\binom{12}{5} = 792$. Pascal's triangle uses $nk - k(k-1)/2 = 60 - 10 = 50$ additions.

2. All paths: $\binom{8}{3} = 56$. By reflection, those that go above the diagonal number $\binom{8}{2} = 28$, so $56 - 28 = 28$ stay on or below it. The paths through $(2, 2)$ number $\binom{4}{2}\binom{4}{1} = 24$, so 32 avoid it.

3. Add $\lfloor 1000/d \rfloor$ with sign $(-1)^r$ over the 16 products $d$ of $r$ distinct primes from $\{2, 3, 5, 7\}$. The answer is 228.

7. Removing the leaf 1 leaves a tree on $\{2, \ldots, 6\}$, one of $5^3 = 125$, and the leaf can hang from any of its 5 vertices. So $625$ trees, which is $625/1296 \approx 0.48$ of the $6^4$ trees.

10. The triples with $d$ dividing all three number $\lfloor 10/d \rfloor^3$. With $\mu$ nonzero at $d = 1, 2, 3, 5, 6, 7, 10$, the sum is $1000 - 125 - 27 - 8 + 1 - 1 + 1 = 841$.

13. Each clause has two literals, so $w_i = 2^{3-2} = 2$ and $W = 6$. The satisfying assignments are those with at least two ones: $110, 101, 011, 111$. The assignment $111$ lies in all three sets and has one first pair, the others lie in one set each, so 4 of the 6 pairs succeed and $p = 2/3$. With $m = 3$, $N = \lceil 9\ln 40/0.01 \rceil = 3320$.

14. The residues are $1, 1, 2, 2, 0, 1, 2, 1, 0, 0, 1, 0, 1, 1, 1, 2$ for $n = 0, \ldots, 15$. Since $B_{13}, B_{14}, B_{15}$ agree with $B_0, B_1, B_2$ modulo 3 and the congruence fixes each term from three earlier ones, the period is 13; no shorter period fits the list. So $B_{100} \equiv B_9 \equiv 0$, since $100 = 7 \cdot 13 + 9$.

19. The divisors of 12 are $2^a 3^b$ with $0 \le a \le 2$ and $0 \le b \le 1$, so the order is the product of a chain of 3 and a chain of 2. A down-set is fixed by how far it reaches in each of the two rows, a weakly decreasing pair, which gives 10 down-sets. The dynamic program, which adds over the maximal elements of each down-set, ends with 5 linear extensions. Reading the elements of a linear extension in order and writing each into the cell $(b, a)$ of a $2 \times 3$ rectangle gives a standard Young tableau of shape $(3, 3)$, and the hook length formula gives $6!/144 = 5$.

20. There are $\binom{11}{4} = 330$ paths. Since $\gcd(7, 4) = 1$, the 11 cyclic shifts of each path are distinct, and exactly one of them stays below the line. So the answer is $330/11 = 30$.

22. The identity has cycle type $x_1^9$, the two quarter turns $x_1 x_4^2$, the half turn $x_1 x_2^4$, and each of the four reflections $x_1^3 x_2^3$. Put $x_k = 1 + y^k$ and take the coefficient of $y^3$: $84$, $0$, $4$ and $10$ for the four types, so $(84 + 0 + 4 + 4 \cdot 10)/8 = 16$.

23. The path counts are $\binom{6}{3} = 20$ from $(0, 2)$ to $(3, 5)$ and from $(2, 0)$ to $(5, 3)$, and $\binom{6}{1} = 6$ for the two crossed pairs. The determinant is $20 \cdot 20 - 6 \cdot 6 = 364$. A path from $(0, 2)$ to $(5, 3)$ and a path from $(2, 0)$ to $(3, 5)$ must cross, and monotone lattice paths that cross share a vertex, so the crossed pairing contributes nothing to the non-intersecting count.

24. Unsigned, $|\det B| = 1$, but the grid has 5 perfect matchings. Read an entry $+1$ as an edge oriented from black to white and $-1$ as the reverse. Around a square face the walk meets black and white vertices in turn, so with all entries $+1$ exactly 2 of its 4 edges are clockwise. Each of the three faces contains exactly one of the two negated edges, which makes its count odd, as Kasteleyn's condition asks. The signed determinant is then $\pm 5$.

25. The exponential generating function is $\exp\bigl(-\ln(1 - z) - z - z^2/2\bigr) = e^{-z - z^2/2}/(1 - z)$, and its coefficients times $n!$ are $1, 0, 0, 2, 6, 24, 160, 1140, 8988$. For a recurrence, delete $n$ from its cycle: a cycle of length at least 4 leaves a valid permutation of $n - 1$ elements, and a 3-cycle leaves one of $n - 3$. So $a_n = (n-1)a_{n-1} + (n-1)(n-2)a_{n-3}$, and $a_8 = 7 \cdot 1140 + 42 \cdot 24 = 8988$.

26. A rotation by $s$ places has $\gcd(s, 12)$ cycles of length $d = 12/\gcd(s, 12)$, and it fixes a colouring with 4 black beads only when $d$ divides 4. Exactly $\varphi(d)$ rotations have cycle length $d$. So the count is $\frac{1}{12}\bigl(\binom{12}{4} + \varphi(2)\binom{6}{2} + \varphi(4)\binom{3}{1}\bigr) = \frac{495 + 15 + 6}{12} = 43$.
