## What to remember

- A sieve inverts the question "which primes divide $m$" into "which $m$ does $p$ divide", and visits the multiples of $p$ at constant cost each. The total is $\sum_{p \le n} n/p = n \ln \ln n + O(n)$ for one pass per prime, and $\sum_{e \le n} n/e \approx n \ln n$ for one pass per integer.
- The [sieve of Eratosthenes](/sieve-of-eratosthenes/) needs only the primes $p \le \sqrt n$, and may start each pass at $p^2$, because every composite $m \le n$ has a prime factor at most $\sqrt m$. It takes $\Theta(n \log \log n)$ steps.
- The [segmented sieve](/segmented-sieve/) lists the primes in $[L, R]$ with the base primes up to $\sqrt R$ and one block in memory, in $O(\Delta \log \log R + \sqrt R)$ steps for $\Delta = R - L + 1$.
- The [linear sieve](/linear-sieve/) writes each composite $m$ once, as $p \cdot i$ with $p = \mathrm{lp}(m) \le \mathrm{lp}(i)$. It builds the [smallest prime factor table](/smallest-prime-factor-table/) in $\Theta(n)$, and any $m \le n$ then factors in $\Omega(m) \le \lg m$ divisions.
- A [multiplicative function](/multiplicative-functions-up-to-n/) is fixed by its values on prime powers, so the linear sieve computes it for all $m \le n$ in $\Theta(n)$ from $f(p i) = f(p) f(i)$ when $p < \mathrm{lp}(i)$, with the stored power of $p$ when $p = \mathrm{lp}(i)$. The [Möbius sieve](/mobius-sieve/) and the [totient sieve](/euler-phi-sieve/) are the common cases.
- [Legendre's formula](/legendre-phi-function/) $\pi(x) = \phi(x, a) + a - 1$ with $a = \pi(\sqrt x)$ counts primes without listing them. Sieving only the $2\sqrt x$ values $\lfloor x/k \rfloor$ gives the [Lucy_Hedgehog method](/lucy-hedgehog-prime-counting/), $O(x^{3/4} / \log x)$; cutting the recursion at $x^{1/3}$ and correcting with $P_2$ gives [Meissel-Lehmer](/meissel-lehmer-algorithm/), $O(x^{2/3} \log x)$.
- [Sieve theory](/sieve-theory/) estimates $S(\mathcal{A}, z)$, the number of elements of $\mathcal{A}$ with no prime factor below $z$, from the densities $g(d)$ and the remainders $r_d$. [Brun](/brun-sieve/) truncates inclusion-exclusion and [Selberg](/selberg-sieve/) minimizes a quadratic form. Both give upper bounds of the right order, such as $\pi_2(x) = O(x / \log^2 x)$ for twin primes.
- Sieves alone cannot separate primes from products of two primes. This parity problem is why they bound twin primes from above but cannot prove there are infinitely many.

## The sieves side by side

| Method | Time | Memory | Computes |
|---|---|---|---|
| [Eratosthenes](/sieve-of-eratosthenes/) | $\Theta(n \log \log n)$ | $\Theta(n)$ flags | primes up to $n$ |
| [Sundaram](/sieve-of-sundaram/) | $\Theta(n \log n)$ | $n/2$ flags | odd primes up to $n$ |
| [Segmented](/segmented-sieve/) | $O(\Delta \log \log R + \sqrt R)$ | $O(\sqrt R / \log R + B)$ | primes in $[L, R]$ |
| [Linear](/linear-sieve/) | $\Theta(n)$ | $\Theta(n)$ words | primes and $\mathrm{lp}(m)$ up to $n$ |
| [Atkin](/sieve-of-atkin/) | $\Theta(n)$, or $O(n / \log \log n)$ with a wheel | $\Theta(n)$, or $n^{1/2 + o(1)}$ | primes up to $n$ |
| [Divisor-count sieve](/divisor-count-sieve/) | $\Theta(n \log n)$ | the output | $d(m)$ or $\sigma(m)$ up to $n$ |
| [Totient sieve](/euler-phi-sieve/) | $\Theta(n \log \log n)$ | the output | $\varphi(m)$ up to $n$ |
| Linear sieve with prime powers | $\Theta(n)$ | two arrays of $n + 1$ words | any multiplicative $f$ up to $n$ |
| [Lucy_Hedgehog](/lucy-hedgehog-prime-counting/) | $O(x^{3/4} / \log x)$ | $O(\sqrt x)$ | $\pi(x)$, sums over primes |
| [Meissel-Lehmer](/meissel-lehmer-algorithm/) | $O(x^{2/3} \log x)$ | $O(x^{2/3})$ | $\pi(x)$ |

: Sieves for tables and for counting. $n$ and $x$ are the bounds, $\Delta = R - L + 1$ the length of an interval, $B$ the block length. Times count word operations.

## Choosing a method

For a small table of primes, a plain sieve of Eratosthenes on the odd numbers is short and fast. When the table does not fit in the cache, sieve in segments; the same code then lists the primes in any interval $[L, R]$. A short interval near a huge number is cheaper to scan with a [probable prime test](/miller-rabin/) on each candidate.

When you also need factorizations or an arithmetic function, use the linear sieve: it gives the primes, the least prime factors and $\varphi$, $\mu$, $d$ or $\sigma$ in one pass. The harmonic sieve is simpler and fine when $n \log n$ steps are affordable.

For $\pi(x)$ or a sum over primes up to $x$ without the list, use the Lucy_Hedgehog method for $x$ up to about $10^{12}$; beyond that the Meissel-Lehmer family, in the form of Deléglise and Rivat, is the standard. The sieve of Atkin is of interest for its idea more than for speed.
