## What to remember

- **Gaussian elimination answers almost every question.** Over any field it gives the rank, a nullspace basis, the determinant, the inverse and the solutions of a system, in about $2n^3/3$ field operations for an $n \times n$ matrix. The [determinant](/determinant/) formulas, [Laplace expansion](/laplace-expansion/) and [Cramer's rule](/cramers-rule/), are for proofs: expansion costs more than $n!$ multiplications.
- **The [rank-nullity theorem](/rank-nullity-theorem/)** says that rank plus nullity is the number of columns. Over a field with $q$ elements, a consistent system in $n$ unknowns of rank $r$ has exactly $q^{n-r}$ solutions.
- **Over a finite field, numbers never grow.** [Elimination modulo a prime](/gaussian-elimination-modular/) replaces division by a [modular inverse](/modular-inverse/). Over the field of two elements, [bitset elimination](/bitset-gaussian-elimination/) adds 64 entries with one XOR.
- **Over the rationals, the size of numbers is the cost.** The [Hadamard bound](/hadamard-bound/) bounds every minor in advance. The [Bareiss algorithm](/bareiss-algorithm/) keeps every entry a minor of the input by dividing exactly; the [multimodular determinant](/multimodular-determinant/) and [Dixon's lifting](/dixon-p-adic-lifting/) do the work modulo small primes and rebuild the answer at the end.
- **Over the integers, the operations are unimodular.** The [Hermite normal form](/hermite-normal-form/) is the integer echelon form of a lattice; the [Smith normal form](/smith-normal-form/) is diagonal, each entry dividing the next, and it decides [linear Diophantine systems](/linear-diophantine-system/). [Kannan and Bachem](/kannan-bachem-algorithm/) first computed them in polynomial time.
- **Every matrix satisfies its characteristic polynomial** ([Cayley-Hamilton](/cayley-hamilton-theorem/)), and the [minimal polynomial](/matrix-minimal-polynomial/) divides it. The [Berkowitz algorithm](/berkowitz-algorithm/) computes the characteristic polynomial with no division at all, so it works over any commutative ring.
- **Sparse matrices are touched only through products with vectors.** The [Wiedemann algorithm](/wiedemann-algorithm/) finds a minimal polynomial from a sequence of scalars with [Berlekamp-Massey](/berlekamp-massey/) and solves the system with $O(n)$ products; its block form and [block Lanczos](/block-lanczos-algorithm/) do the linear algebra of integer factoring.

## The main algorithms side by side

| Algorithm | Operations, worst case | Extra space | Over |
|---|---|---|---|
| [Gaussian elimination](/gaussian-elimination/) | $2n^3/3 + O(n^2)$ | $\Theta(1)$ | any field |
| [Determinant by elimination](/determinant-gaussian-elimination/) | $2n^3/3 - n^2/2 + 5n/6$ | $\Theta(1)$ | any field |
| [Kraut's method](/kraut-determinant/) | $2n^3/3 - n^2/2 + 5n/6 - 1$ | $\Theta(1)$ | any field |
| [Gauss-Jordan elimination](/gauss-jordan-elimination/) | $n^3 + n^2/2 - n/2$ | $\Theta(1)$ | any field |
| [LU decomposition](/lu-decomposition/) | $2n^3/3 + O(n^2)$ | $\Theta(m^2 + mn)$ | any field |
| [Bareiss algorithm](/bareiss-algorithm/) | $4n^3/3 + O(n^2)$ ring | $\Theta(1)$ | integral domain |
| [Multimodular determinant](/multimodular-determinant/) | $O(n^4 (b + \log n)/\ell)$ modular | $O(n^2 \ell + n(b + \log n))$ | $\mathbb{Z}$ |
| [Dixon lifting](/dixon-p-adic-lifting/) | $O(n^3 (b + \log n)^2)$ bit | $O(n^2 (b + \log n))$ | $\mathbb{Z}$ |
| [Kannan-Bachem](/kannan-bachem-algorithm/) | $O(m r^2 (n + m))$ ring | $O((n + m) r)$ | $\mathbb{Z}$ |
| [Berkowitz algorithm](/berkowitz-algorithm/) | $n^4/2 + O(n^3)$ ring | $\Theta(n)$ | commutative ring |
| [Faddeev-LeVerrier](/faddeev-leverrier-algorithm/) | $2n^4 + O(n^3)$ | $\Theta(n^2)$ | field, $1, \ldots, n$ invertible |
| [Wiedemann algorithm](/wiedemann-algorithm/) | $6nw + O(n^2)$ expected | $\Theta(n)$ | finite field |
| [Block Wiedemann](/block-wiedemann-algorithm/) | $3nw + O(sn^2)$ | $O(ns)$ | finite field |
| [Levinson-Durbin](/levinson-durbin-algorithm/) | $7n^2 + O(n)$ | $\Theta(n)$ | any field |

: The main algorithms of the chapter. Operations are field operations unless marked otherwise. The matrix is $n \times n$, or $m \times n$ of rank $r$; integer entries have at most $b$ bits, the primes have $\ell$ bits, $w$ is the number of nonzero entries and $s$ is the block size. Over $\mathbb{Z}$ with schoolbook arithmetic, the Bareiss algorithm costs $O(n^5 (b + \log n)^2)$ bit operations and the multimodular determinant $O(n^4 (b + \log n) \log(nb) + n^3 b (b + \log n))$.

## Choosing a method

- Over a finite field, or modulo a prime in a contest, use Gaussian elimination with modular inverses. Over the field of two elements, pack rows into words.
- To solve many systems with the same matrix, compute the LU decomposition once and solve each system in $O(n^2)$.
- For the determinant of a small integer matrix, use the Bareiss algorithm. For a large one, use the multimodular determinant, with the number of primes set by the Hadamard bound.
- To solve a large nonsingular integer system exactly, use Dixon lifting.
- For integer solutions, or the structure of a lattice or a finitely generated abelian group, compute the Hermite or Smith normal form with a method that bounds its numbers.
- For the characteristic polynomial over a ring where division is not allowed, use the Berkowitz algorithm.
- For a sparse system over a finite field that is too large to eliminate, shrink it first with [structured Gaussian elimination](/structured-gaussian-elimination/), then use block Wiedemann or block Lanczos.
