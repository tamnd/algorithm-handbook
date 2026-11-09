## What to remember

- $a \equiv b \pmod n$ means $n \mid a - b$. Congruence respects $+$, $-$ and $\times$, so you can reduce after every step. It does not respect division: you divide by multiplying with an inverse.
- $a$ has an inverse modulo $n$ exactly when $\gcd(a, n) = 1$. The [extended Euclidean algorithm](/extended-euclidean-algorithm/) finds it in $O(\log n)$ division steps; modulo a prime $p$, $a^{p-2}$ is the inverse too.
- [Binary exponentiation](/binary-exponentiation/) computes $a^b \bmod n$ with about $2 \lg b$ modular multiplications. Every public-key system and every probabilistic primality test spends most of its time in this loop.
- $ax \equiv b \pmod n$ has a solution exactly when $d = \gcd(a, n)$ divides $b$, and then it has $d$ solutions modulo $n$, spaced $n/d$ apart.
- **Chinese remainder theorem**: for pairwise coprime $n_1, \ldots, n_k$, the map $x \mapsto (x \bmod n_1, \ldots, x \bmod n_k)$ is a ring isomorphism from $\mathbb{Z}/N\mathbb{Z}$, $N = \prod n_i$, to the product of the $\mathbb{Z}/n_i\mathbb{Z}$. Work can be split by moduli and joined again by [Garner's algorithm](/garner-algorithm/).
- **Euler's theorem**: $a^{\varphi(n)} \equiv 1 \pmod n$ when $\gcd(a, n) = 1$; for a prime $p$ this is **Fermat's little theorem** $a^{p-1} \equiv 1$. Both are Lagrange's theorem applied to $\mathbb{Z}_n^*$, a group of size $\varphi(n) = n \prod_{p \mid n}(1 - 1/p)$. So exponents may be reduced modulo $\varphi(n)$, or better modulo $\lambda(n)$.
- The order of $a$ divides $\lambda(n)$, which divides $\varphi(n)$. A **primitive root** has order $\varphi(n)$; one exists exactly for $n = 1, 2, 4, p^k, 2p^k$ with $p$ an odd prime, and then there are $\varphi(\varphi(n))$ of them.
- Modulo an odd prime $p$, exactly $(p-1)/2$ nonzero residues are squares. **Euler's criterion** $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2}$ tests one with a single power, and **quadratic reciprocity** computes the symbol by a Euclid-like loop. The [Jacobi symbol](/jacobi-symbol/) extends the loop to odd composite $n$, but there the value $1$ no longer means "square".

## The main algorithms side by side

| Algorithm | Computes | Cost | Condition |
|---|---|---|---|
| [Binary exponentiation](/binary-exponentiation/) | $a^b \bmod n$ | $\Theta(\log b)$ multiplications | none |
| [Extended Euclid](/extended-euclidean-algorithm/) | $a^{-1} \bmod n$ | $O(\log n)$ divisions | $\gcd(a, n) = 1$ |
| [Batch modular inverse](/batch-modular-inverse/) | $k$ inverses | one inversion and $3(k-1)$ multiplications | all residues invertible |
| [Barrett reduction](/barrett-reduction/) | $x \bmod n$, $x < 4^k$ | two multiplications, at most two corrections | fixed modulus |
| [Montgomery multiplication](/montgomery-multiplication/) | $abR^{-1} \bmod n$ | two multiplications, at most one subtraction | $n$ odd, values in Montgomery form |
| [Garner's algorithm](/garner-algorithm/) | $x$ from $t$ residues | $\Theta(t^2)$ word operations, then one evaluation | pairwise coprime moduli |
| [Tonelli-Shanks](/tonelli-shanks/) | $\sqrt a \bmod p$ | $O(\log p + s^2)$ multiplications | $p - 1 = q \cdot 2^s$, $q$ odd; a nonresidue |
| [Cipolla's algorithm](/cipolla-algorithm/) | $\sqrt a \bmod p$ | $O(\log p)$ expected multiplications | a $t$ with $t^2 - a$ a nonresidue |

: The main algorithms of modular arithmetic. Barrett's constant is $\lfloor 4^k / n \rfloor$ for a $k$-bit modulus; Montgomery's $R$ is a power of two above $n$. Both square root algorithms find their nonresidue by random trial, about two tries on average.

## Choosing a method

- For $a^b \bmod n$ with word-size $n$, use binary exponentiation with a 128-bit product or a [modular multiplication](/modular-multiplication/) that avoids overflow. Reduce $b$ modulo $\varphi(n)$ first only when $\gcd(a, n) = 1$.
- For an inverse modulo a prime that you also raise to powers, $a^{p-2}$ is simplest to write; the extended Euclidean algorithm is faster. For many inverses with one modulus, use the batch method.
- For long chains of products with one odd modulus, as in RSA, use Montgomery form. For a fixed modulus that may be even, or for single reductions, use Barrett.
- For a square root modulo $p \equiv 3 \pmod 4$, compute $a^{(p+1)/4}$. Otherwise use Tonelli-Shanks when $s$ is small and Cipolla's algorithm when $p - 1$ has a large power of 2.
- For dates, convert to a day count, compute with integers, and convert back.
