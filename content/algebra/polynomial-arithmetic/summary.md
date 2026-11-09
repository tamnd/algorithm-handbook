## What to remember

- **$M(n)$ is the unit of cost.** It is the cost of multiplying two polynomials with $n$ coefficients: $n^2$ multiplications by the school method, $O(n^{\log_2 3})$ by [Karatsuba](/karatsuba-multiplication/), $O(n \log n)$ by [FFT multiplication](/fft-polynomial-multiplication/) when the ring has principal roots of unity of order $2^k$ and $2$ is a unit, and $O(n \log n \log \log n)$ over every commutative ring.
- **Horner's rule is optimal for one point.** It evaluates a polynomial of degree $n$ with $n$ multiplications and $n$ additions, and Pan proved in 1966 that no method for a general polynomial uses fewer. Its running values give the quotient by $x - a$.
- **Values are as good as coefficients.** Over a field, a polynomial of degree less than $n$ is fixed by its values at $n$ distinct points, and evaluation is a ring homomorphism. So a product can be computed pointwise; at the roots of unity the FFT does both conversions in $O(n \log n)$.
- **Newton iteration makes division as cheap as multiplication.** Each step $g \leftarrow g(2 - fg)$ doubles the number of correct coefficients of $1/f$, so inversion modulo $x^n$ costs $3M(n) + o(M(n))$. Reversing the coefficients turns division with remainder into one inversion and two products.
- **Many points cost a logarithm more.** The [subproduct tree](/subproduct-tree/) of $x - u_0, \ldots, x - u_{n-1}$ gives evaluation at all $n$ points and interpolation through them in $O(M(n) \log n)$, against $\Theta(n^2)$ by the classical methods.
- **The gcd follows the integer Euclidean algorithm.** Over a field it costs $O(n^2)$ by repeated remainders and $O(M(n) \log n)$ by the [half-gcd](/half-gcd/) method. Over $\mathbb{Z}$ the obstacle is coefficient growth, which the [subresultant](/subresultant-gcd/) and [modular](/brown-modular-gcd/) algorithms control.
- **Repeated factors come out with gcds.** Over $\mathbb{Q}$, $\mathbb{R}$ and every finite field, $f$ is square-free exactly when $\gcd(f, f') = 1$. [Yun's algorithm](/yun-square-free-factorization/) splits $f$ by multiplicity for a constant times the cost of one gcd, in characteristic $0$ or larger than $\deg f$.
- **Over $\mathbb{F}_q$, everything rests on $x^{q^i} - x$.** It is the product of the monic irreducibles of degree dividing $i$. It drives distinct-degree factorization and Rabin's irreducibility test. Factoring takes expected polynomial time in $n$ and $\log q$ by the [Cantor-Zassenhaus algorithm](/cantor-zassenhaus-algorithm/); no deterministic algorithm with that cost is known.
- **Over $\mathbb{Z}$, factor modulo $p$ and lift.** By [Gauss's lemma](/gauss-lemma/), factoring over $\mathbb{Z}$ and over $\mathbb{Q}$ are the same problem up to constants. The [Zassenhaus algorithm](/zassenhaus-algorithm/) factors modulo a prime, applies [Hensel lifting](/hensel-lifting/) and recombines the lifted factors by a subset search that is exponential in the worst case.

## Classical and fast methods side by side

| Problem | Classical method | Operations | Fast method | Operations |
|---|---|---|---|---|
| Multiplication | school method | $n^2 + (n-1)^2$ | [FFT](/fft-polynomial-multiplication/) | $O(n \log n)$ |
| Division, degrees $m \ge n$ | [long division](/polynomial-long-division/) | $\le (2n + 1)(m - n + 1)$ | [Newton and reversal](/fast-polynomial-division/) | $O(M(m))$ |
| Inversion modulo $x^n$ | term-by-term recurrence | $O(n^2)$ | [Newton iteration](/newton-power-series-inversion/) | $3M(n) + o(M(n))$ |
| Gcd, degrees $m \ge n$ | [Euclidean algorithm](/polynomial-euclidean-algorithm/) | $\le (2n + 1)(m + n + 1)$ | [half-gcd](/half-gcd/) | $O(M(m) \log m)$ |
| Evaluation at $n$ points | Horner at each point | $\Theta(n^2)$ | [subproduct tree](/fast-multipoint-evaluation/) | $O(M(n) \log n)$ |
| Interpolation at $n$ points | Lagrange or Newton | $\Theta(n^2)$ | [subproduct tree](/fast-interpolation/) | $O(M(n) \log n)$ |
| $f(g) \bmod h$, $\deg h = n$ | Horner in $R[x]/(h)$ | $O(n\, M(n))$ | [Brent-Kung](/brent-kung-composition/) | $O(\sqrt{n}\, M(n) + n^{(\omega+1)/2})$ |
| $N$-th term, order $d$ | run the recurrence | $\Theta(N d)$ | [Bostan-Mori](/bostan-mori-algorithm/) | $O(M(d) \log N)$ |

: Operations in the coefficient ring; $n$ is the degree unless the row says otherwise, and $\omega$ is the exponent of matrix multiplication. The FFT bound needs suitable roots of unity; over any commutative ring, $M(n) = O(n \log n \log \log n)$. Over $\mathbb{Z}$ these counts hide the size of the coefficients.

## Choosing a method

- Use the school method for small degrees, then Karatsuba, then FFT methods, with crossovers found by measurement.
- Modulo a prime $p = c \cdot 2^k + 1$, use the [number-theoretic transform](/number-theoretic-transform/). Over $\mathbb{Z}$, multiply modulo several such primes and rebuild by Chinese remaindering, or use [Kronecker substitution](/kronecker-substitution/).
- Keep few-term polynomials [sparse](/sparse-polynomial-representation/); division and gcds may still give dense results.
- For gcds over $\mathbb{Z}$, use a modular or subresultant method, not the Euclidean algorithm over $\mathbb{Q}$.
- To factor over a large finite field, use Cantor-Zassenhaus; over a small prime field, Berlekamp's algorithm also works well. Over $\mathbb{Z}$, current systems use Zassenhaus with lattice-based recombination.
- To isolate real roots, the [Vincent-Collins-Akritas](/vincent-collins-akritas/) method is one of the fastest exact methods in practice.
