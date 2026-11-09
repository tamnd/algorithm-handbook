1. $M_1 = 10$, $M_2 = 4$, $M_3 = 6$, $M_4 = 3$, $M_5 = 2$, $M_6 = -5$, $M_7 = -9$. Then $C_{11} = M_1 + M_4 - M_5 + M_7 = 2$, $C_{12} = M_3 + M_5 = 8$, $C_{21} = M_2 + M_4 = 7$ and $C_{22} = M_1 - M_2 + M_3 + M_6 = 7$, which matches $AB = \begin{pmatrix} 2 & 8 \\ 7 & 7 \end{pmatrix}$.

3. For $k = 100 = 1100100_2$: $\lfloor \lg 100 \rfloor + \nu(100) - 1 = 6 + 3 - 1 = 8$. For $k = 63$: $5 + 6 - 1 = 10$. The chain $A^2, A^3, A^6, A^{12}, A^{24}, A^{48}, A^{60} = A^{48}A^{12}, A^{63} = A^{60}A^3$ uses 8.

4. The square has ones at $(0, 2)$, $(1, 3)$, $(2, 1)$ and $(3, 2)$: the pairs joined by a walk of exactly two edges.

5. Only one entry changes: $(0, 1)$ drops from 5 to $\min(0 + 5, 5 + 0, 1 + 2) = 3$, the path through vertex 2. A shortest path has at most $n - 1$ edges, so $\lceil \lg(n - 1) \rceil$ squarings are enough.

7. For $AB$, each of the $n$ nonzeros of column 0 of $A$ meets all $n$ nonzeros of row 0 of $B$: $f = n^2$, and $AB$ is full, with $n^2$ nonzeros. For $BA$, the only matches are $B_{0k}$ with $A_{k0}$: $f = n$, and $BA$ has one nonzero, at $(0, 0)$.

8. The scheme gives $\omega \le \log_3 r$, which is below $\lg 7$ when $r < 3^{\lg 7} \approx 21.85$. So $r \le 21$ is needed; Laderman's 23 is not enough.

9. Try $T(n) = a n^{\lg 7} + b n^2$. The $n^2$ terms give $b = \frac{7}{4} b + \frac{15}{4}$, so $b = -5$, and $T(1) = 1$ gives $a = 6$: $T(n) = 6n^{\lg 7} - 5n^2$.

12. With the matrix $\begin{pmatrix} 0 & 1 \\ 2 & 1 \end{pmatrix}$ acting on $(a_m, a_{m+1})$, the tenth power gives $a_{10} = 341$. The eigenvalues are $2$ and $-1$, and $a_m = (2^m - (-1)^m)/3$.

14. $\operatorname{tr}(A^3)$ counts closed walks of length 3. In a simple graph each one goes round a triangle, and each triangle gives 6 of them: 3 starting vertices times 2 directions.

17. A rank-one tensor flattens to a rank-one matrix, so the tensor rank is at least the rank of each flattening. The flattening along the first factor has rank $nm$, because every entry of $A$ is used by some entry of $AB$. For the inner product $\langle 1, n, 1 \rangle$ the bound is $n$.

21. Replace $A_{ik}$ by $k \cdot A_{ik}$ and multiply over the integers: an entry with a single witness gets exactly that witness. For many witnesses, keep each column of $A$ with probability $2^{-t}$ for $t = 0, 1, \ldots, \lg n$; an entry with $w$ witnesses has exactly one left with constant probability when $2^t \approx w$, and $O(\log n)$ repetitions catch every entry with high probability.

22. Cyclic shifts give schemes of rank $r$ for $\langle m, p, n \rangle$ and $\langle p, n, m \rangle$. The Kronecker product of the three is a scheme for $\langle N, N, N \rangle$ with $N = nmp$ and rank at most $r^3$, so $\omega \le \log_N r^3$.

23. Induction on $s$. Each step brings to $(i, j)$ the block of $A$ from $(i, j + 1)$ and the block of $B$ from $(i + 1, j)$, and both have inner index $(i + j + s) + 1$. As $s$ runs through $0, \ldots, q - 1$, $k$ runs through every residue modulo $q$ once.

24. The shift operator on sequences satisfies $\chi$, so if $x^k \equiv \sum_{i < d} c_i x^i \pmod{\chi}$ then $a_k = \sum_i c_i a_i$. Compute $x^k \bmod \chi$ by repeated squaring: $O(\log k)$ products of polynomials of degree below $d$, each $O(d^2)$ with its reduction.
