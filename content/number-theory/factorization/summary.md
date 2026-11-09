## What to remember

- The input has $n \approx \lg N$ bits, and no classical method is polynomial in $n$. [Trial division](/trial-division/) takes $O(\min(p, \sqrt N))$ divisions, where $p$ is the least prime factor: exponential in $n$, but the right first step for every number.
- An odd $N = x^2 - y^2$ splits as $(x - y)(x + y)$. [Fermat's method](/fermat-factorization/) finds this at once when the two factors are close to $\sqrt N$ and takes $\Theta(N)$ steps for $N = 3p$; [Lehman's method](/lehman-factorization/) adds multipliers and proves $O(N^{1/3})$.
- [Pollard's rho](/pollard-rho/) finds a prime factor $p$ in about $\sqrt p$ multiplications, by the birthday paradox, with $O(1)$ memory. The bound is heuristic; [Pollard-Strassen](/pollard-strassen/) proves $N^{1/4 + o(1)}$ deterministically.
- [Pollard's $p - 1$ method](/pollard-p-minus-1/) computes $\gcd(a^M - 1, N)$ with $M = \operatorname{lcm}(1, \ldots, B)$ and finds $p$ when every prime power of $p - 1$ is at most $B$, with $O(B)$ multiplications. The [elliptic curve method](/elliptic-curve-factorization/) replaces the one group of order $p - 1$ by many curve groups of order near $p$, at heuristic cost $L_p[1/2, \sqrt 2]$, which depends on $p$, not on $N$.
- If $x^2 \equiv y^2$ and $x \not\equiv \pm y \pmod N$, then $\gcd(x - y, N)$ is a proper factor. For odd $N$ with $r \ge 2$ distinct prime factors, a random square root of $x^2$ is $\pm x$ with probability only $2^{1-r} \le 1/2$.
- With a factor base of $K$ primes, any $K + 1$ [relations](/relation-collection/) $x_i^2 \equiv a_i$ with smooth $a_i$ contain a subset whose $a_i$ multiply to a square, found by linear algebra over the field with two elements.
- About $\rho(u)\, x$ of the integers up to $x$ are $x^{1/u}$-smooth, where the [Dickman function](/dickman-function/) satisfies $\rho(2) = 1 - \ln 2 \approx 0.307$ and falls roughly like $u^{-u}$. Balancing this chance against the size of the factor base gives the costs $L_N[1/2, c]$.
- The [quadratic sieve](/quadratic-sieve/) tests the values of $x^2 - N$ for smoothness with a sieve, about $\ln \ln B$ additions per value, for $L_N[1/2, 1]$. The [number field sieve](/general-number-field-sieve/) makes both sides of a relation about $N^{1/d}$ in size and reaches $L_N[1/3, (64/9)^{1/3}]$.

## The main methods side by side

| Method | Cost | Status | Finds |
|---|---|---|---|
| [Trial division](/trial-division/) | $O(\min(p, \sqrt N))$ divisions | proved | all factors |
| [Fermat](/fermat-factorization/) | $O((\sqrt b - \sqrt a)^2 + 1)$ steps for $N = ab$ | proved | factors near $\sqrt N$ |
| [Lehman](/lehman-factorization/) | $O(N^{1/3})$ | proved | a factor, or a proof that $N$ is prime |
| [Pollard's rho](/pollard-rho/), [Brent](/brent-pollard-rho/) | $O(\sqrt p)$ multiplications | heuristic | small $p$ |
| [Pollard-Strassen](/pollard-strassen/) | $N^{1/4 + o(1)}$ | proved, deterministic | least $p$ |
| [SQUFOF](/shanks-squfof/) | $O(N^{1/4})$ steps | heuristic | a factor of a one-word $N$ |
| [Pollard's $p - 1$](/pollard-p-minus-1/) | $O(B)$ multiplications | works only when $p - 1$ is smooth | $p$ with smooth $p - 1$ |
| [ECM](/elliptic-curve-factorization/) | $L_p[1/2, \sqrt 2]$ | heuristic | medium $p$ |
| [Dixon](/dixon-random-squares/) | $L_N[1/2, 2\sqrt 2]$ expected | proved | a split of $N$ |
| [CFRAC](/continued-fraction-factorization/) | $L_N[1/2, \sqrt 2]$ | heuristic | a split of $N$ |
| [QS](/quadratic-sieve/), [MPQS](/multiple-polynomial-quadratic-sieve/) | $L_N[1/2, 1]$ | heuristic | a split of $N$ |
| [GNFS](/general-number-field-sieve/) | $L_N[1/3, (64/9)^{1/3}]$, $(64/9)^{1/3} \approx 1.923$ | heuristic | a split of $N$ |
| [SNFS](/special-number-field-sieve/) | $L_N[1/3, (32/9)^{1/3}]$, $(32/9)^{1/3} \approx 1.526$ | heuristic | a split of $N$ of special form |

: Factoring methods. $N$ is the number, $p$ its least prime factor, and $L_x[\alpha, c] = \exp\big((c + o(1)) (\ln x)^\alpha (\ln \ln x)^{1-\alpha}\big)$. Costs count arithmetic operations on numbers of the size of $N$.

## Choosing a method

Always start with trial division by the primes up to some bound, and test the cofactor with a [probable prime test](/miller-rabin/) before you try to split it. For a number that fits in a machine word, Brent's rho, SQUFOF or Hart's method finishes the job.

For a large number, look for small and medium factors first: rho finds factors of up to about 20 digits, and ECM, run on many curves with a growing bound, finds factors of roughly 15 to 40 digits whatever the size of $N$. Run $p - 1$ once along the way; it is cheap and sometimes lucky.

When what is left is a product of large primes with no special form, use MPQS up to around 100 decimal digits and the general number field sieve above roughly 100 to 120 digits. For a divisor of $b^k \pm 1$ or another number of special form, use the special number field sieve.
