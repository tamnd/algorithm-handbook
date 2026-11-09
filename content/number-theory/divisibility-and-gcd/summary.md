## What to remember

- $\gcd(a, b)$ is the common divisor that every other common divisor divides, and the smallest positive value of $ax + by$ over integers $x, y$ ([Bézout's identity](/bezouts-identity/)). The values of $ax + by$ are exactly the multiples of $\gcd(a, b)$.
- The **GCD recursion** $\gcd(a, b) = \gcd(b, a \bmod b)$ is the whole of the [Euclidean algorithm](/euclidean-algorithm/). By [Lamé's theorem](/lames-theorem/), on $a > b \ge 1$ it makes at most $1 + \log_\varphi b$ divisions, at most five per decimal digit of $b$, and consecutive Fibonacci numbers are the worst case. On $n$-bit numbers the cost is $O(n^2)$ bit operations.
- The **extended Euclidean algorithm** returns $x, y$ with $ax + by = \gcd(a, b)$ at no extra asymptotic cost, and its coefficients are small: $|x| \le |b|/(2g)$ and $|y| \le |a|/(2g)$ outside the trivial case. It gives modular inverses and solves $ax + by = c$.
- $ax + by = c$ has an integer solution exactly when $g = \gcd(a, b)$ divides $c$. All solutions are $(x_0 + k\,b/g,\ y_0 - k\,a/g)$ for $k \in \mathbb{Z}$, so counting those in a box is one gcd and a few divisions.
- **Unique factorization** follows from [Euclid's lemma](/euclids-lemma/): if a prime divides $ab$, it divides $a$ or $b$. The gcd, the lcm and every [multiplicative function](/multiplicative-function/) can be read off the prime exponents, for example $d(n) = \prod (e_i + 1)$. Knowing that the factorization exists does not tell you how to find it.
- $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |ab|$ for two numbers, but not for three or more.
- **Möbius inversion**: $g = f * \mathbf{1}$ exactly when $f = g * \mu$. It turns a sum over divisors back into its terms, and it is inclusion-exclusion over the prime divisors.
- The quotients of Euclid's algorithm on $a/b$ are the partial quotients of its [continued fraction](/continued-fraction/). The [convergents](/continued-fraction-convergents/) $p_n/q_n$ are in lowest terms, alternate around $x$, have error below $1/q_n^2$, and are the best approximations with denominators that small.

## The gcd algorithms side by side

| Method | Steps | Bit operations on $n$-bit inputs | What it gives |
|---|---|---|---|
| [Euclidean algorithm](/euclidean-algorithm/) | $\Theta(\log m)$ divisions | $O(n^2)$ | $\gcd(a, b)$ |
| [Binary GCD](/binary-gcd/) | at most $1 + \lg(\lvert a \rvert \cdot \lvert b \rvert)$ passes | $O(n^2)$ | $\gcd(a, b)$, no division |
| [Extended Euclidean algorithm](/extended-euclidean-algorithm/) | $\Theta(\log m)$ divisions | $O(n^2)$ | $\gcd(a, b)$ and $x, y$ |
| [Lehmer's GCD](/lehmers-gcd/) | $O(n^2/w + n)$ word operations | $O(n^2)$ | $\gcd(a, b)$, fewer passes over long numbers |
| [Half-GCD](/half-gcd/) | recursive on halves | $O(M(n) \log n)$ | $\gcd$, quotient matrix, continued fraction |
| [Batch GCD](/batch-gcd/) | product and remainder trees | $O(m \log^2 m)$ for $m$ input digits in all | $\gcd(N_i, \prod_{j \ne i} N_j)$ for every $i$ |

: The ways to compute a gcd. Here $m$ in the first rows is $\min(\lvert a \rvert, \lvert b \rvert)$, $w$ is the word size, and $M(n)$ is the cost of multiplying two $n$-bit numbers. The bound for batch GCD assumes quasi-linear multiplication.

## Choosing a method

- For numbers that fit in a machine word, use the Euclidean algorithm, or binary GCD where division is slow. On 64-bit inputs Euclid makes at most 93 divisions and binary GCD at most 128 passes.
- When you need an inverse or a solution of $ax + by = c$, use the extended algorithm; there is no separate method.
- For a list of numbers, fold the two-number gcd and stop early when the result reaches 1; see [GCD of an array](/gcd-of-array/). For the lcm, divide before you multiply, $|x| / \gcd(x, y) \cdot |y|$, and watch for overflow.
- For numbers of hundreds of digits, a big-number library uses Lehmer's method; past some thousands of digits it switches to the half-GCD. Do not write these yourself unless you must.
- To find which of many numbers share a factor, use batch GCD, not all $\binom n2$ pairs.
- For the divisors of $n$, factor first and then [enumerate](/enumerating-divisors/) the products of prime powers. For $\sum_{k \le n} d(k)$, use the [hyperbola method](/dirichlet-hyperbola-method/) in $O(\sqrt n)$ steps.
