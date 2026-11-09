## What to remember

- The **naive product** of an $n \times m$ and an $m \times p$ matrix makes $nmp$ multiplications. It works over any semiring. Splitting into blocks with eight half-size products does the same work, $T(n) = 8T(n/2) + \Theta(n^2) = \Theta(n^3)$.
- **Strassen's algorithm** multiplies $2 \times 2$ block matrices with 7 products and 18 additions, so $T(n) = 7T(n/2) + \Theta(n^2) = \Theta(n^{\lg 7})$, about $n^{2.807}$. With exact counts it costs $7n^{\lg 7} - 6n^2$ operations, and Winograd's variant with 15 additions costs $6n^{\lg 7} - 5n^2$. It needs subtraction, so it does not work over the Boolean or min-plus semiring directly.
- The **exponent** $\omega$ is the least number with $n \times n$ products in $O(n^{\omega + \varepsilon})$ for all $\varepsilon > 0$. The best bounds known are $2 \le \omega < 2.371552$. A bilinear scheme with $r$ products for $\langle n, m, p \rangle$ gives $\omega \le 3 \log r / \log(nmp)$; for square $k \times k$ blocks that is $\omega \le \log_k r$.
- **Inversion, determinants and linear systems** cost $O(n^\omega)$, and conversely a product can be read off the inverse of a $3n \times 3n$ matrix, so $M(n) \le I(3n)$. They all share the exponent $\omega$.
- **Powers** by repeated squaring take $\lfloor \lg k \rfloor + \nu(k) - 1$ products, where $\nu(k)$ is the number of ones in $k$. With a $2 \times 2$ matrix this gives $F_n$ in $O(\log n)$ arithmetic operations.
- **Semiring products** answer graph questions. The Boolean square of $I \vee A$, repeated, gives the transitive closure; the min-plus square of the weight matrix, repeated $\lceil \lg(n-1) \rceil$ times, gives all shortest path lengths.
- **On real machines** the cost is data movement. A blocked product with tiles of side $\Theta(\sqrt M)$ moves $O(n^3/(B\sqrt M) + n^2/B)$ words, which Hong and Kung showed is optimal for the $n^3$ method. The recursive product reaches the same bound without knowing $M$ or $B$.

## Methods side by side

| Method | Multiplications | Time | Over any semiring | Extra space |
|---|---|---|---|---|
| [Naive](/naive-matrix-multiplication/) | $n^3$ | $\Theta(n^3)$ | yes | $\Theta(1)$ |
| [Divide and conquer](/divide-and-conquer-matrix-multiplication/) | $n^3$ | $\Theta(n^3)$ | yes | $O(\log n)$ |
| [Winograd inner product](/winograd-inner-product-algorithm/) | about $n^3/2 + n^2$ | $\Theta(n^3)$ | no, needs a commutative ring | $\Theta(n)$ |
| [Strassen](/strassen-algorithm/) | 7 for $2 \times 2$ blocks | $\Theta(n^{\lg 7}) \approx n^{2.807}$ | no, needs a ring | $\Theta(n^2)$ |
| [Laderman](/laderman-algorithm/) | 23 for $3 \times 3$ blocks | $\Theta(n^{\log_3 23}) \approx n^{2.854}$ | no, needs a ring | $\Theta(n^2)$ |
| [Coppersmith-Winograd](/coppersmith-winograd-algorithm/) | — | $O(n^{2.375477})$ | no, needs a ring | $O(n^2)$ |
| [Blocked](/blocked-matrix-multiplication/) | $n^3$ | $\Theta(n^3)$, $O(n^3/(B\sqrt M))$ transfers | yes | $\Theta(M)$ |
| [Cache-oblivious](/cache-oblivious-matrix-multiplication/) | $n^3$ | $\Theta(n^3)$, $O(n^3/(B\sqrt M))$ transfers | yes | $\Theta(\log n)$ |

: Products of two $n \times n$ matrices. The bound $\omega < 2.371552$ of 2024 is a refinement of the Coppersmith-Winograd method; the algorithms behind it, like the 1990 one, are far too slow in practice. Laderman's algorithm is worse than Strassen's asymptotically, because $\log_3 23 > \lg 7$.

## Choosing a method

- For dense matrices of floating-point numbers, call a tuned BLAS routine. It is a blocked $n^3$ product, and it beats any hand-written loop.
- For very large dense matrices over exact rings, such as integers modulo a prime, use Strassen's algorithm above a crossover size, with a blocked naive product below it.
- For powers, use repeated squaring. For one term of a linear recurrence of high order, see [the $n$-th term of a linear recurrence](/linear-recurrence-nth-term/), which works with polynomials instead of matrices.
- For Boolean products, use the integer product with a fast algorithm, or bit-packed rows; for min-plus products of general weights, the best known time is $n^3/2^{\Omega(\sqrt{\log n})}$, barely below $n^3$.
- For sparse matrices, use [compressed sparse row](/compressed-sparse-row/) storage and [Gustavson's algorithm](/sparse-matrix-multiplication/), never a dense product.
- Never use the Coppersmith-Winograd family in practice; it matters for what it proves about $\omega$.
