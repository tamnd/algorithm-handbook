## What to remember

- The input of a [primality test](/primality-testing/) has $\ell \approx \lg n$ bits. Trial division takes about $2^{\ell/2}$ steps; one modular exponentiation takes $O(\ell^3)$ bit operations with schoolbook multiplication, and every fast test is a few of them.
- A test that every prime passes gives one-sided answers: a failed check proves $n$ composite, through a [compositeness witness](/compositeness-witness/); a passed check makes $n$ only a [probable prime](/probable-prime/).
- The [Fermat test](/fermat-primality-test/) has no error bound for all inputs: a [Carmichael number](/carmichael-number/), such as $561 = 3 \cdot 11 \cdot 17$, passes for every base coprime to it. By Korselt's criterion these are the squarefree composites with $p - 1 \mid n - 1$ for each prime $p \mid n$.
- If $x^2 \equiv 1$ but $x \not\equiv \pm 1 \pmod n$, then $n$ is composite and $\gcd(x - 1, n)$ is a proper factor. The strong test of [Miller-Rabin](/miller-rabin/) looks for such an $x$ in the chain $a^d, a^{2d}, \ldots, a^{2^s d}$, where $n - 1 = 2^s d$.
- An odd composite $n > 9$ has at most $\varphi(n)/4$ [strong liars](/strong-liar/), so $k$ random rounds of Miller-Rabin err with probability below $4^{-k}$ on every input. Below $2^{64}$, the first 12 primes as bases make the test exact.
- By the [prime number theorem](/prime-number-theorem/), $\pi(x) \sim x / \ln x$, so a random $\ell$-bit integer is prime with probability about $1/(\ell \ln 2)$, and [random prime generation](/random-prime-generation/) needs $O(\ell)$ candidates on average.
- A [primality certificate](/primality-certificate/) turns "prime" into a proof that anyone can check fast. If $a^{n-1} \equiv 1$ and $a^{(n-1)/q} \not\equiv 1 \pmod n$ for every prime $q \mid n - 1$, then $a$ has order $n - 1$ and $n$ is prime; [Pratt](/pratt-certificate/) applies this recursively, and [Pocklington](/pocklington-primality-test/) needs only a factored part $F > \sqrt n$ of $n - 1$.
- For $2^p - 1$, $2^{2^k} + 1$ and $k \cdot 2^m + 1$ with $k < 2^m$, an exact test costs about as much as one probable prime test. Primality is in P by the [AKS test](/aks-primality-test/), but [ECPP](/ecpp/) is what proves large general primes in practice.

## The main tests side by side

| Test | Answer | Cost | Applies to |
|---|---|---|---|
| [Fermat](/fermat-primality-test/) | probable prime | $O(k \ell^3)$ | any $n$; no bound on error |
| [Solovay-Strassen](/solovay-strassen/) | probable prime, error $< 2^{-k}$ | $O(k \ell^3)$ | odd $n$ |
| [Miller-Rabin](/miller-rabin/) | probable prime, error $< 4^{-k}$ | $O(k \ell^3)$ | odd $n$ |
| [Baillie-PSW](/baillie-psw/) | probable prime, no known failure | $O(\ell^3)$ expected | odd $n$ |
| [Frobenius](/frobenius-test/) | probable prime, error $< 7710^{-k}$ | $O(k \ell^3)$ expected | $n$ with no small factor |
| [Pocklington](/pocklington-primality-test/) | proof | a few exponentiations per prime of $F$ | $n - 1 = FR$ with $F$ factored, $F^2 > n$ |
| [Lucas-Lehmer](/lucas-lehmer-test/) | exact | $p - 2$ squarings | $M_p = 2^p - 1$, $p$ odd prime |
| [Pépin](/pepin-test/) | exact | $2^k - 1$ squarings | $F_k = 2^{2^k} + 1$, $k \ge 1$ |
| [Proth](/proth-test/) | exact | one exponentiation | $k \cdot 2^m + 1$, $k$ odd, $k < 2^m$ |
| [AKS](/aks-primality-test/) | exact | $O(\ell^{15/2} \log \ell)$ | any $n$ |
| [ECPP](/ecpp/) | proof with certificate | $O(\ell^{5+\varepsilon})$ heuristic; check $O(\ell^4)$ | any $n$ |

: Primality tests, with $\ell = \lg n$ and $k$ rounds. "Exact" means the test decides both ways with no error; "proof" means it proves primes prime, and a failure leaves $n$ undecided only if the needed base or curve is not found. The Frobenius bound holds per round of the random quadratic test.

## Choosing a method

To test a number below $2^{64}$, use Miller-Rabin with a [deterministic set of bases](/deterministic-miller-rabin-bases/), or Baillie-PSW; both are exact in that range. Above it, use Baillie-PSW or Miller-Rabin with enough random bases for the error you accept; for random candidates far fewer rounds suffice than the worst-case bound suggests. Do trial division by small primes first: it removes most composites at almost no cost.

To generate a prime, draw random odd candidates of the right size, sieve them by small primes and test the survivors. For a [safe prime](/safe-prime/) $2q + 1$, test $q$ and $2q + 1$ together and expect a much longer search.

When an answer of "probable prime" is not enough, prove it. For numbers of special form use the matching exact test. For general numbers of a few hundred digits [APR-CL](/apr-cl-primality-test/) or ECPP both work; for larger ones ECPP, which also leaves a certificate. AKS is a theorem about complexity, not a practical tool.
