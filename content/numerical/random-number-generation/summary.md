## What to remember

- A generator with $k$ bits of state has [period](/generator-period/) $\rho \le 2^k$, and one that is linear over $\mathrm{GF}(2)$ has $\rho \le 2^k - 1$, because the zero state is fixed. A long period is necessary and far from sufficient.
- By the [Hull-Dobell theorem](/hull-dobell-theorem/), $s \mapsto (as + c) \bmod m$ has period $m$ exactly when $\gcd(c, m) = 1$, every prime factor of $m$ divides $a - 1$, and $4 \mid a - 1$ if $4 \mid m$. For $m = 2^w$ this means $c$ odd and $a \equiv 1 \pmod 4$, and then bit $j$ of the state has period only $2^{j+1}$.
- By [Marsaglia's theorem](/marsaglia-hyperplane-theorem/), the $d$-tuples of any LCG with modulus $m$ lie on at most $(d!\,m)^{1/d}$ parallel hyperplanes. [RANDU](/randu/) puts its triples on 15 planes; the [spectral test](/spectral-test/) measures the largest gap $1/\nu_d$ between planes for a given multiplier.
- A [linear feedback shift register](/linear-feedback-shift-register/) or another $\mathrm{GF}(2)$-linear generator with a primitive characteristic polynomial of degree $k$ has period $2^k - 1$ from every nonzero state. It can be $d$-[equidistributed](/equidistribution/) to $v$ bits only for $d \le \lfloor k/v \rfloor$, and its linearity is found from about $2k$ output bits, so it fails linear complexity tests.
- [Statistical tests](/statistical-tests-for-randomness/) give evidence, not proof: a failure rejects a generator, a pass only shows that those tests found nothing. TestU01's BigCrush is the usual standard.
- Reducing a uniform word on $M$ values modulo $n$ has total variation distance $r(n - r)/(nM) \le n/(4M)$ from uniform, where $r = M \bmod n$. With $M = 2^w$, an exact method must reject and has no bound on the number of words unless $n$ is a power of two; rejection needs fewer than 2 words on average.
- From a coin with bias $p$, von Neumann's pairs give fair bits at rate $p(1-p)$ per flip, and no method beats the binary entropy $h(p)$.
- A [cryptographically secure generator](/cryptographically-secure-prng/) is one that no polynomial-time test tells from uniform bits; this is equivalent to next-bit unpredictability, and such generators exist if and only if one-way functions do. Its security never exceeds the entropy of its seed.

## Generators side by side

| Generator | State | Period | Cost per output | Status in the entries |
|---|---|---|---|---|
| [Park-Miller](/park-miller-minimal-standard/) | 31 bits | $2^{31} - 2$ | 1 multiplication mod $2^{31} - 1$ | weak, short period |
| [RANDU](/randu/) | 31 bits | $2^{29}$ | 1 multiplication mod $2^{31}$ | broken: 15 planes in 3 dimensions |
| [MRG32k3a](/mrg32k3a/) | 192 bits | about $2^{191}$ | 4 products mod a 32-bit prime | good, used for parallel streams |
| [Mersenne Twister](/mersenne-twister/) | 19937 bits | $2^{19937} - 1$ | a few shifts and XORs | fails linearity tests |
| [xorshift](/xorshift/) | 32 to 128 bits | $2^w - 1$ or $2^{128} - 1$ | 3 shifts and 3 XORs | fails linearity tests |
| [xoshiro256**](/xoshiro-xoroshiro/) | 256 bits | $2^{256} - 1$ | about 11 operations | passes BigCrush |
| [PCG32](/pcg-random/) | 64 bits and an increment | $2^{64}$ | 1 multiplication and a permutation | passes BigCrush |
| [SplitMix64](/splitmix64/) | 64 bits | $2^{64}$ | 2 multiplications | passes BigCrush |
| [Philox4x32-10](/philox/) | 128-bit counter, 64-bit key | $2^{128}$ per key | 20 multiplications per 4 outputs | passes BigCrush, not a cipher |

: Generators of the chapter with their state, period and cost per output, from the table of the [pseudorandom number generator](/pseudorandom-number-generator/) entry. The periods are theorems; the test results are empirical, except the planes of RANDU.

## Choosing a method

- Simulation on one thread: a fast generator that passes BigCrush, such as xoshiro256** or PCG. The Mersenne Twister, the default of many languages, is adequate for most simulations but large and detectably linear.
- Seeding a generator with a large state from one integer: expand the seed with [SplitMix64](/splitmix64/), which never gives the forbidden all-zero state of a linear generator.
- Many parallel streams: a counter-based generator such as [Philox](/philox/) or [Threefry](/threefry/), keyed per stream, or a long-period generator cut into disjoint blocks by [jump-ahead](/jump-ahead/).
- An integer in $[0, n)$: [Lemire's method](/lemire-bounded-integers/) or plain rejection, not the bare remainder, which is biased. A double in $[0, 1)$: the top 53 bits of a 64-bit word times $2^{-53}$.
- Keys, tokens, nonces or anything an adversary sees: the operating system's generator, or a standard generator such as [HMAC_DRBG](/hmac-drbg/) or [CTR_DRBG](/ctr-drbg/) seeded from an [entropy source](/entropy-source/). Never a statistical generator.
- Integration of a smooth function in moderate dimension: the [Sobol](/sobol-sequence/) or [Halton](/halton-sequence/) points of quasi-Monte Carlo, not random points.
