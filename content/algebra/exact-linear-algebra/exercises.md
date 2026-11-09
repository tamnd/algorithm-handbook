1. ◦ Bring the matrix with rows $(1, 2, 3)$, $(2, 4, 6)$ and $(1, 0, 1)$ to [echelon form](/echelon-form/). What is its [rank](/rank/)? Give a basis of its [nullspace](/nullspace/) and check the [rank-nullity theorem](/rank-nullity-theorem/).

2. ◦ Compute the [determinant](/determinant/) of the matrix with rows $(2, 0, 1)$, $(1, 3, 0)$ and $(0, 1, 4)$ by [Laplace expansion](/laplace-expansion/) along the first row. How many of the $3! = 6$ terms of the permutation formula are nonzero?

3. ◦ Solve $3x + 2y = 7$, $x + 4y = 9$ by [Cramer's rule](/cramers-rule/).

4. ◦ Run [Gaussian elimination](/gaussian-elimination/) on the system $y + z = 5$, $x + y = 3$, $2x + y + z = 7$, with the unknowns in the order $x, y, z$. Where must the rows be swapped? Give the solution, and the determinant of the coefficient matrix as [determinant by Gaussian elimination](/determinant-gaussian-elimination/) computes it, with the sign of the swap.

5. ◦ Find the [LU decomposition](/lu-decomposition/) of the matrix with rows $(2, 1, 1)$, $(4, 3, 3)$ and $(8, 7, 9)$, with no row swaps. Use it to read off the determinant, and to solve $Ax = (4, 10, 24)$ by one forward and one back substitution.

6. ◦ Invert the matrix with rows $(3, 1)$ and $(2, 5)$ modulo $7$ by [Gauss-Jordan elimination](/gauss-jordan-elimination/) on $[A \mid I]$, and check the answer by multiplying.

7. ◦ Solve over the field of two elements: $x_1 + x_2 = 1$, $x_2 + x_3 = 0$, $x_1 + x_3 = 1$. List all the solutions, as a [system modulo 2](/linear-system-modulo-2/) solver would report them: one particular solution and a nullspace basis.

8. ◦ Which of these integer matrices are [unimodular](/unimodular-matrix/): the matrix with rows $(2, 3)$, $(1, 2)$; the one with rows $(2, 4)$, $(1, 3)$; the one with rows $(1, 0, 0)$, $(5, 1, 0)$, $(7, -2, -1)$? Give the inverse of the first.

9. ◦ Give the [characteristic polynomial](/characteristic-polynomial/) and the [minimal polynomial](/matrix-minimal-polynomial/) of the matrix with rows $(2, 1, 0)$, $(0, 2, 0)$ and $(0, 0, 2)$.

10. • Let $A$ be the matrix with rows $(2, 1)$ and $(1, 1)$. Use the [Cayley-Hamilton theorem](/cayley-hamilton-theorem/) to write $A^{-1}$ as $aA + bI$, and to compute $A^5$ by reducing $x^5$ modulo the characteristic polynomial. Which numbers appear?

11. • Prove that $\operatorname{rank}(A^\top A) = \operatorname{rank} A$ for every real or rational matrix $A$. Give a $2 \times 1$ matrix over the field of two elements for which it fails.

12. • Let $M(n)$ be the number of multiplications that Laplace expansion along the first row makes on an $n \times n$ matrix, expanding down to $1 \times 1$ minors and counting the sign as free. Show that $M(n) = n(M(n-1) + 1)$ with $M(1) = 0$, that $M(n) = \sum_{k=1}^{n-1} n!/k!$, and compute $M(10)$. Compare it with the cost of elimination in the summary table.

13. • Run the [Bareiss algorithm](/bareiss-algorithm/) on the matrix with rows $(3, 1, 2)$, $(1, 4, 1)$ and $(2, 1, 5)$. Show the matrix after each step, check that every entry after the first step is a $2 \times 2$ minor of the input, and read off the determinant.

14. • Using the operation counts of [Gauss-Jordan elimination](/gauss-jordan-elimination/) and of Gaussian elimination, find the limit, as $n$ grows, of the ratio of their costs when each solves one $n \times n$ system with one right-hand side. Back substitution costs $O(n^2)$.

15. • Compute the determinant of the matrix with rows $(2, 7, 1)$, $(8, 2, 8)$ and $(1, 8, 2)$ as the [multimodular determinant](/multimodular-determinant/) does. First use the row form of the [Hadamard bound](/hadamard-bound/) to show that the primes $11$, $13$ and $17$ are enough, then compute the determinant modulo each and combine the residues with the [Chinese remainder theorem](/chinese-remainder-theorem/), taking the symmetric residue.

16. • A $100 \times 100$ integer matrix has entries with $|a_{ij}| < 2^{20}$. Bound $\log_2$ of its Hadamard bound $H$. If the multimodular method uses primes larger than $2^{30}$ and needs the product of the primes to exceed $2H$, how many primes does it need?

17. • Find the [Hermite normal form](/hermite-normal-form/) of the lattice spanned by the rows $(3, 5)$ and $(7, 4)$: the upper triangular basis with positive diagonal and the entry above the second pivot reduced to $[0, 23)$. Give integer combinations of the rows that produce each row of the form.

18. • Find the [Smith normal form](/smith-normal-form/) of the matrix with rows $(2, 4)$ and $(6, 8)$. What is the abelian group $\mathbb{Z}^2 / L$, where $L$ is the lattice spanned by the rows?

19. • Consider the [linear Diophantine system](/linear-diophantine-system/) $x + 2y + 3z = 6$, $4x + 5y + 6z = c$. For $c = 15$, find all integer solutions. For $c = 16$, show that rational solutions exist but integer ones do not, and give a rational vector $y$ with $yA$ integral and $y \cdot (6, 16)$ not an integer.

20. • The matrix with rows $(2, 1, 0)$, $(1, 3, 1)$ and $(0, 1, 4)$ has determinant $18$. For which primes $p$ is its rank over $\mathbb{Z}/p\mathbb{Z}$ less than $3$, and what is the rank then? Use [Gaussian elimination for modular systems](/gaussian-elimination-modular/).

21. • Run the [Faddeev-LeVerrier algorithm](/faddeev-leverrier-algorithm/) on the matrix with rows $(1, 2, 0)$, $(0, 1, 3)$ and $(1, 0, 1)$. Give $M_1, M_2, M_3$, the characteristic polynomial, the determinant and the inverse.

22. • Over the field of two elements, let $A$ have rows $(0, 1)$ and $(1, 1)$, and let $u = b = e_1$. Compute the first five terms of the sequence $u^\top A^i b$, find its minimal polynomial as [Berlekamp-Massey](/berlekamp-massey/) would, and use it, as the [Wiedemann algorithm](/wiedemann-algorithm/) does, to solve $Ax = b$.

23. • Run LEVINSON from the [Levinson-Durbin algorithm](/levinson-durbin-algorithm/) on the symmetric [Toeplitz system](/toeplitz-system-solving/) with $t_0 = 4$, $t_{\pm 1} = 2$, $t_{\pm 2} = 1$ and $c = (5, 4, 5)$. Give $f$, $g$ and $x$ after each step. Why are $\varepsilon_f$ and $\varepsilon_g$ zero at $k = 2$?

24. ★ Show that the product $d_1 d_2 \cdots d_k$ of the first $k$ invariant factors of an integer matrix is the gcd of its $k \times k$ minors. Use this to find the Smith normal form of the matrix with rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 10)$, and the group $\mathbb{Z}^3 / L$ for its row lattice $L$.

25. ★ To compute the rank of the $100 \times 100$ matrix of exercise 16 over $\mathbb{Q}$, a [rank computation](/rank-computation/) picks a prime $p > 2^{30}$ at random and computes the rank modulo $p$. Show that the rank modulo $p$ is never larger than the rank over $\mathbb{Q}$, and that at most $77$ primes larger than $2^{30}$ make it smaller.

26. ★ In [Dixon's p-adic lifting](/dixon-p-adic-lifting/), each coordinate of the solution of a nonsingular integer system $Ax = b$ is a fraction $u/v$ with $|u| \le N$ and $0 < v \le D$. Derive such $N$ and $D$ from Cramer's rule and the Hadamard bound. Then show that two different fractions with these bounds and denominators prime to $p$ cannot be congruent modulo $p^k$ once $p^k > 2ND$.

27. ★ Let $A$ be a nonsingular $n \times n$ integer matrix with row lattice $L$, and $H$ its Hermite normal form. Prove that the product of the diagonal entries of $H$ is $|\det A|$, and that $|\det A| \cdot \mathbb{Z}^n \subseteq L$. Explain why the second fact lets an HNF algorithm work modulo $|\det A|$.

28. ★ *Division-free elimination* replaces $a_{ij}$ by $a_{kk} a_{ij} - a_{ik} a_{kj}$ at step $k$ and never divides. Let $q_j$ be the pivot of the Bareiss algorithm at step $j$, the leading $j \times j$ minor of $A$. Prove that after step $k$ every entry of the division-free matrix equals the Bareiss entry in the same place times $c_k = \prod_{j=1}^{k-1} q_j^{2^{k-1-j}}$. Conclude that the bit length of the entries can double at every step.
