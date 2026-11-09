Many programs need facts about every integer up to a bound at once: all the primes below $10^8$, the least prime factor of each $m \le n$ so that many small numbers can be factored fast, or the table of $\varphi(m)$ for a counting problem. Answering each question one number at a time, by [trial division](/trial-division/), costs about $\sqrt m$ per number. A sieve turns the work around. Instead of asking which primes divide $m$, it takes each prime $p$ and visits its multiples $p, 2p, 3p, \ldots$, so every divisibility fact is found by a step of fixed cost. The whole table then costs $\Theta(n \log \log n)$ steps, or $\Theta(n)$ with more care, which is close to the size of the output.

The chapter has two halves. The first is algorithmic: sieves that list primes, sieves that compute arithmetic functions on a whole range, and methods that count the primes up to $x$ in about $x^{2/3}$ steps without listing them. The second is sieve theory, the part of analytic number theory that grew from the same idea. It does not compute tables; it bounds how many elements of a set, such as the pairs $n, n + 2$, have no small prime factor. Its tools give upper bounds of the right order for twin primes and for primes in short intervals.

## What the chapter covers

1. **Listing primes.** The problem of [listing the primes up to n](/primes-up-to-n/), the [sieve of Eratosthenes](/sieve-of-eratosthenes/) and the [sieve of Sundaram](/sieve-of-sundaram/), and the [segmented sieve](/segmented-sieve/) for [primes in an interval](/primes-in-range/).
2. **Sieves in linear time.** The [smallest prime factor table](/smallest-prime-factor-table/), the [linear sieve](/linear-sieve/) that builds it in $\Theta(n)$, and the [sieve of Atkin](/sieve-of-atkin/), based on quadratic forms.
3. **Arithmetic functions on a whole range.** Tables of [divisor functions](/divisor-function-up-to-n/), with the [divisor-count sieve](/divisor-count-sieve/); of [totients](/totient-values-up-to-n/), with the [Euler totient sieve](/euler-phi-sieve/); of [any multiplicative function](/multiplicative-functions-up-to-n/); and the [Möbius sieve](/mobius-sieve/).
4. **Counting primes without listing them.** The [prime-counting function](/prime-counting-function/), [Legendre's phi function](/legendre-phi-function/), the [Lucy_Hedgehog method](/lucy-hedgehog-prime-counting/) and the [Meissel-Lehmer algorithm](/meissel-lehmer-algorithm/).
5. **Sieve theory.** The general setting of [sieve theory](/sieve-theory/), the [Buchstab function](/buchstab-function/), [Brun's sieve](/brun-sieve/), [Selberg's sieve](/selberg-sieve/) and the [large sieve inequality](/large-sieve-inequality/).

## A first reading

Read these in order:

1. [Listing primes up to n](/primes-up-to-n/)
2. [Sieve of Eratosthenes](/sieve-of-eratosthenes/)
3. [Segmented sieve](/segmented-sieve/)
4. [Smallest prime factor table](/smallest-prime-factor-table/)
5. [Linear sieve](/linear-sieve/)
6. [Euler totient sieve](/euler-phi-sieve/)
7. [Multiplicative function values up to n](/multiplicative-functions-up-to-n/)
8. [Möbius sieve](/mobius-sieve/)
9. [Prime-counting function](/prime-counting-function/)
10. [Legendre's phi function](/legendre-phi-function/)
11. [Lucy_Hedgehog prime counting](/lucy-hedgehog-prime-counting/)

These cover what programs use: prime tables of any size, factor tables, arithmetic functions in linear time, and $\pi(x)$ far beyond the reach of a table. The sieve of Atkin and the Meissel-Lehmer algorithm are refinements for a second reading. The last group is mathematics rather than programming; read the sieve theory entry for the ideas, and the three sieves after it when you need the estimates.

## Before you start

You need [prime numbers](/prime-number/) and the [fundamental theorem of arithmetic](/fundamental-theorem-of-arithmetic/), and for the third group [multiplicative functions](/multiplicative-function/), the [divisor function](/divisor-function/), [Euler's totient](/euler-totient/), the [Möbius function](/mobius-function/) and [Möbius inversion](/mobius-inversion-formula/), all from Chapters 10.1 and 10.2. The running times rest on two sums: the [harmonic series](/harmonic-series/) $\sum_{e \le n} 1/e \approx \ln n$ and its cousin over primes, $\sum_{p \le n} 1/p \approx \ln \ln n$. Correctness proofs use [loop invariants](/loop-invariant/). The analytic entries assume the [prime number theorem](/prime-number-theorem/) and inclusion-exclusion; the large sieve uses the [discrete Fourier transform](/discrete-fourier-transform/) and the [Chinese remainder theorem](/chinese-remainder-theorem/).
